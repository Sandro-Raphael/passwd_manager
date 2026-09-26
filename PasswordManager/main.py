from fastapi import FastAPI
from routes.crud import router as senha_router


app = FastAPI(
    title="Password Manager API",
    description="API para gerenciamento seguro de senhas",
    version="1.0.0"
)


app.include_router(
    senha_router,
    prefix="/api"
)


@app.get("/")
def root():
    return {
        "message": "Password Manager API online"
    }