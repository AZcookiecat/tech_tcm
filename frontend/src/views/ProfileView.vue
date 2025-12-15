<template>
  <div class="profile">
    <div class="container">
      <!-- 未登录状态 -->
      <div v-if="!isLogged" class="profile-login">
        <div class="login-container">
          <div class="login-icon">👤</div>
          <h1>请先登录</h1>
          <p>登录后可以查看和管理您的个人资料</p>
          <div class="login-buttons">
            <router-link to="/login" class="btn btn-primary">立即登录</router-link>
            <router-link to="/register" class="btn btn-secondary">注册账号</router-link>
          </div>
        </div>
      </div>
      
      <!-- 已登录状态 -->
      <div v-else class="profile-content">
        <h1>个人中心</h1>
        
        <div class="profile-header">
          <div class="header-info">
            <div class="user-avatar">
              <img src="/1761709868750.png" alt="用户头像" />
            </div>
            <div class="user-basic">
              <h2>{{ user?.username }}</h2>
              <p class="user-email">{{ user?.email }}</p>
              <div class="user-stats">
                <div class="stat-item">
                  <span class="stat-label">会员等级</span>
                  <span class="stat-value">{{ user?.member_level || '普通会员' }}</span>
                </div>
                <div class="stat-item">
                  <span class="stat-label">注册时间</span>
                  <span class="stat-value">{{ user?.register_date || '未知' }}</span>
                </div>
                <div class="stat-item">
                  <span class="stat-label">问诊次数</span>
                  <span class="stat-value">0</span>
                </div>
              </div>
            </div>
          </div>
        </div>
        
        <div class="profile-body">
          <div class="profile-main">
            <div class="profile-section">
              <div class="section-header">
                <h3>基本信息</h3>
                <button 
                  class="btn btn-primary edit-btn" 
                  @click="toggleEditMode"
                >
                  {{ isEditMode ? '取消修改' : '修改资料' }}
                </button>
              </div>
              
              <!-- 查看模式 -->
              <div v-if="!isEditMode" class="profile-view">
                <div class="view-grid">
                  <div class="view-item">
                    <div class="view-item-header">
                      <span class="view-label">用户名</span>
                    </div>
                    <div class="view-value">{{ user?.username }}</div>
                  </div>
                  <div class="view-item">
                    <div class="view-item-header">
                      <span class="view-label">电子邮箱</span>
                    </div>
                    <div class="view-value">{{ user?.email }}</div>
                  </div>
                  <div class="view-item">
                    <div class="view-item-header">
                      <span class="view-label">手机号码</span>
                    </div>
                    <div class="view-value">{{ user?.phone || '未设置' }}</div>
                  </div>
                  <div class="view-item">
                    <div class="view-item-header">
                      <span class="view-label">性别</span>
                    </div>
                    <div class="view-value">{{ user?.gender ? (user.gender === 'male' ? '男' : user.gender === 'female' ? '女' : '其他') : '未设置' }}</div>
                  </div>
                  <div class="view-item">
                    <div class="view-item-header">
                      <span class="view-label">年龄</span>
                    </div>
                    <div class="view-value">{{ user?.age ? user.age + '岁' : '未设置' }}</div>
                  </div>
                  <div class="view-item">
                    <div class="view-item-header">
                      <span class="view-label">居住地址</span>
                    </div>
                    <div class="view-value">{{ user?.address || '未设置' }}</div>
                  </div>
                  <div class="view-item full-width">
                    <div class="view-item-header">
                      <span class="view-label">既往病史</span>
                    </div>
                    <div class="view-value">{{ user?.medical_history || '无' }}</div>
                  </div>
                </div>
              </div>
              
              <!-- 修改模式 -->
              <form v-else class="profile-form" @submit.prevent="saveProfile">
                <div class="form-grid">
                  <div class="form-group">
                    <label for="phone">手机号码</label>
                    <input type="tel" id="phone" v-model="editForm.phone" placeholder="请输入手机号码" />
                  </div>
                  <div class="form-group">
                    <label for="gender">性别</label>
                    <select id="gender" v-model="editForm.gender">
                      <option value="">请选择性别</option>
                      <option value="male">男</option>
                      <option value="female">女</option>
                      <option value="other">其他</option>
                    </select>
                  </div>
                  <div class="form-group">
                    <label for="age">年龄</label>
                    <input type="number" id="age" v-model="editForm.age" placeholder="请输入年龄" min="0" max="120" />
                  </div>
                  <div class="form-group full-width">
                    <label for="address">居住地址</label>
                    <input type="text" id="address" v-model="editForm.address" placeholder="请输入您的详细地址" />
                  </div>
                  <div class="form-group full-width">
                    <label for="medicalHistory">既往病史</label>
                    <textarea id="medicalHistory" v-model="editForm.medical_history" rows="4" placeholder="请输入您的既往病史，如有多个请用逗号分隔"></textarea>
                  </div>
                </div>
                <div class="form-actions">
                  <button type="button" class="btn btn-secondary" @click="toggleEditMode">取消</button>
                  <button type="submit" class="btn btn-primary">保存修改</button>
                </div>
              </form>
            </div>
            
            <!-- 健康管理模块 -->
            <div class="profile-section">
              <div class="section-header">
                <h3>健康管理</h3>
              </div>
              <div class="health-cards">
                <div class="health-card">
                  <div class="card-icon">🩺</div>
                  <h4>我的病历</h4>
                  <p>查看和管理您的问诊记录</p>
                  <router-link to="/records" class="btn btn-outline">查看病历</router-link>
                </div>
                <div class="health-card">
                  <div class="card-icon">📊</div>
                  <h4>健康数据</h4>
                  <p>记录您的健康指标</p>
                  <a href="#" class="btn btn-outline">添加数据</a>
                </div>
                <div class="health-card">
                  <div class="card-icon">💊</div>
                  <h4>用药记录</h4>
                  <p>管理您的用药情况</p>
                  <a href="#" class="btn btn-outline">查看记录</a>
                </div>
              </div>
            </div>
          </div>
          
          <div class="profile-sidebar">
            <div class="sidebar-section">
              <h4>快速导航</h4>
              <div class="sidebar-menu">
                <div class="menu-item active">
                  <span class="menu-icon">👤</span>
                  <span>个人信息</span>
                </div>
                <div class="menu-item">
                  <span class="menu-icon">📋</span>
                  <span>我的病历</span>
                </div>
                <div class="menu-item">
                  <span class="menu-icon">🔒</span>
                  <span>账户安全</span>
                </div>
                <div class="menu-item">
                  <span class="menu-icon">⚙️</span>
                  <span>设置</span>
                </div>
                <div class="menu-item">
                  <span class="menu-icon">💬</span>
                  <span>意见反馈</span>
                </div>
              </div>
            </div>
            
            <div class="sidebar-section">
              <h4>系统消息</h4>
              <div class="message-list">
                <div class="message-item">
                  <div class="message-content">
                    <p class="message-title">欢迎使用慧脉中医</p>
                    <p class="message-text">感谢您的注册，祝您使用愉快！</p>
                  </div>
                  <span class="message-time">今天</span>
                </div>
                <div class="message-item">
                  <div class="message-content">
                    <p class="message-title">系统更新</p>
                    <p class="message-text">我们已完成系统升级，新增了多项功能</p>
                  </div>
                  <span class="message-time">昨天</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, watch } from 'vue'
