from sys import stdin


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def put(self, key):
        value = key
        if self.root:
            self.root.put(key, value)
        else:
            self.root = TreeNode(key, value)

    def get(self, key):
        if self.root:
            return self.root.get(key)
        else:
            return None

    def nextl(self, key):
        if self.root:
            return self.root.nextl(key)
        else:
            return print('none')

    def prevl(self, key):
        if self.root:
            return self.root.prevl(key)
        else:
            return print('none')

    def delete(self, key):
        if self.root:
            self.root = self.root.delete(key)


class TreeNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None

    def put(self, key, val):
        if self.key == key:
            self.val = val
        elif self.key > key:
            if self.left:
                self.left.put(key, val)
            else:
                self.left = TreeNode(key, val)
        else:
            if self.right:
                self.right.put(key, val)
            else:
                self.right = TreeNode(key, val)

    def get(self, key):
        if self.key == key:
            return self.val
        if self.key > key:
            if self.left:
                return self.left.get(key)
            else:
                return None
        else:
            if self.right:
                return self.right.get(key)
            else:
                return None

    def nextl(self, key):
        v = self
        res = None
        while v != None:
            if v.val > key:
                res = v.val
                v = v.left
            else:
                v = v.right
        if res:
            return print(res)
        else: print('none')

    def prevl(self, key):
        v = self
        res = None
        while v != None:
            if v.val < key:
                res = v.val
                v = v.right
            else:
                v = v.left
        if res:
            return print(res)
        else:
            print('none')

    def delete(self, key):
        if self.key == key:
            if self.right and self.left:
                [psucc, succ] = self.right._findMin(self)
                if psucc.left == succ:
                    psucc.left = succ.right
                else:
                    psucc.right = succ.right
                succ.left = self.left
                succ.right = self.right

                return succ

            else:
                if self.left:
                    return self.left
                else:
                    return self.right
        else:
            if self.key > key:
                if self.left:
                    self.left = self.left.delete(key)
            else:
                if self.right:
                    self.right = self.right.delete(key)
        return self

    def _findMin(self, parent):
        if self.left:
            return self.left._findMin(self)
        else:
            return [parent, self]


def main():
    tree = BinarySearchTree()
    for line in stdin.buffer.read().decode().splitlines():
        inpt_oper = line
        oper, val = map(str, inpt_oper.split())
        if oper == 'insert':
            tree.put(int(val))
        elif oper == 'delete':
            tree.delete(int(val))
        elif oper == 'exists':
            print('false' if not tree.get(int(val)) else 'true')
        elif oper == 'next':
            tree.nextl(int(val))
        elif oper == 'prev':
            tree.prevl(int(val))


if __name__ == '__main__':
    main()

