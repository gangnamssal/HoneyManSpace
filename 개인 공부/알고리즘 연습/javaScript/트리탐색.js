class Node {
  constructor(value) {
    this.value = value;
    this.left = null;
    this.right = null;
  }
}

class BinarySearchTree {
  constructor() {
    this.root = null;
  }
  insert(value) {
    const newNode = new Node(value);
    let current = this.root;
    if (!current) {
      this.root = newNode;
      return this;
    }
    while (true) {
      if (value === current.value) return undefined;
      if (value < current.value) {
        if (!current.left) {
          current.left = newNode;
          return this;
        }
        current = current.left;
      } else {
        if (!current.right) {
          current.right = newNode;
          return this;
        }
        current = current.right;
      }
    }
  }
  BFS() {
    const data = [];
    const queue = [];
    let node = this.root;

    queue.push(node);
    while (queue.length) {
      node = queue.shift();
      data.push(node.value);
      if (node.left) queue.push(node.left);
      if (node.right) queue.push(node.right);
    }
    return data;
  }
  DFSPreOrder() {
    const data = [];
    const current = this.root;
    function dfs(node) {
      data.push(node.value);
      if (node.left) dfs(node.left);
      if (node.right) dfs(node.right);
    }
    dfs(current);

    return data;
  }
  DFSInOrder() {
    const data = [];
    const current = this.root;
    function dfs(node) {
      if (node.left) dfs(node.left);
      data.push(node.value);
      if (node.right) dfs(node.right);
    }
    dfs(current);
    return data;
  }
  DFSPostOrder() {
    const data = [];
    const current = this.root;
    function dfs(node) {
      if (node.left) dfs(node.left);
      if (node.right) dfs(node.right);
      data.push(node.value);
    }
    dfs(current);
    return data;
  }
}

const tree = new BinarySearchTree();
tree.insert(10);
tree.insert(12);
tree.insert(7);
tree.insert(9);
tree.insert(5);
tree.insert(15);
tree.insert(11);

console.log(tree.BFS());
console.log(tree.DFSPreOrder());
console.log(tree.DFSInOrder());
console.log(tree.DFSPostOrder());
