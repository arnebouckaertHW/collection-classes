from node.node import *
from stack.stack import *
from stack.balancedparens import *
from stack.calculator import *
from stack.serialsearch import *
from stack.insertionsort import *
from queues.queue import *
from queues.palindrome import *
from queues.queuepalindrome import *
from queues.advancedpalindrome import *
from loops import *
from recursion import *

def main():
    # print("Parantheses are balanced?", balancedparens.isBalanced("{X+Y")) # False
    # print("Parantheses are balanced?", balancedparens.isBalanced("{X+Y)")) # False
    # print("Parantheses are balanced?", balancedparens.isBalanced("({X+Y}*Z)")) # True
    # print("Parantheses are balanced?", balancedparens.isBalanced("[A+B]*({X+Y}*Z)")) # True
    # print("(((6+9)/3)*(6-4)) =", calculator.evaluate("(((6+9)/3)*(6-4))")) # 10.0
    # print("(6+(3*(6-4))) =", calculator.evaluate("(6+(3*(6-4)))")) # 12.0
    # print("((5+2)-(3*(6/9))) =", calculator.evaluate("((5+2)-(3*(6/9)))")) # 5.0
    # print("((5*2)-(3*(6/2))) =", calculator.evaluate("((5*2)-(3*(6/2)))")) # 1.0
    #testSerialSearch()
    #testInsertionSort(1)
    #testInsertionSort(4)
    #testInsertionSort(6)
    #testQueueIsPalindrome()
    #testAdvancedIsPalindrome()
    santaClaus()
    getPalindromes()
    testRecursion()

def testRecursion():
    print("Final Exam Recursion")

    # Question 7
    print("LOOP")
    loops.evens(-10, 10)
    print()
    print("RECURSION")
    recursion.evens(-10, 10)

def getPalindromes():
    print("Final Exam Stacks & Queues")

    # Question 6
    palindromes = stack()
    nonPalindromes = stack()
    expressions = list(map(str, input("Please enter ten words seperated by a space:").split()))

    for exp in expressions:
        if palindrome.isPalindrome(exp):
            palindromes.push(exp)
        else:
            nonPalindromes.push(exp)

    nonPalindromeStr = ""

    tempStack = stack()
    while(not nonPalindromes.isEmpty()):
        tempStack.push(nonPalindromes.pop())
    
    while(not tempStack.isEmpty()):
        nonPalindromeStr += tempStack.pop() + " "

    print("The palindromes are:", palindromes.getData()[::-1])
    print("The non-palindromes are:", nonPalindromeStr)

def santaClaus():
    print("Final Exam Nodes")

    # Question 1
    s = node('S', None) # S
    s.addNodeAfter('A') # S -> A
    s.addNodeAfter('T') # S -> T -> A
    s.addNodeAfter('N') # S -> N -> T -> A
    s.addNodeAfter('A') # S -> A -> N -> T -> A
    # Question 2
    c = node('C', None) # C
    c.addNodeAfter('S') # C -> S
    c.addNodeAfter('U') # C -> U -> S
    c.addNodeAfter('A') # C -> A -> U -> S
    c.addNodeAfter('L') # C -> L -> A -> U -> S
    
    # Question 3
    selection = s

    # Question 4
    selection = selection.getLink()
    selection = selection.getLink()
    selection = selection.getLink()
    selection = selection.getLink()

    # Question 5
    selection.setLink(c)

def testAdvancedIsPalindrome():
    print("Testing Advanced Is Palindrome")
    exp = input("Please enter an expression:")

    while exp != "":
        isPalindrome, lineStr = advancedpalindrome.isPalindrome(exp)

        if isPalindrome:
            print("The expression is a palindrome.")
        else:
            print("The expression is not a palindrome.")
            print("Mismatch detected at:", lineStr)

        exp = input("Please enter an expression:")
    
    print("Good bye!")

def testQueueIsPalindrome():
    print("Testing Is Palindrome")
    exp = input("Please enter an expression:")

    while exp != "":
        if queuePalindrome.isPalindrome(exp):
            print("The expression is a palindrome.")
        else:
            print("The expression is not a palindrome.")

        exp = input("Please enter an expression:")
    
    print("Good bye!")

