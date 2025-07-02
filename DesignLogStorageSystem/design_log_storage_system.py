class LogSystem:

    def __init__(self):
        self.logs = []
        self.granularity_map = {
            "Year": 0,
            "Month": 1,
            "Day": 2,
            "Hour": 3,
            "Minute": 4,
            "Second": 5
        }
        self.min_vals = [1, 1, 0, 0, 0]
        self.max_vals = [12, 31, 23, 59, 59]

    def _parse_timestamp(self, timestamp_str: str) -> list[int]:
        return [int(x) for x in timestamp_str.split(':')]

    def put(self, timestamp: str, message: str) -> None:
        parsed_ts = self._parse_timestamp(timestamp)
        self.logs.append((parsed_ts, message))

    def retrieve(self, start_str: str, end_str: str, granularity: str) -> list[str]:
        start_parts = self._parse_timestamp(start_str)
        end_parts = self._parse_timestamp(end_str)
        granularity_idx = self.granularity_map[granularity]

        for i in range(granularity_idx + 1, 6):
            start_parts[i] = self.min_vals[i-1]
            end_parts[i] = self.max_vals[i-1]

        result_messages = []
        for log_ts_parts, message in self.logs:
            if start_parts <= log_ts_parts <= end_parts:
                result_messages.append(message)
        
        return result_messages

