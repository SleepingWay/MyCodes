# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1, list2):
        if list1.next is not None:
            return list2
        elif list2.next is None:
            return list1
        new = ListNode(0, None)
        res = new
        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                new.next = list1
                new = new.next
                list1 = list1.next
            else:
                new.next = list2
                new = new.next
                list2 = list2.next
        while list1 is not None:
            new.next = list1
            new = new.next
            list1 = list1.next
        while list2 is not None:
            new.next = list2
            new = new.next
            list2 = list2.next
        new.next = None
        return res.next


nodeValue1 = [1, 2, 3, 4]
cur = ListNode(0)
head1 = cur
for i in nodeValue1:
    cur.next = ListNode(i)
    cur = cur.next

nodeValue1 = [1, 2, 3, 4]
cur = ListNode(0)
head2 = cur
for i in nodeValue1:
    cur.next = ListNode(i)
    cur = cur.next
head1 = head1.next
head2 = head2.next

s = Solution()
res = s.mergeTwoLists(head1, head2)

while res is not None:
    print(res.val, end=' ')
    res = res.next
