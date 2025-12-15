<template>
  <div class="home">
    <!-- Introduction Section -->
    <section class="introduction">
      <div class="container">
        <div class="intro-content">
          <div class="intro-text">
            <p class="intro-subtitle">传承千年中医智慧</p>
            <h2 class="intro-title">融合现代科技，守护您的健康</h2>
            <p class="intro-description">
              慧脉中医平台将传统中医理论与现代人工智能技术相结合，为您提供专业、便捷的中医健康管理服务。
              通过智能问诊、名医推荐、病历管理等功能，让中医诊疗触手可及，为您的健康保驾护航。
            </p>
            <div class="intro-buttons">
              <router-link to="/diagnosis" class="btn btn-primary">智能问诊</router-link>
              <router-link to="/doctors" class="btn btn-secondary">名医咨询</router-link>
              <router-link to="/records" class="btn btn-tertiary">病历管理</router-link>
            </div>
          </div>
          <div class="intro-visual">
            <div class="visual-container">
              <div class="visual-element">
                <span class="visual-icon">🌿</span>
                <div class="visual-text">中医辨证</div>
              </div>
              <div class="visual-element">
                <span class="visual-icon">📊</span>
                <div class="visual-text">智能分析</div>
              </div>
              <div class="visual-element">
                <span class="visual-icon">👨⚕️</span>
                <div class="visual-text">专家指导</div>
              </div>
              <div class="visual-element">
                <span class="visual-icon">📱</span>
                <div class="visual-text">便捷管理</div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Features Section -->
    <section class="features">
      <div class="container">
        <div class="section-header">
          <h2 class="section-title">核心服务</h2>
          <p class="section-subtitle">专业中医健康管理服务，全方位呵护您的健康</p>
        </div>
        <div class="features-grid">
          <div class="feature-card">
            <div class="feature-icon">
              <span class="icon">🔍</span>
            </div>
            <h3>智能问诊</h3>
            <p>基于中医四诊理论，结合现代AI技术，快速分析您的症状，提供初步诊断建议</p>
          </div>
          <div class="feature-card">
            <div class="feature-icon">
              <span class="icon">📋</span>
            </div>
            <h3>电子病历</h3>
            <p>安全存储您的诊断记录，随时查看历史诊疗信息，方便医生全面了解您的健康状况</p>
          </div>
          <div class="feature-card">
            <div class="feature-icon">
              <span class="icon">👨⚕️</span>
            </div>
            <h3>名医推荐</h3>
            <p>汇聚全国知名中医专家，提供在线咨询服务，让您足不出户享受优质医疗资源</p>
          </div>
          <div class="feature-card">
            <div class="feature-icon">
              <span class="icon">🌿</span>
            </div>
            <h3>中药调理</h3>
            <p>根据诊断结果，提供个性化中药处方建议，结合现代药剂学，确保用药安全有效</p>
          </div>
          <div class="feature-card">
            <div class="feature-icon">
              <span class="icon">💡</span>
            </div>
            <h3>健康科普</h3>
            <p>提供丰富的中医健康知识，包括养生保健、食疗调理、节气养生等实用内容</p>
          </div>
          <div class="feature-card">
            <div class="feature-icon">
              <span class="icon">📊</span>
            </div>
            <h3>健康监测</h3>
            <p>长期跟踪您的健康状况，生成健康报告，帮助您了解身体变化，预防疾病发生</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Philosophy Section -->
    <section class="philosophy">
      <div class="container">
        <div class="philosophy-content">
          <div class="philosophy-image">
            <div class="image-container">
              <span class="philosophy-icon">📜</span>
            </div>
          </div>
          <div class="philosophy-text">
            <h2 class="philosophy-title">中医理念</h2>
            <p class="philosophy-description">
              中医强调"天人合一"、"辨证论治"，注重整体观念和个体化治疗。慧脉中医平台秉承这一理念，
              结合现代科技手段，为用户提供更加精准、便捷的中医健康管理服务。
            </p>
            <div class="philosophy-points">
              <div class="philosophy-point">
                <span class="point-icon">✨</span>
                <span class="point-text">整体观念：从全身状况出发，综合分析病情</span>
              </div>
              <div class="philosophy-point">
                <span class="point-icon">✨</span>
                <span class="point-text">辨证论治：根据个体差异，制定个性化治疗方案</span>
              </div>
              <div class="philosophy-point">
                <span class="point-icon">✨</span>
                <span class="point-text">预防为主：强调未病先防，既病防变</span>
              </div>
              <div class="philosophy-point">
                <span class="point-icon">✨</span>
                <span class="point-text">自然疗法：推崇中药、针灸、推拿等自然治疗方法</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
