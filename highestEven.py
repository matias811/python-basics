def highest_even(li):
    li.sort(reverse=True)
    for item in li:
        if item % 2 == 0:
            return item


print(highest_even([8, 9, 4, 20, 2, 10]))
