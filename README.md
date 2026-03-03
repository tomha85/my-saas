## POST /todos

### Description
- Creates a new todo item.

### Example Request
```http
POST /todos HTTP/1.1
Content-Type: application/json
{
    "task": "Your task description"
}
```

### Response
```json
{
    "id": <int>,
    "task": "Your task description"
}
```

## GET /todos

### Description
- Returns a list of all todo items.

### Example Request
```http
GET /todos HTTP/1.1
```

### Response
```json
[
    {
        "id": 1,
        "task": "Your task description"
    }
]