import { useRouter } from 'vue-router'
import { isLoggedIn, getCurrentUser, updateUserInfo } from '../utils/auth'
import axios from 'axios'

const router = useRouter()
const isEditMode = ref(false)
const isLogged = computed(() => isLoggedIn())
const user = ref(getCurrentUser())

// 编辑表单数据
const editForm = ref({
  phone: '',
  gender: '',
  age: '',
  address: '',
  medical_history: ''
})

// 切换编辑模式
const toggleEditMode = () => {
  if (isEditMode.value) {
    // 取消编辑，重置表单
    resetForm()
  } else {
    // 进入编辑模式，填充表单数据
    fillForm()
  }
  isEditMode.value = !isEditMode.value
}

// 填充表单数据
const fillForm = () => {
  if (user.value) {
    editForm.value = {
      phone: user.value.phone || '',
      gender: user.value.gender || '',
      age: user.value.age || '',
      address: user.value.address || '',
      medical_history: user.value.medical_history || ''
    }
  }
}

// 重置表单
const resetForm = () => {
  fillForm()
}

// 保存个人资料
const saveProfile = async () => {
  try {
    // 发送请求到后端保存个人资料
    const token = localStorage.getItem('access_token')
    const response = await axios.put('http://localhost:5000/api/user/profile', editForm.value, {
      headers: {
        'Authorization': `Bearer ${token}`
      }
    })
    
    // 更新本地用户信息
    const updatedUser = updateUserInfo(response.data.data)
    user.value = updatedUser
    
    // 退出编辑模式
    isEditMode.value = false
    
    alert('个人资料保存成功！')
  } catch (error) {
    console.error('保存失败:', error)
    alert(error.response?.data?.message || '保存失败，请稍后重试')
  }
}

// 初始化
onMounted(() => {
  if (isLogged.value) {
    // 可以在这里从后端获取最新的用户信息
    user.value = getCurrentUser()
  }
})

// 监听登录状态变化
watch(isLogged, (newVal) => {
  if (newVal) {
    user.value = getCurrentUser()
  }
})
</script>

