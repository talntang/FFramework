from fastapi import FastAPI  # FastAPI 是一个为你的 API 提供了所有功能的 Python 类。

app = FastAPI()  # 这个实例将是创建你所有 API 的主要交互对象。这个 app 同样在如下命令中被 uvicorn 所引用


@app.get("/")
async def root():
    return {"message": "Hello FFreamwork"}


# 方式一：终端输入命令启动 
# main是程序的名称
# app 是实例化的名称
# uvicorn main:app --reload


# 方式二
if __name__ == '__main__':
    # 生产环境可以使用[Uvicorn],上线环境用ASGI 服务器
    import uvicorn

    print(__name__)
    uvicorn.run("run:app", host="127.0.0.1", port=8000, reload=True)



'''创建一个fastapi程序
（1）导入 FastAPI。
（2）创建一个 app 实例。
（3）编写一个路径操作装饰器（如 @app.get("/")）。
（4）编写一个路径操作函数（如上面的 def root(): ...）
（5）定义返回值
（6）运行开发服务器（如 uvicorn main:app --reload）
'''