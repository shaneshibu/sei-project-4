from app import app
from controllers import images, users

app.register_blueprint(images.api, url_prefix='/api')
app.register_blueprint(users.api, url_prefix='/api')
