// 等待DOM加载完成
 document.addEventListener('DOMContentLoaded', function() {
    // 移动端菜单切换
    const menuToggle = document.querySelector('.menu-toggle');
    const navLinks = document.querySelector('.nav-links');
    const loginRegister = document.querySelector('.login-register');
    
    menuToggle.addEventListener('click', function() {
        // 切换汉堡菜单样式
        const bars = document.querySelectorAll('.bar');
        bars[0].classList.toggle('active');
        bars[1].classList.toggle('active');
        bars[2].classList.toggle('active');
        
        // 切换导航栏显示/隐藏
        navLinks.classList.toggle('active');
        loginRegister.classList.toggle('active');
    });
    
    // 为汉堡菜单的bar添加active样式
    const style = document.createElement('style');
    style.textContent = `
        .bar.active:nth-child(1) {
            transform: translateY(8px) rotate(45deg);
        }
        .bar.active:nth-child(2) {
            opacity: 0;
        }
        .bar.active:nth-child(3) {
            transform: translateY(-8px) rotate(-45deg);
        }
        .nav-links.active,
        .login-register.active {
            display: flex;
        }
    `;
    document.head.appendChild(style);
    
    // 症状选择功能
    const symptomTags = document.querySelectorAll('.symptom-tags .tag');
    const selectedTagsContainer = document.getElementById('selected-tags');
    const analyzeBtn = document.getElementById('analyze-btn');
    const selectedSymptoms = [];
    
    symptomTags.forEach(tag => {
        tag.addEventListener('click', function() {
            // 切换选中状态
            this.classList.toggle('selected');
            
            const symptomText = this.textContent;
            const symptomIndex = selectedSymptoms.indexOf(symptomText);
            
            if (symptomIndex === -1) {
                // 添加到已选择症状
                selectedSymptoms.push(symptomText);
                addSelectedTag(symptomText);
            } else {
                // 从已选择症状中移除
                selectedSymptoms.splice(symptomIndex, 1);
                removeSelectedTag(symptomText);
            }
        });
    });
    
    // 添加选中的标签
    function addSelectedTag(text) {
        const tagElement = document.createElement('span');
        tagElement.className = 'tag selected';
        tagElement.textContent = text;
        tagElement.dataset.symptom = text;
        
        // 添加移除按钮
        const removeBtn = document.createElement('button');
        removeBtn.textContent = '×';
        removeBtn.className = 'remove-tag-btn';
        removeBtn.addEventListener('click', function(e) {
            e.stopPropagation();
            const symptomText = tagElement.dataset.symptom;
            const symptomIndex = selectedSymptoms.indexOf(symptomText);
            
            if (symptomIndex !== -1) {
                selectedSymptoms.splice(symptomIndex, 1);
                tagElement.remove();
                
                // 取消原标签的选中状态
                symptomTags.forEach(tag => {
                    if (tag.textContent === symptomText) {
                        tag.classList.remove('selected');
                    }
                });
            }
        });
        
        tagElement.appendChild(removeBtn);
        selectedTagsContainer.appendChild(tagElement);
        
        // 添加移除按钮样式
        const removeBtnStyle = document.createElement('style');
        removeBtnStyle.textContent = `
            .remove-tag-btn {
                margin-left: 8px;
                background: none;
                border: none;
                color: white;
                font-size: 18px;
                cursor: pointer;
                line-height: 1;
                padding: 0;
                width: 20px;
                height: 20px;
                display: inline-flex;
                align-items: center;
                justify-content: center;
                border-radius: 50%;
                background-color: rgba(255, 255, 255, 0.3);
            }
            .remove-tag-btn:hover {
                background-color: rgba(255, 255, 255, 0.5);
            }
        `;
        document.head.appendChild(removeBtnStyle);
    }
    
    // 移除选中的标签
    function removeSelectedTag(text) {
        const tags = selectedTagsContainer.querySelectorAll('.tag');
        tags.forEach(tag => {
            if (tag.dataset.symptom === text) {
                tag.remove();
            }
        });
    }
    
    // 分析按钮点击事件
    analyzeBtn.addEventListener('click', function() {
        if (selectedSymptoms.length === 0) {
            alert('请至少选择一个症状');
            return;
        }
        
        // 在实际应用中，这里会发送症状数据到后端进行分析
        alert('已选择症状：\n' + selectedSymptoms.join('\n') + '\n\n正在分析中...');
        
        // 模拟分析结果
        setTimeout(() => {
            alert('分析完成！\n\n根据您选择的症状，初步判断为：肝郁气滞证\n\n建议：\n1. 保持心情舒畅\n2. 适当运动\n3. 可考虑逍遥丸调理\n\n请前往智能诊断页面获取更详细的诊断。');
        }, 1500);
    });
    
    // 平滑滚动功能
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            
            const targetId = this.getAttribute('href');
            const targetElement = document.querySelector(targetId);
            
            if (targetElement) {
                window.scrollTo({
                    top: targetElement.offsetTop - 80, // 考虑导航栏高度
                    behavior: 'smooth'
                });
                
                // 如果是移动端，点击后关闭菜单
                if (navLinks.classList.contains('active')) {
                    navLinks.classList.remove('active');
                    loginRegister.classList.remove('active');
                    const bars = document.querySelectorAll('.bar');
                    bars.forEach(bar => bar.classList.remove('active'));
                }
            }
        });
    });
    
    // 诊断方法卡片点击事件
    const methodCards = document.querySelectorAll('.method-card');
    methodCards.forEach(card => {
        const button = card.querySelector('button');
        
        button.addEventListener('click', function(e) {
            e.stopPropagation();
            const cardTitle = card.querySelector('h3').textContent;
            
            // 在实际应用中，这里会跳转到对应的诊断页面
            alert(`即将进入${cardTitle}页面`);
        });
        
        card.addEventListener('click', function() {
            const cardTitle = card.querySelector('h3').textContent;
            alert(`您点击了${cardTitle}卡片`);
        });
    });
    
    // 知识卡片点击事件
    const knowledgeCards = document.querySelectorAll('.knowledge-card');
    knowledgeCards.forEach(card => {
        const readMore = card.querySelector('.read-more');
        
        readMore.addEventListener('click', function(e) {
            e.stopPropagation();
            const cardTitle = card.querySelector('h3').textContent;
            
            // 在实际应用中，这里会跳转到对应的知识详情页面
            alert(`即将进入${cardTitle}详情页面`);
        });
        
        card.addEventListener('click', function() {
            const cardTitle = card.querySelector('h3').textContent;
            alert(`您点击了${cardTitle}卡片`);
        });
    });
    
    // 响应式导航栏 - 在滚动时改变样式
    window.addEventListener('scroll', function() {
        const navbar = document.querySelector('.navbar');
        
        if (window.scrollY > 50) {
            navbar.style.backgroundColor = 'rgba(255, 255, 255, 1)';
            navbar.style.boxShadow = '0 2px 15px rgba(0, 0, 0, 0.1)';
            navbar.style.padding = '15px 0';
        } else {
            navbar.style.backgroundColor = 'rgba(255, 255, 255, 0.95)';
            navbar.style.boxShadow = '0 2px 10px rgba(0, 0, 0, 0.1)';
            navbar.style.padding = '20px 0';
        }
    });
    
    // 为登录和注册按钮添加点击事件
    const loginBtn = document.querySelector('.login-register a:first-child');
    const registerBtn = document.querySelector('.login-register a:last-child');
    
    loginBtn.addEventListener('click', function(e) {
        e.preventDefault();
        alert('即将进入登录页面');
    });
    
    registerBtn.addEventListener('click', function(e) {
        e.preventDefault();
        alert('即将进入注册页面');
    });
    
    // 初始化页面
    console.log('智慧中医平台前端脚本已加载');
});