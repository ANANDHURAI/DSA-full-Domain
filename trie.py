from collections import deque

class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.end = False

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insertion(self , word):
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.end = True
        
    def search(self , word):
        current = self.root
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
        return current.end
    
    def delete(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False  
            node = node.children[char]
        if not node.end:
            return False  
        
        node.end = False  
        return True 
    

    def prefix_fuction(self , prefix):
        current = self.root
        for char in prefix:
            if char not in current.children:
                return False
            current = current.children[char]
        return True
    
    def count_fuction(self):
        if not self.root:
            return 0
        queue = deque([self.root])
        count = 0
        while queue:
            node = queue.popleft()
            if node.end:
                count+= 1
            queue.extend(node.children.values())
        return count
    
    def longest_word(self):
        if not self.root :
            return "empty Trie !!!"
        
        queue = deque([(self.root , "")])
        long_word = ''
        while queue:
            node , word = queue.popleft()
            if node.end and len(word) > len(long_word):
                long_word = word
            
            for char in sorted(node.children.keys()):
                queue.append((node.children[char] , word+char))
        return long_word
    
    def list_all_words(self):
        if not self.root :
            return []
        queue = deque([(self.root , "")])
        words = []
        while queue:
            node , word = queue.popleft()
            if node.end :
                words.append(word)

            for char, child in node.children.items():
                queue.append((child , word + char))
        return words
    
    def auto_complete(self ,prefix):
        current = self.root
        for char in prefix:
            if char not in current.children:
                return []
            current = current.children[char]
        queue = deque([(current , prefix)])
        words = []
        while queue:
            node , word = queue.popleft()
            if node.end:
                words.append(word)
            for char , child in node.children.items():
                queue.append((child , word+char))
        return words
    
t = Trie()
t.insertion('anand')
t.insertion('varun')
t.insertion('thiru')
t.insertion('kadir')
t.insertion('anandkumar')
t.insertion('arun')
t.insertion('aathi')
print(t.search('kadir'))
print(t.prefix_fuction('ana'))

print('total number of words :  ',t.count_fuction())
print('the longest word', t.longest_word())
print('all words')
print(t.list_all_words())
print('all auto complete words')
print(t.auto_complete('a'))
print(t.delete('arun'))
print(t.list_all_words())

 