import collections

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: list[str]) -> int:
        if startGene == endGene:
            return 0
        
        bank_set = set(bank)
        
        if endGene not in bank_set:
            return -1

        queue = collections.deque([(startGene, 0)]) # (gene_string, mutations_count)
        visited = {startGene}
        
        chars = ['A', 'C', 'G', 'T']
        gene_length = len(startGene)
        
        while queue:
            current_gene, mutations_count = queue.popleft()
            
            if current_gene == endGene:
                return mutations_count
            
            for i in range(gene_length):
                original_char = current_gene[i]
                for char in chars:
                    if char == original_char:
                        continue
                    
                    next_gene_list = list(current_gene)
                    next_gene_list[i] = char
                    next_gene = "".join(next_gene_list)
                    
                    if next_gene in bank_set and next_gene not in visited:
                        visited.add(next_gene)
                        queue.append((next_gene, mutations_count + 1))
                        
        return -1