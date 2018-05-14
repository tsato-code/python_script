from rtree import index
import random

# Construct an instance
idx = index.Index()

# Create bounding box
left, bottom, right, top = (0.0, 0.0, 1.0, 1.0)

# Insert records into the index
idx.insert(0, (left, bottom, right, top))

# Intersection
isec_idx = list(idx.intersection((0.9, 0.0, 1.0, 0.5)))
print(isec_idx)

# Nearest Neighbors
idx.insert(1, (left, bottom, right, top))
isec_idx = list(idx.nearest((1.0000001, 1.0000001, 2.0, 2.0), 1))
print(isec_idx)


# Insert random points
for i in range(100):
	left, bottom = random.random(), random.random()
	# right, top = left+0.01, bottom+0.01
	right, top = left, bottom
	idx.insert(i, (left, bottom, right, top))

# Search intersection
hits = idx.intersection((0.0, 0.0, 0.1, 0.1), objects=True)

# Output
[print('{}: {}'.format(i.id, i.bbox)) for i in hits]


"""
$ python -u test_rtree.py 
[0]
[0, 1]
0: [0.0, 0.0, 1.0, 1.0]
1: [0.0, 0.0, 1.0, 1.0]
35: [0.07992105414325956, 0.0036073219748183893, 0.07992105414325956, 0.0036073219748183893]
98: [0.014593629500436855, 0.06622339638122332, 0.014593629500436855, 0.06622339638122332]
13: [0.06341062164646083, 0.06676878504910322, 0.06341062164646083, 0.06676878504910322]
"""