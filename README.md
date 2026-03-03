# Flask App with Health Check and Login

## Overview
This is a simple Flask application that provides the following endpoints:

- **GET** `/health`: Returns a health check status.
- **POST** `/login`: Returns a token if valid credentials are provided.

## Endpoints

### Health Check Endpoint
- **URL**: `/health`
- **Method**: `GET`
- **Response**: `{"ok": true}`

### Login Endpoint
- **URL**: `/login`
- **Method**: `POST`
- **Request JSON**: `{"username": "<your_username>", "password": "<your_password>"}`
- **Response on success**: `{"ok": true, "token": "demo"}`
- **Response on failure**: `{"ok": false}`

## Run Steps
1. Install requirements: `pip install -r requirements.txt`
2. Run the app: `flask run`
3. Run tests: `pytest`

## Test Steps
- Health Check: `curl http://localhost:5000/health`
- Login: `curl -X POST http://localhost:5000/login -H "Content-Type: application/json" -d '{"username": "demo", "password": "pass"}'`