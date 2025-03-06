### 快速搭建后端

* 第一步：安装fastapi; protobuf; sqlite已经内置  
`pip install fastapi[all] protobuf`

* 第二步：使用shell，生成proto 文件  
`protoc --python_out=. --csharp_out=. ./message.proto`

* 第三步：直接执行下面，有名称为main.py文件  
`uvicorn main:app --reload`

* 第四步：运行后，打开浏览器访问：
> http://127.0.0.1:8080/，将看到 {"message": "Hello, FFreamwork!"}  
> http://127.0.0.1:8080/docs，可以访问自动生成的 Swagger UI 文档  
> http://127.0.0.1:8080/redoc，可以访问 Redoc 风格的 API 文档  


### 目录结构

game_backend/  
│── app/  
│   ├── main.py              # 入口  
│   ├── models.py            # 数据库模型  
│   ├── routers/  
│   │   ├── user.py          # 用户 API  
│   │   ├── game.py          # 游戏 API  
│   ├── services/            # 业务逻辑层  
│   ├── schemas/             # 数据模型（Pydantic）  
│   ├── websocket.py         # WebSocket 逻辑  
│── migrations/              # Alembic 迁移  
│── tests/                   # 测试代码  
│── docker-compose.yml       # Docker 部署配置  
│── requirements.txt         # 依赖  
│── README.md  


