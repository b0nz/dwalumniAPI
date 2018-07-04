from django.apps import AppConfig


class EducationConfig(AppConfig):
    name = 'education'

class MajorConfig(AppConfig):
    name = 'major'

class EducationMajorConfig(AppConfig):
    name = 'education_major'

class UserEducationConfig(AppConfig):
    name = 'user_education'