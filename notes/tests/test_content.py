from datetime import datetime, timedelta

from django.contrib.auth import get_user_model
from django.conf import settings
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from notes.models import Note


User = get_user_model()


class TestNoteList(TestCase):
    NOTE_LIST_URL = reverse('notes:list')

    @classmethod
    def setUpTestData(cls):
        pass