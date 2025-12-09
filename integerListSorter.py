import argparse
import sys

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            j -= 1
    return arr

def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def main():
    parser = argparse.ArgumentParser(
        description="Sort a list of integers using classic algorithms."
    )

    alg = parser.add_mutually_exclusive_group(required=True)
    alg.add_argument("--insertion", action="store_true", help="Use insertion sort")
    alg.add_argument("--selection", action="store_true", help="Use selection sort")
    alg.add_argument("--bubble", action="store_true", help="Use bubble sort")

    out = parser.add_mutually_exclusive_group(required=True)
    out.add_argument("--print", action="store_true", help="Print output to screen")
    out.add_argument("--store", type=str, help="Save output to file")

    parser.add_argument(
        "numbers",
        nargs="+",
        type=int,
        help="The integers to sort"
    )

    args = parser.parse_args()

    if args.insertion:
        sorted_list = insertion_sort(args.numbers)
    elif args.selection:
        sorted_list = selection_sort(args.numbers)
    elif args.bubble:
        sorted_list = bubble_sort(args.numbers)
    else:
        print("No algorithm chosen.")
        sys.exit(1)

    if args.print:
        print("Sorted list:", sorted_list)
    elif args.store:
        with open(args.store, "w") as f:
            f.write(" ".join(map(str, sorted_list)))
        print(f"Output saved to {args.store}")

if __name__ == "__main__":
    main()
