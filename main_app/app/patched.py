def get_patched_app():
    from gevent import monkey
    monkey.patch_all()
    from app.app import app
    return app


app = get_patched_app()