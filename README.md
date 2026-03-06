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
If you encounter issues with endpoints, here are some steps to help resolve them:
- Ensure the server is running at `localhost:5000`.
- Verify that any dependencies are correctly installed.
- Check for proper configuration in your testing and development setups.