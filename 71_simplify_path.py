'''
You are given an absolute path in a Unix-style file system that starts with a slash '/'. Your task is to simplify the path following these rules:
+ '.' means the current directory, and '..' means the parent directory;
+ Multiple consecutive slashes are treated as one;
+ Valid directory or file names may include periods (e.g., '...' and '....');
+ The simplified path must:
    + Start with a single slash;
    + Use exactly one slash to separate directories;
    + Not end with a slash unless it's the root directory.

Return the simplified canonical path.

Examples:
Input: path = "/home/"
Output: "/home"

Input: path = "/home//foo/"
Output: "/home/foo"

Дан абсолютный путь в файловой системе Unix, начинающийся с символа '/'. Ваша задача — упростить путь в соответствии со следующими правилами:
+ Символ '.' обозначает текущую директорию, а '..' — родительскую директорию;
+ Несколько подряд идущих слэшей ('//') считаются одним слэшем;
+ Допустимые имена файлов и директорий могут содержать точки (например, '...' и '....' — это допустимые имена);
+ Упрощённый (канонический) путь должен:
    + Начинаться с одного '/';
    + Использовать ровно один слэш между директориями;
    + Не заканчиваться слэшем, если только это не корневая директория ('/').

Верните упрощённый канонический путь.

Примеры:
Вход: path = "/home/"
Выход: "/home"

Вход: path = "/home//foo/"
Выход: "/home/foo"
'''

def simplify_path(path: str) -> str:
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