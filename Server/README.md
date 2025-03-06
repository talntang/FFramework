# 轻量游戏后端框架

这是一个基于 FastAPI 和 SQLite 构建的轻量游戏后端框架。该框架提供了基础的用户系统和游戏核心功能，支持 HTTP API 和 WebSocket 实时通信。

## 技术栈

- **Web 框架**: FastAPI
- **数据库**: SQLite
- **认证**: JWT (JSON Web Tokens)
- **实时通信**: WebSocket
- **数据序列化**: Protocol Buffers
- **API 文档**: Swagger UI / ReDoc

## 快速开始

1. **安装依赖**
```bash
pip install -r requirements.txt
```

2. **启动服务器**
```bash
uvicorn app.main:app --reload
```

3. **访问 API 文档**
- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

## 项目结构

```
game_backend/
├── app/
│   ├── main.py              # 应用入口
│   ├── models.py            # 数据库模型
│   ├── database.py          # 数据库配置
│   ├── routers/             # API 路由
│   │   └── user.py          # 用户相关接口
│   ├── services/            # 业务逻辑
│   │   └── user.py          # 用户服务
│   └── schemas/             # 数据模型
│       └── user.py          # 用户数据模型
├── requirements.txt         # 项目依赖
└── README.md
```

## 核心功能

### 用户系统
- 用户注册
- 用户登录
- JWT 认证

### 游戏功能
- 基础资源管理
- 实时数据同步
- WebSocket 通信

## API 示例

### 用户注册
```http
POST /api/users/register
Content-Type: application/json

{
    "username": "testuser",
    "email": "test@example.com",
    "password": "password123"
}
```

### 用户登录
```http
POST /api/users/token
Content-Type: application/x-www-form-urlencoded

username=testuser&password=password123
```

## 开发说明

1. **数据库**
   - 使用 SQLite 作为数据库
   - 数据库文件自动创建在项目根目录
   - 支持自动迁移

2. **认证系统**
   - 使用 JWT 进行身份验证
   - 支持 token 过期机制
   - 密码使用 bcrypt 加密存储

3. **WebSocket**
   - 支持实时游戏数据同步
   - 支持多客户端连接
   - 支持自定义消息格式

## 注意事项

1. 生产环境部署时请修改 `SECRET_KEY`
2. 建议使用环境变量管理敏感信息
3. 可以根据需要扩展数据库模型和游戏逻辑
4. WebSocket 连接需要实现心跳机制



