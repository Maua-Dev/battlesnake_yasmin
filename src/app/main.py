from fastapi import FastAPI
from mangum import Mangum
from random import choice

app = FastAPI()

@app.get("/")
def read_root():
    return {
  "apiversion": "1",
  "author": "yasbonilha",
  "color": "#2874A6",
  "head": "rudolph",
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
    size = request['board']['height']
    directions = ["left", "right", "up", "down"]
    if request['board']['snakes'][0]['body'][0]['x'] == 0:
        directions.remove('left')
    elif request['board']['snakes'][0]['body'][0]['x'] == size -1:
        directions.remove('right')
    if request['board']['snakes'][0]['body'][0]['y'] == 0:
        directions.remove('down')
    elif request['board']['snakes'][0]['body'][0]['y'] == size -1 :
        directions.remove('up')
    corpo = desviar_corpo(request)
    directions.remove(corpo)
    direction = choice(directions)
    print("direção é igual:", direction)
    response = {
  "move": direction,
  "shout": f"moving {direction}"
}
    return response
        
def desviar_corpo(request):
    cabeca = request['board']['snakes'][0]['body'][0]
    meio = request['board']['snakes'][0]['body'][1]
    cauda = request['board']['snakes'][0]['body'][2]
    if cabeca['x'] - meio['x'] >=1:
        return 'left'
    elif cabeca['x'] - meio['x'] <0:
        return 'right'
    elif cabeca['y'] - meio['y'] >=1:
        return 'down'
    elif cabeca['y'] - meio['y'] <0:
        return 'up'


handler = Mangum(app, lifespan="off")
