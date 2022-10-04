import pytest
import palindrome_stack

def tests_success():
  assert palindrome_stack.palindrome('Anna') == 'This is a Palindrome!'
  assert palindrome_stack.palindrome('anNA') == 'This is a Palindrome!'
  assert palindrome_stack.palindrome('An  N a') == 'This is a Palindrome!'

def tests_fail():
  assert palindrome_stack.palindrome('Catherine') == 'This is not a Palindrome!'