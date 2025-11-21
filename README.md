# Maintenance AI Portfolio API

FastAPI로 만든 포트폴리오용 백엔드 프로젝트입니다.  
향후 설비/설비 관리, 로그 분석, AI 서빙 기능 등을 붙일 예정입니다.

## Requirements

- Python 3.10+
- pip
- (optional) virtualenv 또는 venv

## 설치 & 실행

```bash
git clone https://github.com/ybbcman/physical-ai-dev.git
cd physical-ai-dev

python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

pip install -r requirements.txt

uvicorn backend.src.main:app --reload
