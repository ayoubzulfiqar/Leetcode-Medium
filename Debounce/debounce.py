import threading

def debounce(fn, t):
    delay_seconds = t / 1000.0
    
    current_timer = None 

    def debounced(*args, **kwargs):
        nonlocal current_timer

        if current_timer is not None:
            current_timer.cancel()
        
        def execute_fn():
            fn(*args, **kwargs)
        
        new_timer = threading.Timer(delay_seconds, execute_fn)
        
        current_timer = new_timer
        
        new_timer.start()
    
    return debounced