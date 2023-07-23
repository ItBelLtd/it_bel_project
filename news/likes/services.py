from django.contrib.contenttypes.models import ContentType

from ..models.like import Like


def add_like(obj, user):
    """Добавить лайк к объекту"""
    obj_type = ContentType.objects.get_for_model(obj)
    like, is_created = Like.objects.get_or_create(
        content_type=obj_type,
        object_id=obj.pk,
        user=user
    )
    return like


def remove_like(obj, user):
    """Удалить лайк с объекта"""
    obj_type = ContentType.objects.get_for_model(obj)
    Like.objects.filter(
        content_type=obj_type,
        object_id=obj.pk,
        user=user
    ).delete()
