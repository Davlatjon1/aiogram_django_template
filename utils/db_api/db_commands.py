from django_project.telegrambot.usersmanage.models import User
from asgiref.sync import sync_to_async


async def get_user(user_id, full_name, username):
    user = await select_user(user_id=int(user_id), username=username)
    if not user:
        user = User(user_id=int(user_id), name=full_name, username=username)
        user.save()
    return user


@sync_to_async
def select_user(user_id: int, username: str = None):
    user = User.objects.filter(user_id=user_id).first()
    # if username:
    #     user.username = username
    #     user.save()
    return user
