QUEUE

What is a Queue? 
A queue is a data structure used for storing data (similar to Linked Lists and stacks). 
In queue, the order in which data arrives is important. In general, a queue is a line of people or things waiting to be served in sequential order starting at the beginning of the line or sequence. 

Definition: A queue is an ordered list in which insertions are done at one end (rear) and deletions are done at other end (front). 
The first element to be inserted is the first one to be deleted. Hence, it is called First in First out (FIFO) or Last in Last out (LILO) list. 
Similar to Stacks, special names are given to the two changes that can be made to a queue. 
When an element is inserted in a queue, the concept is called EnQueue, and when an element is removed from the queue, the concept is culled DeQueue. 
Dequeuing an empty queue is called underflow and EnQueuing an element in a full queue is called overflow. 


              TREE
What is a Tree? 
A tree is a data structure similar to a linked LisL but instead of each node pointing simply to the next node in a linear fashion, each node points to a number of nodes. 
Tree is an example of non-linear data structures. A tree structure is a way of representing the hierarchical nature of a structure in a graphical form. 
In trees ADT (Abstract Data Type), the order of the elements is not important. If we need ordering information, linear data structures like linked lists, stacks, queues, etc. can be used. 

Glossary 
• The root of a tree is the node with no parents. There can be at most one root node in a tree.
• An edge refers to the link from parent to child (all links in the figure). 
• A node with no children is called leaf node 
• Children of same parent are called siblings.
• A node p is an ancestor of node q if there exists a path from root to q and p appears on the path. The node q is called a descendant of p.
• The set of all node at a given depth is called the level of the tree. The root node is at level zero.
• The depth of a node is the length of the path from the root to the node. 
• The height of a node is the length of the path from that node to the deepest node. The height of a tree is the length of the path from the root to the deepest node in the tree. A (rooted) tree with only one node (the root) has a height of zero.
• Height of the tree is the maximum height among all the nodes in the tree and depth of the tree is the maximum depth among all the nodes in the tree. For a given tree, depth and height returns the same value. 
But for individual nodes we may get different results. 
• The size of a node is the number of descendants it has including itself.
• If every node in a tree has only one child (except leaf nodes) then we call such trees skew trees. If every node 
has only left child then we call them left skew trees. Similarly, if every node has only right child then we call 
them right skew trees.

            Binary Trees
A tree is called binary tree if each node has zero child, one child or two children. Empty tree is also a valid binary tree. 
We can visualize a binary tree as consisting of a root and two disjoint binary trees, called the left and right subtrees of the root.

Types of Binary Trees 
1- Strict Binary Tree: A binary tree is called strict binary tree if each node has exactly two children or no children.
2- Full Binary Tree: A binary tree is called full binary tree if each node has exactly two children and all leaf nodes are at the same level.
3- Complete Binary Tree: Before defining the complete binary tree, let us assume that the height of the binary tree is h. 
In complete binary trees, if we give numbering for the nodes by starting at the root (let us say the root node has 1) then we get a complete sequence from 1 to the number of nodes in the tree. 
While traversing we should give numbering for NULL pointers also. 
A binary tree is called complete binary tree if all leaf nodes are at height h or h - 1 and also without any missing number in the sequence.