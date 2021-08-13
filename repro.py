from dro import OnlineDRO
import numpy as np
import collections as col
import math
from data import gen_arrays



def eval_ci(data, tau):
    ci = OnlineDRO.OnlineCressieReadLB(alpha=0.05, tau=tau)
    w =[]

    for i in range(len(data)):
        e = data[i]
        #format is [w,r,lb]
        ci.update(c=1, w=e[0], r=e[1])
        ci.recomputeduals()
        lb = ci.duals[0][0]
        w.append(e[0])
        print(f'[{i}] w:{e[0]} r:{e[1]} log:{e[2]} lb:{lb} delta:{lb - e[2]} avg-w:{sum(w)/len(w)}')
        # if i > 5:
            # break


x = gen_arrays()
eval_ci(x[0], 0.9999)

