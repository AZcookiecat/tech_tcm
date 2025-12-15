// 认证工具函数

// 获取当前用户信息
export const getCurrentUser = () => {
  const user = localStorage.getItem('user')
  return user ? JSON.parse(user) : null
}

// 获取访问令牌
export const getAccessToken = () => {
  return localStorage.getItem('access_token')
}

// 获取刷新令牌
export const getRefreshToken = () => {
  return localStorage.getItem('refresh_token')
}

// 检查是否已登录
export const isLoggedIn = () => {
  return !!getAccessToken() && !!getCurrentUser()
}

// 保存登录信息
export const saveLoginInfo = (accessToken, refreshToken, user) => {
  localStorage.setItem('access_token', accessToken)
  localStorage.setItem('refresh_token', refreshToken)
  localStorage.setItem('user', JSON.stringify(user))
}

// 清除登录信息
export const clearLoginInfo = () => {
  localStorage.removeItem('access_token')
  localStorage.removeItem('refresh_token')
  localStorage.removeItem('user')
}

// 更新用户信息
export const updateUserInfo = (userData) => {
  const currentUser = getCurrentUser()
  if (currentUser) {
    const updatedUser = { ...currentUser, ...userData }
    localStorage.setItem('user', JSON.stringify(updatedUser))
    return updatedUser
  }
  return null
}
