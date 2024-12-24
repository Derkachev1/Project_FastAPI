from fastapi import APIRouter, HTTPException, Depends
from fastapi.templating import Jinja2Templates
from fastapi import Request
from fastapi.responses import HTMLResponse  # Импортируем HTMLResponse для корректного типа ответа
from sqlalchemy.orm import Session
from app.service.weather_service import get_weather  # Импортируем функцию get_weather из weather_service
from app.models import Weather  # Исправляем импорт модели на правильное имя
from app.database import SessionLocal

router = APIRouter()
templates = Jinja2Templates(directory="templates")

# Получение погоды и отображение в шаблоне
@router.get("/weather", response_class=HTMLResponse)
async def get_weather_page(request: Request, city: str = "Moscow", db: Session = Depends(SessionLocal)):
    # Получаем данные о текущей погоде
    weather_data = get_weather(city)
    
    if not weather_data:
        raise HTTPException(status_code=404, detail="City not found")
    
    # Формируем объект погоды для сохранения в БД
    weather_info = Weather(
        city=city,
        temperature=weather_data["main"]["temp"],
        description=weather_data["weather"][0]["description"],
        humidity=weather_data["main"]["humidity"],
        pressure=weather_data["main"]["pressure"],
        wind_speed=weather_data["wind"]["speed"]
    )
    
    # Сохраняем данные о погоде в базу данных
    db.add(weather_info)
    db.commit()
    
    # Отправляем данные в шаблон
    return templates.TemplateResponse("index.html", {
        "request": request,
        "weather": weather_info
    })
