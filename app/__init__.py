from flask import Flask

from config import Config

from app.extensions import db


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_mapping(
    SECRET_KEY='dev',
    SQLALCHEMY_DATABASE_URI='sqlite:///app.db'
)
    app.config.from_object(config_class)
    # Initialize Flask extensions here

    db.init_app(app)

    # Register blueprints here

    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app.users import bp as users_bp
    app.register_blueprint(users_bp, url_prefix='/users')


    from app.register import bp as register_bp
    app.register_blueprint(register_bp, url_prefix='/register')
    

    from app.auth import bp as auth_bp
    app.register_blueprint(auth_bp,url_prefix='/auth')

    

    


    @app.route('/test/')
    def test_page():
        return '<h1>Testing the Flask Application Factory Pattern</h1>'

    return app