/**
 * UI Module - Handles all UI interactions and DOM updates
 */

class MagicBallUI {
    constructor() {
        this.domElements = {};
        this.init();
    }

    async init() {
        this.cacheDOMElements();
        this.setupEventListeners();
        this.applyTheme();
        await this.loadThemes();
        await this.loadAchievements();
        this.updateStats();
    }

    cacheDOMElements() {
        const ids = [
            'magicBall', 'answerText', 'answerType',
            'questionInput', 'responsePack', 'askBtn', 'clearBtn', 'shareBtn',
            'themeToggleBtn', 'soundToggleBtn', 'historyBtn', 'achievementsBtn',
            'themeModal', 'historyModal', 'achievementsModal', 'modalOverlay',
            'closeThemeModal', 'closeHistoryModal', 'closeAchievementsModal',
            'themeGrid', 'historyList', 'clearHistoryBtn', 'historySearch',
            'charCount', 'totalQuestions', 'dailyCount', 'favoriteCount',
            'achievementToast', 'achievementIcon', 'achievementName', 'achievementDesc',
            'achievementsGrid'
        ];

        ids.forEach(id => {
            const el = document.getElementById(id);
            if (el) {
                this.domElements[id] = el;
            }
        });
    }

    setupEventListeners() {
        this.domElements.questionInput?.addEventListener('input', (e) => {
            this.updateCharCount();
            if (e.key === 'Enter' && !game.isAsking) {
                this.askQuestion();
            }
        });

        this.domElements.questionInput?.addEventListener('keypress', (e) => {
            if (e.key === 'Enter' && !game.isAsking) {
                this.askQuestion();
            }
        });

        this.domElements.askBtn?.addEventListener('click', () => this.askQuestion());
        this.domElements.clearBtn?.addEventListener('click', () => this.clearQuestion());
        this.domElements.shareBtn?.addEventListener('click', () => this.shareResult());
        this.domElements.themeToggleBtn?.addEventListener('click', () => this.toggleThemeModal());
        this.domElements.soundToggleBtn?.addEventListener('click', () => this.toggleSound());
        this.domElements.historyBtn?.addEventListener('click', () => this.toggleHistoryModal());
        this.domElements.achievementsBtn?.addEventListener('click', () => this.toggleAchievementsModal());

        this.domElements.closeThemeModal?.addEventListener('click', () => this.closeModal('themeModal'));
        this.domElements.closeHistoryModal?.addEventListener('click', () => this.closeModal('historyModal'));
        this.domElements.closeAchievementsModal?.addEventListener('click', () => this.closeModal('achievementsModal'));
        this.domElements.modalOverlay?.addEventListener('click', () => this.closeAllModals());

        this.domElements.historySearch?.addEventListener('input', (e) => {
            this.filterHistory(e.target.value);
        });

        this.domElements.clearHistoryBtn?.addEventListener('click', () => {
            if (confirm('Clear all history? This cannot be undone.')) {
                game.clearHistory();
                this.updateStats();
                this.updateHistory();
            }
        });

        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape') {
                this.closeAllModals();
            }
        });
    }

    updateCharCount() {
        const count = this.domElements.questionInput?.value.length || 0;
        if (this.domElements.charCount) {
            this.domElements.charCount.textContent = count;
        }
    }

    async askQuestion() {
        const question = this.domElements.questionInput?.value.trim();

        if (!question) {
            this.showError('Please ask a question first!');
            return;
        }

        if (game.isAsking) {
            return;
        }

        game.isAsking = true;
        this.domElements.askBtn.disabled = true;
        this.domElements.askBtn.textContent = 'Thinking...';

        try {
            game.playSound('shake');

            const ballOuter = this.domElements.magicBall?.querySelector('.ball-outer');
            if (ballOuter) {
                ballOuter.classList.add('shaking');
                
                await new Promise(resolve => 
                    setTimeout(resolve, 600)
                );
                
                ballOuter.classList.remove('shaking');
            }

            await new Promise(resolve => 
                setTimeout(resolve, game.getAnimationDelay())
            );

            const responsePack = this.domElements.responsePack?.value || 'default';
            const response = await api.ask(question, responsePack);

            game.playSound('reveal');

            this.displayAnswer(response);

            game.addToHistory(question, response.answer, response.answer_type);

            this.updateStats();

            const achievement = game.checkAchievements();
            if (achievement) {
                this.showAchievement(achievement);
            }

            this.clearQuestion();

        } catch (error) {
            console.error('Error:', error);
            this.showError(error.message || 'Failed to get an answer. Please try again.');
        } finally {
            game.isAsking = false;
            this.domElements.askBtn.disabled = false;
            this.updateAskButtonText();
        }
    }

    displayAnswer(response) {
        const answerText = this.domElements.answerText;
        const answerType = this.domElements.answerType;

        if (!answerText || !answerType) return;

        answerText.textContent = 'Ask a question...';
        answerType.textContent = '';
        answerText.classList.remove('show');
        answerType.classList.remove('show');

        setTimeout(() => {
            answerText.textContent = response.answer;
            answerType.textContent = response.answer_type.replace(/_/g, ' ').toUpperCase();
            answerText.classList.add('show');
            answerType.classList.add('show');

            const ballOuter = this.domElements.magicBall?.querySelector('.ball-outer');
            if (ballOuter) {
                ballOuter.classList.add('glowing');
                setTimeout(() => ballOuter.classList.remove('glowing'), 1000);
            }

            // Show combo notification if combo > 1
            const combo = game.getCombo();
            if (combo > 2) {
                this.showComboNotification(combo);
            }
            
            // Show best combo milestone
            if (game.getCombo() === game.getBestCombo() && game.getBestCombo() > 1) {
                this.showMilestoneNotification(`New Personal Best! ${game.getBestCombo()} Combo! 🏆`);
            }
        }, 100);
    }

    showComboNotification(combo) {
        const notification = document.createElement('div');
        notification.className = 'combo-notification';
        notification.textContent = `✨ ${combo} Combo! ✨`;
        document.body.appendChild(notification);

        setTimeout(() => {
            notification.classList.add('show');
        }, 10);

        setTimeout(() => {
            notification.classList.remove('show');
            setTimeout(() => notification.remove(), 500);
        }, 2000);
    }

    showMilestoneNotification(message) {
        const notification = document.createElement('div');
        notification.className = 'milestone-notification';
        notification.textContent = message;
        document.body.appendChild(notification);

        setTimeout(() => {
            notification.classList.add('show');
        }, 10);

        setTimeout(() => {
            notification.classList.remove('show');
            setTimeout(() => notification.remove(), 500);
        }, 3000);
    }

    clearQuestion() {
        if (this.domElements.questionInput) {
            this.domElements.questionInput.value = '';
            this.updateCharCount();
        }
    }

    updateAskButtonText() {
        if (this.domElements.askBtn) {
            this.domElements.askBtn.innerHTML = '<span class="btn-text">Ask the Magic 8 Ball</span><span class="btn-icon">🎱</span>';
        }
    }

    shareResult() {
        if (!game.currentAnswer) {
            this.showError('Ask a question first!');
            return;
        }

        const text = `I asked the Magic 8 Ball: "${this.domElements.questionInput?.value}"\n\nThe answer was: "${game.currentAnswer}"\n\nTry it yourself: Ask the Magic 8 Ball!`;

        if (navigator.share) {
            navigator.share({
                title: 'Magic 8 Ball',
                text: text
            }).catch(err => console.log('Error sharing:', err));
        } else {
            navigator.clipboard.writeText(text);
            this.showNotification('Result copied to clipboard!');
        }
    }

    toggleThemeModal() {
        this.domElements.themeModal?.classList.toggle('active');
        this.domElements.modalOverlay?.classList.toggle('active');
    }

    toggleHistoryModal() {
        if (this.domElements.historyModal?.classList.contains('active')) {
            this.closeModal('historyModal');
        } else {
            this.openModal('historyModal');
            this.updateHistory();
        }
    }

    toggleAchievementsModal() {
        if (this.domElements.achievementsModal?.classList.contains('active')) {
            this.closeModal('achievementsModal');
        } else {
            this.openModal('achievementsModal');
            this.renderAchievements();
        }
    }

    openModal(modalId) {
        const modal = this.domElements[modalId];
        if (modal) {
            modal.classList.add('active');
            this.domElements.modalOverlay?.classList.add('active');
        }
    }

    closeModal(modalId) {
        const modal = this.domElements[modalId];
        if (modal) {
            modal.classList.remove('active');
        }
        if (!this.isAnyModalOpen()) {
            this.domElements.modalOverlay?.classList.remove('active');
        }
    }

    closeAllModals() {
        Object.keys(this.domElements).forEach(key => {
            if (key.includes('Modal')) {
                this.domElements[key]?.classList.remove('active');
            }
        });
        this.domElements.modalOverlay?.classList.remove('active');
    }

    isAnyModalOpen() {
        return Array.from(document.querySelectorAll('.modal')).some(m => m.classList.contains('active'));
    }

    async loadThemes() {
        try {
            const response = await api.getThemes();
            this.renderThemes(response.themes);
        } catch (error) {
            console.error('Failed to load themes:', error);
        }
    }

    renderThemes(themes) {
        const grid = this.domElements.themeGrid;
        if (!grid) return;

        grid.innerHTML = themes.map(theme => `
            <div class="theme-option ${game.currentTheme === theme.id ? 'active' : ''}" 
                 data-theme-id="${theme.id}">
                <div class="theme-preview" style="background: linear-gradient(135deg, ${theme.colors.primary}, ${theme.colors.accent})"></div>
                <div class="theme-name">${theme.name}</div>
                <div class="theme-description">${theme.description}</div>
            </div>
        `).join('');

        grid.querySelectorAll('.theme-option').forEach(option => {
            option.addEventListener('click', () => {
                const themeId = option.dataset.themeId;
                this.selectTheme(themeId);
            });
        });
    }

    selectTheme(themeId) {
        game.setTheme(themeId);
        this.applyTheme();
        
        this.domElements.themeGrid?.querySelectorAll('.theme-option').forEach(option => {
            option.classList.toggle('active', option.dataset.themeId === themeId);
        });

        game.playSound('click');
    }

    applyTheme() {
        document.body.className = `theme-${game.currentTheme}`;
    }

    toggleSound() {
        const enabled = game.toggleSound();
        const icon = this.domElements.soundToggleBtn?.querySelector('.sound-icon');
        if (icon) {
            icon.textContent = enabled ? '🔊' : '🔇';
        }
        game.playSound('click');
    }

    updateStats() {
        if (this.domElements.totalQuestions) {
            this.domElements.totalQuestions.textContent = game.getTotalQuestions();
        }
        if (document.getElementById('streakCount')) {
            document.getElementById('streakCount').textContent = game.getStreak();
        }
        if (document.getElementById('comboCount')) {
            document.getElementById('comboCount').textContent = game.getCombo();
        }
        if (document.getElementById('bestCombo')) {
            document.getElementById('bestCombo').textContent = game.getBestCombo();
        }
    }

    showAchievement(achievement) {
        const section = this.domElements.achievementToast;
        const icon = this.domElements.achievementIcon;
        const name = this.domElements.achievementName;
        const desc = this.domElements.achievementDesc;

        if (!section) return;

        if (icon) icon.textContent = achievement.icon;
        if (name) name.textContent = achievement.name;
        if (desc) desc.textContent = achievement.description;
        
        section.style.display = 'block';

        setTimeout(() => {
            section.style.display = 'none';
        }, 4000);

        game.playSound('reveal');
    }

    updateHistory() {
        this.renderHistory(game.history);
    }

    filterHistory(query) {
        const results = game.searchHistory(query);
        this.renderHistory(results);
    }

    renderHistory(items) {
        const list = this.domElements.historyList;
        if (!list) return;

        if (items.length === 0) {
            list.innerHTML = '<p class="empty-message">No history found.</p>';
            return;
        }

        list.innerHTML = items.map(entry => `
            <div class="history-item" data-id="${entry.id}">
                <div class="history-question">Q: ${this.escapeHtml(entry.question)}</div>
                <div class="history-answer">A: ${this.escapeHtml(entry.answer)}</div>
                <div class="history-meta">
                    <span>${this.formatDate(entry.timestamp)}</span>
                    <div class="history-btn">
                        <span class="btn-icon-small favorite-btn" title="Favorite" data-id="${entry.id}">
                            ${entry.is_favorite ? '❤️' : '🤍'}
                        </span>
                        <span class="btn-icon-small copy-btn" title="Copy" data-id="${entry.id}">📋</span>
                        <span class="btn-icon-small delete-btn" title="Delete" data-id="${entry.id}">🗑️</span>
                    </div>
                </div>
            </div>
        `).join('');

        list.querySelectorAll('.favorite-btn').forEach(btn => {
            btn.addEventListener('click', (e) => {
                const id = parseInt(e.target.dataset.id);
                game.toggleFavorite(id);
                this.updateHistory();
                this.updateStats();
                game.playSound('click');
            });
        });

        list.querySelectorAll('.copy-btn').forEach(btn => {
            btn.addEventListener('click', (e) => {
                const id = parseInt(e.target.dataset.id);
                const entry = game.history.find(h => h.id === id);
                if (entry) {
                    navigator.clipboard.writeText(entry.answer);
                    this.showNotification('Answer copied!');
                }
            });
        });

        list.querySelectorAll('.delete-btn').forEach(btn => {
            btn.addEventListener('click', (e) => {
                const id = parseInt(e.target.dataset.id);
                game.history = game.history.filter(h => h.id !== id);
                game.saveToLocalStorage();
                this.updateHistory();
                this.updateStats();
            });
        });
    }

    async loadAchievements() {
        try {
            const response = await api.getAchievements();
            game.allAchievements = response.achievements;
        } catch (error) {
            console.error('Failed to load achievements:', error);
        }
    }

    renderAchievements() {
        const grid = this.domElements.achievementsGrid;
        if (!grid || !game.allAchievements.length) return;

        grid.innerHTML = game.allAchievements.map(ach => {
            const isUnlocked = game.achievements.includes(ach.id);
            return `
                <div class="achievement-card ${isUnlocked ? 'unlocked' : 'locked'}">
                    <div class="achievement-icon-large">${ach.icon}</div>
                    <div class="achievement-title">${ach.name}</div>
                    <div class="achievement-text">${ach.description}</div>
                    ${isUnlocked ? '<div class="achievement-badge">✓ Unlocked</div>' : ''}
                </div>
            `;
        }).join('');
    }

    formatDate(timestamp) {
        const date = new Date(timestamp);
        const now = new Date();
        const diffMs = now - date;
        const diffMins = Math.floor(diffMs / 60000);
        const diffHours = Math.floor(diffMs / 3600000);
        const diffDays = Math.floor(diffMs / 86400000);

        if (diffMins < 1) return 'just now';
        if (diffMins < 60) return `${diffMins}m ago`;
        if (diffHours < 24) return `${diffHours}h ago`;
        if (diffDays < 7) return `${diffDays}d ago`;

        return date.toLocaleDateString();
    }

    escapeHtml(text) {
        const div = document.createElement('div');
        div.textContent = text;
        return div.innerHTML;
    }

    showNotification(message) {
        const notification = document.createElement('div');
        notification.style.cssText = `
            position: fixed;
            bottom: 20px;
            right: 20px;
            background: #e94560;
            color: white;
            padding: 15px 20px;
            border-radius: 8px;
            z-index: 2000;
            animation: slideInUp 0.3s ease-out;
            font-weight: 600;
            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.3);
        `;
        notification.textContent = message;
        document.body.appendChild(notification);

        setTimeout(() => {
            notification.style.animation = 'slideInDown 0.3s ease-out';
            setTimeout(() => notification.remove(), 300);
        }, 2000);
    }

    showError(message) {
        const notification = document.createElement('div');
        notification.style.cssText = `
            position: fixed;
            top: 20px;
            right: 20px;
            background: #d32f2f;
            color: white;
            padding: 15px 20px;
            border-radius: 8px;
            z-index: 2000;
            animation: slideInDown 0.3s ease-out;
            font-weight: 600;
            max-width: 300px;
            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.3);
        `;
        notification.textContent = message;
        document.body.appendChild(notification);

        setTimeout(() => {
            notification.style.animation = 'slideInUp 0.3s ease-out';
            setTimeout(() => notification.remove(), 300);
        }, 4000);
    }
}

const ui = new MagicBallUI();
