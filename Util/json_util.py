
from Util.common_util import CommonUtil


class JsonUtil:

    @staticmethod
    def append_obj(obj, jsonpath, value, datatype):
        value = CommonUtil.type_cast(value, datatype)


