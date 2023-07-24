from fastapi import FastAPI
from mangum import Mangum
from random import choice

app = FastAPI()

@app.get("/")
def read_root():
    return {
  "apiversion": "1",
  "author": "yasbonilha",
  "color": "#FF5733",
  "head": "all-seeing",
  "tail": "do-sammy",
  "version": "0.0.1-beta"
}

@app.post("/start")
def start():
    print("o jogo começou!")
    return "ok"

@app.post("/end")
def end():
    print("o jogo acabou")
    return "ok"

@app.post("/move")
def move(request: dict):
    print("iniciando o movimento!")
    print(request)
    directions = ["left", "right", "up", "down"]
    direction = choice(directions)
    print("direção é igual:", direction)
    response = {
  "move": direction,
  "shout": f"moving {direction}"
}
    return response



handler = Mangum(app, lifespan="off")