<style scoped>
.profile {
  padding: 40px 20px;
  background: #f8f9fa;
  min-height: 100vh;
}

.container {
  max-width: 1200px;
  margin: 0 auto;
}

.profile h1 {
  text-align: center;
  color: #333;
  margin-bottom: 40px;
  font-size: 2.5rem;
}

.profile-content {
  background: white;
  padding: 40px;
  border-radius: 15px;
  box-shadow: 0 5px 20px rgba(0,0,0,0.1);
  display: flex;
  flex-direction: column;
  gap: 30px;
}

/* Profile Header */
.profile-header {
  background: linear-gradient(135deg, #4caf50 0%, #2e7d32 100%);
  color: white;
  padding: 30px;
  border-radius: 12px;
  box-shadow: 0 4px 20px rgba(76, 175, 80, 0.3);
}

.header-info {
  display: flex;
  align-items: center;
  gap: 30px;
}

.user-avatar {
  margin-bottom: 0;
}

.user-avatar img {
  width: 120px;
  height: 120px;
  border-radius: 50%;
  object-fit: cover;
  border: 4px solid white;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
}

.user-basic {
  flex: 1;
}

.user-basic h2 {
  color: white;
  margin-bottom: 10px;
  font-size: 1.8rem;
}

.user-email {
  color: rgba(255, 255, 255, 0.9);
  margin-bottom: 20px;
  font-size: 1rem;
}

.user-stats {
  display: flex;
  gap: 40px;
  flex-wrap: wrap;
}

.stat-item {
  display: flex;
  flex-direction: column;
  gap: 5px;
}

.stat-label {
  color: rgba(255, 255, 255, 0.8);
  font-size: 0.9rem;
  font-weight: 500;
}

.stat-value {
  color: white;
  font-size: 1.2rem;
  font-weight: bold;
}

/* Profile Body */
.profile-body {
  display: grid;
  grid-template-columns: 1fr 320px;
  gap: 30px;
}

/* Profile Main */
.profile-main {
  display: flex;
  flex-direction: column;
  gap: 30px;
}

.profile-section {
  background: #fafafa;
  padding: 30px;
  border-radius: 12px;
  border: 1px solid #e0e0e0;
}

.section-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 25px;
  padding-bottom: 15px;
  border-bottom: 2px solid #e8f5e8;
}

.section-header h3 {
  color: #333;
  margin-bottom: 0;
  font-size: 1.3rem;
  font-weight: 600;
}

.edit-btn {
  padding: 10px 25px;
  font-size: 0.95rem;
}

/* Profile View */
.profile-view {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.view-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 20px;
}

.view-item {
  background: white;
  padding: 20px;
  border-radius: 10px;
  border: 1px solid #e0e0e0;
  box-shadow: 0 2px 10px rgba(0,0,0,0.05);
  transition: all 0.3s ease;
}

.view-item:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 15px rgba(0,0,0,0.1);
}

.view-item.full-width {
  grid-column: 1 / -1;
}

.view-item-header {
  margin-bottom: 10px;
}

.view-label {
  color: #666;
  font-weight: 500;
  font-size: 0.9rem;
  display: block;
}

.view-value {
  color: #333;
  font-weight: 600;
  font-size: 1.1rem;
  line-height: 1.6;
}

/* Profile Form */
.profile-form {
  display: flex;
  flex-direction: column;
  gap: 25px;
}

.form-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 20px;
}

