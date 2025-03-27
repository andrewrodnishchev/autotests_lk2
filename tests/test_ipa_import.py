from pages.auth_page import AuthPage
from pages.import_ipa_page import IPAImportPage
import config


class TestIPAImport:
    def test_ipa_devices_import(self, page, stand):
        auth_page = AuthPage(page)
        ipa_import_page = IPAImportPage(page)

        auth_page.navigate_to_login_page()
        auth_page.login(config.LOGIN, config.CORRECT_PASSWORD)
        auth_page.should_be_on_dashboard()

        ipa_import_page.navigate_to_devices_section()
        ipa_import_page.open_import_modal()
        ipa_import_page.select_ipa_domain()
        ipa_import_page.fill_connection_details()
