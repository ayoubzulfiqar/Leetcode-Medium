class Solution:
    def sampleStats(self, count: list[int]) -> list[float]:
        minimum = 256
        maximum = -1
        total_sum = 0
        total_elements = 0
        mode = -1
        max_freq = -1

        for i in range(256):
            if count[i] > 0:
                if minimum == 256:
                    minimum = i
                maximum = i
                total_sum += i * count[i]
                total_elements += count[i]
                if count[i] > max_freq:
                    max_freq = count[i]
                    mode = i
        
        mean = float(total_sum) / total_elements

        median1_val = -1
        median2_val = -1
        
        median_pos1 = (total_elements - 1) // 2
        median_pos2 = total_elements // 2
        
        current_elements_passed = 0
        for i in range(256):
            if count[i] > 0:
                if current_elements_passed <= median_pos1 < current_elements_passed + count[i]:
                    median1_val = i
                
                if current_elements_passed <= median_pos2 < current_elements_passed + count[i]:
                    median2_val = i
                
                current_elements_passed += count[i]
                
                if median1_val != -1 and median2_val != -1:
                    break

        median = (float(median1_val) + float(median2_val)) / 2.0
        
        return [float(minimum), float(maximum), mean, median, float(mode)]