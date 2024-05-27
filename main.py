import uvicorn
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path
from StealthPortal.wif_FastAPI.main import stealth


app = FastAPI()

BASE_PATH = Path(__file__).resolve().parent
print(BASE_PATH)
app.mount("/static", StaticFiles(directory=BASE_PATH / "static"), name="static")
templates = Jinja2Templates(directory=BASE_PATH / "templates")

# Mount the StealthPortal application
app.mount("/portal", stealth)


@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", reload="True")
