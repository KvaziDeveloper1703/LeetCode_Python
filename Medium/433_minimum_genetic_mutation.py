'''
A gene string is a string of length 8 using the characters 'A', 'C', 'G', 'T'.
You're given:
+ start_gene: the initial gene string;
+ end_gene: the target gene string;
+ bank: a list of valid gene strings.

Each mutation must:
+ Change exactly one character;
+ Result in a string present in bank.

Return the minimum number of mutations needed to mutate from start_gene to end_gene.
If no mutation is possible, return -1.

Example:
Input:
start_gene = "AACCGGTT"
end_gene = "AACCGGTA"
bank = ["AACCGGTA"]

Output:
1

Ген представлен строкой длиной 8 символов, состоящей из букв 'A', 'C', 'G', 'T'.
Ты должен найти минимальное количество мутаций, чтобы превратить строку start_gene в строку end_gene.
+ Одна мутация — это изменение одного символа в строке;
+ Все промежуточные строки должны быть в списке bank.

Если преобразовать невозможно — верни -1.

Пример:
Ввод:
start_gene = "AACCGGTT"
end_gene = "AACCGGTA"
bank = ["AACCGGTA"]

Вывод:
1
'''

from typing import List
from collections import deque

def min_mutation(start_gene: str, end_gene: str, bank: List[str]) -> int:
    valid_genes = set(bank)
    if end_gene not in valid_genes:
        return -1
    gene_options = ['A', 'C', 'G', 'T']
    visited = set()
    bfs_queue = deque([(start_gene, 0)])
    while bfs_queue:
        current_gene, mutation_count = bfs_queue.popleft()
        if current_gene == end_gene:
            return mutation_count
        for i in range(len(current_gene)):
            for nucleotide in gene_options:
                if nucleotide != current_gene[i]:
                    mutated_gene = current_gene[:i] + nucleotide + current_gene[i+1:]
                    if mutated_gene in valid_genes and mutated_gene not in visited:
                        visited.add(mutated_gene)
                        bfs_queue.append((mutated_gene, mutation_count + 1))
    return -1