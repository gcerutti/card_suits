import os
import argparse

import numpy as np

import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patch
import matplotlib.font_manager as fm

from imageio import imread

from PyPDF2 import PdfFileMerger

parser = argparse.ArgumentParser()
parser.add_argument('-c', '--suit-colors', default='rainbow', help='Color scheme for the suits',choices=['rainbow', 'red_black'])
args = parser.parse_args()

save_cards = True

vertices = {}
codes = {}
colors = {}

vertices['pique'] = [
    (-0.15,-0.5),
    (0.15,-0.5),
    (0.01, -0.2), (0., -0.1),
    (0., -0.4), (0.5, -0.4), (0.5, -0.1),
    (0.5, 0.1), (0.2, 0.2), (0., 0.5),
    (-0.2, 0.2), (-0.5, 0.1),(-0.5, -0.1),
    (-0.5, -0.4), (0, -0.4), (0, -0.1),
    (-0.01, -0.2), (-0.15, -0.5),
    (0., 0.),
]

codes['pique'] = [
    Path.MOVETO,
    Path.LINETO,
    Path.CURVE3, Path.CURVE3,
    Path.CURVE4, Path.CURVE4, Path.CURVE4,
    Path.CURVE4, Path.CURVE4, Path.CURVE4,
    Path.CURVE4, Path.CURVE4, Path.CURVE4,
    Path.CURVE4, Path.CURVE4, Path.CURVE4,
    Path.CURVE3, Path.CURVE3,
    Path.CLOSEPOLY,
]

vertices['coeur'] = [
    (0., -0.5),
    (-0.2, -0.2),(-0.5, -0.1),(-0.5, 0.25),
    (-0.5, 0.4), (-0.35, 0.5), (-0.25, 0.5),
    (-0.25, 0.5), (0, 0.5), (0, 0.25),
    (0., 0.5), (0.25, 0.5), (0.25, 0.5),
    (0.4, 0.5), (0.5, 0.35), (0.5, 0.25),
    (0.5, -0.1),(0.2, -0.2),(0., -0.5),
    (0., 0.),
]

codes['coeur'] = [
    Path.MOVETO,
    Path.CURVE4, Path.CURVE4, Path.CURVE4,
    Path.CURVE4, Path.CURVE4, Path.CURVE4,
    Path.CURVE4, Path.CURVE4, Path.CURVE4,
    Path.CURVE4, Path.CURVE4, Path.CURVE4,
    Path.CURVE4, Path.CURVE4, Path.CURVE4,
    Path.CURVE4, Path.CURVE4, Path.CURVE4,
    Path.CLOSEPOLY,
]

vertices['carreau'] = [
    (-0.5, 0.),
    (-0.2, 0.2), (0., 0.5),
    (0.2, 0.2), (0.5, 0.),
    (0.2, -0.2), (0., -0.5),
    (-0.2, -0.2), (-0.5, 0.),
    (0., 0.),
]


codes['carreau'] = [
    Path.MOVETO,
    Path.CURVE3, Path.CURVE3,
    Path.CURVE3, Path.CURVE3,
    Path.CURVE3, Path.CURVE3,
    Path.CURVE3, Path.CURVE3,
    Path.CLOSEPOLY,
]


