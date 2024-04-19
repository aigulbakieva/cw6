import secrets
import random

from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect

from users.forms import UserRegisterForm, UserForm
from users.models import User

from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        token = secrets.token_hex(16)
        user = form.save()
        user.token = token
        user.is_active = False
        user.save()
        host = self.request.get_host()
        link = f"http://{host}/users/confirm-register/{token}"
        message = f"Вы успешно зарегистрировались на нашей платформе, подтвердите почту по ссылке: {link}"
        send_mail(
            subject='Поздравляем с регистрацией',
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[user.email]
        )
        return super().form_valid(form)


def confirm_email(request, token):
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse('users:login'))


class UserUpdateView(UpdateView):
    model = User
    success_url = reverse_lazy('users:profile')
    form_class = UserForm

    def get_object(self, queryset=None):
        return self.request.user


def generate_new_password(request):
    new_password = "".join([str(random.randint(0, 9) for _ in range(12))])
    send_mail(
        subject='Восстановление пароля',
        message=f'Ваш новый пароль: {new_password}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[request.user.email]
    )
    request.user.set_password(new_password)
    request.user.save()
    return redirect(reverse('users:login'))
