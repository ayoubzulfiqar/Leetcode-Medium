class Solution:
    def subdomainVisits(self, cpdomains: list[str]) -> list[str]:
        counts = {}
        
        for cpdomain in cpdomains:
            space_idx = cpdomain.find(" ")
            count = int(cpdomain[:space_idx])
            domain = cpdomain[space_idx + 1:]
            
            # Add the full domain to counts
            counts[domain] = counts.get(domain, 0) + count
            
            # Find and add parent domains
            current_dot_idx = -1
            while True:
                current_dot_idx = domain.find(".", current_dot_idx + 1)
                if current_dot_idx == -1:
                    break
                
                subdomain = domain[current_dot_idx + 1:]
                counts[subdomain] = counts.get(subdomain, 0) + count
                
        result = []
        for domain, total_count in counts.items():
            result.append(str(total_count) + " " + domain)
            
        return result