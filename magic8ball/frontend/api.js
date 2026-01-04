/**
 * API Module - Handles all communication with the backend
 */

class MagicBallAPI {
    constructor(baseUrl = '') {
        this.baseUrl = baseUrl || this.getBaseUrl();
        this.timeout = 10000;
    }

    getBaseUrl() {
        const protocol = window.location.protocol;
        const hostname = window.location.hostname;
        const port = window.location.port;
        
        if (hostname === 'localhost' || hostname === '127.0.0.1') {
            return `${protocol}//${hostname}:8000`;
        }
        
        return `${protocol}//${hostname}${port ? ':' + port : ''}`;
    }

    async request(endpoint, options = {}) {
        const url = `${this.baseUrl}${endpoint}`;
        const controller = new AbortController();
        const timeoutId = setTimeout(() => controller.abort(), this.timeout);

        try {
            const response = await fetch(url, {
                ...options,
                signal: controller.signal,
                headers: {
                    'Content-Type': 'application/json',
                    ...options.headers,
                },
            });

            clearTimeout(timeoutId);

            if (!response.ok) {
                const error = await response.json();
                throw new Error(error.detail || `HTTP ${response.status}`);
            }

            return await response.json();
        } catch (error) {
            clearTimeout(timeoutId);
            if (error.name === 'AbortError') {
                throw new Error('Request timeout - please try again');
            }
            throw error;
        }
    }

    async ask(question, responsePack = 'default') {
        return this.request('/ask', {
            method: 'POST',
            body: JSON.stringify({ question, response_pack: responsePack }),
        });
    }

    async getThemes() {
        return this.request('/themes');
    }

    async getTheme(themeId) {
        return this.request(`/themes/${themeId}`);
    }

    async getResponsePacks() {
        return this.request('/response-packs');
    }

    async getAchievements() {
        return this.request('/achievements');
    }

    async healthCheck() {
        return this.request('/health');
    }

    async getAppInfo() {
        return this.request('/info');
    }
}

const api = new MagicBallAPI();
