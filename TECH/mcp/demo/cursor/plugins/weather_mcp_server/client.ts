import axios from 'axios';

export class MCPClient {
    private baseUrl: string;

    constructor(baseUrl: string = 'http://localhost:8080') {
        this.baseUrl = baseUrl;
    }

    async queryWeather(location: string) {
        try {
            const response = await axios.post(`${this.baseUrl}/api/weather`, {
                location
            });
            return response.data;
        } catch (error) {
            console.error('Weather query failed:', error);
            throw error;
        }
    }

    async checkHealth() {
        try {
            const response = await axios.get(`${this.baseUrl}/health`);
            return response.data;
        } catch (error) {
            console.error('Health check failed:', error);
            throw error;
        }
    }
} 