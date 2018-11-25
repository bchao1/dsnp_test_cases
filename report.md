# Data Structures and Programming HW5 Report
B06901104 趙崇皓
***
## Implementations 
### Binary Search Tree
Binary Search Trees (a.k.a. BST) are binary trees that has the following property: the key of each node is larger than the key of its left children and smaller than the key of its right children (given left/right children are present). This allows us to perform simple lookup and insertion by simply traversing a root-to-leaf path. 

![BST](./img/BST.png)

There are two template classes in the BST implementation:

```c++
template <class T> class BSTreeNode;
template <class T> class BSTree;
```