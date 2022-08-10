from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlite_utils import Database

db = Database("customs.db")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:9000'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello Edy"}

@app.get("/entry/{bl}")
async def read_item(bl):

    return_val = {}
    for row in  db.query("select * from customs where bl = ? limit 1", [bl]):
      return_val = row
    return return_val
