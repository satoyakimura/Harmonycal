from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
@app.get("/")
async def hello():
    hello= "hello"
    return hello

origins = [
    "http://localhost:5173"
# ここに許可するオリジンを記入
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)