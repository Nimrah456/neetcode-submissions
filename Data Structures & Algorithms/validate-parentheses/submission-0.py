class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for char in s:
            match char:
                # Push opening brackets to stack
                case "(" | "{" | "[":
                    stack.append(char)
                    
                # Match closing brackets against the popped stack element
                case ")":
                    if not stack or stack.pop() != "(": return False
                case "}":
                    if not stack or stack.pop() != "{": return False
                case "]":
                    if not stack or stack.pop() != "[": return False
                    
        return len(stack) == 0


        