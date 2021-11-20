from sys import stdin


class BinaryNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1
        self.rcount = 0


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
            v.rcount += 1
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
            v.rcount -= 1
        else:

            if v.right == None:
                return v.left

            elif v.left == None:
                return v.right

            m = self.find_min(v.right)
            rc = v.rcount
            m.right = self.delete_min(v.right)
            m.left = v.left
            m.rcount = rc - 1
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
        t.rcount += v.rcount + 1
        self.calc_height(v)
        self.calc_height(t)
        return t

    def rotate_left(self, v):
        t = v.right
        v.right = t.left
        t.left = v
        v.rcount -= (1 + t.rcount)
        self.calc_height(v)
        self.calc_height(t)
        return t

    def get_height(self, v):
        if v == None:
            return 0
        return v.height

    def print_tree(self, v, indent=0):
        if v != None:
            self.printTree(v.left, indent + 2)
            print(indent * '_' + str(v.value) + '-' + str(v.rcount))
            self.printTree(v.right, indent + 2)
        return

    def find_kmax(self, k):
        v = self.root
        while True:
            if k <= v.rcount:
                v = v.right
            elif k == v.rcount + 1 or v.left == None:
                return v.value
            else:
                k -= v.rcount + 1
                v = v.left

    def add(self, x):
        self.root = self.insert(self.root, x)

    def remove(self, x):
        self.root = self.delete(self.root, x)

    def print(self):
        self.printTree(self.root)

    def print(self):
        self.printTree(self.root)


def main():
    tree = AVLTree()
    for line in stdin.read().splitlines()[1:]:
        command, val = map(int, line.split())
        if command == 1:
            tree.add(val)
        elif command == -1:
            tree.remove(val)
        elif command == 0:
            print(tree.find_kmax(val))


if __name__ == "__main__":
    main()
