from flask import Flask
from app.config import Config



app = Flask(__name__)
app.config.from_object(Config)


# Импорт моделей и api
from app import routes
from app import ml
if __name__ == "__main__":
    app.run(host='0.0.0.0')
