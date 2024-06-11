def find_duplicates(chars_list):
    chars_list.sort()
    duplicates = []
    current_char = ''
    for item in chars_list:
        if item == current_char:
            duplicates.append(item)
        else:
            current_char = item

    return duplicates


"""
Video solution
"""


def find_duplicates_v2(chars_list):
    duplicates = []
    for item in chars_list:
        if chars_list.count(item) > 1 and item not in duplicates:
            duplicates.append(item)

    return duplicates
