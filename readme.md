# 慧脉中医

慧脉中医是一个基于前后端分离架构的智慧中医服务平台，致力于传承中医智慧，利用现代科技为用户提供便捷的中医健康服务。

## 技术栈

### 前端
- **框架**: Vue 3 (Composition API)
- **构建工具**: Vite
- **路由**: Vue Router
- **HTTP客户端**: Axios
- **样式**: CSS3 (原生)
- **状态管理**: localStorage (用于认证状态管理)

### 后端
- **框架**: Flask
- **ORM**: SQLAlchemy
- **认证**: JWT (JSON Web Token)
- **CORS**: Flask-CORS
- **数据库**: MySQL

## 项目结构

```
tech-tcm/
├── frontend/              # 前端代码
│   ├── public/            # 静态资源
│   ├── src/               # 源代码
│   │   ├── components/    # Vue组件
│   │   ├── views/         # 页面视图
│   │   ├── router/        # 路由配置
│   │   ├── utils/         # 工具函数
│   │   ├── App.vue        # 根组件
│   │   └── main.js        # 入口文件
│   ├── package.json       # 前端依赖
│   └── vite.config.js     # Vite配置
├── backend/               # 后端代码
│   ├── app/               # Flask应用
│   │   ├── __init__.py    # 应用初始化
│   │   ├── models/        # 数据模型
│   │   ├── routes/        # API路由
│   │   └── utils/         # 工具函数
│   ├── config.py          # 配置文件
│   ├── app.py             # 后端入口
│   └── requirements.txt   # 后端依赖
└── README.md              # 项目说明
```

## 功能特性

- ✅ 用户注册与登录
- ✅ 个人中心（查看/编辑资料）
- ✅ 智能问诊
- ✅ 名医推荐
- ✅ 病历记录
- ✅ 健康管理
- ✅ 响应式设计
- ✅ 中医风格UI

## 本地部署与启动

### 环境要求

- **Node.js**: 16.x 或更高版本
- **Python**: 3.8 或更高版本
- **MySQL**: 5.7 或更高版本

### 后端部署

1. **安装依赖**
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

2. **配置数据库**
   - 确保MySQL服务已启动
   - 创建数据库 `tech_tcm`
   - 修改 `config.py` 中的数据库连接信息（如果需要）

3. **初始化数据库**
   ```bash
   python
   >>> from app import db
   >>> db.create_all()
   >>> exit()
   ```

4. **启动后端服务**
   ```bash
   python app.py
   ```
   - 服务将运行在 `http://127.0.0.1:5000`

### 前端部署

1. **安装依赖**
   ```bash
   cd frontend
   npm install
   ```

2. **启动前端开发服务器**
   ```bash
   npm run dev
   ```
   - 服务将运行在 `http://localhost:5173`（或其他可用端口）

3. **访问应用**
   - 打开浏览器访问前端服务地址（如：http://localhost:5173）

## API接口

### 认证相关
- `POST /api/auth/register` - 用户注册
- `POST /api/auth/login` - 用户登录

### 用户相关
- `GET /api/user/profile` - 获取用户信息
- `PUT /api/user/profile` - 更新用户信息

## 开发说明

### 前端开发
- 所有页面组件放在 `src/views/` 目录下
- 可复用组件放在 `src/components/` 目录下
- API请求统一使用Axios
- 登录状态通过localStorage管理

### 后端开发
- 所有API路由放在 `app/routes/` 目录下
- 数据模型放在 `app/models/` 目录下
- 配置信息放在 `config.py` 中
- 使用JWT进行认证保护

## 注意事项

1. 确保MySQL数据库服务已正常启动
2. 后端服务默认运行在5000端口，前端默认运行在5173端口
3. 首次启动需要初始化数据库
4. 前端API请求地址已配置为后端服务地址

## 许可证

MIT License