def testIsPalindrome():
    print("Testing Is Palindrome")
    exp = input("Please enter an expression:")

    if palindrome.isPalindrome(exp):
        print("The expression is a palindrome.")
    else:
        print("The expression is not a palindrome.")

def testQueuePeek():
    print("Testing Queue Peek")

    q = queue()
    print("Queue size:", q.size()) # 0
    print("Queue contains:", q) # []

    q.enqueue("J")
    print("Queue size:", q.size()) # 1
    print("Queue contains:", q) # [J]
    print("Front element in queue is:", q.peek()) # J

    q.enqueue("O")
    print("Queue size:", q.size()) # 2
    print("Queue contains:", q) # [J O]
    print("Front element in queue is:", q.peek()) # J

    q.enqueue("B")
    print("Queue size:", q.size()) # 3
    print("Queue contains:", q) # [J O B]
    print("Front element in queue is:", q.peek()) # J

    q.enqueue("S")
    print("Queue size:", q.size()) # 4
    print("Queue contains:", q) # [J O B S]
    print("Front element in queue is:", q.peek()) # J

def testQueueIsEmpty():
    print("Testing Queue Is Empty")

    q = queue()
    q.enqueue('J')
    q.enqueue('O')
    q.enqueue('B')
    q.enqueue('S')

    print("Queue size:", q.size()) # 4
    print("Queue contains:", q) # [J O B S]

    while(not q.isEmpty()):
        print("Just dequeued:", q.dequeue())

    print("Queue size:", q.size()) # 0
    print("Queue contains:", q) # []

def testDequeue():
    print("Testing Queue Dequeue")

    q = queue()
    q.enqueue('J')
    q.enqueue('O')
    q.enqueue('B')
    q.enqueue('S')

    print("Queue size:", q.size()) # 4
    print("Queue contains:", q) # [J O B S]
    print("Just dequeued:", q.dequeue()) # J

    print("Queue size:", q.size()) # 3
    print("Queue contains:", q) # [O B S]
    print("Just dequeued:", q.dequeue()) # O    

    print("Queue size:", q.size()) # 2
    print("Queue contains:", q) # [B S]
    print("Just dequeued:", q.dequeue()) # B

    print("Queue size:", q.size()) # 1
    print("Queue contains:", q) # [S]
    print("Just dequeued:", q.dequeue()) # S

def testEnqueue():
    print("Testing Queue Enqueue")

    q = queue()
    print("Queue size:", q.size()) # 0
    print("Queue contains:", q) # []

    q.enqueue('J')
    print("Queue size:", q.size()) # 1
    print("Queue contains:", q) # [J]

    q.enqueue('O')
    print("Queue size:", q.size()) # 2
    print("Queue contains:", q) # [J O]

    q.enqueue('B')
    print("Queue size:", q.size()) # 3
    print("Queue contains:", q) # [J O B]

    q.enqueue('S')
    print("Queue size:", q.size()) # 4
    print("Queue contains:", q) # [J O B S]

def testInsertionSort(first: int):
    # create an empty stack
    s = stack()

    # initialize first
    # see parameter

    # push -7 onto the top of the stack
    s.push(-7)

    # push 42 onto the top of the stack
    s.push(42)

    # push 70 onto the top of the stack
    s.push(70)

    # push 39 onto the top of the stack
    s.push(39)

    # push 3 onto the top of the stack
    s.push(3)

    # push 63 onto the top of the stack
    s.push(63)

    # push 8 onto the top of the stack
    s.push(8)

    # print unsorted stack
    print("Stack contains:", s)

    # call insertion sort method
    insertionsort.insertionsort(s, first)

    # print sorted stack
    print("Stack contains:", s)

