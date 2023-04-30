def solution(cap, n, deliveries, pickups):
    answer = 0
    reversedDeliveries = deliveries[::-1]
    reversedPickups = pickups[::-1]

    deliveryCount = 0
    pickupsCount = 0
    for i in range(n):
        deliveryCount += reversedDeliveries[i]
        pickupsCount += reversedPickups[i]

        while deliveryCount > 0 or pickupsCount > 0:
            deliveryCount -= cap
            pickupsCount -= cap
            answer += (n-i)*2
    return answer