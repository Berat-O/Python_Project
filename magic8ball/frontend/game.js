/**
 * Game Module - Core game logic and state management
 */

class MagicBallGame {
    constructor() {
        this.isAsking = false;
        this.currentAnswer = null;
        this.animationSpeed = 1;
        this.soundEnabled = true;
        this.currentTheme = 'classic';
        this.history = [];
        this.achievements = [];
        this.allAchievements = [];
        this.streak = 0;
        this.combo = 0;
        this.bestCombo = 0;
        this.lastAnswerType = null;
        this.lastAskTime = null;
        
        this.init();
    }

    init() {
        this.loadFromLocalStorage();
    }

    saveToLocalStorage() {
        localStorage.setItem('magic8ball_history', JSON.stringify(this.history));
        localStorage.setItem('magic8ball_achievements', JSON.stringify(this.achievements));
        localStorage.setItem('magic8ball_theme', this.currentTheme);
        localStorage.setItem('magic8ball_sound', JSON.stringify(this.soundEnabled));
        localStorage.setItem('magic8ball_animation_speed', JSON.stringify(this.animationSpeed));
        localStorage.setItem('magic8ball_streak', JSON.stringify(this.streak));
        localStorage.setItem('magic8ball_best_combo', JSON.stringify(this.bestCombo));
    }

    loadFromLocalStorage() {
        try {
            const saved_history = localStorage.getItem('magic8ball_history');
            this.history = saved_history ? JSON.parse(saved_history) : [];
            
            const saved_achievements = localStorage.getItem('magic8ball_achievements');
            this.achievements = saved_achievements ? JSON.parse(saved_achievements) : [];
            
            const saved_theme = localStorage.getItem('magic8ball_theme');
            this.currentTheme = saved_theme || 'classic';
            
            const saved_sound = localStorage.getItem('magic8ball_sound');
            this.soundEnabled = saved_sound !== null ? JSON.parse(saved_sound) : true;
            
            const saved_speed = localStorage.getItem('magic8ball_animation_speed');
            this.animationSpeed = saved_speed ? JSON.parse(saved_speed) : 1;
            
            const saved_streak = localStorage.getItem('magic8ball_streak');
            this.streak = saved_streak ? JSON.parse(saved_streak) : 0;
            
            const saved_best_combo = localStorage.getItem('magic8ball_best_combo');
            this.bestCombo = saved_best_combo ? JSON.parse(saved_best_combo) : 0;
            
            // Check if streak should be reset (new day)
            this.checkStreakReset();
        } catch (error) {
            console.error('Failed to load game state:', error);
        }
    }

    checkStreakReset() {
        const lastPlay = localStorage.getItem('magic8ball_last_play_date');
        const today = new Date().toDateString();
        
        if (lastPlay && lastPlay !== today) {
            // Different day - reset streak if no questions today yet
            const todayCount = this.getDailyCount();
            if (todayCount === 0) {
                this.streak = 0;
            }
        }
        
        localStorage.setItem('magic8ball_last_play_date', today);
    }

    addToHistory(question, answer, answerType) {
        const entry = {
            question,
            answer,
            answer_type: answerType,
            timestamp: new Date().toISOString(),
            is_favorite: false,
            id: Date.now(),
        };

        this.history.unshift(entry);
        
        if (this.history.length > 100) {
            this.history = this.history.slice(0, 100);
        }

        // Update streak - increment each question
        this.streak += 1;
        
        // Update combo - increment for same type in a row
        if (this.lastAnswerType === answerType) {
            this.combo += 1;
            if (this.combo > this.bestCombo) {
                this.bestCombo = this.combo;
            }
        } else {
            this.combo = 1;
            this.lastAnswerType = answerType;
        }

        this.saveToLocalStorage();
        this.checkAchievements();
        return entry;
    }

    getStreak() {
        return this.streak;
    }

    getCombo() {
        return this.combo;
    }

    getBestCombo() {
        return this.bestCombo;
    }

    getTotalQuestions() {
        return this.history.length;
    }

    getDailyCount() {
        const today = new Date().toDateString();
        return this.history.filter(entry => {
            const entryDate = new Date(entry.timestamp).toDateString();
            return entryDate === today;
        }).length;
    }

