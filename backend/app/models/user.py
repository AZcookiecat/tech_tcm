# 用户模型
from app import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    __tablename__ = 'users'
    
    # 主键
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    
    # 基本信息
    username = db.Column(db.String(50), unique=True, nullable=False, comment='用户名')
    password_hash = db.Column(db.String(255), nullable=False, comment='密码哈希')
    email = db.Column(db.String(100), unique=True, nullable=False, comment='邮箱')
    phone = db.Column(db.String(20), nullable=True, comment='手机号码')
    
    # 个人信息
    gender = db.Column(db.Enum('male', 'female', 'other'), nullable=True, comment='性别')
    age = db.Column(db.Integer, nullable=True, comment='年龄')
    address = db.Column(db.String(255), nullable=True, comment='居住地址')
    medical_history = db.Column(db.Text, nullable=True, comment='既往病史')
    
    # 会员信息
    member_level = db.Column(db.String(20), default='普通会员', comment='会员等级')
    member_expire = db.Column(db.DateTime, nullable=True, comment='会员到期时间')
    
    # 系统信息
    register_date = db.Column(db.DateTime, default=datetime.now, comment='注册时间')
    last_login = db.Column(db.DateTime, nullable=True, comment='最后登录时间')
    status = db.Column(db.Boolean, default=True, comment='账户状态')
    avatar = db.Column(db.String(255), nullable=True, comment='头像URL')
    
    # 角色信息
    role = db.Column(db.Enum('user', 'doctor', 'admin'), default='user', comment='用户角色')
    
    # 密码相关方法
    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')
    
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    # 序列化方法
    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'phone': self.phone,
            'gender': self.gender,
            'age': self.age,
            'address': self.address,
            'medical_history': self.medical_history,
            'member_level': self.member_level,
            'register_date': self.register_date.strftime('%Y-%m-%d %H:%M:%S') if self.register_date else None,
            'last_login': self.last_login.strftime('%Y-%m-%d %H:%M:%S') if self.last_login else None,
            'status': self.status,
            'avatar': self.avatar,
            'role': self.role
        }
    
    def __repr__(self):
        return f'<User {self.username}>'
