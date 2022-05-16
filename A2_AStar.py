class Node():
    """A node class for A* Pathfinding"""

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        # f is the total cost of the node.
        # g is the distance between the current node and the start node.
        # h is the heuristic — estimated distance from the current node to the end node.
        self.g = 0
        self.h = 0
        self.f = 0  # f = g+h
        # With A*,we see that once we get past the obstacle, the algorithm
        # prioritizes the node with the lowest f and the ‘best’ chance of reaching the end.

    def __eq__(self, other):
        return self.position == other.position


def astar(maze, start, end):
    """Returns a list of tuples as a path from the given start to the given end in the given maze"""

    # Create start and end node
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    # Initialize both open and closed list
    open_list = []
    # in this list we will put all node that are yet to be visited for exploration.
    # From here we will find the lowest cost node to expand next

    closed_list = []
    # in this list we will put all node those already explored so that we don't explore it again

    # Add the start node
    open_list.append(start_node)

    # Adding a stop condition. This is to avoid any infinite loop and stop
    # execution after some reasonable number of steps
    # outer_iterations = 0
    # max_iterations = (len(maze) // 2) ** 10
    # Loop until you find the end
    while len(open_list) > 0:

        # Get the current node
        # Every time any node is referred from yet_to_visit list, counter of limit operation incremented
        # outer_iterations += 1
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            # if the item in open list is better than the item at index 0
            if item.f < current_node.f:
                current_node = item
                current_index = index

        # if we hit this point return the path such as it may be no solution or
        # computation cost is too high
        # if outer_iterations > max_iterations:
        #     print("Giving up on pathfinding as there are too many iterations")
        #     break

        # Pop current off open list, add to closed list, that means the current node is visited.
        open_list.pop(current_index)
        closed_list.append(current_node)

        # test if goal is reached or not, if yes then return the path
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:  # while current doesn't have parent
                path.append(current.position)  # position: coordinate of the node
                current = current.parent
            return path[::-1]  # Return reversed path

        # Generate children
        children = []
        # Adjacent squares
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]:

            # Get node position
            node_position = (
                current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Make sure within range
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (
                    len(maze[len(maze) - 1]) - 1) or node_position[1] < 0:
                continue

            # Make sure walkable terrain
            if maze[node_position[0]][node_position[1]] != 0:
                continue

            # Create new node
            new_node = Node(current_node, node_position)

            # Append
            children.append(new_node)

        # Loop through children
        for child in children:

            # Child is on the closed list
            for closed_child in closed_list:
                if child == closed_child:
                    continue

            # Create the f, g, and h values
            child.g = current_node.g + 1
            child.h = ((child.position[0] - end_node.position[0]) **
                       2) + ((child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h

            # Child is already in the open list
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue

            # Add the child to the open list
            open_list.append(child)


def main():
    maze = []
    r = int(input("Enter the number of rows in the maze matrix: "))
    c = int(input("Enter the number of columns in the maze matrix: "))

    # for i in range(0, r):
    #     number_list = list(
    #         map(int, input("\nEnter row : ").strip().split()))[:c]
    #
    #     maze.append(number_list)
    #


    # maze
    list1 = []
    for i in range(0, r):
        l = []
        for i in range(0, c):
            input1 = int(input("Enter a value: "))
            l.append(input1)
        list1.append(l)

    maze = list1

    for i in range(len(maze)):
        print(maze[i])

    xStart = int(input("Enter x coordinate: "))
    yStart = int(input("Enter y coordinate: "))
    l = [xStart, yStart]
    start = tuple(l)

    print(l)

    xEnd = int(input("Enter x coordinate: "))
    yEnd = int(input("Enter y coordinate: "))
    l1 = [xEnd, yEnd]
    end = tuple(l1)

    print(l1)




    # start_list = list(
    #     map(int, input("\nEnter start coordinate : ").strip().split()))[:2]
    # start = tuple(start_list)
    #
    # end_list = list(
    #     map(int, input("\nEnter end coordinate : ").strip().split()))[:2]
    # end = tuple(end_list)

    path = astar(maze, start, end)
    for i in range(len(path)):
        print(path[i])
        print("\n")


if __name__ == '__main__':
    main()

