from app import app
from controllers import images

app.register_blueprint(images.api, url_prefix='/api')
