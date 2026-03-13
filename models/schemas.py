from pydantic import BaseModel
from typing import Optional


class LogRequest(BaseModel):
    log_text: str                    # 분석할 로그 내용 (필수)
    log_type: Optional[str] = "일반"  # 로그 종류 (선택, 기본값: 일반)


class LogAnalysisResult(BaseModel):
    is_threat: bool          # 위협 여부
    threat_level: str        # LOW / MEDIUM / HIGH
    threat_type: str         # 위협 종류 (예: 브루트포스, SQL인젝션 등)
    reason: str              # 판단 근거
    recommendation: str      # 권고사항