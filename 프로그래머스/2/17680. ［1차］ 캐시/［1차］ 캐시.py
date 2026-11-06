from collections import deque

def solution(cacheSize, cities):
    cache = deque([])
    total = 0
    # 도시 이름 정리
    for i in range(len(cities)):
        cities[i] = cities[i].lower()
    # 캐시 사이즈 0인 경우
    if cacheSize == 0: return len(cities) * 5
    for city in cities:
        # cache hit인 경우
        if city in cache:
            total += 1
            cache.remove(city)
            cache.append(city)
        # cache miss인 경우
        else:
            total += 5
            # 캐시 사이즈 초과한 경우 처리
            if len(cache) >= cacheSize:
                cache.popleft()
            cache.append(city)
    return total