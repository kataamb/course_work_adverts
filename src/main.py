from __future__ import annotations

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

from routers.deal import deals_router
from routers.main import main_router
from routers.user import user_router
from routers.advert import advert_router
from routers.liked import likes_router

from core.create_jwt import JWTManager

app = FastAPI()

templates = Jinja2Templates(directory="templates")


# Глобальный обработчик ошибок подключения к БД
@app.exception_handler(ConnectionRefusedError)
async def database_connection_exception_handler(request: Request, exc: ConnectionRefusedError) -> HTMLResponse:
    return templates.TemplateResponse(
        "database_error.html",
        {"request": request, "error": "База данных недоступна. Попробуйте позже."},
        status_code=503
    )


@app.exception_handler(Exception)
async def general_database_exception_handler(request: Request, exc: Exception) -> HTMLResponse:
    error_name = type(exc).__name__

    db_error_keywords = [
        "Connection", "Postgres", "Database", "SQL",
        "Timeout", "Operational", "Interface", "Data"
    ]

    if any(keyword in error_name for keyword in db_error_keywords):
        return templates.TemplateResponse(
            "database_error.html",
            {"request": request, "error": f"Ошибка базы данных: {error_name}"},
            status_code=503
        )
    raise exc



# Middleware: определяет текущего пользователя
@app.middleware("http")
async def add_user_to_request(request: Request, call_next):
    token = request.cookies.get("access_token")
    request.state.user = None
    if token:
        try:
            payload = JWTManager.decode_token(token)
            request.state.user = {
                "id": payload.get("id"),
                "email": payload.get("sub"),
                "role": payload.get("role"),
            }
        except Exception:
            request.state.user = None
    response = await call_next(request)
    return response


# Подключаем роутеры
app.include_router(main_router)
app.include_router(user_router)
app.include_router(advert_router)
app.include_router(likes_router)
app.include_router(deals_router)