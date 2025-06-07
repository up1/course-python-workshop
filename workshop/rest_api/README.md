# Workshop with REST API
* CRUD application with FastAPI
* MySQL database

## 1. Install dependencies
```
$pip install -r requirements.txt
```

## 2. Start mysql database
```
$docker compose up -d mysql
$docker compose ps
```

## 3. Start API server with FastAPI
```
# Development mode
$fastapi dev main.py

# Production mode
$fastapi run main.py

# Multiple workers
$fastapi run --workers 4 main.py
```

List of endpoints
* OpenAPI Documentation = http://127.0.0.1:8000/docs

## 4. Testing with Postman
* newman
* PyTest