from node.node import *

def main():
    #testInit()
    #testGettersAndSetters()
    testAddNodeAfter()

def testAddNodeAfter():
    print("Testing Node Add Node After")

    # construct node with data equal to J and link
    # equal to None and assign its reference to head
    head = node('J', None) # J
    print("The head node contains data:", head.getData())

    # declare a new node named selection and make it refer
    # to the same node as head
    selection = head # J

    print("The head node contains data:", head.getData())
    print("The selection node contains data:", selection.getData())

    # add a node with data equal to O after the node selection refers to
    selection.addNodeAfter('O') # J -> O

    # get selection's link and assign its reference back to selection
    selection = selection.getLink() # O

    print("The head node contains data:", head.getData())
    print("The selection node contains data:", selection.getData())

    # add a node with data equal to B after the node selection refers to
    selection.addNodeAfter('B') # O -> B

    # get selection's link and assign its reference back to selection
    selection = selection.getLink() # B

    print("The head node contains data:", head.getData())
    print("The selection node contains data:", selection.getData())

    # add a node with data equal to S after the node selection refers to
    selection.addNodeAfter('S') # B -> S

    # get selection's link and assign its reference back to selection
    selection = selection.getLink() # S

    print("The head node contains data:", head.getData())
    print("The selection node contains data:", selection.getData())

    # declare a new node named tail and make it refer to the same node as head
    tail = head # J -> O -> B -> S

    # get tail's link and assign its reference back to tail
    tail = tail.getLink() # O -> B -> S
    tail = tail.getLink() # B -> S
    tail = tail.getLink() # S

    # add a node with data equal to Z after the node tail refers to
    tail.addNodeAfter('Z') # S -> Z

    # get tail's link and assign its reference back to tail
    tail = tail.getLink() # Z

    print("The head node contains data:", head.getData())
    print("The selection node contains data:", selection.getData())
    print("The tail node contains data:", tail.getData())

def testGettersAndSetters():
    print("Testing Node Getters and Setters")

    # construct node with data equal to R and link
    # equal to None and assign its reference to head
    head = node('R', None) # R
    print("The head node contains data:", head.getData())

    head.setData('S') # S
    print("The head node contains data:", head.getData())

    head = node('B', head) # B -> S
    print("The head node contains data:", head.getData())

    head = node('O', head) # O -> B -> S
    print("The head node contains data:", head.getData())

    head = node('J', head) # J -> O -> B -> S
    print("The head node contains data:", head.getData())

    # get head's link and assign its reference back to head
    head = head.getLink() # O -> B -> S
    print("The head node contains data:", head.getData())

    # get head's link and assign its reference back to head
    head = head.getLink() # B -> S
    print("The head node contains data:", head.getData())

    # get head's link and assign its reference back to head
    head = head.getLink() # S
    print("The head node contains data:", head.getData())

    # get head's link and assign its reference back to head
    """head = head.getLink() # None
    print("The head node contains data:", head.getData())"""

    print("The head node contains link:", head.getLink())

    # set head's link to a new node with data equal to 'O'
    # and link equal to None
    head.setLink(node('O', None)) # S -> O

def testInit():
    print("Testing Node Init")

    # construct node with data equal to S and link
    # equal to None and assign its reference to head
    head = node('S', None) # S

    # construct node with data equal to B and link equal to head
    # and assign its reference to head
    head = node('B', head) # B -> S

    # construct node with data equal to O and link equal to head
    # and assign its reference to head
    head = node('O', head) # O -> B -> S

    # construct node with data equal to J and link equal to head
    # and assign its reference to head
    head = node('J', head) # J -> O -> B -> S

    head = node(1, head) # 1 -> J -> O -> B -> S
    head = node(1.5, head) # 1.5 -> 1 -> J -> O -> B -> S
    head = node([1, 2], head) # [1, 2] -> 1.5 -> 1 -> J -> O -> B -> S
    head = node(('A', 'B'), head) # (A, B) -> [1, 2] -> 1.5 -> 1 -> J -> O -> B -> S

    print()

if __name__ == "__main__":
    main()