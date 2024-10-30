import os
from flask import Flask
from flask_migrate import Migrate
from publicapi.src.ioc.di import DIContainer


def create_app():
    from common.infra.database import DATABASE_URL, db

    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    from publicapi.src.web import project_routes


    di_container = DIContainer()
    di_container.wire(modules=[project_routes])
    
    from common.infra.models import project, result

    db.init_app(app)
    app.register_blueprint(project_routes.projects_api)

    migrations_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'common', 'infra', 'migrations'))
    migrate = Migrate(app, db, directory=migrations_dir)

    return app
