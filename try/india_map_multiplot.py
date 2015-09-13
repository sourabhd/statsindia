from __future__ import print_function
import numpy as np
import shapefile
from bokeh.io import gridplot
from bokeh.plotting import figure, show, output_file
# import colorsys

districtShapefile = "../thirdparty/maps/Districts/Census_2011/2011_Dist.shp"
numPlots = 4

districtReader = shapefile.Reader(districtShapefile)
ptsX = []
ptsY = []
districtCount = 0
districtNames = []
for d in districtReader.shapeRecords():
    # print(d.record, d.shape.parts)
    # print(d.record, d.shape.parts, d.shape.points)
    dPtsX = []
    dPtsY = []
    n_parts = len(d.shape.parts)
    if n_parts == 0:
        pass
    elif n_parts == 1:
        # print('A: ', d.shape.parts, ' ', d.shape.pointsts)
        L = np.array(d.shape.points)
        dPtsX = L[:, 0]
        dPtsY = L[:, 1]
    else:
        for i in range(n_parts-1):
            L = np.array(d.shape.points[d.shape.parts[i]:d.shape.parts[i+1]])
            dPtsX = L[:, 0]
            dPtsY = L[:, 1]
    print(d.record[0], ', ', d.record[1], ' : ', len(dPtsX))
    districtNames.append((d.record[0], d.record[1]))
    ptsX.append(dPtsX)
    ptsY.append(dPtsY)
    districtCount = districtCount + 1

#print(len(ptsX))
#print(len(ptsY))
#print(len(districtColors))

print("Total Districts: ", districtCount)

# districtColors = []
# districtHSV = np.random.rand(districtCount, 3)
# for h in range(districtCount):
#     r, g, b = colorsys.hsv_to_rgb(*districtHSV[h, :])
#     hexColor = '#%02x%02x%02x' % (max(int(round(256.0 * r - 1)), 0),
#                                   max(int(round(256.0 * g - 1)), 0),
#                                   max(int(round(256.0 * b - 1)), 0))
#     # print(hexColor)
#     districtColors.append(hexColor)

N = int(districtCount / 2)
districtR1 = 0.05 * np.random.rand(N)
districtR2 = 0.8 + 0.2 * np.random.rand(N)
districtR = []
districtR.extend(districtR1)
districtR.extend(districtR2)
districtR.extend([0.65])
print(len(districtR))

dR = []
districtColors = []
for i in range(numPlots):
    dR.append([])
    districtColors.append([])

for h in range(districtCount):
    if districtNames[h][1] == 'Rajasthan':
        print(districtNames[h][0])
        for i in range(numPlots):
            dR[i].append(min(0.25 * i + districtR[h], 1.0))
            print(0.25 * i + districtR[h])
    else:
        for i in range(numPlots):
            dR[i].append(districtR[h])

print(len(dR[0]))

for i in range(numPlots):
    for h in range(districtCount):
        hexColor = '#%02x%02x%02x' % (max(int(round(256.0 * dR[i][h] - 1)), 0),
                                      0,
                                      0)
        # print(hexColor)
        districtColors[i].append(hexColor)

print(len(districtColors[0]))

p = [None] * numPlots

for i in range(numPlots):
    p[i] = figure(title="%d" % (1981 + 10 * i),
                  toolbar_location="left",
                  plot_width=500, plot_height=500)
    p[i].patches(ptsX, ptsY,
                 fill_color=districtColors[i], fill_alpha=1.0,
                 line_color="black", line_width=2)

output_file("india_map_mp.html", title="Districts of India")

g = gridplot([[p[0], p[1]], [p[2], p[3]]])
show(g)
