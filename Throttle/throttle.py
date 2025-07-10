import time

class Throttler:
    def __init__(self, rate_per_second):
        if rate_per_second <= 0:
            raise ValueError("Rate per second must be positive")
        self.rate_per_second = rate_per_second
        self.period = 1.0 / rate_per_second
        self.next_allowed_time = time.time()

    def wait_for_permission(self):
        current_time = time.time()
        
        actual_start_time = max(current_time, self.next_allowed_time)
        
        if actual_start_time > current_time:
            time.sleep(actual_start_time - current_time)
            
        self.next_allowed_time = actual_start_time + self.period