def custom_filter(func, iter):
    return [i for i in iter if func(i)]
