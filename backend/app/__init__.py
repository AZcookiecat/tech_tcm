# 应用初始化
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from config import config

# 创建数据库实例
db = SQLAlchemy()

# 创建JWT实例
jwt = JWTManager()

# 创建CORS实例
cors = CORS()

def create_app(config_name='default'):
    """创建Flask应用实例"""
    app = Flask(__name__)
    
    # 加载配置
    app.config.from_object(config[config_name])
    
    # 初始化扩展
    db.init_app(app)
    jwt.init_app(app)
    cors.init_app(app, resources={"/*": {"origins": "*"}})
    
    # 注册蓝图
    from app.routes.auth import auth_bp
    from app.routes.user import user_bp
    
    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(user_bp, url_prefix='/api/user')
    
    # 创建数据库表
    with app.app_context():
        db.create_all()
    
    return app
