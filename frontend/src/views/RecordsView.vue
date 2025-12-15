<template>
  <div class="records">
    <div class="container">
      <h1>病历记录</h1>
      <div class="records-content">
        <div class="records-filter">
          <div class="filter-group">
            <label for="date-filter">按时间筛选</label>
            <select id="date-filter" v-model="dateFilter">
              <option value="all">全部</option>
              <option value="week">最近一周</option>
              <option value="month">最近一个月</option>
              <option value="year">最近一年</option>
            </select>
          </div>
          <div class="filter-group">
            <label for="status-filter">按状态筛选</label>
            <select id="status-filter" v-model="statusFilter">
              <option value="all">全部</option>
              <option value="diagnosed">已诊断</option>
              <option value="pending">待诊断</option>
            </select>
          </div>
        </div>

        <div class="records-list">
          <div v-if="records.length > 0" class="records-grid">
            <div v-for="record in filteredRecords" :key="record.id" class="record-card">
              <div class="record-header">
                <div class="record-date">{{ record.date }}</div>
                <div :class="['record-status', record.status]">{{ record.statusText }}</div>
              </div>
              <div class="record-content">
                <h3>{{ record.title }}</h3>
                <div class="record-symptoms">
                  <span v-for="symptom in record.symptoms" :key="symptom" class="symptom-tag">{{ symptom }}</span>
                </div>
                <div class="record-doctor" v-if="record.doctor">
                  <span class="label">医生：</span>
                  <span>{{ record.doctor }}</span>
                </div>
              </div>
              <div class="record-actions">
                <button class="btn btn-primary" @click="viewRecord(record.id)">查看详情</button>
                <button class="btn btn-secondary" @click="exportRecord(record.id)">导出</button>
              </div>
            </div>
          </div>
          <div v-else class="no-records">
            <div class="empty-state">
              <span class="icon">📋</span>
              <h3>暂无病历记录</h3>
              <p>完成首次问诊后，您的诊断记录将显示在这里</p>
              <router-link to="/diagnosis" class="btn btn-primary">开始问诊</router-link>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'

const dateFilter = ref('all')
const statusFilter = ref('all')

const records = ref([
  {
    id: 1,
    date: '2025-12-10',
    title: '感冒问诊记录',
    symptoms: ['头痛', '发热', '咳嗽'],
    doctor: '张医生',
    status: 'diagnosed',
    statusText: '已诊断'
  },
  {
    id: 2,
    date: '2025-12-05',
    title: '失眠调理记录',
    symptoms: ['失眠', '乏力'],
    doctor: '李医生',
    status: 'diagnosed',
    statusText: '已诊断'
  },
  {
    id: 3,
    date: '2025-12-01',
    title: '胃痛问诊',
    symptoms: ['胃痛', '恶心'],
    status: 'pending',
    statusText: '待诊断'
  }
])

const filteredRecords = computed(() => {
  return records.value.filter(record => {
    const dateMatch = dateFilter.value === 'all' ? true : true
    const statusMatch = statusFilter.value === 'all' ? true : record.status === statusFilter.value
    return dateMatch && statusMatch
  })
})

const viewRecord = (id) => {
  console.log('View record:', id)
}

const exportRecord = (id) => {
  console.log('Export record:', id)
}
</script>

<style scoped>
.records {
  padding: 40px 20px;
  background: #f8f9fa;
  min-height: 100vh;
}

.container {
  max-width: 1200px;
  margin: 0 auto;
}

.records h1 {
  text-align: center;
  color: #333;
  margin-bottom: 40px;
  font-size: 2.5rem;
}

.records-content {
  background: white;
  padding: 40px;
  border-radius: 15px;
  box-shadow: 0 5px 20px rgba(0,0,0,0.1);
}

.records-filter {
  display: flex;
  gap: 30px;
  margin-bottom: 40px;
  padding-bottom: 20px;
  border-bottom: 2px solid #f0f0f0;
}

.filter-group {
  display: flex;
  flex-direction: column;
  gap: 10px;
  min-width: 150px;
}

.filter-group label {
  color: #333;
  font-weight: 500;
  font-size: 0.9rem;
}

.filter-group select {
  padding: 10px 15px;
  border: 2px solid #e0e0e0;
  border-radius: 8px;
  font-size: 1rem;
  background: white;
  cursor: pointer;
  transition: all 0.3s ease;
}

.filter-group select:hover {
  border-color: #4caf50;
}

.records-list {
  margin-top: 30px;
}

.records-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
  gap: 25px;
}

.record-card {
  background: #f8f9fa;
  padding: 25px;
  border-radius: 12px;
  border: 1px solid #e0e0e0;
  transition: all 0.3s ease;
}

.record-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 10px 25px rgba(0,0,0,0.1);
  border-color: #4caf50;
}

.record-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}

.record-date {
  color: #666;
  font-size: 0.9rem;
  font-weight: 500;
}

.record-status {
  padding: 5px 12px;
  border-radius: 15px;
  font-size: 0.8rem;
  font-weight: 600;
  text-transform: uppercase;
}

.record-status.diagnosed {
  background: #e8f5e8;
  color: #43a047;
}

.record-status.pending {
  background: #fff3e0;
  color: #fb8c00;
}

.record-content h3 {
  color: #333;
  margin-bottom: 15px;
  font-size: 1.2rem;
}

.record-symptoms {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-bottom: 15px;
}

.symptom-tag {
  background: #e0e0e0;
  color: #666;
  padding: 5px 12px;
  border-radius: 15px;
  font-size: 0.8rem;
}

.record-doctor {
  color: #666;
  font-size: 0.9rem;
  margin-bottom: 20px;
}

.record-doctor .label {
  font-weight: 600;
}

.record-actions {
  display: flex;
  gap: 10px;
}

.btn {
  padding: 8px 16px;
  border: none;
  border-radius: 8px;
  font-size: 0.9rem;
  font-weight: 600;
  text-decoration: none;
  cursor: pointer;
  transition: all 0.3s ease;
  flex: 1;
  text-align: center;
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

.no-records {
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
