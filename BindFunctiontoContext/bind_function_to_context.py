import types

class MyContext:
    def __init__(self, value):
        self.value = value

def standalone_function_to_bind(instance_context, message):
    return f"Bound function output: {instance_context.value} says '{message}'"

context_instance = MyContext(123)

bound_callable = types.MethodType(standalone_function_to_bind, context_instance)

output_from_bound_function = bound_callable("Hello from the bound function!")