import inspect

def curry(func):
    sig = inspect.signature(func)
    num_expected_args = len(sig.parameters)

    def _curried_wrapper(*args_so_far):
        def inner_curried_func(*new_args):
            all_args = args_so_far + new_args
            if len(all_args) >= num_expected_args:
                return func(*all_args[:num_expected_args])
            else:
                return _curried_wrapper(*all_args)
        return inner_curried_func

    return _curried_wrapper()