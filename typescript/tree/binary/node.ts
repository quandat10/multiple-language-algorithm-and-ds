export class Node {
  private readonly value: string
  private left: Node | null
  private right: Node | null

  constructor(value: string) {
    this.value = value
    this.left = null
    this.right = null
  }

  getLeftNode(): Node | null {
    return this.left
  }

  getRightNode(): Node | null {
    return this.right
  }

  setLeftNode(node: Node) {
    this.left = node
  }

  setRightNode(node: Node) {
    this.right = node
  }

  getValue(): string {
    return this.value
  }
}