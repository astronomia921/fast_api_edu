# import datetime
from enum import Enum
from typing import List, Optional
from fastapi import FastAPI
from pydantic import BaseModel, Field


app = FastAPI(
    title='Trading App'
)


@app.get('/')
def hello():
    return 'Hello World'


fake_users = [
    {
        'id': 1,
        'role': 'admin',
        'name': 'Bob',
        'degree': [
            {
                'id': 1,
                'created_at': '2020-01-01T00:00:00',
                'type_degree': 'expert'
            }
        ]
    },
    {
        'id': 2,
        'role': 'user',
        'name': 'Dave'
    }
]

fake_trades = [
    {
        'id': 1,
        'user_id': 1,
        'currency': 'USD',
        'side': 'buy',
        'price': 100,
        'amount': 25
    },
    {
        'id': 2,
        'user_id': 1,
        'currency': 'USD',
        'side': 'buy',
        'price': 500,
        'amount': 20
    }
]


class DegreeType(Enum):
    newbie = 'newbie'
    expert = 'expert'


class Degree(BaseModel):
    id: int
    created_at: str
    type_degree: DegreeType


class User(BaseModel):
    id: int
    role: str
    name: str
    degree: Optional[List[Degree]] = []


@app.get('/users/{user_id}', response_model=List[User])
def get_users(user_id: int) -> dict:
    return [user for user in fake_users if user.get('id') == user_id]


@app.get('/trades')
def get_trades(limit: int = 10, offest: int = 0) -> dict:
    return fake_trades[offest:][:limit]


fake_users_2 = [
    {'id': 2, 'role': 'user', 'name': 'Dave'}
]


@app.post('/users/{user_id}')
def change_user_name(user_id: int, new_name: str) -> dict:
    current_user = list(
        filter(
            lambda user: user['id'] == user_id, fake_users_2
            )
        )[0]
    current_user['name'] = new_name
    return {'status': 200, 'data': current_user}


class Trade(BaseModel):
    id: int
    user_id: int
    currency: str = Field(max_length=5)
    side: str
    price: float = Field(ge=0)
    amount: float


@app.post('/trades')
def add_trades(trades: List[Trade]) -> dict:
    fake_trades.extend(trades)
    return {'status': 200, 'data': fake_trades}
