import math

def solution(cap, n, deliveries, pickups):
    def deliver(arr):
        distance = 0
        boxes = 0
        for i in range(n-1, 0, -1):
            distance += (i+1) * math.ceil(arr[i] / cap)
            if arr[i] % cap:
                arr[i-1] -= cap - (arr[i] % cap)
            arr[i] = 0
        distance += math.ceil(arr[0] / cap)
        
        return distance * 2
    
    return max(deliver(deliveries), deliver(pickups))