from fastapi import APIRouter, HTTPException
from models.schemas import LogRequest, LogAnalysisResult
from services.analyzer import analyze_log
import traceback

router = APIRouter(prefix="/analyze", tags=["분석"])


@router.post("", response_model=LogAnalysisResult)
def analyze(log: LogRequest):
    """로그 직접 입력 분석"""
    try:
        return analyze_log(log)
    except Exception as e:
        traceback.print_exc()  # 터미널에 전체 에러 출력
        raise HTTPException(status_code=500, detail=f"분석 중 오류 발생: {str(e)}")