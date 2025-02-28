from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from http import HTTPStatus
from fastapiplayground.schemas import Message, UserSchema, UserPublic, UserDB, UserList

app = FastAPI()
database = []

@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Hello world'}

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