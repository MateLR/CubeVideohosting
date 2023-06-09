from django.shortcuts import render, HttpResponseRedirect
from users.models import User
from .models import Video, Comment
from .forms import CommentForm
from django.views.generic.base import View
from .mixins import ViewCountMixin
from .forms import UploadVideoForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    context = {
        # 'user' : [User]
        # 'usernames': ['kar', 'unclear legacy', 'lender', 'cyreh', 'cyreh', 'cyreh', 'cyreh', 'cyreh']
        'videos': Video.objects.all().order_by("-id")
    }
    return render(request, 'cubeapp/index.html', context)


class VideoView(View, ViewCountMixin):
    def get(self, request, pk):
        video = Video.objects.get(id=pk)
        context = {
            # 'user' : [User]
            # 'usernames': ['kar', 'unclear legacy', 'lender', 'cyreh', 'cyreh', 'cyreh', 'cyreh', 'cyreh']
            'video': video,
            'comments': Comment.objects.filter(video=video).order_by("-id")
        }
        return render(request, 'cubeapp/view.html', context)


class AddComment(VideoView):
    @login_required(login_url='/users/login')
    def post(self, request, pk):
        form = CommentForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.username = request.user
            form.video_id = pk
            form.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required(login_url='/users/login')
def upload(request):
    if request.method == 'POST':
        form = UploadVideoForm(data=request.POST)
        if form.is_valid():
            print(request.FILES)
            video = Video(username=request.user,
                          title=request.POST.get('title'),
                          description=request.POST.get('description'),
                          image=request.POST.get('image'),
                          )

            video.save()
            # messages.success(request, 'Вы успешно загрузили видео')
            return HttpResponseRedirect('/')
    else:
        form = UploadVideoForm()
    context = {'form': form}
    return render(request, 'cubeapp/upload.html', context)
