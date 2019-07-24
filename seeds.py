from app import app, db
from models.post import Post

with app.app_context():
    db.drop_all()
    db.create_all()
    seed = []

    post_1 = Post(title='Post 1')
    seed.append(post_1)
    post_2 = Post(title='Post 2')
    seed.append(post_2)
    post_3 = Post(title='Post 3')
    seed.append(post_3)
    post_4 = Post(title='Post 4')
    seed.append(post_4)
    post_5 = Post(title='Post 5')
    seed.append(post_5)

    db.session.add_all(seed)
    db.session.commit()
