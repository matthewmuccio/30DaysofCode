#!/usr/bin/env python3


import sys


class Solution:
    def __init__(self):
        self.word = []
        self.queue = []
    def pushCharacter(self, letter):
        self.word.insert(0, letter)
    def enqueueCharacter(self, letter):
        self.queue.append(letter)
    def popCharacter(self):
        return self.word.pop()
    def dequeueCharacter(self):
        return self.queue.pop()


if __name__ == "__main__":
    # Read the string s.
    s = input()
    # Create the Solution class object.
    obj = Solution()

    l = len(s)
    # Push/enqueue all the characters of string s to stack.
    for i in range(l):
        obj.pushCharacter(s[i])
        obj.enqueueCharacter(s[i])

    isPalindrome = True
    '''
    pop the top character from stack
    dequeue the first character from queue
    compare both the characters
    '''
    for i in range(l // 2):
        if obj.popCharacter() != obj.dequeueCharacter():
            isPalindrome=False
            break
    # Finally print whether string s is palindrome or not.
    if isPalindrome:
        print("The word, "+s+", is a palindrome.")
    else:
        print("The word, "+s+", is not a palindrome.")
