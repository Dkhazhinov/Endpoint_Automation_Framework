from resources.base_page import BasePage
from page_objects.Locators import SignInPageLocators
from resources.base_element import BaseElement


class LoginPage(BasePage):
    def open_page(self):
        self.go(SignInPageLocators.SIGN_IN_URL)
        return None

    # Sign In page
    @property
    def email_address(self):
        return BaseElement(self.driver, SignInPageLocators.EMAIL_ADDRESS)

    @property
    def password_filed(self):
        return BaseElement(self.driver, SignInPageLocators.PASSWORD_FIELD)

    @property
    def sign_in_button(self):
        return BaseElement(self.driver, SignInPageLocators.SIGN_IN_BUTTON)

    @property
    def welcome_back(self):
        return BaseElement(self.driver, SignInPageLocators.WELCOME_BACK_TEXT)

    @property
    def error_message(self):
        return BaseElement(self.driver, SignInPageLocators.ERROR_MESSAGE)

    @property
    def error_invalid_email(self):
        return BaseElement(self.driver, SignInPageLocators.ERROR_MESSAGE_INVALID_EMAIL)

    @property
    def forgot_password_link(self):
        return BaseElement(self.driver, SignInPageLocators.FORGOT_PASSWORD)

    @property
    def sign_up_here_link(self):
        return BaseElement(self.driver, SignInPageLocators.SIGN_UP_HERE_LINK)

    # Passcode page
    @property
    def passcode_field(self):
        return BaseElement(self.driver, SignInPageLocators.PASSCODE_FIELD)

    @property
    def verify_and_signin_button(self):
        return BaseElement(self.driver, SignInPageLocators.VERIFY_AND_SIGNIN_BUTTON)

    @property
    def passcode_error(self):
        return BaseElement(self.driver, SignInPageLocators.PASSCODE_ERROR_MSG)

    @property
    def resend_code_link(self):
        return BaseElement(self.driver, SignInPageLocators.RESEND_CODE_LINK)

    @property
    def heading_text(self):
        return BaseElement(self.driver, SignInPageLocators.HEADING_TEXT)

    # Header
    @property
    def logged_in_profile_logo(self):
        return BaseElement(self.driver, SignInPageLocators.PROFILE_LOGO)

