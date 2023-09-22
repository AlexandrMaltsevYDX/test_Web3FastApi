# test_Web3FastApi
Aleksandr Maltsev test task

## Инструкция
```
.
├── .git
│   └── ...
├── test
│   ├── __pycache__
│   ├── __init__.py
│   ├── database.py
│   ├── main.py
│   ├── models.py
│   ├── repositories.py
│   ├── schemas.py
│   ├── services.py
│   └── utils.py
├── sql_app.db(после первого запуска)
├── README.md
└── requirements.txt

```

### Находясь в корневом каталоге  " . "
### 1. Установить окружение  

        1. python -m venv env
        2. source env/bin/activate
        3. pip install -r requirements.txt

### 2. Запустить проект

        1. uvicorn test.main:app --reload
        2. документация http://127.0.0.1:8000/docs