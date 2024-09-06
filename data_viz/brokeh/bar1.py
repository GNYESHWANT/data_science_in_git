import numpy as np
from bokeh.plotting import figure,show

x=np.random.random(50)*10
y=np.random.random(50)*200

p=figure(title="simple bar Charts",x_axis_label="x",y_axis_label="y")
p.vbar(x=x,top=y,width=0.5,bottom=0,color="aqua")
show(p)
