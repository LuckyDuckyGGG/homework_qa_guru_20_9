from selene import browser, have

from demoqa_tests import resource


class RegistrationPage:

    def __init__(self):
        self.registration_user_data = browser.element('.table-responsive').all('td').even
        self.state = browser.element('#state')
        self.city = browser.element('#city')

    def open(self):
        browser.config.window_width = 1920
        browser.config.window_height = 1080
        browser.open('https://demoqa.com/automation-practice-form')

    def set_name(self, value):
        browser.element('#firstName').type(value)

    def set_last_name(self, value):
        browser.element('#lastName').type(value)

    def set_email(self, value):
        browser.element('#userEmail').type(value)

    def set_gender(self, gender):
        if gender == "Male":
            browser.element(f'[for="gender-radio-1"]').click()
        elif gender == "Female":
            browser.element(f'[for="gender-radio-2"]').click()
        elif gender == "Other":
            browser.element(f'[for="gender-radio-3"]').click()

    def set_phone_number(self, value):
        browser.element('#userNumber').type(value)


    def set_date_of_birth(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__year-select').type(year)
        browser.element('.react-datepicker__month-select').type(month)
        browser.element(f'.react-datepicker__day--0{day}:not(.react-datepicker__day--otside-month)').click()

    def set_subject(self, value):
        browser.element('#subjectsInput').type(value).press_enter()

    def set_hobbies(self, *hobbies) -> None:
        hobbies_mapping = {
            "Sports": '1',
            "Reading": '2',
            "Music": '3'
        }

        for hobby in hobbies:
            if hobby in hobbies_mapping:
                browser.element(f'[for="hobbies-checkbox-{hobbies_mapping[hobby]}"]').click()

    def upload_picture(self):
        browser.element('#uploadPicture').set_value(resource.path('photo.jpg'))

    def set_address(self, value):
        browser.element('#currentAddress').type(value)

    def set_state(self, value):
        self.state.click()
        browser.all('[id^=react-select][id*=option]').element_by(
            have.exact_text(value)
        ).click()

    def set_city(self, value):
        self.city.click()
        browser.all('[id^=react-select][id*=option]').element_by(
            have.exact_text(value)
        ).click()

    def submit_form(self):
        browser.element('#submit').click()

    def should_registration_user_data(self, full_name, email, gender, phone_number, date_of_birth, subject, hobbies, picture, address, state_and_city):
        browser.element('.table-responsive').all('td').even.should(
            have.exact_texts(
                full_name,
                email,
                gender,
                phone_number,
                date_of_birth,
                subject,
                hobbies,
                picture,
                address,
                state_and_city
            )
        )



