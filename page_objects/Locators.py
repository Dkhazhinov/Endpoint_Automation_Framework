from selenium.webdriver.common.by import By


class SignInPageLocators(object):
    # Sing In page locators
    SIGN_IN_URL = '/signin'
    WELCOME_BACK_TEXT = (By.XPATH, "//*[contains(text(),'Welcome back!')]")
    EMAIL_ADDRESS = (By.XPATH, "//input[@id='email']")
    PASSWORD_FIELD = (By.XPATH, "//input[@id='password']")
    FORGOT_PASSWORD = (By.XPATH, "//a[contains(text(),'Forgot password?')]")
    SIGN_IN_BUTTON = (By.XPATH, "//button[@type='submit' and contains(text(), 'Sign In')]")
    SIGN_UP_HERE_LINK = (By.XPATH, "//a[contains(text(),'Sign up here')]")
    ERROR_MESSAGE = (By.XPATH, "//div[@class='formError']")
    ERROR_MESSAGE_INVALID_EMAIL = (By.XPATH, "//span[@class='error-msg']")

    # Passcode page
    PASSCODE_FIELD = (By.XPATH, "//input[@id='sms']")
    VERIFY_AND_SIGNIN_BUTTON = (By.XPATH, "//span[contains(@class,'fluid') and contains(@role, 'button')]")
    PASSCODE_ERROR_MSG = (By.XPATH, "//span[contains(@class,'error-msg') or contains(@text, 'Please enter your 6-digit passcode.')]")
    RESEND_CODE_LINK = (By.XPATH, "//button[contains(text(),'Resend code')]")
    HEADING_TEXT = (By.XPATH, "//h3[contains(text(),'Enter your 6-digit passcode')]")

    # Header
    PROFILE_LOGO = (By.XPATH, "//img[@class='profileImage']")

