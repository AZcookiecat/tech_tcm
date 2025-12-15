<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { isLoggedIn, getCurrentUser, clearLoginInfo } from './utils/auth'

const route = useRoute()
const router = useRouter()
const isMenuOpen = ref(false)
const isUserMenuOpen = ref(false)
const isAuthenticated = ref(isLoggedIn())
const currentUser = ref(getCurrentUser())

// 计算当前登录状态
const isLogged = computed(() => isAuthenticated.value)

// 获取当前用户信息
const user = computed(() => currentUser.value)

// 切换菜单
const toggleMenu = () => {
  isMenuOpen.value = !isMenuOpen.value
}

// 切换用户菜单
const toggleUserMenu = () => {
  isUserMenuOpen.value = !isUserMenuOpen.value
}

// 处理登出
const handleLogout = () => {
  clearLoginInfo()
  isAuthenticated.value = false
  currentUser.value = null
  isUserMenuOpen.value = false
  router.push('/')
}

// 初始化登录状态
onMounted(() => {
  isAuthenticated.value = isLoggedIn()
  currentUser.value = getCurrentUser()
})
</script>

<template>
  <div id="app">
    <!-- Navigation Bar -->
    <header class="navbar">
      <div class="container">
        <div class="navbar-brand">
          <router-link to="/" class="brand-link">
            <span class="brand-icon">🏥</span>
            <span class="brand-name">慧脉中医</span>
          </router-link>
        </div>
        
        <!-- Desktop Menu -->
        <nav class="navbar-nav">
          <router-link to="/" class="nav-link" :class="{ active: route.path === '/' }">首页</router-link>
          <router-link to="/diagnosis" class="nav-link" :class="{ active: route.path === '/diagnosis' }">智能问诊</router-link>
          <router-link to="/records" class="nav-link" :class="{ active: route.path === '/records' }">病历记录</router-link>
          <router-link to="/doctors" class="nav-link" :class="{ active: route.path === '/doctors' }">名医推荐</router-link>
          <router-link v-if="isLogged" to="/profile" class="nav-link" :class="{ active: route.path === '/profile' }">个人中心</router-link>
        </nav>
        
        <!-- Auth Section -->
        <div class="auth-section">
          <!-- 未登录状态 -->
          <div v-if="!isLogged" class="auth-buttons">
            <router-link to="/login" class="btn btn-outline">登录</router-link>
            <router-link to="/register" class="btn btn-primary">注册</router-link>
          </div>
          
          <!-- 已登录状态 -->
          <div v-else class="user-menu-container">
            <div class="user-info" @click="toggleUserMenu">
              <div class="user-avatar">
                <img src="/1761709868750.png" alt="用户头像" />
              </div>
              <span class="user-name">{{ user?.username }}</span>
              <span class="menu-arrow">▼</span>
            </div>
            
            <!-- 用户下拉菜单 -->
            <div v-if="isUserMenuOpen" class="user-dropdown-menu">
              <div class="dropdown-menu-item">
                <router-link to="/profile" @click="isUserMenuOpen = false">
                  <span class="menu-icon">👤</span>
                  <span>个人中心</span>
                </router-link>
              </div>
              <div class="dropdown-menu-item">
                <router-link to="/profile" @click="isUserMenuOpen = false">
                  <span class="menu-icon">📝</span>
                  <span>修改资料</span>
                </router-link>
              </div>
              <div class="dropdown-menu-item">
                <router-link to="/records" @click="isUserMenuOpen = false">
                  <span class="menu-icon">📋</span>
                  <span>我的病历</span>
                </router-link>
              </div>
              <div class="dropdown-menu-divider"></div>
              <div class="dropdown-menu-item logout" @click="handleLogout">
                <span class="menu-icon">🚪</span>
                <span>退出登录</span>
              </div>
            </div>
          </div>
        </div>
        
        <!-- Mobile Menu Toggle -->
        <button class="menu-toggle" @click="toggleMenu" aria-label="Toggle menu">
          <span class="menu-icon">☰</span>
        </button>
      </div>
    </header>
    
    <!-- Mobile Menu -->
    <div class="mobile-menu" v-if="isMenuOpen">
      <router-link to="/" class="mobile-link" :class="{ active: route.path === '/' }" @click="toggleMenu">首页</router-link>
      <router-link to="/diagnosis" class="mobile-link" :class="{ active: route.path === '/diagnosis' }" @click="toggleMenu">智能问诊</router-link>
      <router-link to="/records" class="mobile-link" :class="{ active: route.path === '/records' }" @click="toggleMenu">病历记录</router-link>
      <router-link to="/doctors" class="mobile-link" :class="{ active: route.path === '/doctors' }" @click="toggleMenu">名医推荐</router-link>
      
      <!-- 登录状态的菜单 -->
      <template v-if="isLogged">
        <router-link to="/profile" class="mobile-link" :class="{ active: route.path === '/profile' }" @click="toggleMenu">个人中心</router-link>
        <router-link to="/profile" class="mobile-link" @click="toggleMenu">修改资料</router-link>
        <div class="mobile-divider"></div>
        <div class="mobile-link logout-link" @click="handleLogout; toggleMenu">退出登录</div>
      </template>
      
      <!-- 未登录状态的菜单 -->
      <div v-else class="mobile-auth">
        <router-link to="/login" class="mobile-link btn btn-outline" @click="toggleMenu">登录</router-link>
        <router-link to="/register" class="mobile-link btn btn-primary" @click="toggleMenu">注册</router-link>
      </div>
    </div>
    
    <!-- Main Content -->
    <main class="main-content">
      <router-view />
    </main>
    
    <!-- Footer -->
    <footer class="footer">
      <div class="container">
        <div class="footer-content">
          <div class="footer-info">
            <h3>慧脉中医</h3>
            <p>传承中医智慧，科技赋能健康</p>
            <div class="footer-contact">
              <p>📞 400-123-4567</p>
              <p>📧 contact@huimai.com</p>
            </div>
          </div>
          <div class="footer-links">
            <h4>快速链接</h4>
            <ul>
              <li><router-link to="/">首页</router-link></li>
              <li><router-link to="/diagnosis">智能问诊</router-link></li>
              <li><router-link to="/doctors">名医推荐</router-link></li>
              <li><router-link to="/records">病历记录</router-link></li>
            </ul>
          </div>
          <div class="footer-links">
            <h4>关于我们</h4>
            <ul>
              <li><a href="#">公司介绍</a></li>
              <li><a href="#">隐私政策</a></li>
              <li><a href="#">服务条款</a></li>
              <li><a href="#">联系我们</a></li>
            </ul>
          </div>
        </div>
        <div class="footer-bottom">
          <p>&copy; 2025 慧脉中医. 保留所有权利.</p>
        </div>
      </div>
    </footer>
  </div>
