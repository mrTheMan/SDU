/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package binarytrees;


/**
 *
 * @author Alexandros
 */
public class BinaryTrees {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        BinarySearchTree<Integer> t = new BinarySearchTree();
        
        t.insert(3);
        t.insert(4);
        t.insert(1);
        t.insert(5);
        t.insert(2);
        
        
        System.out.println("All nodes " + t.countNodes());
        System.out.println("Full nodes " + t.countFullNodes());
        System.out.println("Leaf nodes " + t.countLeafNodes());
    }
    
}
