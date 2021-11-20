from sys import stdin


class BinaryNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, v, x):
        if v == None:
            return BinaryNode(x)
        if v.value > x:
            v.left = self.insert(v.left, x)
        elif v.value < x:
            v.right = self.insert(v.right, x)

        return self.balance(v)

    def calc_height(self, v):
        heightleft = self.get_height(v.left)
        heightright = self.get_height(v.right)
        v.height = heightleft + 1 if heightleft > heightright else heightright + 1

    def calc_balance(self, v):
        return self.get_height(v.right) - self.get_height(v.left)

    def balance(self, v):
        self.calc_height(v)
        if self.calc_balance(v) == 2:
            if self.calc_balance(v.right) < 0:
                v.right = self.rotate_right(v.right)
            return self.rotate_left(v)
        if self.calc_balance(v) == -2:
            if self.calc_balance(v.left) > 0:
                v.left = self.rotate_left(v.left)
            return self.rotate_right(v)
        return v

    def delete(self, v, x):
        if v == None:
            return None
        if v.value > x:
            v.left = self.delete(v.left, x)
        elif v.value < x:
            v.right = self.delete(v.right, x)
        else:
            if v.right == None:
                return v.left
            elif v.left == None:
                return v.right
            m = self.find_min(v.right)
            m.right = self.delete_min(v.right)
            m.left = v.left
            return self.balance(m)
        return self.balance(v)

    def delete_min(self, v):
        if v.left == None:
            return v.right
        v.left = self.delete_min(v.left)
        return self.balance(v)

    def find_min(self, v):
        while v.left != None:
            v = v.left
        return v

    def rotate_right(self, v):
        t = v.left
        v.left = t.right
        t.right = v

        self.calc_height(v)
        self.calc_height(t)

        return t

    def rotate_left(self, v):
        t = v.right
        v.right = t.left
        t.left = v

        self.calc_height(v)
        self.calc_height(t)

        return t

    def get_height(self, v):
        if v == None:
            return 0
        return v.height

    def next(self, x):
        v = self.root
        res = None
        while v != None:
            if v.value > x:
                res = v
                v = v.left
            else:
                v = v.right
        if res:
            return res.value
        else:
            return 'none'

    def prev(self, x):
        v = self.root
        res = None
        while v != None:
            if v.value < x:
                res = v
                v = v.right
            else:
                v = v.left

        if res:
            return res.value
        else:
            return 'none'

    def search(self, v, x):
        if v == None:
            return None
        if v.value == x:
            return v
        elif x < v.value:
            return self.search(v.left, x)
        else:
            return self.search(v.right, x)

    def print_tree(self, v, indent=0):
        if v != None:
            self.printTree(v.left, indent + 2)
            print(indent * '_' + str(v.value))
            self.printTree(v.right, indent + 2)
        return

    def add(self, x):
        self.root = self.insert(self.root, x)

    def remove(self, x):
        self.root = self.delete(self.root, x)

    def print(self):
        self.printTree(self.root)

    def find(self, x):
        return self.search(self.root, x)


def main():
    bst = AVLTree()
    for operation in stdin:
        act, val_ = operation.split()
        val = int(val_)
        if act == "insert":
            bst.add(val)
        elif act == "delete":
            bst.remove(val)
        elif act == "exists":
            print('true' if bst.find(val) else 'false')
        elif act == "prev":
            res = bst.prev(val)
            print(res)
        elif act == "next":
            res = bst.next(val)
            print(res)


if __name__ == "__main__":
    main()