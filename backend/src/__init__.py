from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_caching import Cache

db = SQLAlchemy()

def init_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object("config.Config")

    db.init_app(app)

    with app.app_context():
        from . import routes, models
        db.create_all()
        db.session.commit()

    return app

app = init_app()
cache = Cache(app)
if __name__ == '__main__':
    app.run()