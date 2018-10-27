def custom_map(function, *collections):
    for list_of_args in zip(*collections):
        function(*list_of_args)