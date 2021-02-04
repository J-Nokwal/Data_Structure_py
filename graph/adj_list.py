class adjNode:
    def __init__(self,data):
        self.data=data
        self.next=None

class graph:
    def __init__(self,v):
        self.v=v # no of vertices
        self.graph=[None]*v
    
    def add_edge(self,source,destination):
        node=adjNode(destination)
        node.next=self.graph[source]
        self.graph[source]=node

        node=adjNode(source)
        node.next=self.graph[destination]
        self.graph[destination]=node

    def print_graph(self):

        for i in range(self.v):
            print(i,end=" --")
            temp=self.graph[i]
            while temp:
                print("->",temp.data,end=" ")
                temp=temp.next
            print()
    

if __name__ == "__main__": 
    v = 5
    g = graph(v)
    g.add_edge(0, 1) 
    g.add_edge(0, 4) 
    g.add_edge(1, 2) 
    g.add_edge(1, 3) 
    g.add_edge(1, 4) 
    g.add_edge(2, 3) 
    g.add_edge(3, 4) 
  
    g.print_graph() 