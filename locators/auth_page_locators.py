class AuthPageLocators:
    LOGIN_FIELD = "#Email"
    PASSWORD_FIELD = "#PasswordUser"
    LOGIN_BUTTON = "body > div:nth-child(2) > div > div > div > form > button"
    ERROR_MESSAGE = "text=Неверно указан логин или пароль"
    WELCOME_MESSAGE = "text=Мои организации"

class ProfilePageLocators:
    USER_MENU = "text=Андрей Роднищев"
    PROFILE_BUTTON = "#page-wrapper-body > div.row.wrapper.border-bottom.white-bg.page-heading > div > nav > ul > li > div > div.buttons > a.btn.btn-primary.profile"
    SECURITY_TAB = "text=Безопасность"
    CHANGE_PASSWORD_BUTTON = "text=Изменить пароль"
    OLD_PASSWORD_FIELD = "#OldPassword"
    NEW_PASSWORD_FIELD = "#NewPassword"
    CONFIRM_PASSWORD_FIELD = "#ConfirmPassword"
    SAVE_PASSWORD_BUTTON = "button:has-text('Сохранить')"
    SUCCESS_MESSAGE = "text=Пароль успешно изменен"