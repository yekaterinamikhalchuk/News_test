from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from .forms import BaseRegisterForm
from django.shortcuts import redirect
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic.edit import CreateView


class BaseRegisterView(CreateView):
    model = User
    form_class = BaseRegisterForm
    success_url = '/'


@login_required
def upgrade_me(request):
    user = request.user
    authors_group = Group.objects.get(name='authors')
    if not request.user.groups.filter(name='authors').exists():
        authors_group.user_set.add(user)
    return redirect('/')

#
# class MyView(PermissionRequiredMixin, CreateView):
#     permission_required = ('news.add_Post',
#                            'news.edit_Post')
