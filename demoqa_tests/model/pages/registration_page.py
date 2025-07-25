from selene import browser, have
from demoqa_tests import resource
from demoqa_tests.data.users import User, Gender, Hobbies


class RegistrationPage:

    def __init__(self):
        self.registration_user_data = browser.element('.table-responsive').all('td').even
        self.state = browser.element('#state')
        self.city = browser.element('#city')
        self.dropdown = browser.all('[id^=react-select][id*=option]')


    def open(self):
        browser.config.window_width = 1920
        browser.config.window_height = 1080
        browser.open('https://demoqa.com/automation-practice-form')

    def register(self, user: User):
        self.set_first_name(user)
        self.set_last_name(user)
        self.set_email(user)
        self.set_gender(user)
        self.set_user_number(user)
        self.set_date_of_birth(user)
        self.set_subject(user)
        self.set_hobbies(user)
        self.upload_photo(user)
        self.set_address(user)
        self.set_state(user)
        self.set_city(user)
        self.submit_form()

    def should_registration_user_data(self, user: User):
        formatted_hobbies = ', '.join([hobby.value[0] for hobby in user.hobbies])
        browser.element('.table-responsive').all('td').even.should(
            have.exact_texts(
                f"{user.first_name} {user.last_name}",
                user.email,
                user.gender.value,
                user.phone_number,
                f"{user.date_of_birth_day} {user.date_of_birth_month},{user.date_of_birth_year}",
                user.subject,
                formatted_hobbies,
                user.picture,
                user.address,
                f"{user.state} {user.city}"
            )
        )

    def set_first_name(self, user: User):
        browser.element('#firstName').type(user.first_name)

    def set_last_name(self, user: User):
        browser.element('#lastName').type(user.last_name)

    def set_email(self, user: User):
        browser.element('#userEmail').type(user.email)

    def set_gender(self, user: User):
        if user.gender == Gender.MALE:
            browser.element(f'[for="gender-radio-1"]').click()
        elif user.gender == Gender.FEMALE:
            browser.element(f'[for="gender-radio-2"]').click()
        elif user.gender == Gender.OTHER:
            browser.element(f'[for="gender-radio-3"]').click()

    def set_user_number(self, user: User):
        browser.element('#userNumber').type(user.phone_number)

    def set_date_of_birth(self, user: User):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__year-select').type(user.date_of_birth_year)
        browser.element('.react-datepicker__month-select').type(user.date_of_birth_month)
        browser.element(
            f'.react-datepicker__day--0{user.date_of_birth_day}:not(.react-datepicker__day--otside-month)').click()

    def set_subject(self, user: User):
        browser.element('#subjectsInput').type(user.subject).press_enter()

    def set_hobbies(self, user: User):
        hobbies_mapping = {
            Hobbies.SPORTS: '1',
            Hobbies.READING: '2',
            Hobbies.MUSIC: '3'
        }
        for hobby in user.hobbies:
            if hobby in hobbies_mapping:
                browser.element(f'[for="hobbies-checkbox-{hobbies_mapping[hobby]}"]').click()

    def upload_photo(self, user: User):
        browser.element('#uploadPicture').set_value(resource.path(user.picture))

    def set_address(self, user: User):
        browser.element('#currentAddress').type(user.address)

    def set_state(self, user: User):
        self.state.click()
        self.dropdown.element_by(
            have.exact_text(user.state)
        ).click()

    def set_city(self, user: User):
        self.city.click()
        self.dropdown.element_by(
            have.exact_text(user.city)
        ).click()

    def submit_form(self):
        browser.element('#submit').click()
