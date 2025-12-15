<template>
  <div class="auth-container">
    <div class="auth-card">
      <div class="auth-header">
        <h1>注册</h1>
        <p>创建您的慧脉中医账号</p>
      </div>
      
      <form class="auth-form" @submit.prevent="handleRegister">
        <div class="form-row">
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
        </div>
        
        <div class="form-row">
          <div class="form-group">
            <label for="email">电子邮箱</label>
            <input 
              type="email" 
              id="email" 
              v-model="formData.email"
              placeholder="请输入电子邮箱"
              required
            />
          </div>
        </div>
        
        <div class="form-row">
          <div class="form-group">
            <label for="password">密码</label>
            <input 
              type="password" 
              id="password" 
              v-model="formData.password"
              placeholder="请输入密码（至少6位）"
              required
              minlength="6"
            />
          </div>
        </div>
        
        <div class="form-row">
          <div class="form-group">
            <label for="confirmPassword">确认密码</label>
            <input 
              type="password" 
              id="confirmPassword" 
              v-model="formData.confirmPassword"
              placeholder="请再次输入密码"
              required
              minlength="6"
            />
          </div>
        </div>
        
        <div class="form-terms">
          <input type="checkbox" id="terms" v-model="agreeTerms" required />
          <label for="terms">
            我已阅读并同意 <a href="#" class="terms-link">《用户协议》</a> 和 <a href="#" class="terms-link">《隐私政策》</a>
          </label>
        </div>
        
        <button type="submit" class="btn btn-primary" :disabled="isLoading || !isFormValid">
          {{ isLoading ? '注册中...' : '立即注册' }}
        </button>
        
        <div class="form-footer">
          <p>已有账号？ <router-link to="/login" class="login-link">立即登录</router-link></p>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import axios from 'axios'

const router = useRouter()
const isLoading = ref(false)
const agreeTerms = ref(false)

const formData = ref({
  username: '',
  email: '',
  password: '',
  confirmPassword: ''
})

// 表单验证
const isFormValid = computed(() => {
  return (
    formData.value.username &&
    formData.value.email &&
    formData.value.password &&
    formData.value.password.length >= 6 &&
    formData.value.password === formData.value.confirmPassword &&
    agreeTerms.value
  )
})

const handleRegister = async () => {
  if (!isFormValid.value) return
  
  isLoading.value = true
  try {
    const response = await axios.post('http://localhost:5000/api/auth/register', {
      username: formData.value.username,
      email: formData.value.email,
      password: formData.value.password
    })
    
    alert('注册成功，请登录')
    router.push('/login')
  } catch (error) {
    alert(error.response?.data?.message || '注册失败，请稍后重试')
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
  max-width: 500px;
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

.form-row {
  display: flex;
  gap: 20px;
}

.form-group {
  flex: 1;
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

.form-terms {
  display: flex;
  align-items: flex-start;
  gap: 10px;
  font-size: 0.9rem;
  color: #666;
}

.form-terms input {
  margin-top: 4px;
}

.form-terms .terms-link {
  color: #8B4513;
  text-decoration: none;
  transition: color 0.3s ease;
}

.form-terms .terms-link:hover {
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

.login-link {
  color: #8B4513;
  text-decoration: none;
  font-weight: 600;
  transition: color 0.3s ease;
}

.login-link:hover {
  color: #654321;
  text-decoration: underline;
}

@media (max-width: 768px) {
  .form-row {
    flex-direction: column;
  }
  
  .auth-card {
    padding: 30px 20px;
  }
}
</style>
