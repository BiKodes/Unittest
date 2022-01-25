def initial_transform(data):
    """
    Flatten nested dicts
    """

    for item in list(data):
        if type(data[item]) is dict:
            for key in data[item]:
                data[key] = data[item][key]
            data.pop(item)

    outside_module.do_something()
    return data



def initial_transform1(data):
    """
    Flatten nested dicts
    """
    for item in list(data):
        if type(data[item]) is dict:
            for key in data[item]:
                data[key] = data[item][key]
            data.pop(item)

    outside_module.do_something()
    outside_module.do_something()
    return data