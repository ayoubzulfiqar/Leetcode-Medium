import collections

class Solution:
    def highAccessEmployees(self, access_times: list[list[str]]) -> list[str]:
        employee_access_map = collections.defaultdict(list)
        for name, time_str in access_times:
            hours = int(time_str[:2])
            minutes = int(time_str[2:])
            total_minutes = hours * 60 + minutes
            employee_access_map[name].append(total_minutes)

        high_access_employees_set = set()

        for name, times in employee_access_map.items():
            times.sort()

            if len(times) >= 3:
                for i in range(len(times) - 2):
                    t1 = times[i]
                    t3 = times[i+2]

                    if t3 - t1 < 60:
                        high_access_employees_set.add(name)
                        break

        return sorted(list(high_access_employees_set))