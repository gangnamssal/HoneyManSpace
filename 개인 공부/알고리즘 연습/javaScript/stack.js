class Node {
  constructor(value) {
    this.value = value;
    this.next = null;
  }
}

class Stack {
  constructor() {
    this.first = null;
    this.last = null;
    this.length = 0;
  }
  push(value) {
    const newNode = new Node(value);
    if (!this.first) {
      this.first = newNode;
      this.last = newNode;
    } else {
      newNode.next = this.first;
      this.first = newNode;
    }

    return ++this.length;
  }
  pop() {
    if (!this.first) return null;
    const oldFirst = this.first;

    if (this.first === this.last) {
      this.last = null;
    }
    this.first = oldFirst.next;
    this.length--;
    return oldFirst.value;
  }
}

const list = new Stack();
list.push(1);
list.push(2);

// console.log(list);
console.log(list.pop());
