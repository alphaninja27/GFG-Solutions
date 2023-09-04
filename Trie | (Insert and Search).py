def insert(root,key):
    for i in key:
        ind = ord(i) - ord('a')
        if root.children[ind]:
            root = root.children[ind]
        else:
            root.children[ind] = TrieNode()
            root = root.children[ind]
    root.isEndOfWord = True
    
    #code here

#Function to use TRIE data structure and search the given string.
def search(root, key):
    for i in key:
        ind = ord(i) - ord('a')
        if root.children[ind]:
            root = root.children[ind]
        else:
            return False
    return root.isEndOfWord
