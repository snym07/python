"""Searching algorithms :
    1) Linear Search
    2) Binary Search
    3) Jump Search
    4) Interpolation Search
    5) Exponential Search
    6) Ternary Search
"""

# global list to search from
search_list = [1, 2, 3, 4, 5, 6, 7, 8, 24, 23, 453, 63, 22, 23, 54, 66, 89, 32, 80, 29, 90]
length_of_list = len(search_list)


def linear_search(search_item):
    for item in range(length_of_list):
        if search_list[item] == search_item:
            print("Yes {} is in the given list at index {}".format(search_item, item))
            return
    print("No match found!")


def main():
    print("Enter the item to be searched : ")
    search_item = int(input("> "))

    print("Select the type of search you want to perform : ")
    print("""
        1) Linear Search
        2) Binary Search
        3) Jump Search
        4) Interpolation Search
        5) Exponential Search
        6) Ternary Search
    """)
    type_of_search = int(input("> "))

    if type_of_search == 1:
        linear_search(search_item)


if __name__ == "__main__":
    main()
