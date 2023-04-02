# python3

class Query:
    def __init__(self, q):
        self.op = q[0]
        self.num = int(q[1])
        if self.op == 'add':
            self.name = q[2]

def read_queries():
    n = int(input())
    return [Query(input().split()) for _ in range(n)]

def write_output(output):
    print('\n'.join(output))

def process_queries(queries):
    output = []
    phonebook = {q.num: q.name for q in queries if q.op == 'add'}
    for query in queries:
        if query.op == 'add':
            phonebook[query.num] = query.name
        elif query.op == 'del':
            phonebook.pop(query.num, None)
        else:
            response = phonebook.get(query.num, 'not found')
            output.append(response)
    return output

if __name__ == '__main__':
    queries = read_queries()
    output = process_queries(queries)
    write_output(output)