</template>

<style>
/* Global Styles */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: 'Microsoft YaHei', 'SimSun', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  line-height: 1.6;
  color: #333;
  background-color: #faf8f5;
  background-image: linear-gradient(to right, rgba(220, 210, 190, 0.1) 0%, rgba(220, 210, 190, 0.1) 100%);
}

/* Container */
.container {
  width: 100%;
  max-width: 2000px;
  margin: 0 auto;
  padding: 0 20px;
}

/* Navigation Bar */
.navbar {
  background: linear-gradient(135deg, #8B4513 0%, #654321 100%);
  color: #fff;
  padding: 15px 20px;
  box-shadow: 0 2px 15px rgba(139, 69, 19, 0.3);
  position: sticky;
  top: 0;
  z-index: 1000;
  width: 100%;
  margin: 0;
  left: 0;
  right: 0;
}

.navbar .container {
  display: flex;
  justify-content: space-between;
  align-items: center;
  max-width: 1400px;
  margin: 0 auto;
  padding: 0;
}

.navbar-brand {
  display: flex;
  align-items: center;
}

.brand-link {
  display: flex;
  align-items: center;
  color: #fff;
  text-decoration: none;
  font-size: 1.6rem;
  font-weight: 700;
  font-family: 'SimSun', serif;
  letter-spacing: 2px;
}

.brand-icon {
  margin-right: 12px;
  font-size: 2rem;
}

.navbar-nav {
  display: flex;
  gap: 35px;
}

.nav-link {
  color: #fff;
  text-decoration: none;
  font-weight: 500;
  padding: 10px 20px;
  border-radius: 25px;
  transition: all 0.3s ease;
  position: relative;
  font-family: 'Microsoft YaHei', sans-serif;
  letter-spacing: 0.5px;
}

.nav-link:hover,
.nav-link.active {
  background: rgba(255, 255, 255, 0.15);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
  transform: translateY(-2px);
}

/* Auth Buttons */
.auth-buttons {
  display: flex;
  gap: 15px;
  align-items: center;
}

.btn {
  padding: 10px 20px;
  border: none;
  border-radius: 25px;
  font-size: 0.95rem;
  font-weight: 600;
  text-decoration: none;
  cursor: pointer;
  transition: all 0.3s ease;
  letter-spacing: 0.5px;
  font-family: 'Microsoft YaHei', sans-serif;
}

.btn-primary {
  background: #fff;
  color: #8B4513;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
}

.btn-primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.3);
}

