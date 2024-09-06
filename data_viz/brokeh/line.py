import numpy as np
from bokeh.plotting import figure,show

x=np.arange(0,10,1)
y=x**2
y1=x**3
y2=x**4

p=figure(title="simple line Charts",x_axis_label="x",y_axis_label="y")

p.line(x,y,legend_label="quadratic finction",line_width=2,color="red")
p.line(x,y1,legend_label="cubic finction",line_width=2,color="green")
p.line(x,y2,legend_label="Quartic finction",line_width=2,color="blue")
show(p)