#Exercise 8.8 from "Grokking Algorithms"; I solved it in my own way
#Task: Color USA map so that no two adjacent states are painted using same color.


from enum import Enum, unique

@unique  #wants name to unique value mapping in case we somehow have two names
#mapped to one value
class Colors(Enum):
    RED, GREEN, BLUE, ORANGE, YELLOW, PINK, VIOLET, GREY, BLACK, WHITE = range(1,11)

    
def color_from_enum_to_set():
        global Colors
        color_as_set = set() #use this notation for empty set
        for color in Colors.__members__.keys(): 
           color_as_set |= {color}

        return set(sorted(color_as_set))
        
def color_map(states_copy):
    global visited, node_color # states #original state

    remaining_node = len(states)
    while True:
        unvisited_node = len([x for x in visited.values() if x == False])
        if unvisited_node == 0:
           print("All cities are colored")
           break
        #list comprehension
        best_node = None
        len_best_node = 0

        #using both lambda and list comprehension
        #so copy of states and removing the visited item from it is no longer necessary

        #http://stackoverflow.com/questions/16569502/get-the-key-correspond-to-maxvalue-in-python-dict
        #http://stackoverflow.com/questions/18296755/python-max-function-using-key-and-lambda-expression
        
        best_node = max([x for x in states_copy.keys() if visited[x]==False], key = lambda x:  len(states_copy[x]))
                         #temp list consisting of all states which are not visited, passing that to function and returning
                         #len
                         #finally for all of these len returing key x ; where state[x] or value (here the length) is maximum  

        if best_node != None:
           #probable_colors = colors_not_in_use(best_node) 
           visited[best_node] = True
           if node_color[best_node] == None:
              try:
                  node_color[best_node] =  colors_not_in_use(best_node).pop() #set is immutable; so this
                  #manipulation would affect only local copy
              except KeyError:
                  print("Not enough color")
                  exit()


def colors_not_in_use(best_node):
    global color_as_set
    colors_in_use = set()
    global states
    print(states)
 
    if node_color[best_node] != None:
        colors_in_use  |= {node_color[best_node]} #use this notation when we are wrapping a set element in it.
        #Because using set(elem) causes problem - it splits the string in element as separate characters and make
        #a set out of those characters.

    print("best_node ", best_node)

    for state in states[best_node]:
        
        if node_color[state] != None:
           colors_in_use |= {node_color[state]}

    print(colors_in_use)
    print("remaining color", color_as_set - colors_in_use)
    return  color_as_set - colors_in_use 




if __name__ == "__main__" :

    states = {}
    states[1] = set([2,3,4])
    states[2] = set([1,3,5])
    states[3] = set([1,2,4,5])
    states[4] = set([1,3,5,6])
    states[5] = set([2, 3, 4, 6])
    states[6] = set([4,5])

    visited = {}
    node_color = {}

    for i in states.keys():
        visited[i] = False
        node_color[i] = None


    color_as_set = color_from_enum_to_set()
    #print(color_as_set)
    #print(colors_not_in_use(3).pop())
    #color_map(states_copy)
    color_map(states)
    print(node_color)

