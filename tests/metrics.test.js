const request = require('supertest');
const app = require('../app'); // Adjust path accordingly

describe('GET /metrics', () => {
    it('should return request counts per route', async () => {
        const response = await request(app).get('/metrics');
        expect(response.statusCode).toBe(200);
        expect(response.body).toHaveProperty('routes'); // Ensure structure is as expected
        // Add assertions for specific counts if needed
    });
});