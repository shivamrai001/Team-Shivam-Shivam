from fastapi import FastAPI

app = FastAPI(
    title="UrbanSense AI",
    version="1.0"
)

@app.get("/")
def home():
    return {
        "message": "UrbanSense AI Running 🚀"
    }

