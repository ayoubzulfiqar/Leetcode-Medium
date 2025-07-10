def callPolyfill(fn, *args):
    obj = args[0]
    function_args = args[1:]
    return fn(obj, *function_args)