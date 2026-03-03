## ME Endpoint

- Endpoint: `/me`
- Method: `POST`
- **Authorization**: Requires Bearer token in the header.
- Returns JSON: `{"message": "Authorized access"}` on success or `{"error": "Unauthorized"}` on failure.

### Run Steps
1. Install requirements: `pip install -r requirements.txt`
2. Run the app: `flask run`
3. Run tests: `pytest`

### Test Steps
- Authorized Access: `curl -X POST http://localhost:5000/me -H "Authorization: Bearer valid_token"`
- Unauthorized Access: `curl -X POST http://localhost:5000/me`