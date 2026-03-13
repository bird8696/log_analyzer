# 🔍 보안 로그 분석기

Claude AI를 활용해 시스템 로그의 위협 여부를 자동으로 분석하는 FastAPI 기반 REST API 서버입니다.
웹 UI를 통해 누구나 쉽게 로그를 붙여넣고 분석할 수 있습니다.

---

## 📌 프로젝트 소개

시스템 로그는 보안 위협의 흔적이 가장 먼저 남는 곳입니다.
이 프로젝트는 Anthropic의 **Claude AI** 에게 사이버 보안 전문가 역할을 부여하여,
별도의 학습 데이터 없이도 다양한 종류의 로그에서 위협을 탐지하고 대응 방법을 제시합니다.

### 탐지 가능한 위협 종류

| 위협 종류     | 설명                               |
| ------------- | ---------------------------------- |
| 브루트포스    | 짧은 시간 내 반복적인 로그인 실패  |
| SQL 인젝션    | SQL 구문이 포함된 비정상적인 입력  |
| 디렉토리 탐색 | `../` 등을 이용한 경로 탐색 시도   |
| 포트 스캔     | 다양한 포트로의 연속적인 접근 시도 |
| 비정상 접근   | 업무 외 시간의 관리자 접근         |
| 대용량 전송   | 비정상적으로 큰 데이터 전송        |

---

## ⚙️ 설치 및 실행

### 1. 패키지 설치

```bash
pip install fastapi uvicorn anthropic pydantic python-dotenv
```

### 2. API 키 설정

`.env` 파일에 Anthropic API 키를 입력하세요.

```
ANTHROPIC_API_KEY=여기에_실제_API키_입력
```

> API 키 발급: https://console.anthropic.com

### 3. 서버 실행

```bash
python main.py
```

### 4. 서버 종료

```
Ctrl + C
```

---

## 🖥️ 사용 방법

### 방법 1. 웹 UI (추천)

서버 실행 후 브라우저에서 아래 주소로 접속하세요.

```
http://localhost:8000/static/index.html
```

#### Step 1. 로그 종류 선택

분석할 로그 종류를 선택하세요.

- 일반 / Apache / Nginx / Linux Syslog / Windows 이벤트 / SSH / 방화벽

#### Step 2. 로그 내용 붙여넣기

분석할 로그를 텍스트 박스에 붙여넣으세요.

#### Step 3. 분석 시작 클릭

**`🔍 분석 시작`** 버튼을 클릭하면 결과가 바로 나타납니다.

---

### 방법 2. Swagger UI

```
http://localhost:8000/docs
```

**입력 예시**

```json
{
  "log_text": "Failed password for root from 192.168.1.105 port 22 ssh2",
  "log_type": "SSH"
}
```

---

### 📊 결과 확인

| 항목             | 설명                                 |
| ---------------- | ------------------------------------ |
| `is_threat`      | 위협 여부 (true: 위협 / false: 정상) |
| `threat_level`   | 위협 수준 (LOW / MEDIUM / HIGH)      |
| `threat_type`    | 위협 종류 (브루트포스, SQL인젝션 등) |
| `reason`         | 위협으로 판단한 근거                 |
| `recommendation` | 권고 행동                            |

---

## 🗂 프로젝트 구조

```
log_analyzer/
├── main.py                  # FastAPI 앱 진입점
├── requirements.txt         # 의존 패키지 목록
├── .env                     # API 키 설정 (GitHub 비공개)
├── models/
│   └── schemas.py           # 요청/응답 데이터 구조
├── routes/
│   └── analyze.py           # API 엔드포인트
├── services/
│   └── analyzer.py          # Claude API 분석 로직
└── static/
    └── index.html           # 웹 UI
```

---

## 🛠 기술 스택

| 역할          | 기술                    |
| ------------- | ----------------------- |
| API 서버      | FastAPI                 |
| AI 분석       | Claude API (Anthropic)  |
| 웹 UI         | HTML / CSS / JavaScript |
| 데이터 검증   | Pydantic                |
| 환경변수 관리 | python-dotenv           |

---

## 📋 요구사항

- Python 3.11.9
- Anthropic API 키 ([발급 바로가기](https://console.anthropic.com))
