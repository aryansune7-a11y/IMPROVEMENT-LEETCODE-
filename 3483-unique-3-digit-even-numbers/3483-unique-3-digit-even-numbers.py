from collections import Counter

class Solution:
    def totalNumbers(self, digits: List[int]) -> int:


        available_counts = Counter(digits)
        valid_count = 0
        
        for num in range(100, 1000, 2):
            d1 = num // 100
            d2 = (num // 10) % 10
            d3 = num % 10  
            needed_counts = Counter([d1, d2, d3])
            
            if all(available_counts[d] >= count for d, count in needed_counts.items()):
                valid_count += 1
                
        return valid_count