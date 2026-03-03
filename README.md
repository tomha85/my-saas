## POST /uptime

### Description
- Returns the uptime of the service in seconds.

### Example Request
```http
POST /uptime HTTP/1.1
```

### Response
```json
{
    "uptime_seconds": <int>
}
```