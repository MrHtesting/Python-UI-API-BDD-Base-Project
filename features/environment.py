from Util.Webbrowser import *
from Util.api_testing_client import *
from Util.csvreader import *


def before_scenario(context, scenario):
    print("Running before")
    # context.browser = WebBrowser().getdriver()
    # context.locator = readConfig("Elements.csv",  context.browser)
    # context.browser.implicitly_wait(10)
    context.apiclient = ApiTestingClient()
    context.configuration = load_config()


# def after_scenario(context, scenario):
#     context.browser.quit()
