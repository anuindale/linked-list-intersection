class Node:
    """ 
    Simple Node class for linked list  
    """
    def __init__(self,v):
        self.value = v
        self.next = None
    
    def __repr__(self):
        return 'Node(' + repr(self.value) + ')'
        

def intersection(a,b):
    """ 
    Find the first common Node of two linked lists
    
    Parameters: 
    a (Node): start Node of first list
    b (Node): start Node of second list
    
    Returns: 
    the first intersection Node of two lists
    """
    
    if (a==b):
        return a
    else:
        x = a
        y = b
        
        a_dist = 0
        b_dist = 0
        
        step = 1
        turn = 0
        
        while True:            
            if turn==0 and x.next:
                for _ in range(step):
                    if x.next:
                        x = x.next
                        a_dist += 1
                        if x==y: return retrace(a,b,a_dist,b_dist)
                    else: break
                        
            elif turn==1 and y.next:
                for _ in range(step):
                    if y.next:
                        y = y.next
                        b_dist += 1
                        if x==y: return retrace(a,b,a_dist,b_dist)
                    else: break
            
            elif x.next == y.next == None:
                return None
            
            step *= 2
            turn = 1-turn


def retrace(a,b,a_dist,b_dist):
    """ 
    Helper function to find the first common Node of two linked lists, given distances to some common Node
  
    Parameters: 
    a (Node): beginning of first list
    b (Node): beginning of second list
    a_dist (int): distance from a to some common Node
    b_dist (int): distance from b to some common Node
  
    Returns: 
    x (Node): the first common Node of the two lists
    """
    
    x = a
    y = b
    
    diff = a_dist - b_dist
   
    if diff>0:
        for _ in range(diff): x = x.next
    elif diff<0:
        for _ in range(-diff): y = y.next
    
    while x!=y:
        x = x.next
        y = y.next
    
    return x
   
   

""" 
EXAMPLE INPUT:   
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    e = Node('e')
    f = Node('f')

    a.next = g
    g.next = c

    b.next = c
    c.next = d
    d.next = e
    e.next = f

    intersection(a,b)

EXAMPLE OUTPUT: 
    Node('c')
"""