    getFavoriteCount() {
        return this.history.filter(entry => entry.is_favorite).length;
    }

    toggleFavorite(id) {
        const entry = this.history.find(e => e.id === id);
        if (entry) {
            entry.is_favorite = !entry.is_favorite;
            this.saveToLocalStorage();
        }
        return entry;
    }

    clearHistory() {
        this.history = [];
        this.saveToLocalStorage();
    }

    searchHistory(query) {
        const q = query.toLowerCase().trim();
        if (!q) return this.history;
        
        return this.history.filter(entry =>
            entry.question.toLowerCase().includes(q) ||
            entry.answer.toLowerCase().includes(q)
        );
    }

    checkAchievements() {
        const total = this.getTotalQuestions();
        const easterEggFound = this.history.some(e => e.answer_type === 'easter_egg');
        
        const achievements = [
            { id: 'first_question', threshold: 1 },
            { id: 'curious_mind', threshold: 10 },
            { id: 'oracle_seeker', threshold: 50 },
            { id: 'master_questioner', threshold: 100 },
            { id: 'devoted_believer', threshold: 250 },
            { id: 'wisdom_collector', threshold: 500 },
        ];

        let newAchievement = null;
        
        for (const ach of achievements) {
            if (total >= ach.threshold && !this.achievements.includes(ach.id)) {
                this.achievements.push(ach.id);
                newAchievement = ach.id;
            }
        }

        if (easterEggFound && !this.achievements.includes('easter_egg_hunter')) {
            this.achievements.push('easter_egg_hunter');
            if (!newAchievement) newAchievement = 'easter_egg_hunter';
        }

        if (newAchievement) {
            this.saveToLocalStorage();
            return this.findAchievementById(newAchievement);
        }

        return null;
    }

    findAchievementById(id) {
        return this.allAchievements.find(a => a.id === id);
    }

    setTheme(themeId) {
        this.currentTheme = themeId;
        document.body.className = `theme-${themeId}`;
        this.saveToLocalStorage();
    }

    toggleSound() {
        this.soundEnabled = !this.soundEnabled;
        this.saveToLocalStorage();
        return this.soundEnabled;
    }

    setAnimationSpeed(speed) {
        this.animationSpeed = Math.max(0.5, Math.min(2, speed));
        this.saveToLocalStorage();
    }

    playSound(type = 'shake') {
        if (!this.soundEnabled) return;

        const audioContext = new (window.AudioContext || window.webkitAudioContext)();
        const now = audioContext.currentTime;

        try {
            if (type === 'shake') {
                const osc = audioContext.createOscillator();
                const gain = audioContext.createGain();
                osc.connect(gain);
                gain.connect(audioContext.destination);
                
                osc.frequency.setValueAtTime(100, now);
                osc.frequency.exponentialRampToValueAtTime(50, now + 0.2);
                gain.gain.setValueAtTime(0.3, now);
                gain.gain.exponentialRampToValueAtTime(0.01, now + 0.2);
                
                osc.start(now);
                osc.stop(now + 0.2);
            } else if (type === 'reveal') {
                const osc = audioContext.createOscillator();
                const gain = audioContext.createGain();
                osc.connect(gain);
                gain.connect(audioContext.destination);
                
                osc.frequency.setValueAtTime(300, now);
                osc.frequency.exponentialRampToValueAtTime(800, now + 0.3);
                gain.gain.setValueAtTime(0.2, now);
                gain.gain.exponentialRampToValueAtTime(0.01, now + 0.3);
                
                osc.start(now);
                osc.stop(now + 0.3);
            } else if (type === 'click') {
                const osc = audioContext.createOscillator();
                const gain = audioContext.createGain();
                osc.connect(gain);
                gain.connect(audioContext.destination);
                
                osc.frequency.setValueAtTime(200, now);
                gain.gain.setValueAtTime(0.1, now);
                gain.gain.exponentialRampToValueAtTime(0.01, now + 0.05);
                
                osc.start(now);
                osc.stop(now + 0.05);
            }
        } catch (error) {
            console.warn('Audio playback failed:', error);
        }
    }

    getAnimationDelay() {
        return 500 / this.animationSpeed;
    }
}

const game = new MagicBallGame();
