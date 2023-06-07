from flask import Flask

from api.views import blueprint
from auth.views import auth_blueprint
from extensions import db, migrate, jwt

app = Flask(__name__)
app.register_blueprint(blueprint=blueprint)
app.register_blueprint(blueprint=auth_blueprint)
app.config.from_object("config")

db.init_app(app)
migrate.init_app(app, db)
jwt.init_app(app)

if __name__ == "__main__":
    app.run(
        host=app.config.get("FLASK_RUN_HOST"),
        port=app.config.get("FLASK_RUN_PORT"),
    )
