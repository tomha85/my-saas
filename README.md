## GET /health

### Description
- Returns the health status of the application.

### Example Request
```http
GET /health HTTP/1.1
```

### Response
```json
{
    "ok": true,
    "version": "0.1.0"
}
```