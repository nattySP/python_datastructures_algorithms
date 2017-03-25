# python3

import sys, threading
# import argparse # remove for submission
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size
ROOT_PARENT = -1
PLACEHOLDER = -1



class TreeHeight:
        def read(self):
                # remove before submission
                # parser = argparse.ArgumentParser()
                # parser.add_argument("filename", help="The filename to be processed")
                # args = parser.parse_args()
                # lines = list()
                # if args.filename:
                #     with open(args.filename) as f:
                #         for line in f:
                #                 lines.append(line)
                # end remove before submission
                self.n = int(sys.stdin.readline())
                # self.n = int(lines[0])
                self.parent = list(map(int, sys.stdin.readline().split()))
                # self.parent = list(map(int, lines[1].split()))
                self.tree = [[] for i in range(self.n)]

        def build_tree(self):
                for nodeValue, parent in enumerate(self.parent):
                        # put index value in parent position of tree
                        if parent is not ROOT_PARENT:
                                self.tree[parent].append(nodeValue)
                        else:
                                self.root = nodeValue

                # print('made tree')



        def compute_height(self):
                # Replace this code with a faster implementation
                maxHeight = 0

                queue = list()
                queue.append(self.root)
                queue.append(PLACEHOLDER)

                while len(queue):
                         currentNodeIndex = queue.pop(0)
                         if currentNodeIndex == PLACEHOLDER:
                                 maxHeight += 1
                                 if len(queue):
                                         queue.append(PLACEHOLDER)
                         else:
                                 currentNodeChildren = self.tree[currentNodeIndex]
                                 for child in currentNodeChildren:
                                         queue.append(child)

                return maxHeight

def main():
  tree = TreeHeight()
  tree.read()
  tree.build_tree()
  print(tree.compute_height())

threading.Thread(target=main).start()
