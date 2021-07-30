

from Util.api_testing_client import load_json
from jsonpath_ng import parse
from Util.common_util import CommonUtil


if __name__ == "__main__":
    json = load_json("SOMEOTHERSITE", "getxyz")
    print(json)
    jsonpath_expr = parse("$.requestBody.array[0].index")
    jsonpath_expr.update(json, CommonUtil.type_cast("4", "int"))
    print(json)

