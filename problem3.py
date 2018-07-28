import snap

#Load the stack overflow grap
G1 = snap.LoadEdgeList(snap.PNGraph, "stackoverflow-Java.txt", 0, 1)

#1. Get the list of all weakly connected components
Components = snap.TCnComV()
snap.GetWccs(G1, Components)
wccCount = 0
for Cc in Components:
    wccCount = wccCount + 1

print "1. Number of Weakly Connected Components: ", wccCount


#2. Get The number of edges and the number 
#   of nodes in the largest weakly connected component
maxWcc = snap.GetMxWcc(G1)
EdgeCount = 0
NodeCount = 0
for E in maxWcc.Edges():
    EdgeCount = EdgeCount + 1

for N in maxWcc.Nodes(): 
    NodeCount = NodeCount + 1

print "2. Number of edges and nodes in largest wcc"
print "EdgeCount : ", EdgeCount
print "NodeCount : ", NodeCount

#3 Get The top 3 most central nodes in the network by PagePank scores
PRankH = snap.TIntFltH()
snap.GetPageRank(G1, PRankH)
count = 0

#sort the rank hash by data in descending order
PRankH.SortByDat(False)
iter = PRankH.BegI()
print "3. The top 3 most central nodes in the network by PagePank scores"
while (count < 3):
    print (iter.GetKey(), iter.GetDat())
    iter = iter.Next()
    count += 1
    


#4 The top 3 hubs and top 3 authorities in the network by HITS scores
NIdHubH = snap.TIntFltH()
NIdAuthH = snap.TIntFltH()
snap.GetHits(G1, NIdHubH, NIdAuthH)

print "4. The top 3 hubs and top 3 authorities in the network by HITS scores"
count = 0

#sort in decending order
NIdHubH.SortByDat(False)
iter = NIdHubH.BegI()
while (count < 3):
    print 'hub :' ,  iter.GetKey(), iter.GetDat()
    iter = iter.Next()
    count += 1

count = 0
#sort in decending order
NIdAuthH.SortByDat(False)
iter = NIdAuthH.BegI()
while (count < 3):
    print 'authority :' ,  iter.GetKey(), iter.GetDat()
    iter = iter.Next()
    count += 1
    
