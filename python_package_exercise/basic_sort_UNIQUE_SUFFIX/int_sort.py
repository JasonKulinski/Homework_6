# =========================================================================
#
#  Copyright Ziv Yaniv
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0.txt
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#
# =========================================================================

"""
This module sorts lists of integers...
"""


def bubble(int_list):
    """
    Performs a bubble sort on a list of integers

    Args:
    int_list (list of int): The list to be sorted

    Returns:
    list of int: The sorted list of integers
    """

    print("bubble sort")
    n = len(int_list)
    if n <= 1:  
        return int_list

    for i in range(n):
        for j in range(0, n - i - 1):
            if int_list[j] > int_list[j + 1]:
                int_list[j], int_list[j + 1] = int_list[j + 1], int_list[j]
    return int_list


def quick(int_list):
    """
    Performs a quick sort on a list of integers

    Args:
    int_list (list of int): The list to be sorted

    Returns:
    list of int: The sorted list of integers
    """

    if len(int_list) <= 1:
        return int_list

    else:
        pivot = int_list[len(int_list) // 2]

        lesser = [x for x in int_list if x < pivot]
        middle = [x for x in int_list if x == pivot]
        greater = [x for x in int_list if x > pivot]

        return quick(lesser) + middle + quick(greater)


def insertion(int_list):
    """
    Perform an insertion sort on a list of integers.

    Args:
    int_list (list of int): The list to be sorted.

    Returns:
    list of int: The sorted list.
    """

    for i in range(1, len(int_list)):
        key = int_list[i]

        j = i - 1

        while j >= 0 and key < int_list[j]:
            int_list[j + 1] = int_list[j]

            j -= 1

        int_list[j + 1] = key

    return int_list