</script>

<style scoped>
.home {
  font-family: 'Microsoft YaHei', 'SimSun', sans-serif;
  width: 100%;
  overflow-x: hidden;
}

/* Introduction Section */
.introduction {
  padding: 60px 20px;
  background: linear-gradient(135deg, #faf8f5 0%, #f5f0e5 100%);
  position: relative;
  width: 100%;
}

.introduction::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-image: 
    radial-gradient(circle at 20% 30%, rgba(139, 69, 19, 0.05) 0%, transparent 50%),
    radial-gradient(circle at 80% 70%, rgba(139, 69, 19, 0.05) 0%, transparent 50%);
  pointer-events: none;
}

.container {
  width: 100%;
  max-width: 1400px;
  margin: 0 auto;
  padding: 0 20px;
  position: relative;
  z-index: 1;
}

.intro-content {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 80px;
  align-items: center;
}

.intro-text {
  display: flex;
  flex-direction: column;
  gap: 25px;
}

.intro-subtitle {
  color: #8B4513;
  font-size: 1.1rem;
  font-weight: 600;
  font-family: 'SimSun', serif;
  letter-spacing: 1px;
  margin: 0;
}

.intro-title {
  font-size: 2.8rem;
  font-weight: 700;
  color: #333;
  line-height: 1.3;
  margin: 0;
  font-family: 'Microsoft YaHei', sans-serif;
}

.intro-description {
  font-size: 1.15rem;
  color: #666;
  line-height: 1.8;
  margin: 0;
}

.intro-buttons {
  display: flex;
  gap: 15px;
  flex-wrap: wrap;
  margin-top: 10px;
}

.btn {
  padding: 14px 28px;
  border: none;
  border-radius: 30px;
  font-size: 1rem;
  font-weight: 600;
  text-decoration: none;
  cursor: pointer;
  transition: all 0.3s ease;
  min-width: 140px;
  display: inline-block;
  text-align: center;
  font-family: 'Microsoft YaHei', sans-serif;
  letter-spacing: 0.5px;
}

.btn-primary {
  background: linear-gradient(135deg, #8B4513 0%, #654321 100%);
  color: #fff;
  box-shadow: 0 4px 15px rgba(139, 69, 19, 0.3);
}

.btn-primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(139, 69, 19, 0.4);
}

.btn-secondary {
  background: transparent;
  color: #8B4513;
  border: 2px solid #8B4513;
}

.btn-secondary:hover {
  background: rgba(139, 69, 19, 0.1);
  transform: translateY(-2px);
  box-shadow: 0 4px 15px rgba(139, 69, 19, 0.2);
}

.btn-tertiary {
  background: transparent;
  color: #8B4513;
  border: 2px solid #8B4513;
}

.btn-tertiary:hover {
  background: rgba(139, 69, 19, 0.1);
  transform: translateY(-2px);
  box-shadow: 0 4px 15px rgba(139, 69, 19, 0.2);
}

.intro-visual {
  display: flex;
  justify-content: center;
  align-items: center;
}

.visual-container {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 30px;
  padding: 40px;
  background: rgba(255, 255, 255, 0.6);
  border-radius: 20px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.8);
}

.visual-element {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 15px;
  padding: 25px;
  background: #fff;
  border-radius: 15px;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.08);
  transition: all 0.3s ease;
}

.visual-element:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.15);
}

.visual-icon {
  font-size: 2.5rem;
}

.visual-text {
  font-size: 1.1rem;
  font-weight: 600;
  color: #333;
  font-family: 'Microsoft YaHei', sans-serif;
}

/* Features Section */
.features {
  padding: 80px 20px;
  background: #fff;
  width: 100%;
}

.section-header {
  text-align: center;
  margin-bottom: 60px;
  display: flex;
  flex-direction: column;
  gap: 15px;
}

