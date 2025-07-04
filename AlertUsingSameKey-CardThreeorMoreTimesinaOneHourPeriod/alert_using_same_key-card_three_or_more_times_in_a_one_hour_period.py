import collections

class Solution:
    def alertNames(self, keyName: list[str], keyTime: list[str]) -> list[str]:
        times_by_person = collections.defaultdict(list)

        for i in range(len(keyName)):
            name = keyName[i]
            time_str = keyTime[i]
            
            hours, minutes = map(int, time_str.split(':'))
            total_minutes = hours * 60 + minutes
            times_by_person[name].append(total_minutes)

        alert_names = set()

        for name, times in times_by_person.items():
            times.sort()

            if len(times) < 3:
                continue

            for i in range(len(times) - 2):
                if times[i+2] - times[i] <= 60:
                    alert_names.add(name)
                    break
        
        return sorted(list(alert_names))