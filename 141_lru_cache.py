class ListNode():
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
    
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    pages = list(map(int, input().split()))

    cache_map = {}
    head = ListNode(-1)
    tail = head

    for ele in pages:
        if ele in cache_map:
            node = cache_map[ele]

            if node == tail:
                tail = node.prev

            if node.prev:
                node.prev.next = node.next

            if node.next:
                node.next.prev = node.prev

            del cache_map[ele]
        else:
            if len(cache_map) >= k:
                lru_node = tail
                del cache_map[lru_node.data]

                tail = tail.prev

                if tail:
                    tail.next = None

                if tail == head:
                    head.next = None
        
        new_node = ListNode(ele)
        new_node.next = head.next
        if head.next:
            head.next.prev = new_node
        head.next = new_node
        new_node.prev = head

        if tail == head:
            tail = new_node
        
        cache_map[ele] = new_node
    
    elements = []
    current = head.next
    while current:
        elements.append(current.data)
        current = current.next

    elements = elements[::-1]
    print(*elements)