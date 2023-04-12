from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import Post
from .forms import PostForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def post_list(request):
    post_lists = Post.objects.all().order_by('-id')

    paginator = Paginator(post_lists, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    page_range = paginator.get_elided_page_range(
        number=page_obj.number,
        on_each_side=2,
        on_ends=2
    )

    return render(request, 'app/post_list.html', context={
        'page_obj': page_obj,
        'page_range': page_range,
    })


def post_detail(request, pk):
    post_data = get_object_or_404(Post, pk=pk)
    return render(request, 'app/post_detail.html', context={
        'post_data': post_data,
    })


@login_required
def new_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST or None)
        if form.is_valid():
            post = form.save(commit=False)
            post.contributor_id = request.user.id
            post.save()
            messages.success(request,'新規投稿をしました')
        return redirect('post:post_list')
    else:
        form = PostForm()

    return render(request, 'app/form_post.html', context={
        'form': form,
    })


@login_required
def post_delete(request, pk):
    post_data = get_object_or_404(Post, pk=pk)
    post_data.delete()
    messages.warning(request, '投稿を削除しました')
    return redirect('post:post_list')
