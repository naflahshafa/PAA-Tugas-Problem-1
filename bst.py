class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

class TreeNode:
    def __init__(self, student):
        self.student = student
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, student):
        if self.root is None:
            self.root = TreeNode(student)
        else:
            self._insert_helper(self.root, student)

    def _insert_helper(self, node, student):
        if student.score < node.student.score:
            if node.left is None:
                node.left = TreeNode(student)
            else:
                self._insert_helper(node.left, student)
        else:
            if node.right is None:
                node.right = TreeNode(student)
            else:
                self._insert_helper(node.right, student)

    def find_highest_score(self):
        if self.root is None:
            return []

        highest_score_students = []
        highest_score = float('-inf')

        self._find_highest_score_helper(self.root, highest_score, highest_score_students)

        return highest_score_students

    def _find_highest_score_helper(self, node, highest_score, highest_score_students):
        if node is None:
            return

        if node.student.score > highest_score:
            highest_score_students.clear()
            highest_score_students.append(node.student)
            highest_score = node.student.score
        elif node.student.score == highest_score:
            highest_score_students.append(node.student)

        self._find_highest_score_helper(node.left, highest_score, highest_score_students)
        self._find_highest_score_helper(node.right, highest_score, highest_score_students)

bst = BST()
bst.insert(Student("Itadori Yuji", 85))
bst.insert(Student("Moana", 92))
bst.insert(Student("Elsa", 78))
bst.insert(Student("Lightning McQueen", 95))
bst.insert(Student("Tehyung", 88))
bst.insert(Student("Haruto", 95))

highest_score_students = bst.find_highest_score()

if highest_score_students:
    print("Siswa dengan nilai tertinggi:")
    for student in highest_score_students:
        print(student.name, "-", student.score)
else:
    print("Tidak ada siswa dalam BST.")
