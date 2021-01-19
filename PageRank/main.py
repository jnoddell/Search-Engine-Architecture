# def pagerank( G ):
# params    G *** a dict of pages and their respective links
# returns   a dict of pages and their respective pagerank values
#
# This purpose of this function is to execute the PageRank function
def pagerank( G ):

    P = G.keys()        # pages
    L = G.values()      # links
    I = dict()          # current PageRank estimate -- k:page, v:PageRank estimate
    R = dict()          # better, resulting PageRank estimate -- k:page, v:PageRank estimate
    LAMBDA = 0.20       # Chance of 'surprise me' button [go to random page]
    TAU = 0.02          # Threshold of convergence
    
    # Start each page to be equally likely, initialize R with values
    for p in P:
        I[p] = 1 / len(P)
        R[p] = 0

    converged = False
    while not converged:
        converged = True
        # Each page has a LAMBDA/len(P) chance of random selection
        for r in R:
            R[r] = LAMBDA / len(P)
        for p in P:
            Q = []          # the set of pages that such that (p, q) belong to L and q belongs to P
            # Populate Q
            for q in G[p]:
                if q in P and len(G[q]) > 0:
                    Q.append( q )

            if len(Q) > 0:
                for q in Q:
                    delta = (1 - LAMBDA) * I[p] / len(Q)            # Probability of of I[p] being at page p
                    R[q] += delta
            else:
                for q in P:
                    delta = (1 - LAMBDA) * I[p] / len(P)
                    R[q] += delta

        # check for convergence
        if abs(R[p] - I[p]) > TAU:
            converged = False

        # Update PageRank estimate
        for r in R:
            I[r] = R[r]
        
    return R

# def create_graph( src ):
# params:   src *** path to file detailing pages and links
# returns   a dict of pages and their respective links
#
# The purpose of this function is to take a text file as input, detailing pages and links, store and return that data
def create_graph( src ):

    G = dict()
    in_file = open( src, "r" )
    # Iterate through file
    for line in in_file:
        page = ""
        link = ""
        tab_reached = False
        for letter in line:
            if ord(letter) == 9 or ord(letter) == 32:
                tab_reached = True
            elif not tab_reached:
                page = page + letter
            elif tab_reached and letter not in "\n":
                link = link + letter
        # add k, v to dict
        if page in G.keys():
            G[page].append(link)
        else:
            G[page] = [link]
        # check if v exists as k
        if link not in G.keys():
            G[link] = []
    # close file
    in_file.close()

    return G

# def main():
# params    none
# does not return
#
# execute the program
def main():

    G = create_graph( "connections.txt" )

    R = pagerank( G )

    print( R )

    return 0

# call main 
main()
