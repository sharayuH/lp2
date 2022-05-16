#include <iostream>
#include <map>
#include <vector>
 
using namespace std;
 
class Queue
{
    int queue[50];
    int front, rear;
 
public:
    friend class Graph;
    Queue()
    {
        front = rear = -1;
    }
 
    bool isFull()
    {
        if (rear == 49)
            return true;
        return false;
    }
 
    bool isEmpty()
    {
        if (front == -1 || front == rear + 1)
            return true;
        return false;
    }
 
    void enqueue(int x)
    {
        if (isFull())
        {
            cout << "Queue is Full" << endl;
            return;
        }
        if (front == -1 && rear == -1)
            front = rear = 0;
        else
            rear++;
        queue[rear] = x;
    }
 
    int dequeue()
    {
        if (isEmpty())
        {
            cout << "Queue is Empty" << endl;
            return -1;
        }
        int y = queue[front++];
        return y;
    }
 
    int getfront()
    {
        if (isEmpty())
        {
            cout << "Queue is Empty" << endl;
            return -1;
        }
        return queue[front];
    }
};
class Graph
{
    map<int, vector<int>> adj_list;
 
public:
    void addEdge(int to, int from)
    {
        adj_list[to].push_back(from);
        adj_list[from].push_back(to);
    }
 
    void display()
    {
        for (auto vertex : adj_list)
        {
            cout << vertex.first << " -> ";
            for (int i : vertex.second)
            {
                cout << i << " ";
            }
            cout << endl;
        }
    }
 
    void search(int ver)
    {
        map<int, vector<int>>::iterator it;
        it = adj_list.find(ver);
        if (it == adj_list.end())
        {
            cout << "| Vertex not present!";
        }
        else
        {
            cout << "| Vertex present!";
        }
    }
 
    void bfs(int start) // bfs recursive
    {
        Queue q; // queue for BFS traversal
        q.enqueue(start);
        map<int, bool> visited; // to keep track of vertices that are visited
        visited[start] = true;
        bfs_main(q, visited);
        cout << endl;
    }
 
    void bfs_main(Queue q, map<int, bool> &visited)
    {
        if (q.isEmpty())
            return;
 
        int v = q.dequeue(); // remove first element
        cout << v << " ";    // print value
        for (int i : adj_list[v])
        // Iterate over all vertices adjacent to the vertex from the queue
        {
            if (!visited[i]) // if vertex is not visited
            {
                visited[i] = true; // set visited to 1
                q.enqueue(i);      // add to queue
            }
        }
        bfs_main(q, visited); // call BFS for the adjacent vertices added to the queue
    }
    void dfs(int start, map<int, bool> &visited)
    {
        visited[start] = true;
        cout << start << " ";
        for (int i : adj_list[start])
        {
            if (!visited[i])
                dfs(i, visited);
        }
    }
};
int main()
{
    int ch = 1;
    while (ch != 0)
    {
        cout << "\n\t\t\t-------------------------------------------------------------------";
        cout << "\n\t\t\t\t |1. Insert the edges in the graph"
                "\n\t\t\t\t |2. Exit";
        cout << "\n\t\t\t-------------------------------------------------------------------";
        cout << "\n\t\t\tEnter your choice:";
        cin >> ch;
        if (ch == 2)
        {
            cout << "Exiting";
            break;
        }
 
        else if (ch == 1)
        {
            int e, x, y;
            cout << "Enter number of edges: ";
            cin >> e;
            Graph g;
            for (int i = 0; i < e; i++)
            {
                cout << "Enter Edge " << i + 1 << " : ";
                cin >> x >> y;
                g.addEdge(x, y);
            }
            int sch = 1;
            while (sch != 0)
            {
                cout << "\n\t\t\t-------------------------------------------------------------------";
                cout << "\n\t\t\t\t |1. Show DFS traversal"
                        "\n\t\t\t\t |2. Show BFS Traversal"
                        "\n\t\t\t\t |3. Print Adjacency List"
                        "\n\t\t\t\t |4. Search for a vertex"
                        "\n\t\t\t\t |0. Exit";
                cout << "\n\t\t\t-------------------------------------------------------------------";
                cout << "\n\t\t\tEnter your choice:";
                cin >> sch;
 
                if (sch == 0)
                {
                    cout << "Exiting Graph Menu";
                    break;
                }
                else if (sch == 4)
                {
                    cout << "Enter vertex you want to search: ";
                    int temp;
                    cin >> temp;
                    g.search(temp);
                    cout << endl;
                }
 
                else if (sch == 1)
                {
                    cout << "Enter vertex to start the DFS traversal from: ";
                    int temp;
                    map<int, bool> visited;
                    cin >> temp;
                    g.dfs(temp, visited);
                    cout << endl;
                }
 
                else if (sch == 2)
                {
                    cout << "Enter vertex to start the BFS traversal from: ";
                    int temp;
                    cin >> temp;
                    g.bfs(temp);
                }
 
                else if (sch == 3)
                {
                    g.display();
                }
 
                else
                {
                    cout << "Invalid input";
                }
            }
        }
 
        else
        {
            cout << "Invalid input";
        }
    }
    return 0;
}
