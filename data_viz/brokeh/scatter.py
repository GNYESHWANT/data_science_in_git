import numpy as np
from bokeh.plotting import figure,show

x=np.random.random(50)*10
y=np.random.random(50)*200

p=figure(title="Scattter plot",x_axis_label="x",y_axis_label="y")

#p.scatter(x,y,legend_label="Random points",color="yellow",size=20)
p.width=1200
p.height=720
circle=p.circle(x,y,legend_label="Random points",color="yellow",size=20)
glyph=circle.glyph
glyph.size=200
glyph.fill_color="red"
show(p)