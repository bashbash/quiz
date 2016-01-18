#list1 = ['eye', 'cat', 'crazylongwordwithnomeaning', 'dog', 'ball',  'catdog', 'cateyedog', 'zenith', 'perhapszenith', 'perhaps', 'perhapstic', 'perhapsticzenith', 'catdogcatdogcatdog', 'cateyeball', 'cateyeballdog']

list2 =[]

with open('word.list.txt') as f:
    for line in f:
    	line = line.strip('\n')
    	list2.append(line)
    	    
    
class Node:
    def __init__(self, letter=None, isTerminal=False):
        self.letter=letter
        self.children={}
        self.isTerminal=isTerminal
        


class Trie: 
	def __init__(self): 
		self.root=Node('')   
		
	def __repr__(self): 
		self.output([self.root]) 
		return ''   
					
	def insert(self, word): 
		current=self.root 
		for letter in word: 
			if letter not in current.children: 
				current.children[letter]=Node(letter) 
			current=current.children[letter] 
		current.isTerminal=True   
				
	def contains(self, word): 
		current=self.root 
		for letter in word: 
			if letter not in current.children: 
				return False 
			current=current.children[letter] 
		return current.isTerminal   
		
	def getPrefix(self, word):
		prefix = ''
		current=self.root 
		
		for letter in word: 
			if letter not in current.children: 
				return prefix
			current=current.children[letter]
			prefix+=letter
			if current.isTerminal: 
				return prefix			
		return prefix
		
	
	def isCompound(self, word):
		prefix = self.getPrefix(word)
		#if returns the word itself, then no prefix was found
		if len(prefix) == len(word): 
			return False
		
		suffix = word[len(prefix):]
		
		if len(suffix) < 1:
			return True
		if self.contains(word):
			return True
		else:
			self.isCompound(suffix)		
		
		return False
		
		
		
		
		
def longestCompound(words): 

	words.sort() 
	words.sort(key=lambda item: (len(item), item)) #the sorting step is really crucial 
												   #otherwise, we have to search the whole list and keep a track of the word length
												
	trie=Trie() 
	longestWord='none!' 
	
	for word in words: 
		trie.insert(word)
		
	for word in reversed(words):
		if trie.isCompound(word):
			longestWord = word
			break
			
	return longestWord
	

print(longestCompound(list2))




	
	
	

