def sortList(h):
    if not h or not h.next: return h

    def get_mid(head):
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None
        return mid

    def merge(l1, l2):
        dummy = ListNode(0)
        cur = dummy
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 if l1 else l2
        return dummy.next

    mid = get_mid(h)
    left = sortList(h)
    right = sortList(mid)
    return merge(left, right)