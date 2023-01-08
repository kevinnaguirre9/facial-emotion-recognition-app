import random
from unittest import TestCase
from unittest.mock import Mock

from faker import Faker

from src.Services.Class.Create.CreateClassCommand import CreateClassCommand
from src.Services.Class.Create.ClassCreator import ClassCreator


class CreateClassTest(TestCase):

    def setUp(self):
        self.__faker = Faker()
        self.__repository = Mock()

    def test_should_create_class(self):

        command = CreateClassCommand(
            subject = self.__faker.word(),
            degree = self.__faker.word(),
            section = self.__faker.word(),
            academic_period=random.choice(['2021-2022', '2022-2023']),
        )

        ClassCreator(self.__repository).handle(command)