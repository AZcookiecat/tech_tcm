# 认证路由
from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity
from app import db
from app.models.user import User
from datetime import datetime

# 创建蓝图
auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    """用户注册接口"""
    try:
        # 获取请求数据
        data = request.get_json()
        
        # 验证必填字段
        required_fields = ['username', 'email', 'password']
        for field in required_fields:
            if field not in data or not data[field]:
                return jsonify({'code': 400, 'message': f'{field}不能为空'}), 400
        
        # 检查用户名是否已存在
        if User.query.filter_by(username=data['username']).first():
            return jsonify({'code': 400, 'message': '用户名已存在'}), 400
        
        # 检查邮箱是否已存在
        if User.query.filter_by(email=data['email']).first():
            return jsonify({'code': 400, 'message': '邮箱已存在'}), 400
        
        # 创建新用户
        user = User(
            username=data['username'],
            email=data['email'],
            password=data['password']
        )
        
        # 添加到数据库
        db.session.add(user)
        db.session.commit()
        
        # 返回成功响应
        return jsonify({
            'code': 201,
            'message': '注册成功',
            'data': {
                'user_id': user.id,
                'username': user.username,
                'email': user.email
            }
        }), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'code': 500, 'message': f'注册失败: {str(e)}'}), 500

@auth_bp.route('/login', methods=['POST'])
def login():
    """用户登录接口"""
    try:
        # 获取请求数据
        data = request.get_json()
        
        # 验证必填字段
        required_fields = ['username', 'password']
        for field in required_fields:
            if field not in data or not data[field]:
                return jsonify({'code': 400, 'message': f'{field}不能为空'}), 400
        
        # 查找用户
        user = User.query.filter_by(username=data['username']).first()
        
        # 验证用户和密码
        if not user or not user.verify_password(data['password']):
            return jsonify({'code': 401, 'message': '用户名或密码错误'}), 401
        
        # 检查账户状态
        if not user.status:
            return jsonify({'code': 403, 'message': '账户已被禁用'}), 403
        
        # 更新最后登录时间
        user.last_login = datetime.now()
        db.session.commit()
        
        # 创建JWT令牌
        access_token = create_access_token(identity=user.id, additional_claims={'role': user.role})
        refresh_token = create_refresh_token(identity=user.id)
        
        # 返回成功响应
        return jsonify({
            'code': 200,
            'message': '登录成功',
            'data': {
                'access_token': access_token,
                'refresh_token': refresh_token,
                'user': user.to_dict()
            }
        }), 200
        
    except Exception as e:
        return jsonify({'code': 500, 'message': f'登录失败: {str(e)}'}), 500

@auth_bp.route('/refresh', methods=['POST'])
@jwt_required(refresh=True)
def refresh():
    """刷新令牌接口"""
    try:
        # 获取当前用户
        current_user_id = get_jwt_identity()
        user = User.query.get(current_user_id)
        
        if not user:
            return jsonify({'code': 404, 'message': '用户不存在'}), 404
        
        # 创建新的访问令牌
        new_access_token = create_access_token(identity=current_user_id, additional_claims={'role': user.role})
        
        return jsonify({
            'code': 200,
            'message': '令牌刷新成功',
            'data': {
                'access_token': new_access_token
            }
        }), 200
        
    except Exception as e:
        return jsonify({'code': 500, 'message': f'令牌刷新失败: {str(e)}'}), 500

@auth_bp.route('/me', methods=['GET'])
@jwt_required()
def get_current_user():
    """获取当前用户信息"""
    try:
        # 获取当前用户
        current_user_id = get_jwt_identity()
        user = User.query.get(current_user_id)
        
        if not user:
            return jsonify({'code': 404, 'message': '用户不存在'}), 404
        
        return jsonify({
            'code': 200,
            'message': '获取成功',
            'data': user.to_dict()
        }), 200
        
    except Exception as e:
        return jsonify({'code': 500, 'message': f'获取失败: {str(e)}'}), 500
