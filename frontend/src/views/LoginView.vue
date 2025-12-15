<template>
  <div class="auth-container">
    <div class="auth-card">
      <div class="auth-header">
        <h1>登录</h1>
        <p>欢迎回到慧脉中医</p>
      </div>
      
      <form class="auth-form" @submit.prevent="handleLogin">
        <div class="form-group">
          <label for="username">用户名</label>
          <input 
            type="text" 
            id="username" 
            v-model="formData.username"
            placeholder="请输入用户名"
            required
          />
        </div>
        
        <div class="form-group">
          <label for="password">密码</label>
          <input 
            type="password" 
            id="password" 
            v-model="formData.password"
            placeholder="请输入密码"
            required
          />
        </div>
        
        <div class="form-options">
          <div class="remember-me">
            <input type="checkbox" id="remember" v-model="rememberMe" />
            <label for="remember">记住我</label>
          </div>
          <a href="#" class="forgot-password">忘记密码？</a>
        </div>
        
        <button type="submit" class="btn btn-primary" :disabled="isLoading">
          {{ isLoading ? '登录中...' : '登录' }}
        </button>
        
        <div class="form-footer">
          <p>还没有账号？ <router-link to="/register" class="register-link">立即注册</router-link></p>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import axios from 'axios'

const router = useRouter()
const isLoading = ref(false)
const rememberMe = ref(false)

const formData = ref({
  username: '',
  password: ''
})

const handleLogin = async () => {
  isLoading.value = true
  try {
    const response = await axios.post('http://localhost:5000/api/auth/login', formData.value)
    
    // 保存token到localStorage
    localStorage.setItem('access_token', response.data.data.access_token)
    localStorage.setItem('refresh_token', response.data.data.refresh_token)
    localStorage.setItem('user', JSON.stringify(response.data.data.user))
    
    // 跳转到首页
    router.push('/')
  } catch (error) {
    alert(error.response?.data?.message || '登录失败，请检查用户名和密码')
  } finally {
    isLoading.value = false
  }
}
</script>

<style scoped>
.auth-container {
  min-height: calc(100vh - 120px);
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, #faf8f5 0%, #f5f0e5 100%);
  padding: 20px;
}

.auth-card {
  background: white;
  padding: 40px;
  border-radius: 20px;
  box-shadow: 0 10px 40px rgba(0, 0, 0, 0.1);
  width: 100%;
  max-width: 400px;
  border: 1px solid rgba(139, 69, 19, 0.1);
}

.auth-header {
  text-align: center;
  margin-bottom: 30px;
}

.auth-header h1 {
  font-size: 2rem;
  color: #333;
  margin-bottom: 10px;
  font-family: 'SimSun', serif;
}

.auth-header p {
  color: #666;
  font-size: 1rem;
}

.auth-form {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.form-group {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.form-group label {
  color: #333;
  font-weight: 500;
  font-size: 0.9rem;
}

.form-group input {
  padding: 12px 15px;
  border: 2px solid #e0e0e0;
  border-radius: 10px;
  font-size: 1rem;
  transition: all 0.3s ease;
}

.form-group input:focus {
  outline: none;
  border-color: #8B4513;
  box-shadow: 0 0 0 3px rgba(139, 69, 19, 0.1);
}

.form-options {
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 0.9rem;
}

.remember-me {
  display: flex;
  align-items: center;
  gap: 8px;
  color: #666;
  cursor: pointer;
}

.forgot-password {
  color: #8B4513;
  text-decoration: none;
  transition: color 0.3s ease;
}

.forgot-password:hover {
  color: #654321;
  text-decoration: underline;
}

.btn-primary {
  padding: 14px 20px;
  background: linear-gradient(135deg, #8B4513 0%, #654321 100%);
  color: white;
  border: none;
  border-radius: 10px;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
}

.btn-primary:hover:not(:disabled) {
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(139, 69, 19, 0.4);
}

.btn-primary:disabled {
  opacity: 0.7;
  cursor: not-allowed;
}

.form-footer {
  text-align: center;
  margin-top: 10px;
  color: #666;
  font-size: 0.9rem;
}

.register-link {
  color: #8B4513;
  text-decoration: none;
  font-weight: 600;
  transition: color 0.3s ease;
}

.register-link:hover {
  color: #654321;
  text-decoration: underline;
}
</style>
