## GET /uptime

### Description
- Returns the uptime of the service in seconds.

### Example Request
```http
GET /uptime HTTP/1.1
```

### Response
```json
{
    "uptime_seconds": <int>
}
```