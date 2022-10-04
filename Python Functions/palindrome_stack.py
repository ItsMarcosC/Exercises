def palindrome(string):
  stack = []
  result = ''
  name = string.replace(" ", "")
  for x in range(len(name)):
    if x <= len(name) / 2 - 1:
      stack.append(name[x])
    elif x >= len(name) / 2 and name[x].lower() == stack[-1].lower():
      stack.pop()
  
  if len(stack) == 0:
    result = 'This is a Palindrome!'
  else:
    result = 'This is not a Palindrome!'
  return result
