from src.app.main import casas, end, move, read_root, start


class Test_App:
    def test_read_root(self):
        resp = read_root()
        
        assert resp == {
  "apiversion": "1",
  "author": "yasbonilha",
  "color": "#FF5733",
  "head": "all-seeing",
  "tail": "do-sammy",
  "version": "0.0.1-beta"
}
    def test_start(self):
        response = start()
        assert response == "ok"
    
    def test_end(self):
        response = end()
        assert response == "ok"
    
    def test_end_wrong(self):
        response = end()
        assert response != "não ok"
    
    def test_move(self):
        request = {
  "game": {
    "id": "totally-unique-game-id",
    "ruleset": {
      "name": "standard",
      "version": "v1.1.15",
      "settings": {
        "foodSpawnChance": 15,
        "minimumFood": 1,
        "hazardDamagePerTurn": 14
      }
    },
    "map": "standard",
    "source": "league",
    "timeout": 500
  },
  "turn": 14,
  "board": {
    "height": 11,
    "width": 11,
    "food": [
      {"x": 5, "y": 5}, 
      {"x": 9, "y": 0}, 
      {"x": 2, "y": 6}
    ],
    "hazards": [
      {"x": 3, "y": 2}
    ],
    "snakes": [
      {
        "id": "snake-508e96ac-94ad-11ea-bb37",
        "name": "My Snake",
        "health": 54,
        "body": [
          {"x": 0, "y": 0}, 
          {"x": 1, "y": 0}, 
          {"x": 2, "y": 0}
        ],
        "latency": "111",
        "head": {"x": 0, "y": 0},
        "length": 3,
        "shout": "why are we shouting??",
        "customizations":{
          "color":"#FF0000",
          "head":"pixel",
          "tail":"pixel"
        }
      }, 
      {
        "id": "snake-b67f4906-94ae-11ea-bb37",
        "name": "Another Snake",
        "health": 16,
        "body": [
          {"x": 5, "y": 4}, 
          {"x": 5, "y": 3}, 
          {"x": 6, "y": 3},
          {"x": 6, "y": 2}
        ],
        "latency": "222",
        "head": {"x": 5, "y": 4},
        "length": 4,
        "shout": "I'm not really sure...",
        "customizations":{
          "color":"#26CF04",
          "head":"silly",
          "tail":"curled"
        }
      }
    ]
  },
  "you": {
    "id": "snake-508e96ac-94ad-11ea-bb37",
    "name": "My Snake",
    "health": 54,
    "body": [
      {"x": 0, "y": 0}, 
      {"x": 1, "y": 0}, 
      {"x": 2, "y": 0}
    ],
    "latency": "111",
    "head": {"x": 0, "y": 0},
    "length": 3,
    "shout": "why are we shouting??",
    "customizations": {
      "color":"#FF0000",
      "head":"pixel",
      "tail":"pixel"
    }
  }
}
        response = move(request)
        expected_response = ["up", "left", "right", "down"]
        assert type(response) == dict
        assert response['move'] in expected_response
    
    def test_move_avoid_wall(self):
        request = {
   'game':{
      'id':'5de0a614-0199-49ab-9a24-8e590ca43091',
      'ruleset':{
         'name':'standard',
         'version':'v1.2.3',
         'settings':{
            'foodSpawnChance':15,
            'minimumFood':1,
            'hazardDamagePerTurn':0,
            'hazardMap':'',
            'hazardMapAuthor':'',
            'royale':{
               'shrinkEveryNTurns':0
            },
            'squad':{
               'allowBodyCollisions':False,
               'sharedElimination':False,
               'sharedHealth':False,
               'sharedLength':False
            }
         }
      },
      'map':'standard',
      'timeout':500,
      'source':'custom'
   },
   'turn':1,
   'board':{
      'height':11,
      'width':11,
      'snakes':[
         {
            'id':'gs_6BfY4q3wWmj4QrgpfycM4FTQ',
            'name':'cobrinhadayas',
            'latency':'31',
            'health':99,
            'body':[
               {
                  'x':0,
                  'y':1
               },
               {
                  'x':1,
                  'y':1
               },
               {
                  'x':1,
                  'y':1
               }
            ],
            'head':{
               'x':0,
               'y':1
            },
            'length':3,
            'shout':'moving left',
            'squad':'',
            'customizations':{
               'color':'#ff5733',
               'head':'all-seeing',
               'tail':'do-sammy'
            }
         },
         {
            'id':'gs_VyYKjWqGDBmVx79RSftS8dfK',
            'name':'isapizi',
            'latency':'500',
            'health':99,
            'body':[
               {
                  'x':9,
                  'y':10
               },
               {
                  'x':9,
                  'y':9
               },
               {
                  'x':9,
                  'y':9
               }
            ],
            'head':{
               'x':9,
               'y':10
            },
            'length':3,
            'shout':'',
            'squad':'',
            'customizations':{
               'color':'#9370db',
               'head':'villain',
               'tail':'coffee'
            }
         }
      ],
      'food':[
         {
            'x':2,
            'y':0
         },
         {
            'x':10,
            'y':8
         },
         {
            'x':5,
            'y':5
         },
         {
            'x':2,
            'y':7
         }
      ],
      'hazards':[
         
      ]
   },
   'you':{
      'id':'gs_6BfY4q3wWmj4QrgpfycM4FTQ',
      'name':'cobrinhadayas',
      'latency':'31',
      'health':99,
      'body':[
         {
            'x':0,
            'y':1
         },
         {
            'x':1,
            'y':1
         },
         {
            'x':1,
            'y':1
         }
      ],
      'head':{
         'x':0,
         'y':1
      },
      'length':3,
      'shout':'moving left',
      'squad':'',
      'customizations':{
         'color':'#ff5733',
         'head':'all-seeing',
         'tail':'do-sammy'
      }
   }
}
        response = move(request)
        expected_response =directions = ["right", "up", "down"]
        casas(request)
        assert type(response) == dict
        assert response['move'] in expected_response
        
