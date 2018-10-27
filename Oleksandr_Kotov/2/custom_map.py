def custom_map(function, *collections):
        """call function for each touple of arguments from collections"""   
        for list_of_args in zip(*collections):
                function(*list_of_args)