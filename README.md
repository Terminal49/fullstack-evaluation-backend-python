# T49 Fullstack Evaluation Bakend - Python

## Pre requisites
- Python 3
- SQLite

## Load dependencies
```
pip3 install -r requirements.txt
```

## Run the app in dev mode
```
uvicorn main:app --reload
```

## Useful Docs
[FastAPI](https://fastapi.tiangolo.com)
[sqlite-utils](https://sqlite-utils.datasette.io/en/stable/)

## Finding some numbers to search with
```
sqlite3 customs.db
select bl from customs limit 10
```
