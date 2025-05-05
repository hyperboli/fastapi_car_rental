# Car Rental System

Мини-приложение на FastAPI для бронирования автомобилей

## Установка

1. Клонируйте проект:

```bash
git clone https://github.com/hyperboli/fastapi_car_rental.git
cd car_rental
```

2. Установите зависимости:

```bash
pip install -r requirements.txt
```

3. Запустите приложение:

```bash
uvicorn main:app --reload
```

## Структура проекта

```
car_rental/
├── main.py              # main
├── database.py          # база данных
├── models.py            # модели SQLAlchemy
├── schemas.py           # схемы Pydantic 
├── users.py             # управление пользователями
├── cars.py              # управления функционалом для машин
├── bookings.py          # алгоритмы бронирований
├── requirements.txt     # requirements 
└── README.md            # READMI
```

## Доступные функции

### Пользователи `/users`
- `POST /users/` — создать пользователя
- `DELETE /users/{user_id}` — удалить пользователя

### Машины `/cars`
- `POST /cars/` — добавить машину
- `DELETE /cars/{car_id}` — удалить машину

### Бронирования `/bookings`
- `GET /bookings/available/` — список доступных машин на указанный интервал
- `GET /bookings/price/` — расчёт стоимости аренды по времени и id машины
- `POST /bookings/` — создать бронирование
- `DELETE /bookings/{booking_id}` — отменить бронирование

## Пример запроса на бронирование

```json
{
  "user_id": 1,
  "car_id": 2,
  "start_time": "2025-05-05T10:00:00",
  "end_time": "2025-05-05T14:00:00"
}
```

Александр Акулов

akulov.am@phystech.edu