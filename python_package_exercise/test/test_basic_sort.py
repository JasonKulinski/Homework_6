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

import pytest
import numpy as np
import sys
sys.path.append("C:\\Coding\\397\\Homework_6\\python_package_exercise")
from basic_sort_UNIQUE_SUFFIX.int_sort import bubble, quick, insertion




def is_sorted(int_list):
    """
    Testing oracle that checks if the input integer list is sorted in ascending order.
    
    Parameters:
    int_list (list): List of integers to be checked for sorted order.
    
    Returns:
    bool: True if the list is sorted in ascending order, False otherwise.
    """
    return all(int_list[i] <= int_list[i + 1] for i in range(len(int_list) - 1))


@pytest.fixture
def int_lists():
    """
    Pytest fixture that has two premade tests, and one randomly genorated test that is returned.
    
    Parameters:
    No parameters in this function.
    
    Returns:
    List: 2D array of ints, two predefined and three randomly generated (Entirely positive integer array, Entirely negative array, Negative and Positive integer array)
    """
    return [[3,2,1], 
            [1,1,1], 
            np.random.randint(low= 0, high=200, size=50),
            np.random.randint(low = -200, high = 0, size = 50),
            np.random.randint(low= -100, high = 100, size=50)] 




def test_bubble(int_lists):
    """
    The test implementation for bubble sort
    
    Parameters:
    int_list (list): An int list that will be sorted and validated.
    
    Returns:
    Bool: True or false based on assertion of whether or not the list has been correctly sorted
    """
    for int_list in int_lists:

        sorted_list = bubble(int_list.copy())

        assert (is_sorted(sorted_list) == True)


def test_quick(int_lists):
    """
    The test implementation for quick sort

    Parameters:
    int_list (list): An int list that will be sorted and validated

    Returns:
    Bool: True or false based on the assertion of whether or not the list has been correctly sorted

    """

    for int_list in int_lists:

        sorted_list = quick(int_list.copy())

        assert (is_sorted(sorted_list) == True)




def test_insertion(int_lists):
    """
    The test implementation for insertion sort

    Parameters:
    int_list (list): An int list that will be sorted and validated

    Returns:
    Bool: True or false based on the assertion of whether or not the list has been correctly sorted

    """
    for int_list in int_lists:

        sorted_list = insertion(int_list.copy())

        assert (is_sorted(sorted_list) == True)
    
    



if __name__ == "__main__":
    pytest.main(["-v", "python_package_exercise\\test\\test_basic_sort.py"])