#
# vertices['coupe'] = [
#     (-0.25, -0.5),
#     (0.25, -0.5),
#     (0.25, -0.4),
#     (0.1, -0.4), (0.05, -0.3), (0.05, -0.2),
#     (0.05, 0.1), (0.5, 0.1), (0.5,0.5),
#     (0, 0.4), (-0.5,0.5),
#     (-0.5, 0.1), (-0.05, 0.1), (-0.05, -0.2),
#     (-0.05, -0.3), (-0.1, -0.4), (-0.25, -0.4),
#     (-0.25, -0.5),
#     (0., 0.)
# ]
#
# codes['coupe'] = [
#     Path.MOVETO,
#     Path.LINETO,
#     Path.LINETO,
#     Path.CURVE4, Path.CURVE4, Path.CURVE4,
#     Path.CURVE4, Path.CURVE4, Path.CURVE4,
#     Path.CURVE3, Path.CURVE3,
#     Path.CURVE4, Path.CURVE4, Path.CURVE4,
#     Path.CURVE4, Path.CURVE4, Path.CURVE4,
#     Path.LINETO,
#     Path.CLOSEPOLY
# ]
#
# vertices['coupe'] = [
#     (-0.15, -0.5),
#     (0.15, -0.5),
#     (0.1, -0.4), (0.05, -0.3), (0.05, -0.2),
#     (0.05, 0.1), (0.45, 0.2), (0.45,0.5),
#     (0, 0.4), (-0.45, 0.5),
#     (-0.45, 0.2), (-0.05, 0.1), (-0.05, -0.2),
#     (-0.05, -0.3), (-0.1, -0.4), (-0.15, -0.5),
#     (0., 0.)
# ]
#
# codes['coupe'] = [
#     Path.MOVETO,
#     Path.LINETO,
#     Path.CURVE4, Path.CURVE4, Path.CURVE4,
#     Path.CURVE4, Path.CURVE4, Path.CURVE4,
#     Path.CURVE3, Path.CURVE3,
#     Path.CURVE4, Path.CURVE4, Path.CURVE4,
#     Path.CURVE4, Path.CURVE4, Path.CURVE4,
#     Path.CLOSEPOLY
# ]

# vertices['coupe'] = [
#     (-0.15, -0.5),
#     (0.15, -0.5),
#     (0.1, -0.4), (0.05, -0.3), (0.05, -0.2),
#     (0.05, 0.1), (0.5, 0.), (0.5, 0.3),
#     (0.5, 0.4), (0.4, 0.5), (0.3, 0.5),
#     (0, 0.4), (-0.3, 0.5),
#     (-0.4, 0.5), (-0.5, 0.4), (-0.5, 0.3),
#     (-0.5, 0.), (-0.05, 0.1), (-0.05, -0.2),
#     (-0.05, -0.3), (-0.1, -0.4), (-0.15, -0.5),
#     (0., 0.)
# ]
#
# codes['coupe'] = [
#     Path.MOVETO,
#     Path.LINETO,
#     Path.CURVE4, Path.CURVE4, Path.CURVE4,
#     Path.CURVE4, Path.CURVE4, Path.CURVE4,
#     Path.CURVE4, Path.CURVE4, Path.CURVE4,
#     Path.CURVE3, Path.CURVE3,
#     Path.CURVE4, Path.CURVE4, Path.CURVE4,
#     Path.CURVE4, Path.CURVE4, Path.CURVE4,
#     Path.CURVE4, Path.CURVE4, Path.CURVE4,
#     Path.CLOSEPOLY
# ]

vertices['coupe'] = [
    (-0.15, -0.5),
    (0.15, -0.5),
    (0.1, -0.4), (0.05, -0.3), (0.05, -0.25),
    (0.05, -0.05), (0.5, 0.1), (0.5, 0.3),
    (0.5, 0.4), (0.4, 0.5), (0.3, 0.5),
    (0, 0.4), (-0.3, 0.5),
    (-0.4, 0.5), (-0.5, 0.4), (-0.5, 0.3),
    (-0.5, 0.1), (-0.05, -0.05), (-0.05, -0.25),
    (-0.05, -0.3), (-0.1, -0.4), (-0.15, -0.5),
    (0., 0.)
]

codes['coupe'] = [
    Path.MOVETO,
    Path.LINETO,
    Path.CURVE4, Path.CURVE4, Path.CURVE4,
    Path.CURVE4, Path.CURVE4, Path.CURVE4,
    Path.CURVE4, Path.CURVE4, Path.CURVE4,
    Path.CURVE3, Path.CURVE3,
    Path.CURVE4, Path.CURVE4, Path.CURVE4,
    Path.CURVE4, Path.CURVE4, Path.CURVE4,
    Path.CURVE4, Path.CURVE4, Path.CURVE4,
    Path.CLOSEPOLY
]

# vertices['or'] = [
#     (0., 0.5),
#     (0.25, 0.5), (0.5, 0.25), (0.5, 0.),
#     (0.5, -0.25), (0.25, -0.5), (0., -0.5),
#     (-0.25, -0.5), (-0.5, -0.25), (-0.5, 0),
#     (-0.5, 0.25), (-0.25, 0.5), (0., 0.5),
#     (0., 0.),
# ]
#
#
# codes['or'] = [
#     Path.MOVETO,
#     Path.CURVE4, Path.CURVE4, Path.CURVE4,
#     Path.CURVE4, Path.CURVE4, Path.CURVE4,
#     Path.CURVE4, Path.CURVE4, Path.CURVE4,
#     Path.CURVE4, Path.CURVE4, Path.CURVE4,
#     Path.CLOSEPOLY,
# ]


