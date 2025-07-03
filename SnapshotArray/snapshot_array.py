import bisect

class SnapshotArray:

    def __init__(self, length: int):
        self.data = [[] for _ in range(length)]
        self.current_snap_id = 0

    def set(self, index: int, val: int) -> None:
        self.data[index].append((self.current_snap_id, val))

    def snap(self) -> int:
        snap_id_to_return = self.current_snap_id
        self.current_snap_id += 1
        return snap_id_to_return

    def get(self, index: int, snap_id: int) -> int:
        history = self.data[index]
        
        idx = bisect.bisect_right(history, (snap_id, float('inf')))

        if idx == 0:
            return 0
        else:
            return history[idx - 1][1]