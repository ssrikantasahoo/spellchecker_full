import os
import logging
from flask import Flask
from blueprints.routes import bp
from config.settings import Config

def create_app():
    # Ensure logs directory exists
    os.makedirs("logs", exist_ok=True)

    # Configure logging
    logging.basicConfig(
        filename='logs/app.log',
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

    app = Flask(__name__)
    app.config.from_object(Config)
    app.register_blueprint(bp)
    return app


if __name__ == '__main__':
    app = create_app()

    print("\n======================================")
    print("🚀 Flask Server is Live!")
    print("👉 Open: http://localhost:5000")
    print("👉 Open: http://127.0.0.1:5000")
    print("======================================\n")
    
    app.run(host='0.0.0.0', port=5000, debug=True, use_reloader=False)

