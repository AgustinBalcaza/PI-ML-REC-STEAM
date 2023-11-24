from fastapi import FastAPI
import functions as func
import importlib

importlib.reload(func)

app = FastAPI()

@app.get("/PlayTimeGenre")
async def PlayTimeGenre(genero: str):
    return func.PlayTimeGenre(genero)

@app.get("/UserForGenre")
async def UserForGenre(genero: str):
    return func.UserForGenre(genero)

@app.get("/UsersRecommend")
async def UsersRecommend(año: int):
    return func.UsersRecommend(año)

@app.get("/UsersWorstDeveloper")
async def UsersWorstDeveloper(año: int):
    return func.UsersWorstDeveloper(año)

@app.get("/sentiment_analysis")
async def sentiment_analysis(desarrolladora: str):
    return func.sentiment_analysis(desarrolladora)

@app.get("/recomendacion_juego")
async def recomendacion_juego(game_id: int):
    return func.recomendacion_juego(game_id)