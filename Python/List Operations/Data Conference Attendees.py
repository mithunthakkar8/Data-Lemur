from collections import Counter
import math
def min_attendees(answers):
    counter = Counter(answers)
    result = 0
    for item, count in counter.items():
        if item == 0:
            result += count
        else:
            result += math.ceil(count/(item+1))*(item+1)
    return result
