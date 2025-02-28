from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from http import HTTPStatus
from fastapiplayground.schemas import Message, UserSchema, UserPublic, UserDB, UserList

app = FastAPI()
database = []

@app.get('/exer', response_class=HTMLResponse)
def read_root():
    return """
        <html>
            <head>
                <title> My test </title>
            </head>
            <body>
                <h1>Hello Worldd</h1>
            </body>
        </html """

@app.post('/users/', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: UserSchema):
    user_with_id = UserDB(**user.model_dump(), id=len(database) + 1)
    
    database.append(user_with_id)
    return user_with_id

@app.get('/users/', response_model=UserList)
def read_users():
    return {'users': database}

@app.get('/users/{user_id}', response_model=UserPublic)
def read_users_by_id(user_id: int):
    if user_id < 1 or user_id > len(database):
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='User not found'
        )
    return database[user_id -1]

@app.put('/users/{user_id}', response_model=UserPublic)
def update_user(user_id: int, user: UserSchema):

    if user_id < 1 or user_id > len(database):
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='User not found'
        )
    user_with_id = UserDB(id=user_id, **user.model_dump())
    database[user_id - 1] = user_with_id

    return user_with_id

@app.delete('/users/{user_id}', response_model = Message)
def delete_user(user_id: int):
    if user_id < 1 or user_id > len(database):
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='User not found'
        )
    
    del database[user_id - 1] 

    return {'message': 'User deleted'}