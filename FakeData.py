from abc import ABC, abstractmethod
from faker import Faker
from random import randint


fake = Faker('uk-UA')


class DataGenerator(ABC):
    @abstractmethod
    def generate_fake_data(self) -> list:
        pass


class StudentDataGenerator(DataGenerator):
    def generate_fake_data(self) -> list:
        """Generate fake data for a student."""
        return [
            fake.first_name(),
            fake.last_name(),
            fake.date_of_birth(minimum_age=17, maximum_age=23),
        ]


class GroupDataGenerator(DataGenerator):
    def generate_fake_data(self) -> list:
        return [fake.bothify(text=f"Group-{randint(1, 12):02}-?", letters="АБВГД"),]


class TeacherDataGenerator(DataGenerator):
    def generate_fake_data(self) -> list:
        return [fake.first_name(), fake.last_name()]


class SubjectDataGenerator(DataGenerator):
    def generate_fake_data(self) -> list:
        return [fake.unique.word().capitalize(),]


class GradeDataGenerator(DataGenerator):
    def generate_fake_data(self) -> list:
        return [fake.date_this_year(),]


class DataGeneratorFactory:
    @staticmethod
    def create_data_generator(generator_type: str) -> DataGenerator:
        mapping = {
            "student": StudentDataGenerator(),
            "group": GroupDataGenerator(),
            "teacher": TeacherDataGenerator(),
            "subject": SubjectDataGenerator(),
            "grade": GradeDataGenerator()
        }
        if generator_type not in mapping:
            raise ValueError(f"Unknown data generator type: {generator_type}")
        return mapping[generator_type]
