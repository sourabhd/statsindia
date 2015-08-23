from __future__ import print_function
import numpy as np
import shapefile
from bokeh.plotting import figure, show, output_file
import colorsys

districtShapefile = "../thirdparty/maps/Districts/Census_2011/2011_Dist.shp"
districtReader = shapefile.Reader(districtShapefile)
ptsX = []
ptsY = []
p = figure(title="Districts of India (disclaimer: not an official map)",
           toolbar_location="left",
           plot_width=1000, plot_height=1000)
districtCount = 0
for d in districtReader.shapeRecords():
    # print(d.record, d.shape.parts)
    # print(d.record, d.shape.parts, d.shape.points)
    dPtsX = []
    dPtsY = []
    n_parts = len(d.shape.parts)
    if n_parts == 0:
        pass
    elif n_parts == 1:
        # print('A: ', d.shape.parts, ' ', d.shape.points)
        L = np.array(d.shape.points)
        dPtsX = L[:, 0]
        dPtsY = L[:, 1]
    else:
        for i in range(n_parts-1):
            L = np.array(d.shape.points[d.shape.parts[i]:d.shape.parts[i+1]])
            dPtsX = L[:, 0]
            dPtsY = L[:, 1]
    print(d.record[0], ', ', d.record[1], ' : ', len(dPtsX))
    ptsX.append(dPtsX)
    ptsY.append(dPtsY)
    districtCount = districtCount + 1

#print(len(ptsX))
#print(len(ptsY))
#print(len(districtColors))

print("Total Districts: ", districtCount)

districtColors = []
districtHSV = np.random.rand(districtCount, 3)
for h in range(districtCount):
    r, g, b = colorsys.hsv_to_rgb(*districtHSV[h, :])
    hexColor = '#%02x%02x%02x' % (max(int(round(256.0 * r - 1)), 0),
                                  max(int(round(256.0 * g - 1)), 0),
                                  max(int(round(256.0 * b - 1)), 0))
    # print(hexColor)
    districtColors.append(hexColor)

p.patches(ptsX, ptsY,
          fill_color=districtColors, fill_alpha=1.0,
          line_color="black", line_width=2)

output_file("india_map.html", title="Districts of India")
show(p)
