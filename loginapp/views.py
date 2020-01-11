from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.views import generic
from .forms import LoginForm, UserCreateForm
from django.contrib.sites.shortcuts import get_current_site
from django.core.signing import BadSignature, SignatureExpired, loads, dumps
from django.http import Http404, HttpResponseBadRequest
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib.auth import get_user_model
#from .models import User

User = get_user_model()
# Create your views here.

class Top(generic.TemplateView):
    template_name = 'top.html'

class LoginMGame(LoginView):
    template_name = 'login.html'

class LogoutMGame(LoginRequiredMixin, LogoutView):
    template_name = 'logout.html'

#class UserCreate(generic.CreateView):
#    template_name = 'user_create.html'
#    form_class = UserCreateForm

class UserCreate(generic.CreateView):
    template_name= 'user_create.html'
    form_class = UserCreateForm

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.save()

        current_site = get_current_site(self.request)
        domain = current_site.domain
        context = {
            'protocol': self.request.scheme,
            'domain': domain,
            'token': dumps(user.pk),
            'user': user,
        }

        subject = render_to_string('mail_template/create/subject.txt', context)
        message = render_to_string('mail_template/create/message.txt', context)

        user.email_user(subject, message)
        return redirect('user_create_done')

class UserCreateDone(generic.TemplateView):
    template_name = 'user_create_done.html'

class UserCreateComplete(generic.TemplateView):
    template_name = 'user_create_complete.html'
    timeout_seconds = getattr(settings, 'ACTIVATION_TIMEOUT_SECONDS', 60*60*24)

    def get(self, request, **kwargs):
        token = kwargs.get('token')
        try:
            user_pk = loads(token, max_age=self.timeout_seconds)
        except SignatureExpired:
            return HttpResponseBadRequest()
        except BadSignature:
            return HttpResponseBadRequest()
        else:
            try:
                user = User.objects.get(pk=user_pk)
            except User.DoesNotExist:
                return HttpResponseBadRequest()
            else:
                if not user.is_active:
                    user.is_active = True
                    user.save()
                    return super().get(request, **kwargs)

        return HttpResponseBadRequest()

