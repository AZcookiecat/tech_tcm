# 用户路由
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import db
from app.models.user import User

# 创建蓝图
user_bp = Blueprint('user', __name__)

@user_bp.route('/profile', methods=['GET'])
@jwt_required()
def get_profile():
    """获取用户个人信息"""
    try:
        # 获取当前用户ID
        user_id = get_jwt_identity()
        
        # 查找用户
        user = User.query.get(user_id)
        
        if not user:
            return jsonify({'code': 404, 'message': '用户不存在'}), 404
        
        # 返回用户信息
        return jsonify({
            'code': 200,
            'message': '获取成功',
            'data': user.to_dict()
        }), 200
        
    except Exception as e:
        return jsonify({'code': 500, 'message': f'获取失败: {str(e)}'}), 500

@user_bp.route('/profile', methods=['PUT'])
@jwt_required()
def update_profile():
    """更新用户个人信息"""
    try:
        # 获取当前用户ID
        user_id = get_jwt_identity()
        
        # 查找用户
        user = User.query.get(user_id)
        
        if not user:
            return jsonify({'code': 404, 'message': '用户不存在'}), 404
        
        # 获取请求数据
        data = request.get_json()
        
        # 更新用户信息
        if 'phone' in data:
            user.phone = data['phone']
        if 'gender' in data:
            user.gender = data['gender']
        if 'age' in data:
            user.age = data['age']
        if 'address' in data:
            user.address = data['address']
        if 'medical_history' in data:
            user.medical_history = data['medical_history']
        if 'avatar' in data:
            user.avatar = data['avatar']
        
        # 保存到数据库
        db.session.commit()
        
        # 返回更新后的用户信息
        return jsonify({
            'code': 200,
            'message': '更新成功',
            'data': user.to_dict()
        }), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'code': 500, 'message': f'更新失败: {str(e)}'}), 500

@user_bp.route('/password', methods=['PUT'])
@jwt_required()
def update_password():
    """更新用户密码"""
    try:
        # 获取当前用户ID
        user_id = get_jwt_identity()
        
        # 查找用户
        user = User.query.get(user_id)
        
        if not user:
            return jsonify({'code': 404, 'message': '用户不存在'}), 404
        
        # 获取请求数据
        data = request.get_json()
        
        # 验证必填字段
        if 'old_password' not in data or not data['old_password']:
            return jsonify({'code': 400, 'message': '旧密码不能为空'}), 400
        if 'new_password' not in data or not data['new_password']:
            return jsonify({'code': 400, 'message': '新密码不能为空'}), 400
        
        # 验证旧密码
        if not user.verify_password(data['old_password']):
            return jsonify({'code': 401, 'message': '旧密码错误'}), 401
        
        # 更新密码
        user.password = data['new_password']
        
        # 保存到数据库
        db.session.commit()
        
        # 返回成功响应
        return jsonify({
            'code': 200,
            'message': '密码更新成功'
        }), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'code': 500, 'message': f'密码更新失败: {str(e)}'}), 500

@user_bp.route('/status', methods=['GET'])
@jwt_required()
def get_user_status():
    """获取用户状态信息"""
    try:
        # 获取当前用户ID
        user_id = get_jwt_identity()
        
        # 查找用户
        user = User.query.get(user_id)
        
        if not user:
            return jsonify({'code': 404, 'message': '用户不存在'}), 404
        
        # 返回用户状态信息
        return jsonify({
            'code': 200,
            'message': '获取成功',
            'data': {
                'user_id': user.id,
                'username': user.username,
                'email': user.email,
                'status': user.status,
                'member_level': user.member_level,
                'last_login': user.last_login.strftime('%Y-%m-%d %H:%M:%S') if user.last_login else None
            }
        }), 200
        
    except Exception as e:
        return jsonify({'code': 500, 'message': f'获取失败: {str(e)}'}), 500
