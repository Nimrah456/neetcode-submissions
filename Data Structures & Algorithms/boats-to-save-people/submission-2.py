class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        n = len(people)
        i = 0
        k = n-1
        boat = 0
        while i <= k:
            if people[i] + people[k] <= limit:
                i+=1
            k-=1 
            boat+=1
        return boat       





            
        