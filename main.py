from fastapi import FastAPI, APIRouter

app = FastAPI()

router = APIRouter()

@router.get("/hello")
async def hello_world():
    return {"message": "Hello World"}

@app.get("/hello/{name}")
async def hello_world(name: str):
    return {"message": f"Hello {name}"}
