class Solution:
    def join(self, arr1: list[dict], arr2: list[dict]) -> list[dict]:
        merged_map = {}

        for obj in arr1:
            merged_map[obj['id']] = obj

        for obj in arr2:
            obj_id = obj['id']
            if obj_id in merged_map:
                # Merge properties, arr2 overrides arr1
                merged_map[obj_id] = {**merged_map[obj_id], **obj}
            else:
                # Add new object from arr2
                merged_map[obj_id] = obj

        # Convert dictionary values to a list and sort by id
        joined_array = list(merged_map.values())
        joined_array.sort(key=lambda x: x['id'])

        return joined_array