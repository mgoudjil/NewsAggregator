import uvicorn
from fastapi import FastAPI

app = FastAPI()

# Connect to Mariadb
# Connect to Redis
# Connect to Redis2


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}


if __name__ == "__main__":
    print("Test1")
    # uvicorn.run(app, host="127.0.0.1", port=8000, log_level="info", reload=True)
    uvicorn.run(app, host="0.0.0.0", log_level="info", reload=True)
