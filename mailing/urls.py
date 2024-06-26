from django.urls import path

from mailing.apps import MailingConfig
from mailing.views import MailingListView, MailingDetailView, MailingCreateView, MailingUpdateView, MailingDeleteView, \
    ClientListView, ClientCreateView, ClientUpdateView, ClientDeleteView, MessageListView, MessageCreateView, \
    MessageUpdateView, MessageDeleteView, IndexView, LogListView

app_name = MailingConfig.name

urlpatterns = [
    path('mailing/', MailingListView.as_view(), name='mailing_list'),
    path('mailing/<int:pk>/', MailingDetailView.as_view(), name='mailing_detail'),
    path('mailing/create', MailingCreateView.as_view(), name='mailing_create'),
    path('mailing/update/<int:pk>', MailingUpdateView.as_view(), name='mailing_update'),
    path('mailing/delete/<int:pk>', MailingDeleteView.as_view(), name='mailing_delete'),

    path('client/', ClientListView.as_view(), name='client_list'),
    path('client/create/', ClientCreateView.as_view(), name='client_create'),
    path('client/update/<int:pk>', ClientUpdateView.as_view(), name='client_update'),
    path('client/delete/<int:pk>', ClientDeleteView.as_view(), name='client_delete'),

    path('message/', MessageListView.as_view(), name='message_list'),
    path('message/create', MessageCreateView.as_view(), name='message_create'),
    path('message/update/<int:pk>', MessageUpdateView.as_view(), name='message_update'),
    path('message/delete/<int:pk>', MessageDeleteView.as_view(), name='message_delete'),

    path('', IndexView.as_view(), name='message_delete'),
    path('mailing/log/', LogListView.as_view(), name='log_list'),
]
