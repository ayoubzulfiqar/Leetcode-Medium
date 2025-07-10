class GroupedArray(list):
    def groupBy(self, fn):
        grouped_result = {}
        for item in self:
            key = fn(item)
            if key not in grouped_result:
                grouped_result[key] = []
            grouped_result[key].append(item)
        return grouped_result