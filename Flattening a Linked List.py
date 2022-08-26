def flatten(root):
    #Your code here
    ans = []
    while root:
        temp = root
        ans.append(root.data)
        while root.bottom:
            ans.append(root.bottom.data)
            root = root.bottom
        temp = temp.next
        root = temp
    ans.sort()
    head = Node(ans[0])
    curr = t = head
    for i in range(1, len(ans)):
        head = Node(ans[i])
        curr.bottom = head
        curr = head
    return t
