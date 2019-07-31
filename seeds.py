from random import randrange
import requests
from app import app, db
from models.user import UserSchema
from models.image import Image
from models.post import Post, Entry
from config.environment import pixabay_api_key

# get random users from randomuser.me
response = requests.get(
    'https://randomuser.me/api/',
    params={
        'results': 74,
        'nat': 'gb',
        'inc': 'name,email,login,picture',
        'noinfo': True
})
api_users = response.json()['results']

# get images from pixabay
response = requests.get(
    'https://pixabay.com/api/',
    params={
        'key': pixabay_api_key,
        'editors_choice': True,
        'page': 1,
        'per_page': 200
    }
)
api_images = response.json()['hits']

# get images from pixabay
response = requests.get(
    'https://pixabay.com/api/',
    params={
        'key': pixabay_api_key,
        'editors_choice': True,
        'page': 2,
        'per_page': 200
    }
)
api_images = api_images + response.json()['hits']

user_schema = UserSchema()

with app.app_context():
    db.drop_all()
    db.create_all()

    # create new users from api users
    users = []
    for user in api_users:
        user, errors = user_schema.load({
            'username': user['login']['username'],
            'email': user['email'],
            'password':'pass',
            'password_confirmation': 'pass',
            'picture': user['picture']['large']
        })
        if errors:
            raise Exception(errors)
        user.save()
        users.append(user)

    user_1, errors = user_schema.load({
        'username':'user1',
        'email':'email1@email.com',
        'password':'pass',
        'password_confirmation': 'pass'
        })
    if errors:
        raise Exception(errors)
    user_1.save()

    user_2, errors = user_schema.load({
        'username':'user2',
        'email':'email2@email.com',
        'password':'pass',
        'password_confirmation': 'pass'
        })
    if errors:
        raise Exception(errors)

    # create new images from api images
    images = []
    for image in api_images:
        image = Image(
            url=image['webformatURL'],
            uploader=users[randrange(len(users))],
            height=image['webformatHeight'],
            width=image['webformatWidth']
        )
        images.append(image)


    # for each user, add all uploaded images to posts, each post no more than 3 entries long
    for user in users:
        if user.uploaded_images:
            i = 0
            while i < len(user.uploaded_images):
                entries = []
                pos = 0
                while pos < randrange(1, 4) and i < len(user.uploaded_images):
                    entry = Entry(
                        image=user.uploaded_images[i],
                        caption=f'Caption {pos}',
                        position=pos
                    )
                    entries.append(entry)
                    pos += 1
                    i += 1
                post = Post(
                    title='New Post',
                    creator=user,
                    post_entries=entries
                )
                post.save()
                print(post.creator, post.post_entries)

    db.session.commit()
