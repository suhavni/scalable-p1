from flask import Flask
from flask_sqlalchemy import SQLAlchemy

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
if __name__ == '__main__':
    app.run()

# def create_app(test_config):
#     app = Flask(__name__)
#     app.config.from_object("config.Config")

#     # db.init_app(app)

#     # with app.app_context():
#         # from . import routes

#         # db.create_all()

# if __name__ == '__main__':
#     app = create_app(None)
#     app.run(host='0.0.0.0')