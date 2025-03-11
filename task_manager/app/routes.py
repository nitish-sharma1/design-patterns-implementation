from flask import Blueprint


def register_routes(app):
    from .controllers import auth_controller, task_controller

    app.register_blueprint(auth_controller.bp, url_prefix="/auth")
    app.register_blueprint(task_controller.bp, url_prefix="/tasks")
