import numpy as np
from bokeh.layouts import row
from bokeh.plotting import show,figure
x=np.arange(0,6,0.1)
x1=np.random.random(50)*10
y1=np.random.random(50)*200
y=x**2
y1=x**3


p1=figure()
p1.line(x,y)
p2=figure()
p2.scatter(x1,y1)
p3=figure()
p3.vbar(x=x,top=y,width=0.5,bottom=0,color="aqua")
p4=figure()
p4.circle(x,y)
show(row(children=[p1,p2],sizing_mode="scale_width"))
