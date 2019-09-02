def binary_search(search_val, search_list):
    midpoint = (len(search_list)-1) // 2

    if search_val == search_list[midpoint]:
        return True
    elif len(search_list) == 1 and search_val != search_list[0]:
        return False
    elif search_val > search_list[midpoint]:
        return binary_search(search_val, search_list[midpoint:])
    else:
        return binary_search(search_val, search_list[:midpoint])


def main():
    test_list = [7, 1, 16, 100, 5, 8, 101, 2, 6, 1560]
    test_list_sorted = sorted(test_list)

    search_val = 101

    print(binary_search(search_val, test_list_sorted))

if __name__ == "__main__":
    main()