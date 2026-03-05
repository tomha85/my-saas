const request = require('supertest');
const app = require('../app'); // Assuming your app is in app.js

describe('GET /version', () => {
    it('should return version info', async () => {
        const res = await request(app).get('/version');
        expect(res.statusCode).toEqual(200);
        expect(res.body).toEqual({ version: '0.0.1' });
    });
});