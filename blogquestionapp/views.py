from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.utils.text import slugify
from django.shortcuts import get_object_or_404
from .models import QuestionPost, QuestionCategory, QuestionTag, QuestionComment
from django.core.exceptions import PermissionDenied
from django.db.models import Q
from .forms import QuestionCommentForm


class QuestionPostList(ListView):
    model = QuestionPost
    ordering = '-pk'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(QuestionPostList, self).get_context_data()
        context['categories'] = QuestionCategory.objects.all()
        context['no_category_post_count'] = QuestionPost.objects.filter(category=None).count()
        return context


class QuestionPostDetail(DetailView):
    model = QuestionPost

    def get_context_data(self, **kwargs):
        context = super(QuestionPostDetail, self).get_context_data()
        context['categories'] = QuestionCategory.objects.all()
        context['no_category_post_count'] = QuestionPost.objects.filter(category=None).count()
        context['comment_form'] = QuestionCommentForm
        return context


class QuestionPostCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = QuestionPost
    fields = ['title', 'hook_text', 'content', 'head_image', 'file_upload', 'category']

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff or self.request.user.is_authenticated

    def form_valid(self, form):
        current_user = self.request.user
        if current_user.is_authenticated and (current_user.is_staff or current_user.is_superuser or current_user.is_authenticated):
            form.instance.author = current_user
            response = super(QuestionPostCreate, self).form_valid(form)

            tags_str = self.request.POST.get('tags_str')
            if tags_str:
                tags_str = tags_str.strip()

                tags_str = tags_str.replace(',', ';')
                tags_list = tags_str.split(';')

                for t in tags_list:
                    t = t.strip()
                    tag, is_tag_created = QuestionTag.objects.get_or_create(name=t)
                    if is_tag_created:
                        tag.slug = slugify(t, allow_unicode=True)
                        tag.save()
                    self.object.tags.add(tag)

            return response

        else:
            return redirect('/blogquestionapp/')


class QuestionPostUpdate(LoginRequiredMixin, UpdateView):
    model = QuestionPost
    fields = ['title', 'hook_text', 'content', 'head_image', 'file_upload', 'category']

    template_name = 'blogquestionapp/questionpost_update_form.html'

    def get_context_data(self, **kwargs):
        context = super(QuestionPostUpdate, self).get_context_data()
        if self.object.tags.exists():
            tags_str_list = list()
            for t in self.object.tags.all():
                tags_str_list.append(t.name)
            context['tags_str_default'] = '; '.join(tags_str_list)

        return context

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user == self.get_object().author:
            return super(QuestionPostUpdate, self).dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied

    def form_valid(self, form):
        response = super(QuestionPostUpdate, self).form_valid(form)
        self.object.tags.clear()

        tags_str = self.request.POST.get('tags_str')
        if tags_str:
            tags_str = tags_str.strip()
            tags_str = tags_str.replace(',', ';')
            tags_list = tags_str.split(';')

            for t in tags_list:
                t = t.strip()
                tag, is_tag_created = QuestionTag.objects.get_or_create(name=t)
                if is_tag_created:
                    tag.slug = slugify(t, allow_unicode=True)
                    tag.save()
                self.object.tags.add(tag)

        return response


def category_page(request, slug):
    if slug == 'no_category':
        category = '미분류'
        post_list = QuestionPost.objects.filter(category=None)
    else:
        category = QuestionCategory.objects.get(slug=slug)
        post_list = QuestionPost.objects.filter(category=category)

    return render(
        request,
        'blogquestionapp/questionpost_list.html',
        {
            'post_list': post_list,
            'categories': QuestionCategory.objects.all(),
            'no_category_post_count': QuestionPost.objects.filter(category=None).count(),
            'category': category,
        }
    )


def tag_page(request, slug):
    tag = QuestionTag.objects.get(slug=slug)
    post_list = tag.questionpost_set.all()
    return render(
        request,
        'blogquestionapp/questionpost_list.html',
        {
            'questionpost_list': post_list,
            'tag': tag,
            'categories': QuestionCategory.objects.all(),
            'no_category_post_count': QuestionPost.objects.filter(category=None).count(),
        }
    )


def new_comment(request, pk):
    if request.user.is_authenticated:
        post = get_object_or_404(QuestionPost, pk=pk)

        if request.method == 'POST':
            comment_form = QuestionCommentForm(request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.post = post
                comment.author = request.user
                comment.save()
                return redirect(comment.get_absolute_url())
        else:
            return redirect(post.get_absolute_url())
    else:
        raise PermissionDenied


class QuestionCommentUpdate(LoginRequiredMixin, UpdateView):
    model = QuestionComment
    form_class = QuestionCommentForm

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user == self.get_object().author:
            return super(QuestionCommentUpdate, self).dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied


def delete_comment(request, pk):
    comment = get_object_or_404(QuestionComment, pk=pk)
    post = comment.post
    if request.user.is_authenticated and request.user == comment.author:
        comment.delete()
        return redirect(post.get_absolute_url())
    else:
        raise PermissionDenied


class QuestionPostSearch(QuestionPostList):
    paginate_by = None

    def get_queryset(self):
        q = self.kwargs['q']
        post_list = QuestionPost.objects.filter(
            Q(title__contains=q) | Q(tags__name__contains=q)
        ).distinct()
        return post_list

    def get_context_data(self, **kwargs):
        context = super(QuestionPostSearch, self).get_context_data()
        q = self.kwargs['q']
        context['search_info'] = f'Search: {q} ({self.get_queryset().count()})'

        return context