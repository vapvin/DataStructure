class Node {
    constructor(data){
        this.data = data;
        this.next = null;
    }

    add() {

    }
}

const node1 = new Node(2);
const node2 = new Node(4);
node1.next = node2;
node2.next = null;
