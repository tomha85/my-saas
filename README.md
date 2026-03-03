## Login Endpoint

- Endpoint: `/login`
- Method: `POST`
- Request JSON format: `{"username": "<your_username>", "password": "<your_password>"}`
- Returns JSON: `{"ok": true, "token": "demo"}` on success, or `{"ok": false}` on failure.

### Run Steps
1. Install requirements: `pip install -r requirements.txt`
2. Run the app: `flask run`
3. Run tests: `pytest`

### Test Steps
- Login: `curl -X POST http://localhost:5000/login -H "Content-Type: application/json" -d '{"username": "test", "password": "pass"}'`