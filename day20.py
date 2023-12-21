##### Day 20 #####
def process_q(notable_set = []):
    global low_to_rx
    s, r, sig = q.pop(0) # send, receive
    sigs[sig] += 1
    if s in notable_set and sig == 1:
        cycles.append(i)
    if r != 'rx':
    # if r != 'output':
        if inst[r][0] == '%':
            if sig == 0:
                last_ins[r] = 1 - last_ins[r]
                q.extend([[r, out, last_ins[r]] for out in inst[r][1]])
        else: # '&'
            last_ins[r][s] = sig
            out_sig = 1-all([v for v in last_ins[r].values()])
            q.extend([[r, out, out_sig] for out in inst[r][1]])

txt = open('day20.txt','r').read().strip().split('\n')
inst = {y[0][1:]:[y[0][0], y[1].split(', ')] for y in [x.split(' -> ') for x in txt]}
cycles = []
last_ins = {k:0 if v[0] == '%' else {k2:0 for k2,v2 in inst.items() if k in v2[1]} for k,v in inst.items() if v[0]!='b'}
sigs = [0,0]
for i in range(1000):
    sigs[0] += 1
    q = [['broadcaster',x,0] for x in inst['roadcaster'][1]]
    while q:
        process_q([])


##### b
# Visualize network
import networkx as nx
import matplotlib.pyplot as plt
G = nx.DiGraph()
txt = open('day20.txt','r').read().strip().split('\n')
inst = {y[0][1:]:[y[0][0], y[1].split(', ')] for y in [x.split(' -> ') for x in txt]}
inst['0'] = inst['roadcaster']
del inst['roadcaster']
t_dict = {k:v[0]+k for k,v in inst.items()}
t_dict['rx'] = ''
for k,v in inst.items():
    G.add_edges_from([[t_dict[k], t_dict[x]] for x in v[1]])

nx.draw(G, with_labels=True)
plt.show()

inst = {y[0][1:]:[y[0][0], y[1].split(', ')] for y in [x.split(' -> ') for x in txt]}
cycles = []
last_ins = {k:0 if v[0] == '%' else {k2:0 for k2,v2 in inst.items() if k in v2[1]} for k,v in inst.items() if v[0]!='b'}
# sigs = [0,0]
for i in range(1,20000):
    if i % 100000 == 0:
        print('runtime: ' + str(i))
    # sigs[0] += 1
    q = [['broadcaster',x,0] for x in inst['roadcaster'][1]]
    while q:
        # process_q(['rk','zf','cd','qx'])
        process_q(['qx'])

# Then find LCM of 3733 3947 3793 4057
