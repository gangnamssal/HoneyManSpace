class MaxBinaryHeap {
  constructor() {
    this.value = [];
  }
  bubbleUp() {
    let idx = this.value.length - 1;
    const element = this.value[idx];
    while (idx > 0) {
      let parentIdx = Math.floor((idx - 1) / 2);
      let parentValue = this.value[parentIdx];
      if (element <= parentValue) break;
      this.value[parentIdx] = element;
      this.value[idx] = parentValue;
      idx = parentIdx;
    }
  }
  insert(element) {
    this.value[this.value.length] = element;
    this.bubbleUp();
  }
}

const heap = new MaxBinaryHeap();
heap.insert(44);
heap.insert(15);
heap.insert(37);
heap.insert(3);
heap.insert(9);
heap.insert(25);
heap.insert(55);
heap.insert(4);
console.log(heap);
