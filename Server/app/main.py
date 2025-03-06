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



'''创建一个fastapi程序
（1）导入 FastAPI。
（2）创建一个 app 实例。
（3）编写一个路径操作装饰器（如 @app.get("/")）。
（4）编写一个路径操作函数（如上面的 def root(): ...）
（5）定义返回值
（6）运行开发服务器（如 uvicorn main:app --reload）
'''