.btn-outline {
  background: transparent;
  color: #fff;
  border: 2px solid #fff;
}

.btn-outline:hover {
  background: rgba(255, 255, 255, 0.15);
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
}

/* Mobile Menu */
.menu-toggle {
  display: none;
  background: transparent;
  border: 2px solid #fff;
  color: #fff;
  font-size: 1.5rem;
  cursor: pointer;
  padding: 8px 12px;
  border-radius: 8px;
  transition: all 0.3s ease;
}

.menu-toggle:hover {
  background: rgba(255, 255, 255, 0.1);
}

.mobile-menu {
  display: none;
  background: linear-gradient(135deg, #8B4513 0%, #654321 100%);
  padding: 20px 0;
  box-shadow: 0 5px 15px rgba(139, 69, 19, 0.3);
  width: 100%;
}

.mobile-link {
  display: block;
  color: #fff;
  text-decoration: none;
  padding: 15px 20px;
  font-weight: 500;
  transition: all 0.3s ease;
  text-align: center;
  font-family: 'Microsoft YaHei', sans-serif;
}

.mobile-link:hover,
.mobile-link.active {
  background: rgba(255, 255, 255, 0.15);
}

/* Mobile Auth */
.mobile-auth {
  display: flex;
  gap: 15px;
  padding: 20px;
  margin-top: 10px;
  border-top: 1px solid rgba(255, 255, 255, 0.2);
}

.mobile-auth .mobile-link {
  flex: 1;
  text-align: center;
  padding: 12px;
  border-radius: 8px;
}

.mobile-auth .btn-outline {
  flex: 1;
}

.mobile-auth .btn-primary {
  flex: 1;
}

/* Auth Section */
.auth-section {
  display: flex;
  align-items: center;
}

/* User Menu */
.user-menu-container {
  position: relative;
}

.user-info {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 10px 15px;
  border-radius: 25px;
  cursor: pointer;
  transition: all 0.3s ease;
  background: rgba(255, 255, 255, 0.1);
  color: white;
}

.user-info:hover {
  background: rgba(255, 255, 255, 0.2);
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
}

.user-avatar {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  overflow: hidden;
  flex-shrink: 0;
  border: 2px solid white;
}

.user-avatar img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.user-name {
  font-weight: 600;
  font-size: 0.95rem;
  white-space: nowrap;
}

.menu-arrow {
  font-size: 0.8rem;
  transition: transform 0.3s ease;
}

.user-info:hover .menu-arrow {
  transform: rotate(180deg);
}

/* User Dropdown Menu */
.user-dropdown-menu {
  position: absolute;
  top: 100%;
  right: 0;
  margin-top: 10px;
  background: white;
  border-radius: 12px;
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.2);
  width: 200px;
  z-index: 1001;
}

