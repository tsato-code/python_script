""" PythonによるK-d tree実装
- コード整理
- prep()プライベートメソッド化
- テスト
- 2d可視化
- Kd_tree.build関数内で使う中央値探索は、Introduction to Algorithmsの10章線形中央値探索を使って高速化
   →複雑なのでpointsを前処理的に各座標成分でソートしておく
- 境界を等式付き不等号とするか当敷なしとするか、特に矩形同士の交差、包含判定
- 一般のk次元
"""

import numpy as np
import copy


class Kd_Node(object):
    def __init__(self, depth=None, cutval=None, left=None, right=None, data=None,):
        self.depth = depth
        self.cutval = cutval
        self.left = left
        self.right = right
        self.data = data


    def __repr__(self):
        if self.is_leaf():
            return "<Kd_node = (depth, data) = ({}, {})>".format(self.depth, self.data)
        else:
            return "<Kd_node = (depth, cutval) = ({}, {})>\n{}\n{}".format(self.depth, self.cutval, self.left.__repr__(), self.right.__repr__())
    
    
    def is_leaf(self):
        return (not self.left) or (not self.right)
    
    
    def is_contained(self, R):
        return R.x_b <= self.data[0] < R.x_t and R.y_b <= self.data[1] < R.y_t


class Rectangle2d(object):
    def __init__(self, x_b=-float('inf'), x_t=float('inf'), y_b=-float('inf'), y_t=float('inf')):
        """ create rectangule """
        self.x_b = x_b
        self.x_t = x_t
        self.y_b = y_b
        self.y_t = y_t
    

    def __repr__(self):
        return "<Rectangle {}, {}, {}, {}>".format(self.x_b, self.x_t, self.y_b, self.y_t)

   
    def intersect_R(self, R):
        return not (self.x_t < R.x_b or self.y_t < R.y_b or R.x_t < self.x_b or R.y_t < self.y_b)

    
    def is_contained_R(self, R):
        return R.x_b <= self.x_b and R.y_b <= self.y_t and self.x_b <= R.x_t and self.y_b <= R.y_t


class Kd_tree(object):
    def __init__(self, points):
        """ constructor """
        self.root = self.build(points)

    
    def build(self, points, depth=0):
        """ build """
        if len(points) == 1:
            return Kd_Node(depth=depth, data=points[0])
        elif depth%2 == 0:
            sort_index = np.argsort(points[:, 0])
        else:
            sort_index = np.argsort(points[:, 1])
        points = points[sort_index]
        axis = int(np.ceil(len(points)/2))
        points1 = points[:axis]               # イコールを含むのでプラス1
        points2 = points[axis:]
        left = self.build(points1, depth+1)
        right = self.build(points2, depth+1)
        cutval = points[axis-1][depth%2]  # 配列は0番から始まるのでマイナス1
        v = Kd_Node(depth=depth, cutval=cutval, left=left, right=right)

        return v


    def _prep(self, v=None):
        """ preprocessing """
        if v == None:
            v = self.root
            v.R = Rectangle2d()
        if not v.is_leaf():
            v.left.R = copy.deepcopy(v.R)
            v.right.R = copy.deepcopy(v.R)
            if v.depth%2 == 0:
                v.left.R.x_t = v.cutval
                v.right.R.x_b = v.cutval
            else:
                v.left.R.y_t = v.cutval
                v.right.R.y_b = v.cutval
            self._prep(v.left)
            self._prep(v.right)



    def search(self, v, R, found=[]):
        """ search """
        if v.is_leaf():
            if v.is_contained(R):
                found.append(v.data)
        else:
            if v.left.R.is_contained_R(R):
                self.report_subtree(v.left, found)
            elif v.left.R.intersect_R(R):
                self.search(v.left, R, found)
            if v.right.R.is_contained_R(R):
                self.report_subtree(v.right, found)
            elif v.right.R.intersect_R(R):
                self.search(v.right, R, found)
        return found

    
    def report_subtree(self, v, found):
        if v.is_leaf():
            found.append(v.data)
        else:
            self.report_subtree(v.left, found)
            self.report_subtree(v.right, found)
    
    
    def view(self):
        pass
        

#if __name__ == '__main__':
dataset = np.random.random((10, 2))
# dataset = np.array([[2,5], [4,1], [1,3]])
print(dataset)

print('* build *')
t = Kd_tree(dataset)
t._prep()
print(t.root)

print('* search *')
R = Rectangle2d(.0, .2, .0, .2)
founds = t.search(t.root, R)
print(founds)

print('* recalculation *')
print([p for p in dataset if R.x_b<=p[0]<=R.x_t and R.y_b<=p[1]<=R.y_t])
