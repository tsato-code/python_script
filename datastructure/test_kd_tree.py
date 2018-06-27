""" PythonによるK-d tree実装
1. Kd_tree.search関数内で使うregionの実装をどうするか検討中
2. Kd_tree.search関数内で使うreport_subtreeをどうするか検討中
3. Kd_tree.search関数内で使うintersectをどうするか
4. Kd_tree.build関数内で使う中央値探索は、Introduction to Algorithmsの10章線形中央値探索を使って高速化
"""

import numpy as np


class Kd_Node(object):
    def __init__(self, depth=None, cutval=None, area=Rectangle(), left=None, right=None, data=None,):
        self.depth = depth
        self.culval = cutval
        self.area = area
        self.left = left
        self.right = right
        self.data = data


    def __repr__(self):
        if self.left is None and self.right is None:
            return "<Kd_node = {}>".format(self.data)
        else:
            return "<Kd_node = {}>\n{}\n{}".format(self.data, self.left.__repr__(), self.right.__repr__())
    
    
    def is_leaf(self):
        return (not self.left) or (not self.right)
    
    
    def contain(self, R):
        return R[0] <= self.data[0] <= R[1] and R[2] <= self.data[1] <= R[3]


class Rectangle2d:
    def __init__(self, x_b=float('inf'), x_t=float('inf'), y_b=float('inf'), y_t=float('inf')):
        """ create rectangule """
        self.x_b = x_b
        self.x_t = x_t
        self.y_b = y_b
        self.y_t = y_t
    

    def __repr__(self):
        return "<Rectangle {}, {}, {}, {}>".format(self.x_b, self.x_t, self.y_b, self.y_t)


    def contains(self, p):
        return self.x_b <= p[0] <= self.x_t and self.y_b <- p[1] <= self.y_t


class Kd_tree(object):
    def __init__(self, points):
        self.root = self.build(points)
    
    
    def build(self, points, depth=0):
        """ build a K-d tree """
        if len(points) == 1:
            v = Kd_Node(depth=depth, data=points[0])
            return v
        elif depth%2 == 0:
            sort_index = np.argsort(points[:, 0])
        else:
            sort_index = np.argsort(points[:, 1])
        points = points[sort_index]
        axis = int(np.ceil(len(points)/2))
        points1 = points[:axis]
        points2 = points[axis:]
        left = self.build(points1, depth+1)
        right = self.build(points2, depth+1)
        v = Kd_Node(points[axis], left, right)
        return v
    
    

    def search(self, v, R, found=None):
        """ search K-d tree """
        if found==None: found = []
        if v.is_leaf():
            if v.contain(R):
                found.append(v.data)
            elif region(v.left) in R:  # debug 要修正 
                self.report_subtree(v.left, found)
            elif self.intersect(regin(v.left), R):
                self.search(v.right, R, found)
            if region(v.right) in R:
                self.report_subtree(v.right)
            elif self.intersect(region(v.right), R):
                self.search(v.right, R, found)
        return found
    
    
    def intersect(self):
        pass
    
    def report_subtree(self, v, found):
        # subtree v に含まれる点をすべて found に追加
        pass
        

if __name__ == '__main__':
    dataset = np.random.random((10, 2))
    print(dataset)
    t = Kd_tree(dataset)
    print(t.root)