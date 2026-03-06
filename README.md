# Troubleshooting

## Common Issues

### Connection Errors
- If you encounter `Connection refused` or `Max retries exceeded` errors when running tests: ensure that the server is up and running on `localhost:5000`. You can start the server using the following command:

```
# Example command to run the server
python app.py
```

### Attribute Errors
- If you see `AttributeError` related to client setups in your tests, check that the client fixture is properly defined and initialized in your test files.

### Testing Commands
- To run the tests, use the following command:
```
pytest -q
```

### Specific Test Failures
- Review logs for details on specific test failures and ensure that relevant components are correctly set up.