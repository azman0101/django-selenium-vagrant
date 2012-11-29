from behave import then, when

from nose.tools import assert_true

BASIC_HELLO_URL = 'http://127.0.0.1:8000/hello/'


@when(u'I open the basic hello page')
def open_basic_hello_page(context):
    context.driver.get(BASIC_HELLO_URL)


@then(u'I receive an ambiguously flirtatious response')
def loves_me_loves_me_not(context):
    print context.driver.page_source
    assert_true('Hello, you!' in context.driver.page_source)
