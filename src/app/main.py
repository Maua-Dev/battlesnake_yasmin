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
    print("função move ativada")
    print(request)
    directions = ["left", "right", "up", "down"]
    if request['board']['snakes'][0]['body'][0]['x'] == 0:
        directions.remove('left')
    elif request['board']['snakes'][0]['body'][0]['y'] == 0:
        directions.remove('down')
    elif request['board']['snakes'][0]['body'][0]['x'] == 11:
        directions.remove('right')
    elif request['board']['snakes'][0]['body'][0]['y'] == 11:
        directions.remove('up')
    direction = choice(directions)
    print("direção é igual:", direction)
    response = {
  "move": direction,
  "shout": f"moving {direction}"
}
    return response
        


handler = Mangum(app, lifespan="off")
