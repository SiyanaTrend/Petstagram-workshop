from django.shortcuts import render, redirect

from petstagram.common.models import Like
from petstagram.photos.models import Photo


def home_page(request):
    all_photos = Photo.objects.all()

    context = {
        'all_photos': all_photos,
    }
    return render(request, 'common/home-page.html', context)


def like_functionality(request, photo_id: int):
    liked_object = Like.objects.filter(
        to_photo_id=photo_id,
    ).first()

    if liked_object:
        liked_object.delete()
    else:
        like = Like(to_photo_id=photo_id)
        like.save()

    return redirect(request.META.get('HTTP_REFERER') + f'#{photo_id}')
    # when a fragment is added -> ... + f'#{photo_id}'
    # => when the heart button is clicked, the page stays on the liked post

    # return redirect(request.META.get('HTTP_REFERER'))
    # => when the heart button is clicked, the page returns at the beginning
