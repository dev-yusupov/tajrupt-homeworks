from typing import List

def min_max_normalization(data: List, range_: str) -> List:
    min_val = min(data)
    max_val = max(data)

    if range_ == "1-1":
        normalized_data: List = [2 * (x - min_val) / (max_val - min_val) - 1 for x in data]
    elif range_ == "0-1":
        normalized_data: List = [(x - min_val) / (max_val - min_val) for x in data]

    return normalized_data


cityA = [20, 25, 30, 35, 40]
cityB = [10, 15, 20, 25, 30]

print(min_max_normalization(cityA, range_="1-1"))
print(min_max_normalization(cityB, range_="1-1"))
print(min_max_normalization(cityA, range_="0-1"))
print(min_max_normalization(cityB, range_="0-1"))