# vertices['gland'] = [
#     (0., 0.5),
#     (-0.2, 0.2), (-0.3, 0.3), (-0.3, 0.1),
#     (-0.3, -0.1),
#     (-0.4, -0.1), (-0.5, -0.2), (-0.5, -0.3),
#     (-0.5, -0.4), (-0.4, -0.5), (-0.3, -0.5),
#     (0, -0.4), (0.3, -0.5),
#     (0.4, -0.5), (0.5, -0.4), (0.5, -0.3),
#     (0.5, -0.2), (0.4, -0.1), (0.3, -0.1),
#     (0.3, 0.1),
#     (0.3, 0.3), (0.2, 0.2), (0., 0.5),
#     (0., 0.)
# ]

vertices['gland'] = [
    (0., 0.5),
    (-0.2, 0.2), (-0.3, 0.35), (-0.3, 0.1),
    (-0.3, -0.1),
    (-0.4, -0.1), (-0.5, -0.2), (-0.5, -0.3),
    (-0.5, -0.4), (-0.4, -0.5), (-0.3, -0.5),
    (0, -0.4), (0.3, -0.5),
    (0.4, -0.5), (0.5, -0.4), (0.5, -0.3),
    (0.5, -0.2), (0.4, -0.1), (0.3, -0.1),
    (0.3, 0.1),
    (0.3, 0.35), (0.2, 0.2), (0., 0.5),
    (0., 0.)
]

codes['gland'] = [
    Path.MOVETO,
    Path.CURVE4, Path.CURVE4, Path.CURVE4,
    Path.LINETO,
    Path.CURVE4, Path.CURVE4, Path.CURVE4,
    Path.CURVE4, Path.CURVE4, Path.CURVE4,
    Path.CURVE3, Path.CURVE3,
    Path.CURVE4, Path.CURVE4, Path.CURVE4,
    Path.CURVE4, Path.CURVE4, Path.CURVE4,
    Path.LINETO,
    Path.CURVE4, Path.CURVE4, Path.CURVE4,
    Path.CLOSEPOLY,
]


vertices['ecu'] = [
    (0., 0.5),
    (-0.2, 0.2), (-0.4, 0.3),
    (-0.4, 0.),
    (-0.4, -0.3), (-0.2, -0.2), (0., -0.5),
    (0.2, -0.2), (0.4, -0.3), (0.4, 0.),
    (0.4, 0.3),
    (0.2, 0.2), (0., 0.5),
    (0., 0.),
]


codes['ecu'] = [
    Path.MOVETO,
    Path.CURVE3, Path.CURVE3,
    Path.LINETO,
    Path.CURVE4, Path.CURVE4, Path.CURVE4,
    Path.CURVE4, Path.CURVE4, Path.CURVE4,
    Path.LINETO,
    Path.CURVE3, Path.CURVE3,
    Path.CLOSEPOLY,
]

vertices['trefle'] = [
    (0.15,-0.5),
    (-0.15,-0.5),
    (0., -0.2), (-0.05, -0.15),

    (-0.15, -0.15), (-0.15, -0.3), (-0.3, -0.3),
    (-0.4, -0.3), (-0.5, -0.2), (-0.5, -0.1),
    (-0.5, 0.), (-0.4, 0.1), (-0.3, 0.1),
    (-0.15, 0.1), (-0.15, -0.05), (-0.05, -0.05),

    (-0.05, 0.15), (-0.2, 0.15), (-0.2, 0.3),
    (-0.2, 0.4), (-0.1, 0.5), (0., 0.5),
    (0.1, 0.5), (0.2, 0.4), (0.2, 0.3),
    (0.2, 0.15), (0.05, 0.15), (0.05, -0.05),

    (0.15, -0.05), (0.15, 0.1), (0.3, 0.1),
    (0.4, 0.1), (0.5, 0.), (0.5, -0.1),
    (0.5, -0.2), (0.4, -0.3), (0.3, -0.3),
    (0.15, -0.3), (0.15, -0.15), (0.05, -0.15),

    (0., -0.2), (0.15, -0.5),
    (0., 0.),
]

