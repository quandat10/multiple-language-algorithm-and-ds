import {Node} from "./node"
import {depthFirstTraversalArray, depthFirstTraversalRecursion} from "./traversal";
const nodeA = new Node("a")
const nodeB = new Node("b")
const nodeC = new Node("c")
const nodeD = new Node("d")
const nodeE = new Node("e")
const nodeF = new Node("f")
const nodeG = new Node("g")
const nodeH = new Node("h")
const nodeI = new Node("i")
const nodeK = new Node("k")
const nodeL = new Node("l")
const nodeM = new Node("m")
const nodeN = new Node("n")

nodeA.setLeftNode(nodeB)
nodeA.setRightNode(nodeC)
nodeB.setLeftNode(nodeD)
nodeB.setRightNode(nodeE)
nodeC.setLeftNode(nodeF)
nodeC.setRightNode(nodeI)
nodeD.setLeftNode(nodeK)
nodeD.setRightNode(nodeL)
nodeE.setLeftNode(nodeM)
nodeE.setRightNode(nodeN)

// const dfsArray = depthFirstTraversalArray(nodeA)
const dfsArray = depthFirstTraversalRecursion(nodeA)

console.log(dfsArray)


//            A
//          /   \
//        B       C
//      /   \   /   \
//    D       EF      I