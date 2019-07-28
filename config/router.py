from app import app
from controllers import images, users, posts

app.register_blueprint(images.api, url_prefix='/api')
app.register_blueprint(users.api, url_prefix='/api')
app.register_blueprint(posts.api, url_prefix='/api')
