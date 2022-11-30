import {Node} from "./node";

// =================== DEPTH FIRST TRAVERSAL (DFS) - USER STACK ===================

export const depthFirstTraversalArray = (root: Node): string[] => {
  let result: string[] = []
  const stack: Node[] = [root]
  while (stack.length) {
    const currentNode = stack.pop()
    // ========== LEFT TO RIGHT ==========
    if (currentNode) {
      const rightNode = currentNode.getRightNode()
      if (rightNode) {
        stack.push(rightNode)
      }

      const leftNode = currentNode.getLeftNode()
      if (leftNode) {
        stack.push(leftNode)
      }

      result.push(currentNode.getValue())
    }
  }

  return result
}

export const depthFirstTraversalRecursion = (root: Node): string[] => {
  if (root) {
    const rightNode = root.getRightNode()
    const leftNode = root.getLeftNode()

    let leftValue:string[] = []
    let rightValue:string[] = []

    if(rightNode) rightValue = depthFirstTraversalRecursion(rightNode)
    if(leftNode) leftValue = depthFirstTraversalRecursion(leftNode)

    return [root.getValue(),...leftValue, ...rightValue]
  }else{
    return []
  }
}

// =================== BREATH FIRST TRAVERSAL (BFS) - USE QUEUE ===================
