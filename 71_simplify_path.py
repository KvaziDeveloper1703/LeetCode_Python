'''
You are given an absolute path in a Unix-style file system that starts with a slash '/'. Your task is to simplify the path following these rules:
+ '.' means the current directory, and '..' means the parent directory.
+ Multiple consecutive slashes are treated as one.
+ Valid directory or file names may include periods (e.g., '...' and '....').
+ The simplified path must:
    + Start with a single slash.
    + Use exactly one slash to separate directories.
    + Not end with a slash unless it's the root directory.

Return the simplified canonical path.

Example 1:
Input: path = "/home/"
Output: "/home"

Example 2:
Input: path = "/home//foo/"
Output: "/home/foo"
'''

class Solution:
    def simplifyPath(self, path: str) -> str:
        parts = path.split('/')
        stack = []
        
        for part in parts:
            if part == '' or part == '.':
                continue
            elif part == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(part)
        
        simplified_path = '/' + '/'.join(stack)
        
        return simplified_path