class Node {
  constructor(value) {
    this.value = value;
    this.right = null;
    this.left = null;
  }
}

class BinarySearchTree {
  constructor() {
    this.root = null;
  }
  insert(value) {
    const newNode = new Node(value);
    let current = this.root;
    if (!this.root) {
      this.root = newNode;
      return true;
    }
    while (true) {
      if (value === current.value) return undefined;
      if (value < current.value) {
        if (!current.left) {
          current.left = newNode;
          return true;
        }
        current = current.left;
      } else {
        if (!current.right) {
          current.right = newNode;
          return true;
        }
        current = current.right;
      }
    }
  }
  find(value) {
    let current = this.root;
    if (!this.root) return undefined;
    while (current) {
      if (value === current.value) {
        return current;
      } else if (value > current.value) {
        current = current.right;
      } else {
        current = current.left;
      }
    }
    return undefined;
  }
}

const tree = new BinarySearchTree();

tree.insert(4);
tree.insert(2);
tree.insert(5);
tree.insert(7);
tree.insert(9);
// console.log(tree);
console.log(tree.find(-1));
