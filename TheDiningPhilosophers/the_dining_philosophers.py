import threading

class DiningPhilosophers:
    def __init__(self):
        self.forks = [threading.Lock() for _ in range(5)]
        self.waiter = threading.Semaphore(4)

    def wantsToEat(self, philosopher: int, pickLeftFork: 'Callable[[], None]', pickRightFork: 'Callable[[], None]', eat: 'Callable[[], None]', putLeftFork: 'Callable[[], None]', putRightFork: 'Callable[[], None]') -> None:
        self.waiter.acquire()

        left_fork_idx = philosopher
        right_fork_idx = (philosopher + 1) % 5

        self.forks[left_fork_idx].acquire()
        pickLeftFork()

        self.forks[right_fork_idx].acquire()
        pickRightFork()

        eat()

        putRightFork()
        self.forks[right_fork_idx].release()

        putLeftFork()
        self.forks[left_fork_idx].release()

        self.waiter.release()