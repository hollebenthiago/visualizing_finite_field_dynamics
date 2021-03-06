

# This file was *autogenerated* from the file test.sage
from sage.all_cmdline import *   # import sage library

_sage_const_1000 = Integer(1000); _sage_const_1 = Integer(1); _sage_const_0 = Integer(0); _sage_const_10 = Integer(10)
def graphField(K): ##this function returns a graph of elements of K
    n = order(K)
    l = [x for x in K]
    G = DiGraph(loops=True)
    T = [str(x) for x in l]
    G.add_vertices(T)
    return G

def plotGraph(G,vertexsize=_sage_const_1000 ,vertexcolor='lightgreen',lay='circular'): 
    return G.plot(vertex_size=vertexsize, layout=lay,vertex_color=vertexcolor)

def rightEdges(G): ##this will give us the cycles and transient elements
    l = []
    for edge in G.edges():
        if (edge[_sage_const_1 ],edge[_sage_const_0 ],None) not in G.edges():
            l.append(edge)
    return l

def dynamics(K,f,c): ##this function returns the information we want
    G = graphField(K)
    edges = []
    z0 = c
    znext = f(z0)
    G.add_edge(str(z0),str(znext))
    while (str(f(z0)),str(f(znext)),None) not in G.edges():
        z0 = znext
        znext = f(znext)
        G.add_edge(str(z0),str(znext))
    return G

def makeimages(K, f, c, figuresize = (_sage_const_10 ,_sage_const_10 ), vertexsize = _sage_const_1000 , vertexcolor = 'lightgreen', lay = 'circular', colorcicles = 'red', initial = 'blue'):
    ciclos = dynamics(K, f, c).all_simple_cycles()[_sage_const_0 ]
    ciclos = list(set(ciclos))
    ims = []
    G = graphField(K)
    #G.set_pos(Q.get_pos())
    ims.append(G.plot(figsize = figuresize, layout = lay ,vertex_size=vertexsize,vertex_color = vertexcolor))
    for edge in rightEdges(dynamics(K,f,c)):
        G.add_edge(edge)
        ims.append(G.plot(figsize = figuresize, layout = lay,vertex_size = vertexsize, vertex_color = vertexcolor))
    G.remove_loops()
    ims[-_sage_const_1 ] = G.plot(figsize = figuresize, layout = lay, vertex_size=vertexsize,
                     vertex_color = vertexcolor,vertex_colors = {colorcicles : ciclos, initial :[str(c)]})
    return ims

def p(l): ##in case we want to define a polynomial based on its coefficients
    def P(x):
        return sum([l[i]*x**i for i in range(len(l))])
    return P

