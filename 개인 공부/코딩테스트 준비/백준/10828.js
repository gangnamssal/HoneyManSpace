class Node {
  constructor(value) {
    this.value = value;
    this.next = null;
  }
}

class Stack {
  constructor() {
    this.head = null;
    this.tail = null;
    this.length = 0;
  }
  push(value) {
    const newNode = new Node(value);

    if (!this.head) {
      this.head = newNode;
      this.tail = newNode;
    } else {
      newNode.next = this.head;
      this.head = newNode;
    }
    this.length++;
  }
  pop() {
    if (!this.head) return -1;
    const oldHead = this.head;
    const newHead = oldHead.next;
    if (this.head === this.tail) {
      this.head = null;
      this.tail = null;
    } else {
      this.head = newHead;
    }
    this.length--;

    return oldHead.value;
  }
  size() {
    return this.length;
  }
  empty() {
    if (!this.head) return 1;
    return 0;
  }
  top() {
    if (!this.head) return -1;
    return this.head.value;
  }
}

const fs = require("fs");
const input = fs.readFileSync("./example.txt").toString().split("\n");

const N = input[1];
const stack = new Stack();

input.forEach((item, index) => {
  if (index !== 0) {
    let itemArr = item.split(" ");

    switch (itemArr[0].split("\r")[0]) {
      case "push":
        stack.push(parseInt(itemArr[1]));
        break;
      case "pop":
        console.log(stack.pop());
        break;
      case "size":
        console.log(stack.size());
        break;
      case "empty":
        console.log(stack.empty());
        break;
      case "top":
        console.log(stack.top());
        break;
      default:
    }
  }
});
