from behave import *


@when(u'Ipip add "{some:d}" in xyz')
def step_impl(context, some):
    print("Printing: ", some)


@then("I should see a good day")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """


# raise NotImplementedError(u'STEP: Then I should see a good day')
@when('I click "{element}" from google')
def step_impl(context, element):
    context.locator[element]().click()


@when('I type "{data}" in "{element}" field')
def step_impl(context, data, element):
    context.locator[element]().send_keys(data)


@given('I have a  {API} request')
def step_impl(context, API):
    API