.form-group {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.form-group.full-width {
  grid-column: 1 / -1;
}

.form-group label {
  color: #333;
  font-weight: 500;
  font-size: 0.9rem;
}

.form-group input,
.form-group select,
.form-group textarea {
  padding: 12px 15px;
  border: 2px solid #e0e0e0;
  border-radius: 8px;
  font-size: 1rem;
  transition: all 0.3s ease;
  background: white;
}

.form-group input:focus,
.form-group select:focus,
.form-group textarea:focus {
  outline: none;
  border-color: #4caf50;
  box-shadow: 0 0 0 3px rgba(76, 175, 80, 0.1);
}

.form-group textarea {
  resize: vertical;
  min-height: 100px;
}

.form-actions {
  display: flex;
  gap: 15px;
  justify-content: flex-end;
  margin-top: 20px;
}

/* Health Cards */
.health-cards {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 20px;
}

.health-card {
  background: white;
  padding: 25px;
  border-radius: 12px;
  border: 1px solid #e0e0e0;
  box-shadow: 0 2px 15px rgba(0,0,0,0.08);
  text-align: center;
  transition: all 0.3s ease;
  display: flex;
  flex-direction: column;
  gap: 15px;
  align-items: center;
}

.health-card:hover {
  transform: translateY(-3px);
  box-shadow: 0 6px 25px rgba(0,0,0,0.15);
  border-color: #4caf50;
}

.card-icon {
  font-size: 3rem;
  margin-bottom: 10px;
}

.health-card h4 {
  color: #333;
  font-size: 1.2rem;
  margin-bottom: 10px;
}

.health-card p {
  color: #666;
  font-size: 0.95rem;
  line-height: 1.6;
  margin-bottom: 15px;
}

/* Profile Sidebar */
.profile-sidebar {
  display: flex;
  flex-direction: column;
  gap: 25px;
}

.sidebar-section {
  background: #fafafa;
  padding: 25px;
  border-radius: 12px;
  border: 1px solid #e0e0e0;
}

.sidebar-section h4 {
  color: #333;
  margin-bottom: 20px;
  font-size: 1.1rem;
  font-weight: 600;
  border-bottom: 1px solid #e0e0e0;
  padding-bottom: 10px;
}

/* Sidebar Menu */
.sidebar-menu {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.menu-item {
  padding: 15px 20px;
  background: white;
  color: #666;
  border: 1px solid #e0e0e0;
  border-radius: 8px;
  cursor: pointer;
  font-size: 0.95rem;
  font-weight: 500;
  transition: all 0.3s ease;
  text-align: left;
  display: flex;
  align-items: center;
  gap: 12px;
}

.menu-item:hover {
  background: #f1f8e9;
  color: #4caf50;
  border-color: #4caf50;
  transform: translateX(5px);
}

.menu-item.active {
  background: #4caf50;
  color: white;
  border-color: #4caf50;
  box-shadow: 0 4px 15px rgba(76, 175, 80, 0.2);
}

.menu-icon {
  font-size: 1.1rem;
  width: 20px;
  text-align: center;
}

/* Message List */
.message-list {
  display: flex;
  flex-direction: column;
  gap: 15px;
}

.message-item {
  background: white;
  padding: 18px;
  border-radius: 8px;
  border: 1px solid #e0e0e0;
  box-shadow: 0 2px 10px rgba(0,0,0,0.05);
  display: flex;
  flex-direction: column;
  gap: 10px;
  transition: all 0.3s ease;
}

.message-item:hover {
  box-shadow: 0 4px 15px rgba(0,0,0,0.1);
  transform: translateY(-2px);
}

.message-content {
  display: flex;
  flex-direction: column;
  gap: 5px;
}

.message-title {
  color: #333;
  font-weight: 600;
  font-size: 0.95rem;
  margin-bottom: 5px;
}

.message-text {
  color: #666;
  font-size: 0.9rem;
  line-height: 1.5;
  margin-bottom: 0;
}

.message-time {
  color: #999;
  font-size: 0.8rem;
  align-self: flex-end;
  margin-top: 5px;
}

/* Buttons */
.btn {
  padding: 12px 30px;
  border: none;
  border-radius: 8px;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  min-width: 120px;
  text-decoration: none;
  display: inline-block;
  text-align: center;
}

.btn-secondary {
  background: #f5f5f5;
  color: #666;
  border: 2px solid #e0e0e0;
}

.btn-secondary:hover {
  background: #e0e0e0;
  transform: translateY(-2px);
  box-shadow: 0 5px 15px rgba(0,0,0,0.1);
}

.btn-primary {
  background: #4caf50;
  color: white;
}

.btn-primary:hover {
  background: #388e3c;
  transform: translateY(-2px);
  box-shadow: 0 5px 15px rgba(0,0,0,0.2);
}

.btn-outline {
  background: white;
  color: #4caf50;
  border: 2px solid #4caf50;
  padding: 10px 20px;
  border-radius: 8px;
  text-decoration: none;
  display: inline-block;
  font-weight: 600;
  transition: all 0.3s ease;
  font-size: 0.9rem;
}

.btn-outline:hover {
  background: #4caf50;
  color: white;
  transform: translateY(-2px);
  box-shadow: 0 5px 15px rgba(0,0,0,0.1);
}

/* Responsive Design */
@media (max-width: 1024px) {
  .profile-body {
    grid-template-columns: 1fr;
  }
  
  .profile-sidebar {
    order: -1;
  }
}

@media (max-width: 768px) {
  .profile-content {
    padding: 20px;
  }
  
  .profile-header {
    padding: 20px;
  }
  
  .header-info {
    flex-direction: column;
    text-align: center;
    gap: 20px;
  }
  
  .user-stats {
    justify-content: center;
    gap: 30px;
  }
  
  .profile-section {
    padding: 20px;
  }
  
  .view-grid {
    grid-template-columns: 1fr;
  }
  
  .health-cards {
    grid-template-columns: 1fr;
  }
  
  .section-header {
    flex-direction: column;
    gap: 15px;
    align-items: flex-start;
  }
  
  .form-actions {
    flex-direction: column;
  }
  
  .btn {
    width: 100%;
  }
}
</style>