codes['trefle'] = [
    Path.MOVETO,
    Path.LINETO,
    Path.CURVE3, Path.CURVE3,
    Path.CURVE4, Path.CURVE4, Path.CURVE4,
    Path.CURVE4, Path.CURVE4, Path.CURVE4,
    Path.CURVE4, Path.CURVE4, Path.CURVE4,
    Path.CURVE4, Path.CURVE4, Path.CURVE4,
    Path.CURVE4, Path.CURVE4, Path.CURVE4,
    Path.CURVE4, Path.CURVE4, Path.CURVE4,
    Path.CURVE4, Path.CURVE4, Path.CURVE4,
    Path.CURVE4, Path.CURVE4, Path.CURVE4,
    Path.CURVE4, Path.CURVE4, Path.CURVE4,
    Path.CURVE4, Path.CURVE4, Path.CURVE4,
    Path.CURVE4, Path.CURVE4, Path.CURVE4,
    Path.CURVE4, Path.CURVE4, Path.CURVE4,
    Path.CURVE3, Path.CURVE3,
    Path.CLOSEPOLY
]

# petal = np.array([
#     (-0.05, 0.2), (-0.15, 0.25), (-0.15, 0.35),
#     (-0.15, 0.45), (-0.05, 0.5), (0., 0.5),
#     (0.05, 0.5), (0.15, 0.45), (0.15, 0.35),
#     (0.15, 0.25), (0.05, 0.2), (0.05, 0.05*np.sqrt(3))
# ])
#
# vertices['rose'] = [
#     (-0.05, 0.05*np.sqrt(3))
# ]

# petal = np.array([
#     (-0.05, 0.2), (-0.1*np.sqrt(3) , 0.25), (-0.1*np.sqrt(3), 0.35),
#     (-0.1*np.sqrt(3), 0.35 + 0.05*np.sqrt(3)), (-0.05*np.sqrt(3), 0.5), (0., 0.5),
#     (0.05*np.sqrt(3), 0.5), (0.1*np.sqrt(3), 0.35 + 0.05*np.sqrt(3)), (0.1*np.sqrt(3), 0.35),
#     (0.1*np.sqrt(3), 0.25), (0.05, 0.2), (0.05, 0.05*np.sqrt(3))
# ])
#
# vertices['rose'] = [
#     (-0.05, 0.05*np.sqrt(3))
# ]

petal = np.array([
    (-0.05, 0.25), (-0.2, 0.25), (-0.2, 0.4),
    (-0.2, 0.5), (-0.1, 0.6), (0., 0.6),
    (0.1, 0.6), (0.2, 0.5), (0.2, 0.4),
    (0.2, 0.25), (0.05, 0.25), (0.05, 0.05),
])

vertices['rose'] = [
    (-0.05, 0.05)
]

# petal = np.array([
#     (-0.2, 0.2*np.sqrt(3)), (-0.15, 0.5), (0., 0.5),
#     (0.15, 0.5), (0.2, 0.2*np.sqrt(3)), (0.2, 0.2*np.sqrt(3))
# ])
#
# vertices['rose'] = [
#     (-0.2, 0.2*np.sqrt(3))
# ]

codes['rose'] = [
    Path.MOVETO
]

# angles = [i*np.pi/3 for i in range(6)]
angles = [i*np.pi/2 for i in range(4)]

for a in angles:
    rotation_matrix = np.array([[ np.cos(a), np.sin(a)],
                                [-np.sin(a), np.cos(a)]])
    rotated_petal = np.einsum("...ij,...j->...i",rotation_matrix,petal)

    vertices['rose'] += [tuple(p) for p in rotated_petal]
    codes['rose'] += [Path.CURVE4 for p in rotated_petal]

vertices['rose'] += [
    (0., 0.)
]

codes['rose'] += [
    Path.CLOSEPOLY
]

rotation_matrix = np.array([[np.cos(np.pi/4), np.sin(np.pi/4)],
                            [-np.sin(np.pi/4), np.cos(np.pi/4)]])
vertices['rose'] = np.einsum("...ij,...j->...i", rotation_matrix, vertices['rose'])

