
"""
Given a singly linked list of N nodes.
The task is to find the middle of the linked list. For example, if the linked list is
1-> 2->3->4->5, then the middle node of the list is 3.
If there are two middle nodes(in case, when N is even), print the second middle element.
For example, if the linked list given is 1->2->3->4->5->6, then the middle node of the list is 4.
"""

def findMid(self, head):
        # Code here
        # return the value stored in the middle node
        if head is None:
            return -1
        
        count = 0
        #print(head.next.data)
        #print("ok")
        temp = head
        while head is not None:
            count = count + 1
            #print(count)
            head = head.next
        
        mid = count // 2
        #print("mid", mid)
        
        while mid:
            temp = temp.next
            mid = mid - 1
        
        return temp.data