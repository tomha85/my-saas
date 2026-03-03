# Simple Flask Health Check App

## Overview
This is a simple Flask application that provides a health check endpoint.

## Health Endpoint
- **GET** `/health`
- Returns JSON: `{"ok": true}`

## Run Steps
1. Install requirements: `pip install -r requirements.txt`
2. Run the app: `flask run`
3. Run tests: `pytest`

## Test Steps
- Check health: `curl http://localhost:5000/health`