def testSerialSearch():
    # create an empty stack
    s = stack()

    # initialize first
    first = 1

    # initialize size
    size = 0

    # initialize target
    target = 70

    # push -7 onto the top of the stack
    s.push(-7)

    # push 42 onto the top of the stack
    s.push(42)

    # push 70 onto the top of the stack
    s.push(70)

    # push 39 onto the top of the stack
    s.push(39)

    # push 3 onto the top of the stack
    s.push(3)

    # push 63 onto the top of the stack
    s.push(63)  

    # push 8 onto the top of the stack
    s.push(8)

    # print the stack
    print("Stack contains:", s) # [8 63 3 39 70 42 -7]

    # call serial search method and display its return.
    print("The target is at position:", serialsearch(s, first, size + 7, target)) # 5
    print("The target is at position:", serialsearch(s, first, size + 4, target)) # -1
    print("The target is at position:", serialsearch(s, first + 5, size + 2, target)) # -1

def testPeek():
    print("Testing Stack Peek")

    s = stack()
    print("Stack size:", s.size()) # 0
    print("Stack contains:", s) # []

    s.push("S")
    print("Stack size:", s.size()) # 1
    print("Stack contains:", s) # [S]
    print("Top element in stack is:", s.peek()) # S

    s.push("B")
    print("Stack size:", s.size()) # 2
    print("Stack contains:", s) # [B S]
    print("Top element in stack is:", s.peek()) # B

    s.push("O")
    print("Stack size:", s.size()) # 3
    print("Stack contains:", s) # [O B S]
    print("Top element in stack is:", s.peek()) # O

    s.push("J")
    print("Stack size:", s.size()) # 4
    print("Stack contains:", s) # [J O B S]
    print("Top element in stack is:", s.peek()) # J

def testIsEmpty():
    print("Testing Stack Is Empty")

    s = stack()
    s.push('S')
    s.push('B')
    s.push('O')
    s.push('J')

    print("Stack size:", s.size()) # 4
    print("Stack contains:", s) # [J O B S]

    while(not s.isEmpty()):
        print("Just popped:", s.pop())

    print("Stack size:", s.size()) # 0
    print("Stack contains:", s) # []

def testPop():
    print("Testing Stack Pop")

    s = stack()
    s.push('S')
    s.push('B')
    s.push('O')
    s.push('J')

    print("Stack size:", s.size()) # 4
    print("Stack contains:", s) # [J O B S]
    print("Just popped:", s.pop()) # J

    print("Stack size:", s.size()) # 3
    print("Stack contains:", s) # [O B S]
    print("Just popped:", s.pop()) # O

    print("Stack size:", s.size()) # 2
    print("Stack contains:", s) # [B S]
    print("Just popped:", s.pop()) # B

    print("Stack size:", s.size()) # 1
    print("Stack contains:", s) # [S]
    print("Just popped:", s.pop()) # S

    print("Just popped:", s.pop()) # this line of code will generate a value error: Stack is empty

def testPush():
    print("Testing Stack Push")

    s = stack()
    print("Stack size:", s.size()) # 0
    print("Stack contains:", s) # []

    s.push('S')
    print("Stack size:", s.size()) # 1
    print("Stack contains:", s) # [S]

    #s.push('B')
    s.push(1)
    print("Stack size:", s.size()) # 2
    print("Stack contains:", s) # [B S]

    #s.push('O')
    s.push((1,2))
    print("Stack size:", s.size()) # 3
    print("Stack contains:", s) # [O B S]

    #s.push('J')
    s.push([1,2,3])
    print("Stack size:", s.size()) # 4
    print("Stack contains:", s) # [J O B S]

def assignment():
    # Question 1
    head = node(2, None)
    head = node("=", head)
    head = node(1, head)
    head = node("+", head)
    head = node(1, head)


    # Question 2
    operator = head

    # Question 3
    operator = operator.getLink()

    # Question 4
    result = head

    # Question 5
    result = result.getLink()
    result = result.getLink()
    result = result.getLink()
    result = result.getLink()

    # Question 6
    operator.setData("-")
    result.setData(0)

    # Question 7
    operator.setData("*")
    result.setData(1)

    # Question 8
    operator.setData("/")
    result.setData(1)

    # Question 9
    head.setData(7)
    result.setData(7)

    # Question 10
    operator = operator.getLink()

    # Question 11
    head.removeNodeAfter()
    operator.removeNodeAfter()

    # Question 12
    print(f"Head contains {node.listLength(head)} Nodes")
    print(f"Operator contains {node.listLength(operator)} Nodes")
    print(f"Result contains {node.listLength(result)} Node")

    # Question 13
    print("Head contains character", node.listSearch(head, 1).getData())
    print("Operator contains character", node.listSearch(operator, 1).getData())
    if node.listSearch(result, 1) != None:
        print("Result contains character", node.listSearch(result, 1).getData())
    else:
        print("Result doesn't contain character 1")

    # Question 14
    copy = node.listCopyWithTail(head)

    # Question 15
    print(f"Copy[0] contains {node.listLength(copy[0])} Nodes")
    print(f"Copy[1] contains {node.listLength(copy[1])} Node")

    # Question 16
    print("Copy[0] contains character", node.listSearch(copy[0], 1).getData())
    if node.listSearch(copy[1], 1) != None:
        print("Copy[1] contains character", node.listSearch(copy[1], 1).getData())
    else:
        print("Copy[1] doesn't contain character 1")