.section-title {
  font-size: 2.5rem;
  font-weight: 700;
  color: #333;
  margin: 0;
  font-family: 'SimSun', serif;
  letter-spacing: 1px;
}

.section-subtitle {
  font-size: 1.1rem;
  color: #666;
  margin: 0;
  line-height: 1.6;
}

.features-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
  gap: 35px;
}

.feature-card {
  background: #faf8f5;
  padding: 40px 35px;
  border-radius: 18px;
  text-align: center;
  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.08);
  transition: all 0.3s ease;
  border: 1px solid rgba(139, 69, 19, 0.1);
}

.feature-card:hover {
  transform: translateY(-8px);
  box-shadow: 0 12px 35px rgba(0, 0, 0, 0.15);
  border-color: rgba(139, 69, 19, 0.3);
}

.feature-icon {
  width: 90px;
  height: 90px;
  margin: 0 auto 25px;
  background: linear-gradient(135deg, #8B4513 0%, #654321 100%);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 2.2rem;
  box-shadow: 0 6px 15px rgba(139, 69, 19, 0.3);
}

.feature-card h3 {
  font-size: 1.4rem;
  color: #333;
  margin-bottom: 18px;
  font-weight: 600;
  font-family: 'Microsoft YaHei', sans-serif;
}

.feature-card p {
  color: #666;
  line-height: 1.7;
  font-size: 1rem;
  margin: 0;
}

/* Philosophy Section */
.philosophy {
  padding: 80px 20px;
  background: linear-gradient(135deg, #f5f0e5 0%, #faf8f5 100%);
  width: 100%;
}

.philosophy-content {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 80px;
  align-items: center;
}

.philosophy-image {
  display: flex;
  justify-content: center;
  align-items: center;
}

.image-container {
  width: 350px;
  height: 350px;
  background: linear-gradient(135deg, #8B4513 0%, #654321 100%);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 10px 30px rgba(139, 69, 19, 0.4);
  position: relative;
}

.image-container::before {
  content: '';
  position: absolute;
  width: 100%;
  height: 100%;
  border-radius: 50%;
  background: radial-gradient(circle at 30% 30%, rgba(255, 255, 255, 0.1) 0%, transparent 50%);
}

.philosophy-icon {
  font-size: 8rem;
  position: relative;
  z-index: 1;
}

.philosophy-text {
  display: flex;
  flex-direction: column;
  gap: 25px;
}

.philosophy-title {
  font-size: 2.5rem;
  font-weight: 700;
  color: #333;
  margin: 0;
  font-family: 'SimSun', serif;
  letter-spacing: 1px;
}

.philosophy-description {
  font-size: 1.15rem;
  color: #666;
  line-height: 1.8;
  margin: 0;
}

.philosophy-points {
  display: flex;
  flex-direction: column;
  gap: 18px;
}

.philosophy-point {
  display: flex;
  align-items: flex-start;
  gap: 15px;
  padding: 15px;
  background: rgba(255, 255, 255, 0.6);
  border-radius: 10px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
}

.point-icon {
  font-size: 1.3rem;
  color: #8B4513;
  margin-top: 2px;
  flex-shrink: 0;
}

.point-text {
  font-size: 1.05rem;
  color: #555;
  line-height: 1.6;
  margin: 0;
}

/* Responsive Design */
@media (max-width: 1024px) {
  .intro-content,
  .philosophy-content {
    grid-template-columns: 1fr;
    gap: 60px;
  }
  
  .intro-visual,
  .philosophy-image {
    order: -1;
  }
  
  .features-grid {
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 25px;
  }
}

@media (max-width: 768px) {
  .intro-title,
  .section-title,
  .philosophy-title {
    font-size: 2rem;
  }
  
  .intro-buttons {
    flex-direction: column;
    align-items: stretch;
  }
  
  .btn {
    width: 100%;
  }
  
  .visual-container {
    grid-template-columns: 1fr;
    gap: 20px;
    padding: 30px 20px;
  }
  
  .visual-element {
    padding: 20px;
  }
  
  .image-container {
    width: 250px;
    height: 250px;
  }
  
  .philosophy-icon {
    font-size: 6rem;
  }
}
</style>
