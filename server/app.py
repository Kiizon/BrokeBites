import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
from services.flipp_persistence import store_flyers_and_deals  
from db import db, migrate

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"]        = os.getenv("DATABASE_URL")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    migrate.init_app(app, db)

    from models.region import Region
    from models.store  import Store
    from models.deal   import Deal


    return app

if __name__ == "__main__":
    create_app().run(debug=True)
