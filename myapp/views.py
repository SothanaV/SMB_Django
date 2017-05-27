from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'myapp/post_list.html', {'posts': posts})
def control(request):
	return render(request,'smb/admin.html')
def smb(request):
	return render(request,'smb/smb.html')
