from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
import logging
from repositories import BakuganRepository

app = FastAPI(title="Bakugan API", version="v2")

#CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#middleware de logging
logger = logging.getLogger("uvicorn.error")

@app.middleware("http")
async def log_requests(request: Request, call_next):
    logger.info(f"[>] Request: {request.method} {request.url}")
    response= await call_next(request)
    logger.info(f"[>] Response status: {response.status_code}")
    return response

repo = BakuganRepository()

@app.get("/")
def root():
    return {"message": "WELCOME! Bakugan API v2"}

@app.get("/api/v1/bakugan")
def get_all():
    try:
        data= repo.get_all()
        if not data:
            raise HTTPException(status_code=404, detail="[!] No hay Bakugan registrados.")
        return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"[!] Error interno: {str(e)}")

@app.get("/api/v1/bakugan/{nombre}")
def get_by_name(nombre: str):
    try:
        bakugan= repo.get_by_name(nombre)
        if not bakugan:
            raise HTTPException(status_code=404, detail=f"[!] Bakugan '{nombre}' no encontrado.")
        return bakugan
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"[!] Error interno: {str(e)}")

@app.get("/healthz")
def health_check():
    return {"status": "ok"}
