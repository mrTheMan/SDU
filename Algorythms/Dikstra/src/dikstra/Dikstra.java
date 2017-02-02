/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package dikstra;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.PriorityQueue;

/**
 *
 * @author Alexandros
 */
public class Dikstra {

    /**
     * @param args the command line arguments
     */
    public static List<Vertice> nodes;
    public static void main(String[] args) {
        
        nodes = new ArrayList();
        
        // All Vertices
        Vertice a = new Vertice("a");
        Vertice b = new Vertice("b");
        Vertice c = new Vertice("c");
        Vertice d = new Vertice("d");
        Vertice e = new Vertice("e");
        Vertice f = new Vertice("f");
        Vertice g = new Vertice("g");
        
        // Edges for A 
        a.AddEdge(new Edge(1, a, b));
        
        // Edges for B
        b.AddEdge(new Edge(3, b, c));
        b.AddEdge(new Edge(2, b, d));
        b.AddEdge(new Edge(1, b, e));
        
        // Edges for C
        c.AddEdge(new Edge(4, c, e));
        c.AddEdge(new Edge(1, c, d));
        
        // Edges for D
        d.AddEdge(new Edge(2, d, a));
        d.AddEdge(new Edge(2, d, e));
        
        // Edges for G
        g.AddEdge(new Edge(1, g, d));
        
        // Edges for E
        e.AddEdge(new Edge(3, e, f));
        
        a.setWeight(0);
        
        ExecuteDikstra(a, f);
        ShowBestPath(f);
    }
    
    
    public static void ExecuteDikstra(Vertice Source, Vertice destination)
    {
        // Set the priority queue
        PriorityQueue<Vertice> queue = new PriorityQueue<Vertice>(201, 
            new Comparator<Vertice>(){
                public int compare(Vertice a, Vertice b){
                    if (a.getWeight() > b.getWeight()) 
                        return 1;
                    else
                        return -1;
                }
            });
        
        queue.add(Source);
        
        while(!queue.isEmpty())
        {
            Vertice v = queue.poll();
            List<Edge> e = v.getEdges();
            
            
            // Set vertice as visited
            v.setVisited(true);
            
            // Show node
            System.out.println(v.ToString());
            
            // Go through edges
            for(int j = 0; j < e.size(); j++ )
            {
                double curDistance = e.get(j).getDestination().getWeight();
                double newDistance = v.getWeight() + e.get(j).getWeight();
                Vertice next = e.get(j).getDestination();
                
                // Compare 
                if( curDistance > newDistance)
                {
                    // set new weight
                    next.setWeight(newDistance);
                    next.setPrev(v);
                }
                
                // if Vertice has not been visited
                if(!next.isVisited())
                { // add Vertice to queue
                    queue.add(next);
                }
                
                // Destination found and has been visited
                if(v.equals(destination) && v.isVisited())
                    return;
                
                // Show Edge 
                System.out.println(e.get(j).ToString());
            }
        }
    }
    
    
    public static void ShowBestPath(Vertice v)
    {
        System.out.println("Best path weight " + v.getWeight());
        
        // Set shortest path ending vertice
        String path = " -> " + v.getName();
        while(true)
        {
            // If previous vertice is empty we are back at the beginning
            if(v.getPrev() != null)
            {
                // combine string of shortest path 
                path =  " -> " + v.getPrev().getName() + path;
                v = v.getPrev();
            }
            else
            {
                System.out.println("Shortest path is: " + path);
                return;
            }
        }
    }
    
}
    

