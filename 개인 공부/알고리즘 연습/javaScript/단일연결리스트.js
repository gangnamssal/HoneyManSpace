class Node {
  constructor(val) {
    this.val = val;
    this.next = null;
  }
}

class SingleLinkedList {
  constructor() {
    this.head = null;
    this.tail = null;
    this.length = null;
  }
  print() {
    const arr = [];
    let current = this.head;
    for (let i = 0; i < this.length; i++) {
      arr[arr.length] = current.val;
      current = current.next;
    }
    return arr;
  }

  push(val) {
    const newNode = new Node(val);
    if (!this.head) {
      this.head = newNode;
      this.tail = newNode;
    } else {
      this.tail.next = newNode;
      this.tail = newNode;
    }
    this.length++;
    return this;
  }

  pop() {
    if (!this.head) return undefined;

    let current = this.head;
    let newTail = current;

    while (current.next) {
      newTail = current;
      current = current.next;
    }
    this.tail = newTail;
    newTail.next = null;
    this.length--;
    if (!this.length) {
      this.head = null;
      this.tail = null;
    }
    return current;
  }
  shift() {
    if (!this.head) return undefined;
    const current = this.head;

    this.head = current.next;
    this.length--;
    if (!this.length) {
      this.head = null;
      this.tail = null;
    }
    return current;
  }
  unshift(val) {
    const newNode = new Node(val);

    if (!this.head) {
      this.head = newNode;
      this.tail = newNode;
    } else {
      newNode.next = this.head;
      this.head = newNode;
    }
    this.length++;

    return this;
  }
  get(index) {
    if (!this.head || index < 0 || index >= this.length) return null;

    let count = 0;
    let current = this.head;

    while (count !== index) {
      current = current.next;
      count++;
    }
    return current;
  }
  set(index, val) {
    const foundNode = this.get(index);
    if (foundNode) {
      foundNode.val = val;
      return true;
    }

    return false;
  }
  insert(index, val) {
    if (index < 0 || index > this.length) return false;
    if (index === 0) {
      this.unshift(val);
      return true;
    }
    if (index === this.length) {
      this.push(val);
      return true;
    }
    const newNode = new Node(val);
    const foundNode = this.get(index - 1);
    newNode.next = foundNode.next;
    foundNode.next = newNode;
    this.length++;

    return true;
  }
  remove(index) {
    if (index < 0 || index >= this.length) return false;
    if (index === 0) {
      this.shift();
      return true;
    }
    if (index === this.length - 1) {
      this.pop();
      return true;
    }
    const foundNode = this.get(index - 1);
    const newTail = foundNode.next;
    foundNode.next = newTail.next;
    this.length--;
    if (!this.length) {
      this.head = null;
      this.tail = null;
    }

    return true;
  }
  reverse() {
    let start = this.head;
    this.head = this.tail;
    this.tail = start;
    let next = null;
    let prev = null;
    let count = 0;

    while (count < this.length) {
      next = start.next;
      start.next = prev;
      prev = start;
      start = next;
      count++;
    }
  }
}

const list = new SingleLinkedList();
list.push(1);
list.push(2);
list.push(3);
list.push(4);
list.push(5);
list.reverse();

console.log(list);
console.log(list.print());
