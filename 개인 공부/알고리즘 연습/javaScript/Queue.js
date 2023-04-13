class Node {
  constructor(value) {
    this.value = value;
    this.next = null;
  }
}

class Queue {
  constructor() {
    this.first = null;
    this.last = null;
    this.size = 0;
  }
  enqueue(value) {
    const newNode = new Node(value);
    if (!this.first) {
      this.first = newNode;
      this.last = newNode;
    } else {
      this.last.next = newNode;
      this.last = newNode;
    }
    return ++this.size;
  }
  dequeue() {
    if (!this.first) return null;
    const unshifted = this.first;
    if (this.first === this.last) {
      this.last = null;
    }
    this.first = unshifted.next;
    this.size--;
    return unshifted.value;
  }
}

const list = new Queue();
list.enqueue(1);
list.enqueue(2);

console.log(list.dequeue());
