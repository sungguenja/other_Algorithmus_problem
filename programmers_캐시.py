def solution(cacheSize, cities):
    answer = 0
    cities2 = [city.lower() for city in cities]
    cache = []
    if cacheSize != 0:
        for city in cities2:
            if city in cache:
                cache.pop(cache.index(city))
                cache.append(city)
                answer+=1
            else:
                if len(cache) < cacheSize:
                    cache.append(city)
                    answer += 5
                else:
                    cache.pop(0)
                    cache.append(city)
                    answer += 5
    else:
        answer = 5*len(cities)
    return answer