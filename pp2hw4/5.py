class Wordplay:
    def __init__(self, list1):
        self.list1 = list1
    def words_with_length(self, l):
        list2 = []
        for word in self.list1:
            if len(word) == l:
                list2.append(word)   
        return list2    
    def starts_with(self):
        list3 = [] 
        for word in self.list1:
            if word[0] == 's':
                list3.append(word)
        return list3
    def ends_with(self):
        list4 = [] 
        for word in self.list1:
            if word[len(word) - 1] == 's':
                list4.append(word)
        return list4   
    def palindrome(self):
        list5 = [] 
        for word in self.list1:
            if word == word[::-1]:
                list5.append(word)
        return list5
    def only(self, L):
        n = 0
        list6 = [] 
        for word in self.list1:
            for letter in word:
                if letter in L:
                    n += 1
            if len(word) == n:
                list6.append(word)
            n = 0
        return list6        
    def avoids(self, L):
        n = 0
        list7 = [] 
        for word in self.list1:
            for letter in word:
                if letter not in L:
                    n += 1      
            if len(word) == n:
                list7.append(word)
            n = 0
        return list7      

L = ['a', 'n', 't', 's', 'p', 'c', 'm', 'e', 'h']
mylist = ['time', 'door', 'table', 'lime', 'access', 'save', 'level', 'map', 'average', 'business', 'myth', 'simple', 'eye', 'computer', 'phone', 'man', 'oeou', 'plant', 'cap', 'success', 'word', 'theme', 'good', 'crypt', 'vip', 'pen', 'rhytm', 'spy', 'euouae', 'name', 'hat', 'owl', 'spring', 'audio', 'aueo', 'radar', 'universe', 'zoom']
a = Wordplay(mylist)
print(a.words_with_length(3))
print(a.starts_with())
print(a.ends_with())
print(a.palindrome())
print(a.only(L))
print(a.avoids(L))