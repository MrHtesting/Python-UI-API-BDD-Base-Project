def readCSV(filename):
    data = []
    with(open(filename)) as file:
        for line in file:
            data.append(tuple(line.split(',')))
    return data


def resolve_locator(driver, loc_id, loc_type):
    loc_type = loc_type.strip().lower()
    loc_id = loc_id.strip()

    def closure():
        return driver.find_element(loc_type, loc_id)

    return closure


def readConfig(filename, driver):
    rows = readCSV(filename)[1:]
    config = {}
    for row in rows:
        config[row[0]] = resolve_locator(driver, row[1], row[2])
    return config
