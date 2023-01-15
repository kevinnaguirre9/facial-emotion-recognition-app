from unittest import TestCase

from src.Domain.Class.ValueObjects.ClassId import ClassId
from src.Domain.Session.Session import Session
from src.Domain.Session.ValueObjects.SessionId import SessionId


class SessionEntityTest(TestCase):

    def test_should_create_session_without_start_date_and_end_date(self):
        session_entity = Session.create(
            SessionId(),
            ClassId(),
        )

        self.assertIsNone(session_entity.start_date())
        self.assertIsNone(session_entity.end_date())