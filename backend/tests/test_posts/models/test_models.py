import pytest

from django.db.utils import IntegrityError

from posts.models import Post


@pytest.mark.django_db
def test_post_creation_successful(sample_user):
    post = Post.objects.create(title="test", description="desc", creator=sample_user)
    assert post.title == "test"
    assert post.description == "desc"
    assert post.creator.email == sample_user.email


@pytest.mark.django_db
def test_post_creation_without_creator():
    with pytest.raises(IntegrityError):
        Post.objects.create(title="test", description="desc")


@pytest.mark.django_db
def test_post_suspending(sample_user):
    post = Post.objects.create(title="test", description="desc", creator=sample_user)
    assert post.suspended == False

    post.suspend()

    reload_post = Post.objects.get(pk=post.pk)
    assert reload_post.suspended == True
