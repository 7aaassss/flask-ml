from app import app
from app import routes
from app import ml

if __name__ == "__main__":
    app.run(debug=True, host='localhost', port=8000)
    