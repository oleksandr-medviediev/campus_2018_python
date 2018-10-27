def custom_map(function, *collections):
        """similar to original map() function"""   
        for list_of_args in zip(*collections):
                function(*list_of_args)