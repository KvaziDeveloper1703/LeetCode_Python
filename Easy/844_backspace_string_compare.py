'''
Given two strings S and T. Each string represents input into a text editor, where:
    + '#' represents a backspace character;
    + typing '#' when the text is empty leaves it empty.

Return True if both strings are equal after processing the backspaces. Otherwise, return False.

Examples:
Input: S = "ab#c", T = "ad#c"
Output: True

Input: S = "ab##", T = "c#d#"
Output: True


'''

def backspace_сompare(S: str, T: str) -> bool:
    def build(text):
        result = []
        for character in text:
            if character == '#':
                if result:
                    result.pop()
            else:
                result.append(character)
        return ''.join(result)

    return build(S) == build(T)