class Solution:
    def splitIntoFibonacci(self, num: str) -> list[int]:
        self.num_str = num
        self.N = len(num)
        self.MAX_INT = 2**31 - 1
        self.result = []

        def backtrack(index, current_list):
            if self.result:
                return

            if index == self.N:
                if len(current_list) >= 3:
                    self.result.extend(current_list)
                return

            for i in range(index, self.N):
                if i > index and self.num_str[index] == '0':
                    break

                current_val_str = self.num_str[index : i + 1]

                if len(current_val_str) > 10:
                    break
                
                current_val = int(current_val_str)
                if current_val > self.MAX_INT:
                    break

                if len(current_list) < 2:
                    current_list.append(current_val)
                    backtrack(i + 1, current_list)
                    current_list.pop()
                else:
                    sum_of_last_two = current_list[-1] + current_list[-2]

                    if current_val < sum_of_last_two:
                        continue
                    elif current_val > sum_of_last_two:
                        break
                    else:
                        current_list.append(current_val)
                        backtrack(i + 1, current_list)
                        current_list.pop()

        backtrack(0, [])
        return self.result