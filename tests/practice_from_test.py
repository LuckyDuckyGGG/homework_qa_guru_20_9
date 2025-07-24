from demoqa_tests.model.pages.registration_page import RegistrationPage

def test_submit_form():
    registration_page = RegistrationPage()

    registration_page.open()
    registration_page.set_name("Michael")
    registration_page.set_last_name("Rodionov")
    registration_page.set_email("jaosnjgotnasgnon@asnfomnoas.weq")
    registration_page.set_gender("Male")
    registration_page.set_phone_number('0123456789')
    registration_page.set_date_of_birth('1997', 'April', '11')
    registration_page.set_subject('English')
    registration_page.set_hobbies('Sports', 'Music')
    registration_page.set_address('Russia, Moscow, st.Pushkina, h.23')
    registration_page.upload_picture()
    registration_page.set_state('NCR')
    registration_page.set_city('Delhi')
    registration_page.submit_form()

    # Проверяем, что форма отправлена
    registration_page.should_registration_user_data(
        'Michael Rodionov',
        'jaosnjgotnasgnon@asnfomnoas.weq',
        'Male',
        '0123456789',
        '11 April,1997',
        'English',
        'Sports, Music',
        'photo.jpg',
        'Russia, Moscow, st.Pushkina, h.23',
        'NCR Delhi'
    )