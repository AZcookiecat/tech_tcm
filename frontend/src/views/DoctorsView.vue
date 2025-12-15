<template>
  <div class="doctors">
    <div class="container">
      <h1>名医推荐</h1>
      <div class="doctors-content">
        <div class="doctors-filter">
          <div class="search-box">
            <input type="text" placeholder="搜索医生姓名或专长" v-model="searchQuery" />
            <button class="search-btn">🔍</button>
          </div>
          <div class="specialty-filter">
            <div v-for="specialty in specialties" :key="specialty" class="specialty-tag" @click="toggleSpecialty(specialty)">
              {{ specialty }}
            </div>
          </div>
        </div>

        <div class="doctors-list">
          <div v-if="filteredDoctors.length > 0" class="doctors-grid">
            <div v-for="doctor in filteredDoctors" :key="doctor.id" class="doctor-card">
              <div class="doctor-avatar">
                <div class="avatar-placeholder">{{ doctor.name.charAt(0) }}</div>
              </div>
              <div class="doctor-info">
                <h3>{{ doctor.name }}</h3>
                <div class="doctor-title">{{ doctor.title }}</div>
                <div class="doctor-specialty">{{ doctor.specialty }}</div>
                <div class="doctor-stats">
                  <div class="stat">
                    <span class="stat-label">问诊次数</span>
                    <span class="stat-value">{{ doctor.consultations }}</span>
                  </div>
                  <div class="stat">
                    <span class="stat-label">好评率</span>
                    <span class="stat-value">{{ doctor.rating }}%</span>
                  </div>
                  <div class="stat">
                    <span class="stat-label">响应时间</span>
                    <span class="stat-value">{{ doctor.responseTime }}</span>
                  </div>
                </div>
                <div class="doctor-tags">
                  <span v-for="tag in doctor.tags" :key="tag" class="tag">{{ tag }}</span>
                </div>
                <button class="btn btn-primary" @click="consultDoctor(doctor.id)">立即咨询</button>
              </div>
            </div>
          </div>
          <div v-else class="no-doctors">
            <div class="empty-state">
              <span class="icon">👨⚕️</span>
              <h3>未找到匹配的医生</h3>
              <p>请尝试调整搜索条件或专长筛选</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'

const searchQuery = ref('')
const selectedSpecialties = ref([])

const specialties = ['中医内科', '中医外科', '中医妇科', '中医儿科', '针灸推拿', '中医骨伤', '中医养生']

const doctors = ref([
  {
    id: 1,
    name: '张医生',
    title: '主任医师',
    specialty: '中医内科',
    consultations: 1256,
    rating: 98,
    responseTime: '15分钟',
    tags: ['擅长脾胃', '经验丰富', '耐心细致']
  },
  {
    id: 2,
    name: '李医生',
    title: '副主任医师',
    specialty: '中医妇科',
    consultations: 987,
    rating: 96,
    responseTime: '20分钟',
    tags: ['擅长妇科调理', '月经不调', '不孕不育']
  },
  {
    id: 3,
    name: '王医生',
    title: '主治医师',
    specialty: '针灸推拿',
    consultations: 845,
    rating: 95,
    responseTime: '10分钟',
    tags: ['针灸减肥', '颈椎病', '腰椎间盘突出']
  },
  {
    id: 4,
    name: '赵医生',
    title: '主任医师',
    specialty: '中医儿科',
    consultations: 1123,
    rating: 97,
    responseTime: '25分钟',
    tags: ['小儿感冒', '消化不良', '体质调理']
  }
])

const toggleSpecialty = (specialty) => {
  const index = selectedSpecialties.value.indexOf(specialty)
  if (index > -1) {
    selectedSpecialties.value.splice(index, 1)
  } else {
    selectedSpecialties.value.push(specialty)
  }
}

const filteredDoctors = computed(() => {
  return doctors.value.filter(doctor => {
    const matchesSearch = doctor.name.toLowerCase().includes(searchQuery.value.toLowerCase()) || 
                        doctor.specialty.toLowerCase().includes(searchQuery.value.toLowerCase())
    const matchesSpecialty = selectedSpecialties.value.length === 0 || 
                           selectedSpecialties.value.includes(doctor.specialty)
    return matchesSearch && matchesSpecialty
  })
})

