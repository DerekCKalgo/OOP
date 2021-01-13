
class SList:
    def __init__(self):
        self.head=None
        
    def add_to_front(self, val):
        new_node=SLNode(val)
        current_head=self.head
        new_node.next=current_head
        self.head=new_node
        return self
    
    def add_to_back(self, val):
        if self.head == None:
            self.add_to_front(val)
            return self
        new_node=SLNode(val)
        runner=self.head
        while (runner.next != None):
            runner=runner.next
        runner.next=new_node
        return self

    def remove_from_front(self):
        runner=self.head
        while (runner.next != None):
                prev_runner=runner
                runner=runner.next
        print(runner.value)
        prev_runner.next=None
        return self

    def remove_from_back(self):
        runner=self.head
        self.head=runner.next
        print(runner.value)
        return self

    def remove_val(self, val):
        runner=self.head
        if runner.value==val:
            self.head=runner.next
        else:
            while (runner.next != None):
                prev_runner=runner
                runner=runner.next
                if runner.value==val:
                    prev_runner.next=runner.next
                    break
        return self
    
    def insert_at(self, val, n):
        runner=self.head
        new_node=SLNode(val)
        if n==0:
            new_node.next=self.head
            self.head=new_node
        else:
            count=0
            while (runner.next != None):
                prev_runner=runner
                runner=runner.next
                count += 1
                if n==count:
                    prev_runner.next=new_node
                    new_node.next=runner
                    break
            count += 1
            if n==count:
                runner.next=new_node
                new_node.next=None
                
    
    def print_values(self):
        runner=self.head
        while (runner != None):
            print(runner.value)
            runner=runner.next
        return self



class SLNode:
    def __init__(self, val):
        self.value=val
        self.next=None



lis=SList()
lis.add_to_front(12).add_to_front(31).add_to_front(2).add_to_back(97).print_values()
lis.insert_at("Oh lord", 5)
lis.print_values()
