from flask import Flask, request
from models import specs

app = Flask(__name__)

@app.route("/<string:model_name>")
def foo(model_name):
    return f'Amazing Load Balancer for inference model {model_name}'

@app.route('/inference', methods=['POST'])
def inference():
    error = None
    if request.method == 'POST' and request.headers.get('Content-Type') == 'application/json':
      for model in request.json:
          askedModel = model["modelName"]
          currentModelLatency = specs.modelsCounter[askedModel]["totalLatency"]

          specs.modelsCounter[askedModel]["stack"] += 1

          if isWarmedUp(currentModelLatency):
            specs.modelsCounter[askedModel]["totalLatency"] += specs.modelsSpecs[askedModel]
          else:
            specs.modelsCounter[askedModel]["totalLatency"] += specs.modelsSpecs[askedModel] * 2
          print(specs.modelsCounter)
      return request.json
    else:
        error = 'Invalid HTTP method or payload'

def isWarmedUp(currLatency):
    if currLatency != 0: return True; return False

if __name__ == "__main__":
    app.run()
