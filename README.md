## POST /login

### Description
- Authenticates a user and returns a JSON Web Token.

### Example Request
```http
POST /login HTTP/1.1
Content-Type: application/json
{
    "username": "demo",
    "password": "demo"
}
```

### Response
```json
{
    "ok": true,
    "token": "demo"
}
```

### Unauthorized Response
```json
{
    "ok": false
}
```