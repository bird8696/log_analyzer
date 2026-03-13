import os
import json
import anthropic
from dotenv import load_dotenv
from models.schemas import LogRequest, LogAnalysisResult

load_dotenv()  # .env 파일에서 API 키 불러오기

SYSTEM_PROMPT = """
당신은 사이버 보안 전문가입니다. 시스템 로그를 분석하고
반드시 아래 JSON 형식으로만 응답하세요.

{
  "is_threat": true 또는 false,
  "threat_level": "LOW" 또는 "MEDIUM" 또는 "HIGH",
  "threat_type": "위협 종류 (위협 없으면 '정상')",
  "reason": "판단 근거 한 줄",
  "recommendation": "권고사항"
}

위협 판단 기준:
- 브루트포스: 짧은 시간 내 반복적인 로그인 실패
- SQL 인젝션: SQL 구문이 포함된 비정상적인 입력
- 디렉토리 탐색: ../  등을 이용한 경로 탐색 시도
- 포트 스캔: 다양한 포트로의 연속적인 접근 시도
- 비정상적인 시간대: 업무 외 시간의 관리자 접근
- 대용량 데이터 전송: 비정상적으로 큰 데이터 전송
"""


def analyze_log(log: LogRequest) -> LogAnalysisResult:
    client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

    response = client.messages.create(
        model="claude-opus-4-6",
        max_tokens=512,
        system=SYSTEM_PROMPT,
        messages=[{
            "role": "user",
            "content": f"로그 종류: {log.log_type}\n\n로그 내용:\n{log.log_text}"
        }]
    )

    raw = response.content[0].text.strip()
    print("Claude 응답:", raw)  # 터미널에서 응답 확인용

    if "```json" in raw:
        raw = raw.split("```json")[1].split("```")[0].strip()
    elif "```" in raw:
        raw = raw.split("```")[1].strip()

    print("파싱할 JSON:", raw)  # JSON 파싱 전 확인용

    data = json.loads(raw)
    return LogAnalysisResult(**data)