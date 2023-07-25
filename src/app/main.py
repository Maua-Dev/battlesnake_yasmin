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
    direcoes_possiveis = desviar_corpo(request, desviar_paredes(request))
    direction = choice(direcoes_possiveis)
    print("direção é igual:", direction)
    response = {
  "move": direction,
  "shout": f"moving {direction}"
}
    return response


def desviar_paredes(request: dict):
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
    return directions

def desviar_corpo(request: dict, directions:dict):
    cabeca = request['board']['snakes'][0]['body'][0]
    body =  request['board']['snakes'][0]['body']
    for item in body:
        if cabeca['x'] - item['x'] ==1 and cabeca['y'] - item['y'] == 0:
            if 'left' in directions:
                directions.remove('left')
        if cabeca['x'] - item['x'] == -1 and cabeca['y'] - item['y'] == 0:
            if 'right' in directions:
                directions.remove('right')
        if cabeca['y'] - item['y'] == -1 and cabeca['x'] - item['x'] == 0:
            if 'up' in directions:
                directions.remove('up')
        if cabeca['y'] - item['y'] == 1 and cabeca['x'] - item['x'] == 0:
            if 'down' in directions:
                directions.remove('down')
    return directions
        

        
        
        



handler = Mangum(app, lifespan="off")
