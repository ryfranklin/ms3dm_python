from flask import Flask


class MS3DM(Flask):
    def __init__(self, name):
        super().__init__(name)

        # load the configuration from config.py
        self.config.from_pyfile('app/config.py')

        # register the web blueprint
        from app.interfaces.web import bp as web_bp
        self.register_blueprint(web_bp)
