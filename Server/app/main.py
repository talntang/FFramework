from fastapi import FastAPI
from app.database import engine
from app.models import Base
from app.routers import user

# 创建数据库表
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Game Backend API")

# 注册路由
app.include_router(user.router, prefix="/api/users", tags=["users"])

@app.get("/")
async def root():
    return {"message": "Hello, FFreamwork!"}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
