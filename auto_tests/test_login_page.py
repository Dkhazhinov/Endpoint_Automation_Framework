from pytest import mark
from page_objects.LoginPage import LoginPage
from faker import Faker
from helpful_functions import gmail_mail_imap

_fake = Faker()


@mark.regression
@mark.smoke
@mark.usefixtures("one_time_setup")
class LoginPageTests:

    def test_verify_that_invalid_email_is_not_accepted(self):
        login_page = LoginPage(self.driver)

        login_page.open_page()
        login_page.email_address.enter_text(_fake.first_name() + _fake.last_name())
        login_page.password_filed.enter_text(
            _fake.password(length=10, special_chars=True, digits=True, upper_case=True, lower_case=True))
        assert "Email Address should be valid email" == login_page.error_invalid_email.get_text

    def test_unable_to_login_with_wrong_credentials(self):
        login_page = LoginPage(self.driver)

        login_page.open_page()
        login_page.email_address.enter_text(_fake.first_name() + _fake.last_name() + "@mailinator.com")
        login_page.password_filed.enter_text(
            _fake.password(length=10, special_chars=True, digits=True, upper_case=True, lower_case=True))
        login_page.sign_in_button.click()
        assert "Whoops!" in login_page.error_message.get_text

    def test_verify_sign_in_button_visible_when_form_not_empty(self):
        login_page = LoginPage(self.driver)

        login_page.open_page()
        login_page.email_address.enter_text(_fake.first_name() + _fake.last_name() + "@mailinator.com")
        login_page.password_filed.enter_text(
            _fake.password(length=10, special_chars=True, digits=True, upper_case=True, lower_case=True))
        assert "Sign In" == login_page.sign_in_button.get_text

    def test_verify_page_elements_presented(self):
        login_page = LoginPage(self.driver)

        login_page.open_page()
        assert "Welcome back!" == login_page.welcome_back.get_text
        assert "Forgot password?" == login_page.forgot_password_link.get_text
        assert "Sign up here" == login_page.sign_up_here_link.get_text

    def test_verify_login_with_valid_credentials(self):
        user_data = self.credentials
        login_page = LoginPage(self.driver)

        login_page.open_page()
        login_page.email_address.enter_text(user_data['user1']['email'])
        login_page.password_filed.enter_text(user_data['user1']['password'])
        login_page.sign_in_button.click()

        assert "Enter your 6-digit passcode" == login_page.heading_text.get_text
        assert "Verify and Sign In" == login_page.verify_and_signin_button.get_text

        # SMS 6 digits passcode is texted to the phone number that forwards message to email
        # Then gmail_mail_imap.get_login_passcode method reads latest email and returns Passcode
        passcode = gmail_mail_imap.get_login_passcode(sleep=5)
        if not passcode:
            login_page.resend_code_link.click()
        else:
            login_page.passcode_field.enter_text(passcode)
        login_page.verify_and_signin_button.click()
        login_page.logged_in_profile_logo.find_element()
        assert "/signin" not in login_page.get_current_url