def testPracticeAssignment():
    # Question 1
    head = node('T', None)
    head = node('K', head)
    head = node('N', head)
    head = node('I', head)
    head = node('L', head)

    # Question 2
    selection = head

    # Question 3
    selection = selection.getLink()
    selection = selection.getLink()
    selection = selection.getLink()

    # Question 4
    selection.addNodeAfter('E')

    # Question 5
    selection = selection.getLink()

    # Question 6
    selection.addNodeAfter('D')

    # Question 7
    selection = selection.getLink()

    # Question 8
    selection.addNodeAfter('L')

    # Question 9
    selection = selection.getLink()

    # Question 10
    selection.addNodeAfter('I')

    # Question 11
    selection = selection.getLink()

    # Question 12
    selection.addNodeAfter('S')

    # Question 13
    print("How many nodes does head contain?", node.listLength(head))
    print("How many nodes does selection contain?", node.listLength(selection))

    # Question 14
    tail = selection

    # Question 15
    tail = tail.getLink()
    tail = tail.getLink()

    # Question 16
    print("How many nodes does tail contain?", node.listLength(tail))

    # Question 17
    tail = node.listCopy(tail)
    selection.removeNodeAfter()
    selection.removeNodeAfter()

    # Question 18
    print("How many nodes does head contain?", node.listLength(head))
    print("How many nodes does selection contain?", node.listLength(selection))
    print("How many nodes does tail contain?", node.listLength(tail))

    # Question 19
    head.removeNodeAfter()
    head.removeNodeAfter()

    # Question 20
    tail = None

    # Question 21
    print("How many nodes does head contain?", node.listLength(head))
    print("How many nodes does selection contain?", node.listLength(selection))
    print("How many nodes does tail contain?", node.listLength(tail))

    # Question 22
    print("Head contains the letter", node.listSearch(head, 'K').getData())
    print("Selection contains the letter", node.listSearch(selection, 'I').getData())

    # Question 23
    copy = node.listCopyWithTail(head)
    print(f"Copy[0] contains {node.listLength(copy[0])} nodes")
    print(f"Copy[1] contains {node.listLength(copy[1])} nodes")

    # Question 24
    print("First node in copy[0] contains letter", copy[0].getData())
    print("First node in copy[1] contains letter", copy[1].getData())

    # Question 25
    i = 1
    while i <= 10:
        if(node.listPosition(head, i) != None):
            print(f"Head contains position {i}")
        else:
            print(f"Head doesn't contain position {i}")
        i += 1

def testListCopyWithTail():
    print("Testing List Copy With Tail")

    # construct node with data equal to S and link
    # equal to None and assign its reference to source
    source = node('S', None) # S

    # construct node with data equal to B and link equal to source
    # and assign its reference to source
    source = node('B', source) # B -> S

    # construct node with data equal to O and link equal to source
    # and assign its reference to source
    source = node('O', source) # O -> B -> S

    # construct node with data equal to J and link equal to source
    # and assign its reference to source
    source = node('J', source) # J -> O -> B -> S

    copy = node.listCopyWithTail(source)
    # [J -> O -> B -> S, S]

    print("Source contains", node.listPosition(source, 1).getData(),
        node.listPosition(source, 2).getData(),
        node.listPosition(source, 3).getData(),
        node.listPosition(source, 4).getData())
    
    print("Copy head contains", node.listPosition(copy[0], 1).getData(),
        node.listPosition(copy[0], 2).getData(),
        node.listPosition(copy[0], 3).getData(),
        node.listPosition(copy[0], 4).getData())

    print("Copy tail contains", node.listPosition(copy[1], 1).getData())

