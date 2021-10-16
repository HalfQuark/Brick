# Brick
  Very simple programming language interpreted in python  
  
  Has a Stack and a 0-indexed dynamic size "Memory" Array.  
  It is also case sensitive.  
  Multiple commands can be on the same line separated by \  
 
 Commands:
- Expression: Pushes the value as an int, float or string on top of the stack
- SET: Pops the first and second elements from the Stack and stores the second element in the Memory at the index specified by the first element
- GET: Pops the first element from the Stack and pushes the value in the Memory at the index specified by this element on top of the stack
- POP: Pops the first element from the Stack
- IN: Waits for an input and pushes it on top of the Stack
- OUT: Pops the first element from the Stack and prints it
- GOTO: Pops the first element from the Stack and goes to the 1-indexed line specified by its value
- END: Terminates the program
- Operators + - * /: Pops the first and second elements from the Stack and pushes the result of the operation on top of the stack
- Comparisons < > =: Pops the first and second elements from the Stack and if the condition evaluates to false skips to the next line
- DEBUG: Prints the Stack and Memory
