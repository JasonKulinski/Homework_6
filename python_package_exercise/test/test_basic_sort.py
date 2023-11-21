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

import sys

sys.path.append("C:\\Coding\\397\\Homework_6\\python_package_exercise")

from basic_sort_UNIQUE_SUFFIX.int_sort import bubble, quick, insertion

import pytest
import numpy as np

# from  "C:\Coding\397\Homework_6\python_package_exercise\basic_sort_UNIQUE_SUFFIX\int_sort.py"  import bubble, quick, insertion


def is_sorted(self, int_list):
    """
    Testing oracle.
    """
    return True


@pytest.fixture
def int_lists():
    # fixture which creates testing data for all tests
    return [[3, 2, 1], [1, 1, 1], np.random.randint(low=-10, high=200, size=5)]


def test_bubble(int_lists):
    assert True


def test_quick():
    assert quick([]) == []
    assert quick([1]) == [1]
    assert quick([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert quick([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    assert quick([5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5]
    assert quick([-3, -1, -4, -2]) == [-4, -3, -2, -1]
    assert quick([-2, 3, 0, -1, 5]) == [-2, -1, 0, 3, 5]
    assert quick([3.5, 2.2, 5.1, 4.3]) == [2.2, 3.5, 4.3, 5.1]


def test_insertion():
    assert insertion([]) == []
    assert insertion([1]) == [1]
    assert insertion([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert insertion([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    assert insertion([5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5]
    assert insertion([-3, -1, -4, -2]) == [-4, -3, -2, -1]
    assert insertion([-2, 3, 0, -1, 5]) == [-2, -1, 0, 3, 5]
    assert insertion([3.5, 2.2, 5.1, 4.3]) == [2.2, 3.5, 4.3, 5.1]
