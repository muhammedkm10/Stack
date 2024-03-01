def eval(s):
   stack = []
   brackets = { "{":"}","[":"]","(":")"}
   for char in s:
       if char in brackets:
           stack.append(char)
       else:
           if stack:
               top = stack.pop()
               if brackets[top] != char:
                   return False
           else:
               return False
   return False if stack else True
s = "{[](){}}"
i = eval(s)
print(i)