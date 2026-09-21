from fastapi import FastAPI

app = FastAPI(
    title="NexoDesk API",
    description="API para la gestión de soporte técnico de NexoDesk",
    version="0.1.0"
)


@app.get("/")
def root():
    return {
        "message": "NexoDesk API funcionando",
        "version": "0.1.0"
    }


@app.get("/health")
def health_check():
    return {
        "status": "ok"
    }