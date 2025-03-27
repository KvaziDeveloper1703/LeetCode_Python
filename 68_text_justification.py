'''
Given an array of words and an integer maxWidth, format the text so that each line has exactly maxWidth characters and is fully justified (aligned on both left and right).
Use a greedy approach: fill each line with as many words as possible.

Rules:
+ Add spaces between words to make the line exactly maxWidth characters long.
+ Distribute spaces as evenly as possible between words.
+ If extra spaces remain, put more on the left.
+ The last line should be left-justified, with words separated by a single space and any extra spaces added at the end.

Examples:
Input: 
  words = ["This", "is", "an", "example", "of", "text", "justification."], 
  maxWidth = 16

Output:
[
  "This    is    an",
  "example  of text",
  "justification.  "
]

Input: 
  words = ["What","must","be","acknowledgment","shall","be"], 
  maxWidth = 16

Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]

Input: 
  words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], 
  maxWidth = 20

Output:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]
'''

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        line = []
        line_len = 0

        for word in words:
            if line_len + len(word) + len(line) > maxWidth:
                spaces = maxWidth - line_len
                if len(line) == 1:
                    res.append(line[0] + ' ' * spaces)
                else:
                    even_space = spaces // (len(line) - 1)
                    extra = spaces % (len(line) - 1)
                    for i in range(extra):
                        line[i] += ' '
                    res.append((' ' * even_space).join(line))
                line = []
                line_len = 0

            line.append(word)
            line_len += len(word)

        res.append(' '.join(line).ljust(maxWidth))
        return res