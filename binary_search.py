def binary_search(search_val, search_list, start, end):
    midpoint = (start + end) // 2

    if search_list[midpoint] == search_val:
        return True
    elif search_val > search_list[midpoint]:
        return binary_search(search_val, search_list, midpoint, end)
    elif search_val < search_list[midpoint]:
        return binary_search(search_list, search_list, start, midpoint)
    

def main():
    test_list = [7, 1, 16, 100, 5, 8, 101, 2, 6, 1560]
    test_list_sorted = sorted(test_list)

    search_val = 101

    print(binary_search(search_val, test_list_sorted, 0, len(test_list_sorted) - 1))

if __name__ == "__main__":
    main()