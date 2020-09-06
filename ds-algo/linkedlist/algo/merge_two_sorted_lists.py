"""
https://leetcode.com/problems/merge-two-sorted-lists/submissions/
https://www.youtube.com/watch?v=r3MAkVZkD0s

yet to solve:
https://leetcode.com/problems/merge-k-sorted-lists/
https://leetcode.com/problems/merge-sorted-array/
https://leetcode.com/problems/sort-list/

O(1) - hashing technique
O(n) - linear
O(n log n)
O(n^2)

time complexity O(n), space complexity O(n)
time complexity O(nlogn), space complexity O(1)

if input size is max, you are over utilizing space in first scenario hence prefer second option
if input size is less, then i prefer first.

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # def mergeTwoLists(self, l1, l2):
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)
        ptr = head

        while True:  # executing infinitely
            if l1 is None and l2 is None:  # if two lists are null, just break
                break
            elif l1 is None:  # if l1 is null, return l2
                ptr.next = l2
                break
            elif l2 is None:  # if l2 is null, return l1
                ptr.next = l1
                break
            else:  # l1 is not null and l2 also not null
                smallerValue = 0  # temp value assignment

                # if l1's val is less than l2's, then take only value from l1
                # and assign it to smallerValue variable
                # and also increment l1 to next pointer
                # similarly in else block for l2
                if l1.val < l2.val:
                    smallerValue = l1.val
                    l1 = l1.next
                else:
                    smallerValue = l2.val
                    l2 = l2.next

                # once smallerValue is available, construct new node with smallerValue
                # assign new Node as ptr's next node
                # increment ptr to ptr.next
                newNode = ListNode(smallerValue)
                ptr.next = newNode
                ptr = ptr.next

        # As we assigned 0 at the head initially, returning result excluding 0.
        return head.next


"""
1->2->4
1->3->4

result:
1->1->2->3->4->4
"""
# l1 = ListNode(1)
# l1.next = ListNode(2)
# l1.next.next = ListNode(4)
#
# l2 = ListNode(1)
# l2.next = ListNode(3)
# l2.next.next = ListNode(4)
#
# solution = Solution()
# resultList = solution.mergeTwoLists(l1, l2)
# while resultList is not None:
#     print(resultList.val)
#     resultList = resultList.next

