## Health Endpoint

- Endpoint: `/health`
- Method: `GET`
- Returns JSON in the format: `{"ok": true, "version": "0.1.0"}`

### Run Steps
1. Install requirements: `pip install -r requirements.txt`
2. Run the app: `flask run`
3. Run tests: `pytest`

### Test Steps
- Check health: `curl http://localhost:5000/health`