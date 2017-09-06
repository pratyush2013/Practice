import copy


class Node(object):

    "Class to Define a node for Trie"

    dictionary={}
    
    def __init__(self):
       
        self.dict = copy.deepcopy(Node.dictionary)
        self.isLeaf = False

    @staticmethod
    def add_to_dictionary():

       """To add all the alphabets in dictionary
           currently A-Z and a-z are the only 
           included range
       """            

       for i in range(0,26):
          Node.dictionary[chr(i+ord('a'))] = None
          Node.dictionary[chr(i+ord('A'))] = None 
    
    def add_word(self,
                 string,
                 index=0):
        
        assert(self)
        
        if index == len(string):
            self.isLeaf = True
            return

        char = string[index]
        
        if self.dict[char] == None:
            self.dict[char] = Node()
       
        node = self.dict[char]
         
        node.add_word(string,index+1)

    def print_dictionary(self,
                         string=""):
        
        assert(self)
        
        if self.isLeaf == True:
            print(string)

        for key,node in self.dict.items():
            if node:
                node.print_dictionary(string+key)
            
    
    def search_word(self,
                    string,
                    index=0):
        
        assert(self)

        if index == len(string) and self.isLeaf == True:

            print ("It is in dictionary")
            return

        elif index>=len(string):
            return

        node = self.dict[string[index]]

        if node:
            node.search_word(string,index+1)

    def suggest_word(self,string,index=0,strNew=""):

        assert(self)
        
        length=len(string)

        if index<length:

            node = self.dict[string[index]]
            
            if node:
                node.suggest_word(string,index+1,strNew)
            
        else:

            if self.isLeaf == True:
                print string+strNew
            

            for key,node in self.dict.items():
                if node:
                    node.suggest_word(string,index+1,strNew+key)
        
Node.add_to_dictionary()
node=Node()
node.add_word("Medicine")
node.add_word("MedCords")
node.print_dictionary()
node.search_word("MedCords")
node.print_dictionary()
node.suggest_word("Med")
