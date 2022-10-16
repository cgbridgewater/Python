class SLNode:
    def __init__(self, value):
        self.value = value
        self.next = None




class SList:
    def __init__(self):
        self.head = None

    def add_to_front(self, val):   #added this, takes a value
        new_node = SLNode(val)    #create a new instance of our Node Classusing the given value
        current_head = self.head  #save the current head in a variable
        new_node.next = current_head   #set the new nodes next to the list's current head
        self.head = new_node        #SET the lists head TO the node we created in the last step
        return self                 #return self to allow for chaining

    def print_values(self):
        runner = self.head     # a pointer to the list's first node
        while (runner != None):     #iterating while runner is a node and not None
            print(runner.value)    
            runner= runner.next        #set the runner to its neighbor
        return self                 #once the loop is done, return self to allow for chaining

    def add_to_back(self, val):     #accepts a value
        if self.head == None:           #if the list is empty
            self.add_to_front(val)      #run the add_to_front method
            return self                 #let's make sure the rest of this function doesnt happen if we add to the front
        new_node = SLNode(val)      # create a new instance of our Node class with the given value
        runner = self.head          # set an iterator to start at the front of the list
        while (runner.next != None):       #iterate until the iterator doesn't have a neighbor
            runner = runner.next    # increment the runner to the next node in the list
        runner.next = new_node      #increment the runner tot he next node in the list
        return self                 #reurn self to allow for chaining

my_list = SList()       #create a new instance of a list
my_list.add_to_front("are").add_to_front("Linked lists").add_to_back("fun!").print_values()         #chaining!

##output is
# Linked lists
# are
# fun!

# my_list.remove_from_front(self).print_values()