from behave import *
from Util.api_testing_client import *
from Util.common_util import CommonUtil
from jsonpath_ng import parse


@given('I am testing {site}')
def step_impl(context, site):
    context.site = site


@when('I make a {request_type} Request to {request_file}')
def step_impl(context, request_type: RequestType, request_file):
    context.request = load_json(context.site, request_file)
    context.request_type = request_type
    context.url = "{BASE_URL}{URI}".format(
        BASE_URL=context.configuration[context.site]["BASEURL"],
        URI=context.request.get("uri")
    )
    context.request = context.request.get("requestBody", {})


@then('I replaced value of {jsonpath_query} with {value} of datatype {datatype}')
def step_impl(context, jsonpath_query, value, datatype):
    jsonpath_expr = parse(jsonpath_query)
    jsonpath_expr.update(context.request, CommonUtil.type_cast(value, datatype))


@then('I should see response code {response_code}')
def step_impl(context, response_code):
    context.response = context.apiclient.make_request(context.url,
                                                      context.request_type,
                                                      context.request)
    assert context.response is not None, "Error! No response found"
    context.response.assert_status_code(response_code)


@then('I should see response body has {jsonpath_query} value {expected_value} of datatype {expected_datatype}')
def step_impl(context, jsonpath_query, expected_value, expected_datatype):
    # print(context.response.json()["id"])

    assert context.response is not None, "Error! No response found"

    expected_value = CommonUtil.type_cast(expected_value, expected_datatype)

    context.response.assert_jsonpath(
        jsonpath_query, expected_value=expected_value)
