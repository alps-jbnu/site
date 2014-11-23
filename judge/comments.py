from django import forms
from django.forms import ModelForm
from django.http import HttpResponseRedirect
from django.views.generic import View
from django.views.generic.base import TemplateResponseMixin
from django.views.generic.detail import SingleObjectMixin

from judge.models import Comment


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['title', 'body', 'parent']
        widgets = {
            'parent': forms.HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'style': 'min-width:100%', 'placeholder': 'Comment title'})
        self.fields['body'].widget.attrs.update({'style': 'min-width:100%', 'placeholder': 'Comment body'})


class CommentedDetailView(TemplateResponseMixin, SingleObjectMixin, View):
    comment_page = None

    def get_comment_page(self):
        if self.comment_page is None:
            raise NotImplementedError()
        return self.comment_page

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user.profile
            comment.page = self.get_comment_page()
            comment.save()
            return HttpResponseRedirect(request.path)

        context = self.get_context_data(object=self.object, comment_form=form)
        return self.render_to_response(context)

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return self.render_to_response(self.get_context_data(
            object=self.object,
            comment_form=CommentForm(initial={'page': self.get_comment_page(), 'parent': None})
        ))

    def get_context_data(self, **kwargs):
        context = super(CommentedDetailView, self).get_context_data(**kwargs)
        context['comment_list'] = Comment.objects.filter(page=self.get_comment_page(), parent=None)
        return context
