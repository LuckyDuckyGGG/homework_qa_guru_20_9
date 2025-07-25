from demoqa_tests.data.users import User, Gender, Hobbies
from demoqa_tests.model.pages.registration_page import RegistrationPage

def test_submit_form():
    registration_page = RegistrationPage()
    user = User(
        first_name="Michael",
        last_name="Rodionov",
        email="jaosnjgotnasgnon@asnfomnoas.weq",
        gender=Gender.MALE,
        phone_number="0123456789",
        date_of_birth_year= 1997,
        date_of_birth_month="April",
        date_of_birth_day=11,
        subject="English",
        hobbies=[Hobbies.SPORTS, Hobbies.MUSIC],
        picture="photo.jpg",
        address="Russia, Moscow, st.Pushkina, h.23",
        state="NCR",
        city="Delhi"
    )
    registration_page.open()
    registration_page.register(user)
    registration_page.should_registration_user_data(user)