.dropdown-menu-item {
  padding: 12px 15px;
  cursor: pointer;
  transition: all 0.3s ease;
}

.dropdown-menu-item a {
  display: flex;
  align-items: center;
  gap: 12px;
  color: #333;
  text-decoration: none;
  width: 100%;
  font-weight: 500;
  font-size: 0.95rem;
}

.dropdown-menu-item:hover {
  background: #f5f0e5;
}

.dropdown-menu-item.logout:hover {
  background: #ffebee;
}

.dropdown-menu-item.logout a,
.dropdown-menu-item.logout span {
  color: #d32f2f;
}

.menu-icon {
  font-size: 1.1rem;
  flex-shrink: 0;
}

.dropdown-menu-divider {
  height: 1px;
  background: #e0e0e0;
  margin: 8px 0;
}

/* Mobile Menu Updates */
.mobile-divider {
  height: 1px;
  background: rgba(255, 255, 255, 0.2);
  margin: 10px 20px;
}

.logout-link {
  color: #fff;
  cursor: pointer;
}

.logout-link:hover {
  background: rgba(221, 46, 68, 0.2) !important;
  color: #fff;
}

/* Responsive Design */
@media (max-width: 768px) {
  .auth-section {
    display: none;
  }
}

/* Main Content */
.main-content {
  min-height: calc(100vh - 200px);
}

/* Footer */
.footer {
  background: linear-gradient(135deg, #8B4513 0%, #654321 100%);
  color: #fff;
  padding: 50px 20px 20px;
  width: 100%;
  margin-top: 60px;
  margin: 60px 0 0 0;
  left: 0;
  right: 0;
}

.footer .container {
  max-width: 1400px;
  margin: 0 auto;
  padding: 0;
}

.footer-content {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 40px;
  margin-bottom: 40px;
  max-width: 1400px;
  margin-left: auto;
  margin-right: auto;
}

.footer-info h3 {
  font-size: 1.5rem;
  margin-bottom: 20px;
  color: #fff;
  font-family: 'SimSun', serif;
  letter-spacing: 2px;
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
}

.footer-info p {
  margin-bottom: 12px;
  color: rgba(255, 255, 255, 0.9);
  line-height: 1.8;
}

.footer-contact p {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 10px;
  color: rgba(255, 255, 255, 0.9);
}

.footer-links h4 {
  font-size: 1.2rem;
  margin-bottom: 20px;
  color: #fff;
  font-family: 'Microsoft YaHei', sans-serif;
  letter-spacing: 1px;
  border-bottom: 2px solid rgba(255, 255, 255, 0.2);
  padding-bottom: 10px;
}

.footer-links ul {
  list-style: none;
}

.footer-links li {
  margin-bottom: 12px;
}

.footer-links a {
  color: rgba(255, 255, 255, 0.9);
  text-decoration: none;
  transition: all 0.3s ease;
  display: inline-block;
  padding: 5px 0;
  border-bottom: 1px solid transparent;
}

.footer-links a:hover {
  color: #fff;
  border-bottom-color: #fff;
  transform: translateX(5px);
}

.footer-bottom {
  text-align: center;
  padding-top: 30px;
  border-top: 1px solid rgba(255, 255, 255, 0.2);
  color: rgba(255, 255, 255, 0.8);
  font-size: 0.95rem;
  font-family: 'Microsoft YaHei', sans-serif;
  max-width: 1400px;
  margin-left: auto;
  margin-right: auto;
}

/* Responsive Design */
@media (max-width: 768px) {
  .navbar-nav {
    display: none;
  }
  
  .menu-toggle {
    display: block;
  }
  
  .mobile-menu {
    display: block;
  }
  
  .brand-name {
    font-size: 1.2rem;
  }
  
  .footer-content {
    grid-template-columns: 1fr;
    text-align: center;
  }
}
</style>
