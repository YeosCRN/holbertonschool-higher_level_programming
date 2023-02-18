#!/usr/bin/python3
"""First"""


class MyList(list):
    def print_sorted(self):
        """Use bubble sort to create a sorted list to print
        Args:
            self (list): unsorted list
        """
        arr = self[:]
        done = False
        while not done:
            done = True
            for i in range(len(arr)-1):
                if arr[i] > arr[i+1]:
                    arr[i], arr[i+1] = arr[i+1], arr[i]
                    done = False
        print(arr)