def testListCopy():
    print("Testing List Copy")

    # construct node with data equal to S and link
    # equal to None and assign its reference to source
    source = node('S', None) # S

    # construct node with data equal to B and link equal to source
    # and assign its reference to source
    source = node('B', source) # B -> S

    # construct node with data equal to O and link equal to source
    # and assign its reference to source
    source = node('O', source) # O -> B -> S

    # construct node with data equal to J and link equal to source
    # and assign its reference to source
    source = node('J', source) # J -> O -> B -> S

    copy = node.listCopy(source)

    print("Source contains", node.listPosition(source, 1).getData(),
        node.listPosition(source, 2).getData(),
        node.listPosition(source, 3).getData(),
        node.listPosition(source, 4).getData())
    
    print("Copy contains", node.listPosition(copy, 1).getData(),
        node.listPosition(copy, 2).getData(),
        node.listPosition(copy, 3).getData(),
        node.listPosition(copy, 4).getData())

def testListPosition():
    print("Testing List Position")

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

    print("First node contains data:", node.listPosition(head, 1).getData()) # J -> O -> B -> S
    print("Second node contains data:", node.listPosition(head, 2).getData()) # O -> B -> S
    print("Third node contains data:", node.listPosition(head, 3).getData()) # B -> S
    print("Fourth node contains data:", node.listPosition(head, 4).getData()) # S

    if(node.listPosition(head, 5) != None):
        print("Fifth node contains data:", node.listPosition(head, 5).getData())
    else:
        print("Fifth node does not exist.")

def testListSearch():
    print("Testing List Length")

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

    print("Head contains: ", node.listSearch(head, "J").getData())
    print("Head contains: ", node.listSearch(head, "O").getData())
    print("Head contains: ", node.listSearch(head, "B").getData())
    print("Head contains: ", node.listSearch(head, "S").getData())

    if(node.listSearch(head, "Z") != None):
        print("Head contains: ", node.listSearch(head, "Z").getData())
    else:
        print("Head does not contain Z.")

def testListLength():
    print("Testing List Length")

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

    print("Length of head is: ", node.listLength(head))

def review():
    print("Reviewing Node")

    # Question 1
    head = node('X', None)
    head = node('X', head)
    head = node('X', head)
    head = node('X', head)

    # Question 2
    selection1 = head

    # Question 3
    selection1.addNodeAfter('O')

    # Question 4
    selection1 = selection1.getLink()
    selection1 = selection1.getLink()

    # Question 5
    selection1.addNodeAfter('O')

    # Question 6
    selection1 = selection1.getLink()
    selection1 = selection1.getLink()

    # Question 7
    selection1.addNodeAfter('O')

    # Question 8
    tail = head

    # Question 9
    tail = tail.getLink()
    tail = tail.getLink()
    tail = tail.getLink()
    tail = tail.getLink()
    tail = tail.getLink()
    tail = tail.getLink()

    # Question 10
    selection2 = head

    # Question 11
    selection2 = selection2.getLink()
    selection2 = selection2.getLink()

    # Question 12
    head.setData('A')
    selection1.setData('A')
    selection2.setData('A')
    tail.setData('A')

    # Question 13
    head.removeNodeAfter()
    selection1.removeNodeAfter()
    selection2.removeNodeAfter()

def testRemoveNodeAfter():
    print("Testing Node Remove Node After")

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

    print("The head node contains data:", head.getData())

    # remove the node after the node head refers to (node that contains O)
    head.removeNodeAfter() # J -> B -> S

    head = head.getLink() # B -> S

    print("The head node contains data:", head.getData())

    # remove the node after the node head refers to (node that contains S)
    head.removeNodeAfter() # B

    print("The head node contains data:", head.getData())

    # remove the node after the node head refers to (node that contains B)
    # head.removeNodeAfter() # this line of code will generate an atribute error

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