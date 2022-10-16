from data.data import Person, Color
from faker import Faker

faker_ru = Faker('ru-RU')
Faker.seed()


def generated_person():
    yield Person(
        full_name= faker_ru.first_name() + " " + faker_ru.last_name() + " " + faker_ru.middle_name(),
        email= faker_ru.email(),
        current_address= faker_ru.address(),
        permanent_address= faker_ru.address(),
    )

def generated_color():
    yield Color(
        color_name=["Red", "Blue", "Green", "Yellow", "Purple", "Black", "White", "Voilet", "Indigo", "Magenta", "Aqua"]
    )