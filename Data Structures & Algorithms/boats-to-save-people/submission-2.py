class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        def quick_sort(arr,low,high):
            if low<high:
                pi = partition(arr,low,high)
                quick_sort(arr,low,pi-1)
                quick_sort(arr,pi+1,high)
        def partition(arr,low,high):
            pivot = arr[high]
            i = low -1
            for j in range(low,high):
                if arr[j]<pivot:
                    i+1
                    arr[i],arr[j]=arr[j],arr[i]
            arr[i+1],arr[high]=arr[high],arr[i+1]
            return i+1
        quick_sort(people, 0, len(people) - 1)
        
        # Two pointer approach
        left = 0
        right = len(people) - 1
        boats = 0
        
        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1
                right -= 1
            else:
                right -= 1
            boats += 1
            
        return boats