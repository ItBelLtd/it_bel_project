from django.contrib.contenttypes.models import ContentType

from news.models.like import LikeDislike


def add_remove_like(obj, user):
    """Добавить или удалить лайк у объекта"""

    obj_type = ContentType.objects.get_for_model(obj)
    vote_val = get_remove_vote(obj=obj, obj_type=obj_type, user=user)

    if vote_val == LikeDislike.LIKE:
        return
    if vote_val == LikeDislike.DISLIKE or vote_val is None:
        LikeDislike.objects.create(
            content_type=obj_type,
            object_id=obj.pk,
            user=user,
            vote=LikeDislike.LIKE
        )
    return


def add_remove_dislike(obj, user):
    """Добавить или удалить дизлайк у объекта"""

    obj_type = ContentType.objects.get_for_model(obj)
    vote_val = get_remove_vote(obj=obj, obj_type=obj_type, user=user)

    if vote_val == LikeDislike.DISLIKE:
        return
    if vote_val == LikeDislike.LIKE or vote_val is None:
        LikeDislike.objects.create(
            content_type=obj_type,
            object_id=obj.pk,
            user=user,
            vote=LikeDislike.DISLIKE
        )
    return


def get_remove_vote(obj, obj_type, user):
    """Удалить лайк или дизлайк с объекта
    и вернуть его значение"""

    vote = LikeDislike.objects.filter(
        content_type=obj_type,
        object_id=obj.pk,
        user=user
        ).first()
    if vote:
        vote_value = vote.vote
        vote.delete()
        return vote_value  # noqa

    return None
