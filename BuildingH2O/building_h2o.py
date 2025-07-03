import threading

class H2O:
    def __init__(self):
        self.lock = threading.Lock()
        self.h_count = 0
        self.o_count = 0
        self.h_cond = threading.Condition(self.lock)
        self.o_cond = threading.Condition(self.lock)

    def releaseHydrogen(self, releaseHydrogen_func) ->