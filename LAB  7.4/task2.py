def sort_list(data):
    try:
        return sorted(data)
    except TypeError:
        return sorted(data, key=str)

items = [3, "apple", 1, "banana", 3]
print(sort_list(items))
