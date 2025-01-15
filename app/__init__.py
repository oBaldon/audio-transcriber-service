from flask import Flask

def create_app():
    app = Flask(__name__)
    
    # Importar e registrar rotas
    from app.routes.transcribe import transcribe_bp
    from app.routes.health import health_bp
    
    app.register_blueprint(transcribe_bp, url_prefix="/transcribe")
    app.register_blueprint(health_bp, url_prefix="/health")
    
    return app
