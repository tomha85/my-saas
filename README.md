## GET /me

### Description
- Returns user information if authorized with a Bearer token.

### Example Request
```http
GET /me HTTP/1.1
Authorization: Bearer demo
```

### Response
```json
{
    "username": "demo"
}
```

### Unauthorized Response
```json
{
    "error": "Unauthorized"
}
```