if args.suit_colors == "rainbow":
    colors['pique'] = '#000000'
    colors['coeur'] = '#cc0000'
    colors['carreau'] = '#ff6600'
    #colors['or'] = '#cccc00'
    colors['coupe'] = "#cccc00"
    colors['gland'] = '#009900'
    # colors['coupe'] = '#0099ff'
    colors['ecu'] = '#0099ff'
    colors['trefle'] = '#000099'
    # colors['ecu'] = '#660099'
    colors['rose'] = '#660099'
elif args.suit_colors == "red_black":
    colors['pique'] = '#000000'
    colors['coeur'] = '#cc0000'
    colors['rose'] = '#cc3399'
    colors['carreau'] = '#cc0000'
    # colors['or'] = '#cc0000'
    colors['ecu'] = '#000000'
    colors['gland'] = '#000000'
    colors['coupe'] = '#cc0000'
    colors['trefle'] = '#000000'
    colors['rose'] = '#cc0000'

suit_centers = {}
suit_centers['pique'] = (0,1)
suit_centers['coeur'] = (1,1)
suit_centers['carreau'] = (2,1)
suit_centers['trefle'] = (3,1)
suit_centers['coupe'] = (0,0)
suit_centers['gland'] = (1,0)
suit_centers['ecu'] = (2,0)
suit_centers['rose'] = (3,0)

suit_scale = 0.9

figure = plt.figure(0)
figure.clf()

for suit in suit_centers.keys():
    path = Path(suit_scale*np.array(vertices[suit])+np.array(suit_centers[suit]), codes[suit])

    suit_patch = patch.PathPatch(path, fc=colors[suit], ec='none', alpha=1)
    #suit_patch = patch.PathPatch(path, fc='k', ec='none', alpha=0.5, linewidth=2)
    figure.gca().add_patch(suit_patch)

figure.gca().axis('equal')
figure.gca().set_xlim(np.min([suit_centers[suit][0] for suit in suit_centers])-0.5,
                      np.max([suit_centers[suit][0] for suit in suit_centers])+0.5)
figure.gca().axis('off')
figure.set_size_inches(10,5)
figure.tight_layout()
figure.savefig("../suits.png")
figure.show()

figure = plt.figure(1)
figure.clf()

for i_s, suit in enumerate(codes.keys()):
    path = Path(vertices[suit], codes[suit])

    suit_patch = patch.PathPatch(path, ec=colors[suit], fc='none', alpha=1)
    figure.gca().add_patch(suit_patch)


figure.gca().axis('equal')
figure.gca().set_xlim(-1, 1)
figure.show()

for i_s, suit in enumerate(codes.keys()):
    svg_file = open("../suits/"+suit+".svg","w+")
    svg_file.write("<svg width=\"200\" height=\"200\" xmlns=\"http://www.w3.org/2000/svg\" xmlns:svg=\"http://www.w3.org/2000/svg\">\n")
    svg_file.write("<g class=\"layer\">\n")
    svg_file.write("  <title>"+suit+"</title>\n")
    svg_file.write("  <path id=\""+suit+"\" d=\"")

    q_index = 0
    c_index = 0
    for (x,y), c in zip(vertices[suit],codes[suit]):
        svg_x = 100 + 160*x
        svg_y = 100 - 160*y
        if c == Path.MOVETO:
            svg_file.write("M "+str(svg_x)+", "+str(svg_y)+" ")
        elif c == Path.LINETO:
            svg_file.write("L "+str(svg_x)+", "+str(svg_y)+" ")
        elif c == Path.CURVE3:
            if q_index == 0:
                svg_file.write("Q ")
            svg_file.write(str(svg_x) + ", " + str(svg_y) + " ")
            q_index = (q_index+1) % 2
        elif c == Path.CURVE4:
            if c_index == 0:
                svg_file.write("C ")
            svg_file.write(str(svg_x) + ", " + str(svg_y) + " ")
            c_index = (c_index+1) % 3
        elif c == Path.CLOSEPOLY:
            svg_file.write("Z ")
    svg_file.write("\" ")
    #svg_file.write("stroke-linecap=\"null\" ")
    #svg_file.write("stroke-linejoin=\"null\" ")
    #svg_file.write("stroke-dasharray=\"null\" ")
    #svg_file.write("stroke-width=\"5\" ")
    #svg_file.write("stroke=\"#000000\" ")
    svg_file.write("stroke=\"none\" ")
    #svg_file.write("fill=\"none\" ")
    svg_file.write("fill=\""+colors[suit]+"\" ")
    svg_file.write("/>\n")
    svg_file.write("</g>\n")
    svg_file.write("</svg>\n")
    svg_file.flush()
    svg_file.close()

