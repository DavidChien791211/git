"""
    linklist.py
    功能：實現單鏈表的構建和功能操作
    重點代碼：
"""


# 創建節點類
class Node:
    """
        思考方式：
            將自定義的類，節點的生成類
            實力對象中，包含數據部份和指向下個節點的NEXT
    """

    def __init__(self, value, next = None):
        self.value = value  # 存儲有用的數據
        self.next = next  # 循環下個類點關係


# node1 = Node(1)
# node2 = Node(2, node1)  # node2.next == node 1
# node3 = Node(3, node2)  # #node3.next == node 2
# 鏈表的各種操作
class LinkList():
    """
        思路：單鏈表，生成對象可以進行增刪改查操作
        具體操作通過調用具體方法完成。
    """

    def __init__(self):
        """
            初始化鏈表，標記一個鏈表的開端，以便於後續的節點。
        """
        # 杰點頭
        self.head = Node(None)

    # 通過list_target為鏈表添加一組節點
    def init_list(self, list_target):
        p = self.head  # p 作為移動變量
        for i in list_target:
            p.next = Node(i)
            p = p.next

    def show(self):
        p = self.head.next
        while p is not None:
            print(p.value)
            p = p.next

    # 判斷鏈表為空
    def is_empty(self):
        if self.head.next is None:
            return True
        else:
            return False

    # 清空鏈表
    def clear(self):
        self.head.next = None

    # 尾部插入
    def appen(self, val):
        p = self.head
        while p.next is not None:
            p = p.next
        p.next = Node(val)

    # 頭部插入
    def head_insert(self, val):
        node = Node(val)
        node.next = self.head.next
        self.head.next = node

    # 指定插入位置
    def insert(self, index, val):
        # if index == 0:
        #     self.head_insert(val)
        # else:
        #     count = 0
        #     p = self.head.next
        #     while p is not None:
        #         if index - 1 == count:
        #             node = Node(val)
        #             node.next = p.next
        #             p.next = node
        #             break
        #         count += 1
        #         p = p.next

        # 解答
        p = self.head
        for i in range(index):
            if p.next is None:
                # 超出位置的最大範圍
                break
            p = p.next
        node = Node(val)
        node.next = p.next
        p.next = node

    # 刪除節點
    def delete(self, x):
        p = self.head
        while p.next and p.next.value != x:
            p = p.next
        if p.next is None:
            raise ValueError("x is not in Linklist")
        else:
            p.next = p.next.next

    # 獲取某個節點的值
    def get_index(self, index):
        if index < 0:
            raise IndexError("Linklist index out of range ")
        p = self.head.next
        for item in range(index):
            if p.next is None:
                raise IndexError("Linklist index out of range ")
            p = p.next
        return p.value
