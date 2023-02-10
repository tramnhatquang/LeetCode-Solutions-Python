def findDay(day: str, k: int) -> str:
    map_day_number = {
        'mon': 0,
        'tue': 1,
        'wed': 2,
        'thu': 3,
        'fri': 4,
        'sat': 5,
        'sun': 6,
    }
    next_day_index = (map_day_number[day] + k) % 7

    for day, index in map_day_number.items():
        if index == next_day_index:
            return day
    # space: O(7) = O(1), since we only have 7 days a week
    # time: O(7) = O(1) 

assert findDay('wed', 2) == 'fri'
assert findDay('wed', 3) == 'sat'
assert findDay('tue', 9) == 'thu'
