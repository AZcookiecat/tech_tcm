<template>
  <div class="diagnosis">
    <div class="container">
      <h1>智能问诊</h1>
      <div class="diagnosis-steps">
        <div class="step-indicator">
          <div class="step active">1. 症状选择</div>
          <div class="step">2. 详细描述</div>
          <div class="step">3. 诊断结果</div>
        </div>

        <div class="diagnosis-content">
          <div class="symptom-selection">
            <h2>请选择您的主要症状</h2>
            <div class="symptom-categories">
              <div class="category">
                <h3>常见症状</h3>
                <div class="symptoms-grid">
                  <div v-for="symptom in commonSymptoms" :key="symptom.id" class="symptom-tag" @click="toggleSymptom(symptom)">
                    {{ symptom.name }}
                  </div>
                </div>
              </div>
              <div class="category">
                <h3>其他症状</h3>
                <div class="symptoms-grid">
                  <div v-for="symptom in otherSymptoms" :key="symptom.id" class="symptom-tag" @click="toggleSymptom(symptom)">
                    {{ symptom.name }}
                  </div>
                </div>
              </div>
            </div>
          </div>

          <div class="selected-symptoms">
            <h3>已选择症状</h3>
            <div class="selected-tags" v-if="selectedSymptoms.length > 0">
              <div v-for="symptom in selectedSymptoms" :key="symptom.id" class="selected-tag">
                {{ symptom.name }}
                <span class="remove-tag" @click="removeSymptom(symptom)">&times;</span>
              </div>
            </div>
            <p v-else class="no-symptoms">请选择您的症状</p>
          </div>

          <div class="diagnosis-actions">
            <router-link to="/" class="btn btn-secondary">取消</router-link>
            <button class="btn btn-primary" :disabled="selectedSymptoms.length === 0" @click="nextStep">下一步</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const selectedSymptoms = ref([])

const commonSymptoms = [
  { id: 1, name: '头痛' },
  { id: 2, name: '发热' },
  { id: 3, name: '咳嗽' },
  { id: 4, name: '乏力' },
  { id: 5, name: '失眠' },
  { id: 6, name: '胃痛' },
  { id: 7, name: '腹泻' },
  { id: 8, name: '便秘' }
]

const otherSymptoms = [
  { id: 9, name: '鼻塞' },
  { id: 10, name: '流涕' },
  { id: 11, name: '咽痛' },
  { id: 12, name: '恶心' },
  { id: 13, name: '呕吐' },
  { id: 14, name: '关节痛' },
  { id: 15, name: '胸闷' },
  { id: 16, name: '心悸' }
]

const toggleSymptom = (symptom) => {
  const index = selectedSymptoms.value.findIndex(s => s.id === symptom.id)
  if (index > -1) {
    selectedSymptoms.value.splice(index, 1)
  } else {
    selectedSymptoms.value.push(symptom)
  }
}

const removeSymptom = (symptom) => {
  const index = selectedSymptoms.value.findIndex(s => s.id === symptom.id)
  if (index > -1) {
    selectedSymptoms.value.splice(index, 1)
  }
}

const nextStep = () => {
  // 这里可以添加下一步逻辑
  console.log('Selected symptoms:', selectedSymptoms.value)
}
</script>

<style scoped>
.diagnosis {
  padding: 40px 20px;
  background: #f8f9fa;
  min-height: 100vh;
}

.container {
  max-width: 1200px;
  margin: 0 auto;
}

.diagnosis h1 {
  text-align: center;
  color: #333;
  margin-bottom: 40px;
  font-size: 2.5rem;
}

.step-indicator {
  display: flex;
  justify-content: center;
  margin-bottom: 50px;
  background: white;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 2px 10px rgba(0,0,0,0.1);
}

.step {
  flex: 1;
  text-align: center;
  padding: 15px;
  color: #666;
  font-weight: 500;
  position: relative;
}

.step::after {
  content: '';
  position: absolute;
  top: 50%;
  right: -50%;
  width: 100%;
  height: 2px;
  background: #e0e0e0;
  transform: translateY(-50%);
  z-index: 1;
}

.step:last-child::after {
  display: none;
}

.step.active {
  color: #4caf50;
  font-weight: 700;
}

.step.active::before {
  content: '';
  position: absolute;
  top: 50%;
  left: 50%;
  width: 20px;
  height: 20px;
  background: #4caf50;
  border-radius: 50%;
  transform: translate(-50%, -50%);
  z-index: 2;
}

.diagnosis-content {
  background: white;
  padding: 40px;
  border-radius: 15px;
  box-shadow: 0 5px 20px rgba(0,0,0,0.1);
}

.symptom-selection h2 {
  color: #333;
  margin-bottom: 30px;
  text-align: center;
  font-size: 1.8rem;
}

.symptom-categories {
  margin-bottom: 40px;
}

.category {
  margin-bottom: 30px;
}

.category h3 {
  color: #4caf50;
  margin-bottom: 20px;
  font-size: 1.3rem;
  border-bottom: 2px solid #e8f5e8;
  padding-bottom: 10px;
}

.symptoms-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(150px, 1fr));
  gap: 15px;
}

.symptom-tag {
  background: #f1f8e9;
  color: #43a047;
  padding: 12px 20px;
  border-radius: 30px;
  text-align: center;
  cursor: pointer;
  transition: all 0.3s ease;
  border: 2px solid transparent;
}

.symptom-tag:hover {
  background: #e8f5e8;
  transform: translateY(-2px);
  box-shadow: 0 5px 15px rgba(0,0,0,0.1);
}

.symptom-tag:active {
  background: #c8e6c9;
  border-color: #4caf50;
}

.selected-symptoms {
  margin-bottom: 40px;
  padding: 20px;
  background: #f8f9fa;
  border-radius: 10px;
}

.selected-symptoms h3 {
  color: #333;
  margin-bottom: 20px;
  font-size: 1.2rem;
}

.selected-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
}

.selected-tag {
  background: #4caf50;
  color: white;
  padding: 10px 15px;
  border-radius: 25px;
  display: flex;
  align-items: center;
  gap: 10px;
  font-size: 0.9rem;
}

.remove-tag {
  cursor: pointer;
  font-size: 1.2rem;
  font-weight: bold;
  transition: opacity 0.3s ease;
}

.remove-tag:hover {
  opacity: 0.8;
}

.no-symptoms {
  color: #999;
  text-align: center;
  padding: 20px;
}

.diagnosis-actions {
  display: flex;
  justify-content: flex-end;
  gap: 20px;
  margin-top: 40px;
}

.btn {
  padding: 12px 30px;
  border: none;
  border-radius: 50px;
  font-size: 1rem;
  font-weight: 600;
  text-decoration: none;
  cursor: pointer;
  transition: all 0.3s ease;
  min-width: 120px;
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

.btn-primary:disabled {
  background: #c8e6c9;
  cursor: not-allowed;
  transform: none;
  box-shadow: none;
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
</style>
