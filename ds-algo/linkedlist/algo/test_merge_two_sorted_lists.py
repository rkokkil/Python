import unittest
from .merge_two_sorted_lists import ListNode, Solution


class TestSolution(unittest.TestCase):
    def test_merge_two_lists(self):
        l1 = ListNode(1)
        l1.next = ListNode(2)
        l1.next.next = ListNode(4)

        l2 = ListNode(1)
        l2.next = ListNode(3)
        l2.next.next = ListNode(4)

        # solution = Solution()
        resultList = Solution().mergeTwoLists(l1, l2)

        expectedList = [1, 1, 2, 3, 4, 4]

        counter = 0
        while resultList is not None:
            self.assertEqual(resultList.val, expectedList[counter])
            counter += 1
            resultList = resultList.next

