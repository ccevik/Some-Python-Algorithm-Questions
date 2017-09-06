############### Question 1 ######################

# Check if s1 and s2 are anagram to each other
def anagram_check(s1, s2):
    # sorted returns a new list and compare
    return sorted(s1) == sorted(s2)

# Check if anagram of t is a substring of s
def question1(s, t):
    for i in range(len(s) - len(t) + 1):
        if anagram_check(s[i: i+len(t)], t):
            return True
    return False

def main():
    print question1("udacity", "city")

if __name__ == '__main__':
    main()  

'''
Test Case 1: question1("udacity", "city") -- True
Test Case 2: question1("udacity", "ud") -- True
Test Case 3: question1("udacity", "ljljl") -- False
'''


############### Question 2 ######################
def main():
    def next_substring(s):
        # Declare variable for the length of string
        string_length = len(s)


        for i in xrange(string_length, 0, -1):
            for j in xrange(string_length-i+1):
                yield s[j : j + i]

    def palindrome(s):
        '''
           From http://pythoncentral.io/how-to-slice-listsarrays-and-tuples-in-python/
           If there is no value before the first colon, 
           it means to start at the beginning index of the list. 
           If there isn't a value after the first colon, 
           it means to go all the way to the end of the list. 
           This saves us time so that we don't have to manually specify len(a) as the ending index.
           And that -1 means to increment the index every time by -1, 
           meaning it will traverse the list by going backwards. 
           If you wanted the even indexes going backwards, 
           you could skip every second element and set the iteration to -2.
        '''
        return s == s[::-1]

    def question2(a):
        for string_length in next_substring(a):
            if palindrome(string_length):
                return string_length

    print question2("abcba")                    

if __name__ == '__main__':
    main()                   

'''
Test Case 1: question("a")
Test Case 2: question2("aba")
Test Case 3: question2("abcba")
'''    

################ Question 3 ######################
#Utility function to find set of an element i
def find(self, parent, i):
    if parent[i] == i:
        return i
    return self.find(parent, parent[i])

# Union function of two sets of x and y
# using union by rank
def union(self, parent, rank, x, y):
    xroot = self.find(parent, x)
    yroot = self.find(parent, y)

    # Attach smaller rank tree under root of high rank tree
    # using union by rank
    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
        # If ranks are same, then make one as root and 
        # increment its rank by one
    else:
        parent[yroot] = xroot
        rank[xroot] += 1

# Main function to construct MST using Kruskal's algorithm
def KruskalMST(graph, V, inv_dict):
    
    result = [] # This will store the resultant MST

    i = 0 # An index variable for sorted edges
    e = 0 # An index variable for result[]

    # Step 1: Sort all the edges in non-decreasing order of theif
    # weight. If we are not allowed to change
    # the given graph, then we can create a copy of graph
    self.graph = sorted(self.graph, key = lambda item: item[2])
    # print self.graph

    parent = [] ; rank = []

    # Create V subsets with single elements
    for node in range(self.V):
        parent.append(node)
        rank.append(0)

    # Number of edges to be taken is equal to V-1
    while e < self.V - 1:

        # Step 2: Pick the smallest edge and increment the index
        # for next iteration
        u, v, w = self.graph[i]
        i = i + 1
        x = self.find(parent, u)
        y = self.find(parent, v)

        # If including this edge doesn't cause cycle,
        # include it in result and increment the 
        # index of result for next edge
        if x != y:
            e = e + 1
            result.append([u, v, w])
            self.union(parent, rank, x, y)
        # else discard the edge
    # Print the contents of result[] to display the built MST
    # print "Followint are the edges in the constructed MST"            
    
    tree = []
    final_result = {}
    for u, v, weight in result:
        tree = [(inv_dict[v], weight)]
        if inv_dict[u] not in final_result:
            tree = final_result[inv_dict[u]]
        else:
            final_result[inv_dict[u]] = final_result[inv_dict[u]].append(p1)

        #print str(u) + " -- " + str(v) + " == " + str(weight)
        #print ("%c -- %c == %d" % (inv_dict[u],inv_dict[v],weight)

    return final_result

def question3(G):
    n = len(G)
    tmp_dict = {}
    inv_dict = {}
    count = 0
    u, v, w = None, None, None
    graph = []
    for i in G:
        tmp_dict[i] = count
        inv_dict[count] = i
        count += 1
    # print tmp_dict    

    for i in G:
        for j in G[i]:
            # print tmp_dict[i], tmp_dict[j[0]], j[1]
            u, v, w = tmp_dict[i], tmp_dict[j[0]], j[1]
            graph.append([u, v, w])
        # print graph   
         
        return KruskalMST(graph, count, inv_dict)


# Main program
def main():
    G = {'A': [('B', 2)],
          'B': [('A', 4), ('C', 2)],
          'C': [('A', 2), ('B', 5)]}
                
    print question3(G)

if __name__ == '__main__':
    main()                    


################ Question 4 ######################
Class Node:
    #Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    # Function to find least common ancestor
    def question4(root, n1, n2):
        
        # Base case
        if root is None:
            return None

        # If both n1 and n2 are smaller than root,
        # then LCA lies on left
        if(root.data > n1 and root.data > n2):
            return question4(root.left, n1, n2)

        # if both n1 and n2 are greater than root,
        # then LCA lies on right
        if(root.data < n1 and root.data < n2):
            return lca(root.right, n1, n2) 
           
        return root


################ Question 5 ######################
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

    

def question5(ll, m):
    first_element = ll
    second_element = ll
    node_start = 0

    for i in range(0, m):
        if(first_element == None):
            return None
        first_element = first_element.next

    while(first_element != None):
        first_element = first_element.next
        second_element = second_element.next

    return second_element.data

A = Node(2)
B = Node(3)
C = Node(8)

A.next = B
B.next = C
print question5(A, 3)
