from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/health")
def health_check():
    #TODO add wellness check for other stuff along the way (like db etc.)
    return {"status": "ok"}






