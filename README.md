## Uptime Endpoint

- Endpoint: `/uptime`
- Method: `GET`
- Returns JSON in the format: `{"uptime_seconds": <int>}`

### Run Steps
1. Install requirements: `pip install -r requirements.txt`
2. Run the app: `flask run`
3. Run tests: `pytest`

### Test Steps
- Check uptime: `curl http://localhost:5000/uptime`