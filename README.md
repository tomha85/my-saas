# API Documentation

## POST /login

### Description
- Login endpoint that returns a token.

### Example Request
```http
POST /login HTTP/1.1
Content-Type: application/json
{
    "username": "your_username",
    "password": "your_password"
}
```

### Response
```json
{
    "token": "your_generated_token_here"
}
```

## GET /version

### Description
- Returns the current version of the API.

### Example Request
```http
GET /version HTTP/1.1
```

### Response
```json
{
    "version": "0.0.1"
}
```

## Troubleshooting

### 1. Connection Errors
- **Issue**: If you encounter `Connection refused` or `Max retries exceeded` errors when running tests.
  - **Solution**: Ensure the server is running at `localhost:5000`. You can start the server using:
    ```bash
    python app.py
    ```

### 2. Attribute Errors
- **Issue**: Attribute errors related to client setups in your tests.
  - **Solution**: Verify that the `test_client` fixture is correctly defined and initialized in your test files.

### 3. Testing Commands
- **Issue**: Tests fail to run.
  - **Solution**: Run the tests using:
    ```bash
    pytest -q
    ```

### 4. Missing dependencies
- **Issue**: Import errors or any other Python package related issues.
  - **Solution**: Ensure all dependencies listed in `requirements.txt` are installed by running:
    ```bash
    pip install -r requirements.txt
    ```

### 5. Specific Test Failures
- **Issue**: Specific tests fail with unclear messages or log outputs.
  - **Solution**: Review logs to identify the failing tests and ensure all relevant components are correctly set up.