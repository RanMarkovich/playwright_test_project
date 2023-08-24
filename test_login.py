def test_login_successfully(login_page, main_page):
    login_page.submit_login_form('ran@oolo.io', 'Rm123456!')
    main_page.expect_element_to_be_visible(main_page.welcome_banner)


def test_failed_login_wrong_email(login_page):
    login_page.submit_login_form('ranadscad@oolo.io', 'Rm123456!')
    login_page.expect_element_to_be_visible(login_page.invalid_credentials_banner)

#
# def test_failed_login_wrong_password():
#     pass
#
#
# def test_failed_login_invalid_email():
#     pass
#
#
# def test_failed_login_invalid_password():
#     pass
#
#
# def test_failed_login_with_empty_email():
#     pass
#
#
# def test_failed_login_with_empty_password():
#     pass