const consultDoctor = (id) => {
  console.log('Consult doctor:', id)
}
</script>

<style scoped>
.doctors {
  padding: 40px 20px;
  background: #f8f9fa;
  min-height: 100vh;
}

.container {
  max-width: 1200px;
  margin: 0 auto;
}

.doctors h1 {
  text-align: center;
  color: #333;
  margin-bottom: 40px;
  font-size: 2.5rem;
}

.doctors-content {
  background: white;
  padding: 40px;
  border-radius: 15px;
  box-shadow: 0 5px 20px rgba(0,0,0,0.1);
}

.doctors-filter {
  margin-bottom: 40px;
}

.search-box {
  display: flex;
  margin-bottom: 25px;
  max-width: 500px;
}

.search-box input {
  flex: 1;
  padding: 15px 20px;
  border: 2px solid #e0e0e0;
  border-radius: 8px 0 0 8px;
  font-size: 1rem;
  transition: all 0.3s ease;
}

.search-box input:focus {
  outline: none;
  border-color: #4caf50;
}

.search-btn {
  padding: 15px 25px;
  background: #4caf50;
  color: white;
  border: none;
  border-radius: 0 8px 8px 0;
  font-size: 1.2rem;
  cursor: pointer;
  transition: all 0.3s ease;
}

.search-btn:hover {
  background: #388e3c;
}

.specialty-filter {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
}

.specialty-tag {
  padding: 10px 20px;
  background: #f1f8e9;
  color: #43a047;
  border: 2px solid transparent;
  border-radius: 25px;
  cursor: pointer;
  font-size: 0.9rem;
  font-weight: 500;
  transition: all 0.3s ease;
}

.specialty-tag:hover {
  background: #e8f5e8;
  transform: translateY(-2px);
}

.specialty-tag:active {
  background: #4caf50;
  color: white;
  border-color: #4caf50;
}

.doctors-list {
  margin-top: 30px;
}

.doctors-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 25px;
}

.doctor-card {
  background: #f8f9fa;
  padding: 25px;
  border-radius: 12px;
  border: 1px solid #e0e0e0;
  transition: all 0.3s ease;
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
}

.doctor-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 10px 25px rgba(0,0,0,0.1);
  border-color: #4caf50;
}

.doctor-avatar {
  margin-bottom: 20px;
}

.avatar-placeholder {
  width: 100px;
  height: 100px;
  background: linear-gradient(135deg, #4caf50 0%, #2e7d32 100%);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-size: 2.5rem;
  font-weight: bold;
}

.doctor-info h3 {
  color: #333;
  margin-bottom: 5px;
  font-size: 1.3rem;
}

.doctor-title {
  color: #666;
  font-size: 0.9rem;
  margin-bottom: 10px;
}

.doctor-specialty {
  color: #4caf50;
  font-weight: 600;
  margin-bottom: 15px;
  font-size: 1rem;
}

.doctor-stats {
  display: flex;
  justify-content: space-around;
  margin-bottom: 15px;
  padding: 15px;
  background: white;
  border-radius: 8px;
  width: 100%;
}

.stat {
  display: flex;
  flex-direction: column;
  gap: 5px;
}

.stat-label {
  color: #666;
  font-size: 0.8rem;
}

.stat-value {
  color: #333;
  font-weight: 600;
  font-size: 1rem;
}

.doctor-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-bottom: 20px;
  justify-content: center;
}

.doctor-tags .tag {
  background: #e0e0e0;
  color: #666;
  padding: 5px 12px;
  border-radius: 15px;
  font-size: 0.8rem;
}

.btn-primary {
  padding: 10px 25px;
  background: #4caf50;
  color: white;
  border: none;
  border-radius: 8px;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  width: 100%;
}

.btn-primary:hover {
  background: #388e3c;
  transform: translateY(-2px);
  box-shadow: 0 5px 15px rgba(0,0,0,0.2);
}

.no-doctors {
  text-align: center;
  padding: 60px 20px;
}

.empty-state {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 20px;
  color: #666;
}

.empty-state .icon {
  font-size: 4rem;
  color: #ccc;
}

.empty-state h3 {
  color: #333;
  font-size: 1.5rem;
  margin-bottom: 10px;
}

.empty-state p {
  max-width: 400px;
  line-height: 1.6;
}
</style>