if save_cards:
    centers = {}
    centers[0] = []
    centers[1] = [(0,0)]
    centers[2] = [(0,6),(0,-6)]
    centers[3] = [(0,6),(0,0),(0,-6)]
    centers[4] = [(-3,6),(3,6),(-3,-6),(3,-6)]
    centers[5] = [(-3,6),(3,6),(0,0),(-3,-6),(3,-6)]
    centers[6] = [(-3,6),(3,6),(-3,0),(3,0),(-3,-6),(3,-6)]
    centers[7] = [(-3,6),(3,6),(0,3),(-3,0),(3,0),(-3,-6),(3,-6)]
    centers[8] = [(-3,6),(3,6),(0,3),(-3,0),(3,0),(0,-3),(-3,-6),(3,-6)]
    centers[9] = [(-3,6),(3,6),(-3,2),(3,2),(0,0),(-3,-2),(3,-2),(-3,-6),(3,-6)]
    centers[10] = [(-3,6),(3,6),(0,4),(-3,2),(3,2),(-3,-2),(3,-2),(0,-4),(-3,-6),(3,-6)]
    #centers[11] = [(0,0)]
    #centers[19] = [(-3,6),(3,6),(-3,2),(3,2),(0,0),(-3,-2),(3,-2),(-3,-6),(3,-6)]
    centers['A'] = []
    centers['V'] = [(-3.4,6.3),(3.4,-6.3)]
    centers['D'] = [(-3.4,6.3),(3.4,-6.3)]
    centers['R'] = [(-3.4,6.3),(3.4,-6.3)]

    orientations = {}
    orientations[0] = []
    orientations[1] = [1]
    orientations[2] = [1,-1]
    orientations[3] = [1,1,-1]
    orientations[4] = [1,1,-1,-1]
    orientations[5] = [1,1,1,-1,-1]
    orientations[6] = [1,1,1,1,-1,-1]
    orientations[7] = [1,1,1,1,1,-1,-1]
    orientations[8] = [1,1,1,1,1,-1,-1,-1]
    orientations[9] = [1,1,1,1,1,-1,-1,-1,-1]
    orientations[10] = [1,1,1,1,1,-1,-1,-1,-1,-1]
    #orientations[11] = [1]
    #orientations[19] = [1,1,1,1,1,-1,-1,-1,-1]
    orientations['A'] = []
    orientations['V'] = [1,-1]
    orientations['D'] = [1,-1]
    orientations['R'] = [1,-1]

    names = {}
    names['A'] = 'as'
    names['V'] = 'valet'
    names['D'] = 'dame'
    names['R'] = 'roi'

    figures = ['V','D','R','A']
    watermark = ['A']

    scale = 1.133
    suit_coef = 2.
    number_coef = 1.
    figure_coef = 4.
    watermark_coef = 8.*scale

    figure = plt.figure(2)
    figure.clf()

    for i in range(50):
        for i_s, suit in enumerate(codes.keys()):
            center = 1-2*np.random.rand(2)

            rotation_matrix = np.array([[np.cos(np.pi / 6), np.sin(np.pi / 6)],
                                        [-np.sin(np.pi / 6), np.cos(np.pi / 6)]])
            verts = np.einsum("...ij,...j->...i", rotation_matrix, np.array(vertices[suit]))

            for y in [-2,0,2]:
                path = Path(6.*(center + np.array([0,y]) + verts), codes[suit])

                suit_patch = patch.PathPatch(path, ec=colors[suit], fc='none', alpha=0.5, lw=5)
                figure.gca().add_patch(suit_patch)

    figure.gca().axis('auto')
    figure.gca().set_xlim(-5.7, 5.7)
    figure.gca().set_ylim(-8.8, 8.8)
    figure.gca().axis('off')

    figure.set_size_inches(2.283, 3.503)
    figure.tight_layout()
    figure.savefig("../cards/back.pdf", dpi=300)

    merger = PdfFileMerger()
    for i_s, suit in enumerate(codes.keys()):
        for n in centers.keys():
            figure = plt.figure(2)
            figure.clf()

            for c,o in zip(centers[n], orientations[n]):
                path = Path(scale*( np.array(c) + o*suit_coef*np.array(vertices[suit])), codes[suit])
                suit_patch = patch.PathPatch(path, fc=colors[suit], ec='none', alpha=1)
                #suit_patch = patch.PathPatch(path, ec=colors[suit], fc='none', alpha=1)
                figure.gca().add_patch(suit_patch)

            rect = patch.Rectangle((-6.*scale,4.5*scale),height=figure_coef*scale,width=0.5*figure_coef*scale,fc='w',ec='none')
            figure.gca().add_patch(rect)

            rect = patch.Rectangle((6.*scale,-4.5*scale),height=figure_coef*scale,width=0.5*figure_coef*scale,fc='w',ec='none',angle=180)
            figure.gca().add_patch(rect)

            if n in watermark:
                path = Path(scale*(watermark_coef*np.array(vertices[suit])), codes[suit])
                suit_patch = patch.PathPatch(path, fc=colors[suit], ec='none', alpha=0.2)
                figure.gca().add_patch(suit_patch)

            if n in figures:
                name = names[n] if n in names else str(n).zfill(2)
                figure_filename = "../figures/"+name+"_"+str(suit)+".png"

                if os.path.exists(figure_filename):
                    figure_img = imread(figure_filename)
                    print(name,suit,figure_img.shape)
                    extent = (-4,4,0,8)
                    figure.gca().imshow(figure_img,extent=extent)
                    extent = (4,-4,0,-8)
                    figure.gca().imshow(figure_img,extent=extent)
                else:
                    for c in [[0,0.5],[0,-0.5],[0.5,0],[-0.5,0]]:
                        path = Path(scale*(np.array([c]) + np.sqrt(2)*figure_coef*np.array(vertices[suit])), codes[suit])
                        suit_patch = patch.PathPatch(path, fc='none', ec=colors[suit], linewidth=2, alpha=0.2)
                        figure.gca().add_patch(suit_patch)

                    path = Path(scale*(figure_coef*np.array(vertices[suit])), codes[suit])
                    suit_patch = patch.PathPatch(path, fc=colors[suit], ec='none', alpha=1)
                    figure.gca().add_patch(suit_patch)

                    path = Path(scale*(figure_coef*np.array(vertices[suit])), codes[suit])
                    suit_patch = patch.PathPatch(path, fc='w', ec=colors[suit], alpha=0.5, linewidth=2)
                    figure.gca().add_patch(suit_patch)

            font = fm.FontProperties(family='Raleway', fname='/Users/gcerutti/Library/Fonts/Raleway-Regular.ttf', size=24)

            figure.gca().text(-5.2,8.4,str(n),color=colors[suit], ha='center', va='center', fontproperties=font)
            path = Path((np.array([-5.2,7.]) + number_coef * np.array(vertices[suit])), codes[suit])
            suit_patch = patch.PathPatch(path, fc=colors[suit], ec='none', alpha=1)
            figure.gca().add_patch(suit_patch)

            figure.gca().text(5.2,-8.4,str(n),color=colors[suit], ha='center', va='center', rotation=180, fontproperties=font)
            path = Path((np.array([5.2,-7.]) - number_coef * np.array(vertices[suit])), codes[suit])
            suit_patch = patch.PathPatch(path, fc=colors[suit], ec='none', alpha=1)
            figure.gca().add_patch(suit_patch)

            figure.gca().axis('auto')
            figure.gca().set_xlim(-5.7, 5.7)
            figure.gca().set_ylim(-8.8, 8.8)
            figure.gca().axis('off')

            figure.set_size_inches(2.283, 3.503)
            figure.tight_layout()
            name = names[n] if n in names else str(n).zfill(2)
            figure.savefig("../cards/"+name+"_"+str(suit)+".pdf", dpi=300)
            merger.append("../cards/"+name+"_"+str(suit)+".pdf")

    merger.write("../cards/all_cards.pdf")
    merger.close()
