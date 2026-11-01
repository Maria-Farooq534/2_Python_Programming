import fastapi as FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"Message" : "FastAPI"}

