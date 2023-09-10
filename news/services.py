from django.contrib.contenttypes.models import ContentType

from news.models.like import Like


def add_remove_like(obj, user):
    """Добавить или удалить лайк у объекта"""

    obj_type = ContentType.objects.get_for_model(obj)
    vote_val = get_remove_vote(obj=obj, user=user)

    if vote_val == Like.LIKE:
        return
    if vote_val == Like.DISLIKE or vote_val is None:
        Like.objects.create(
            content_type=obj_type,
            object_id=obj.pk,
            user=user,
            vote=Like.LIKE
        )
    return


def add_remove_dislike(obj, user):
    """Добавить или удалить дизлайк у объекта"""

    obj_type = ContentType.objects.get_for_model(obj)
    vote_val = get_remove_vote(obj=obj, user=user)

    if vote_val == Like.DISLIKE:
        return
    if vote_val == Like.LIKE or vote_val is None:
        Like.objects.create(
            content_type=obj_type,
            object_id=obj.pk,
            user=user,
            vote=Like.DISLIKE
        )
    return


def get_remove_vote(obj, user):
    """Удалить лайк или дизлайк с объекта
    и вернуть его значение"""

    like = get_vote(obj, user)

    if not like:
        return None

    vote_value = like.vote
    like.delete()
    return vote_value  # noqa


def get_vote(obj, user):
    obj_type = obj_type = ContentType.objects.get_for_model(obj)
    return Like.objects.filter(
        object_id=obj.pk,
        content_type=obj_type,
        user=user
    ).first()
