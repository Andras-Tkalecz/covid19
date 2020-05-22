import matplotlib.pyplot as plt
import numpy as np


groups = ["0-9","10-19","20-29","30-39","40-49","50-59","60-69","70-79","80-89","90+"]

#demo_sweden = [ 601	   593	   586	   541	   544	   733	   693	   627	   609	   655	   679	   617	   567	   527	   564	   430	   270	   162	   77	   21	   2]

pop_sweden = 10_327_600
pop_germany = 83_042_200

sweden = [1,0,9,13,33,110,253,783,1453,873]
germany = [1,2,8,19,54,257,702,1737,3490,1448]

rat_sw = [d/pop_sweden*1e5 for d in sweden]
rat_de = [d/pop_germany*1e5 for d in germany]

labels = groups

x = np.arange(len(groups))
width = 0.35

fig, ax  = plt.subplots()
rects_sw = ax.bar(x - width/2, rat_sw, width, label="Sweden")
rects_de = ax.bar(x + width/2, rat_de, width, label="Germany")

ax.set_ylabel('Deaths per 100k')
ax.set_title('Age group')
ax.set_xticks(x)
ax.set_xticklabels(groups)
ax.legend()