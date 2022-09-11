def digest_data(data):
    # digest data
    pass












class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.up = None
        self.down = None
        self.left = None
        self.right = None
        
    def __repr__(self):
        rep = [self.x,self.y]
        if self.up != None:
            rep.append("up")
        if self.down != None:
            rep.append("down")
        if self.left != None:
            rep.append("left")
        if self.right != None:
            rep.append("right")
        return str(rep)

class Graph:
    def __init__(self, info):
        self.start = None
        self.info = info
        self.nodes = []
    
    # def put
# nlist = [node,...]
def nodelist(n):
    nlist = [Node(i,j) for i in range(n) for j in range(n)]
    return nlist

# jsondata = dict{"edges":dict{"positionPosition": 1/0}, 'end':"position"}
def connect_node(n,nlist,jsondata):
    for node in nlist:
        x,y = node.x,node.y
        if jsondata["edges"]["E[V_"+str(x)+'_'+str(y)+"][V_"+str(x+1)+'_'+str(y)+']'] == 0:
            node.up = nlist[n*x+y-1]
        if jsondata["edges"]["E[V_"+str(x)+'_'+str(y)+"][V_"+str(x)+'_'+str(y+1)+']'] == 0:
            node.left = nlist[n*(x-1)+y]
        if jsondata["edges"]["E[V_"+str(x)+'_'+str(y+1)+"][V_"+str(x+1)+'_'+str(y+1)+']'] == 0:
            node.down = nlist[n*x+y+1]
        if jsondata["edges"]["E[V_"+str(x+1)+'_'+str(y)+"][V_"+str(x+1)+'_'+str(y+1)+']'] == 0:
            node.right = nlist[n*(x+1)+y]
