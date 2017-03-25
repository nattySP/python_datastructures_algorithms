# python3
import argparse

class Query:

    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1].rstrip())
        else:
            self.s = query[1].rstrip()

class Chain:
    def __init__(self):
        self.head = None
        self.tail = None
        self.iterPointer = self.head

    def __iter__(self):
        while self.iterPointer is not None:
            yield self.iterPointer
            self.iterPointer = self.iterPointer.next
        self.iterPointer = self.head

    def updateHead(self, value):
        self.head = value
        self.iterPointer = self.head

    def add(self, string):
        node = Node(string)
        exists = self.find(string)
        if exists is None:
            if self.head is None:
                self.updateHead(node)
                self.tail = node
            else:
                node.next = self.head
                self.head.prev = node
                self.updateHead(node)

    def find(self, string):
        node = self.head
        while node is not None:
            if node.string == string:
                return node
            node = node.next
        return None

    def dele(self, string):
        node = self.find(string)
        if node is None:
            return
        if node is self.head and node is self.tail:
            self.updateHead(None)
            self.tail = None
        elif node is self.head:
            self.updateHead(node.next)
            node.next.prev = None
        elif node is self.tail:
            self.tail = node.prev
            node.prev.next = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev




class Node:
    def __init__(self, string):
        self.string = string
        self.next = None
        self.prev = None

    def __str__(self):
        return self.string

class Table:
    def __init__(self, m):
        self.store = [Chain() for i in range(m)]

    def __getitem__(self, i):
        return self.store[i]


class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count, lines):
        self.bucket_count = bucket_count
        # store all strings in one list
        self.elems = []
        self.lines = lines
        self.table = Table(bucket_count)

    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    def write_search_result(self, was_found):
        print('yes' if was_found else 'no')

    def write_chain(self, chain):
        print(' '.join(str(node) for node in chain))

    # def read_query(self):
    #     return Query(input().split())

    def read_query(self, line):
        return Query(line.split())

    def process_query(self, query):
        if query.type == "check":
            self.write_chain(self.table[query.ind])
        else:
            if query.type == 'find':
                index = self._hash_func(query.s)
                chain = self.table[index]
                result = chain.find(query.s)
                self.write_search_result(result is not None)
            elif query.type == 'add':
                index = self._hash_func(query.s)
                chain = self.table[index]
                chain.add(query.s)
            else:
                index = self._hash_func(query.s)
                chain = self.table[index]
                chain.dele(query.s)

    def process_queries(self):
        # n = int(input())
        n = int(self.lines.pop(0))
        for i in range(n):
            # self.process_query(self.read_query())
            self.process_query(self.read_query(self.lines.pop(0)))

if __name__ == '__main__':
    # remove before submission
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="The filename to be processed")
    args = parser.parse_args()
    lines = list()
    if args.filename:
        with open(args.filename) as f:
            for line in f:
                    lines.append(line)
    # end remove before submission
    # bucket_count = int(input())
    bucket_count = int(lines.pop(0))
    proc = QueryProcessor(bucket_count, lines)
    proc.process_queries()
