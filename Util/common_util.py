

class CommonUtil:

    @staticmethod
    def type_cast(expected_value, expected_datatype):
        if expected_datatype == "int":
            return int(expected_value)
        elif expected_datatype == "float":
            return float(expected_value)
        elif expected_datatype == "bool":
            return True if bool(expected_value) else False
        return None

