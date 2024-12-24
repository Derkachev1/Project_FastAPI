import uvicorn
from fastapi import FastAPI
from app.config import settings
from fastapi.staticfiles import StaticFiles
from app.routers import router as api_router  # Подключаем ваши роуты
from app.routers.weather import router as weather_router  # Подключаем роут для погоды
from app.database import engine
import app.models

# Инициализация FastAPI приложения
app = FastAPI()

# Включаем статические файлы (например, для CSS, JS или изображений)
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Подключаем маршруты для API
app.include_router(api_router, prefix=settings.api.prefix)

# Подключаем роут для погоды
app.include_router(weather_router, prefix="/weather")

# Этот маршрут для тестирования работы API
@app.get("/test")
def test():
    return {"message": "TEST"}

# Главная страница (можно обновить по необходимости)
@app.get("/")
def home():
    return {"message": "Hello World"}

# Создание таблиц в базе данных при запуске приложения
@app.on_event("startup")
def on_startup():
    app.models.Base.metadata.create_all(bind=engine)

# Запуск приложения через uvicorn (если запустим main.py напрямую)
if __name__ == "__main__":
    uvicorn.run("app.main:app", host=settings.run.host, port=settings.run.port, reload=True)
