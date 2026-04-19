from fastapi import APIRouter
from pydantic import BaseModel
from app.internal.weather_service import get_weather

router = APIRouter()


# Request body model
class WeatherRequest(BaseModel):
    latitude: float
    longitude: float


@router.post("/weather")
async def get_weather_endpoint(request: WeatherRequest):
    
    return await get_weather(request.latitude, request.longitude)
