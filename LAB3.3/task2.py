
from typing import List
def sort_numbers(numbers: List[int]) -> List[int]:
    
    if len(numbers) <= 1:
        return numbers.copy()

    middle_index = len(numbers) // 2
    left_sorted = sort_numbers(numbers[:middle_index])
    right_sorted = sort_numbers(numbers[middle_index:])
    return _merge_sorted_lists(left_sorted, right_sorted)


def _merge_sorted_lists(left_values: List[int], right_values: List[int]) -> List[int]:
    result: List[int] = []
    left_index = 0
    right_index = 0

    while left_index < len(left_values) and right_index < len(right_values):
        if left_values[left_index] <= right_values[right_index]:
            result.append(left_values[left_index])
            left_index += 1
        else:
            result.append(right_values[right_index])
            right_index += 1

    if left_index < len(left_values):
        result.extend(left_values[left_index:])
    if right_index < len(right_values):
        result.extend(right_values[right_index:])

    return result


if __name__ == "__main__":
    example = [5, 2, 9, 1, 5, 6]
    print("Input:", example)
    print("Sorted:", sort_numbers(example))

