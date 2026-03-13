from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from dotenv import load_dotenv
from routes.analyze import router

load_dotenv()

app = FastAPI(
    title="보안 로그 분석기",
    description="Claude AI를 활용한 보안 로그 분석 API",
    version="1.0.0"
)

# static 폴더 연결 (웹 UI)
app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(router)

@app.get("/")
def root():
    return {"message": "보안 로그 분석기 서버 실행 중 🔍"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True)