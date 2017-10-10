import cv2
import matplotlib.pyplot as plot
from matplotlib import animation
from mpl_toolkits.mplot3d import Axes3D
import random
import math
from Pixel import Pixel


def init_graph():
    image = cv2.imread("./Images/A_Sunday_on_La_Grande_Jatte,_Georges_Seurat,_1884.png", 1)
    image = image[:, :, ::-1]  # Reverses OpenCV2's BGR color order to more-standard RGB color order
    pixel_list = []
    number_of_pixels = min((image.shape[0] * image.shape[1])/30, 2000)
    random_pixel_x = random.choices(range(0, image.shape[0]), k=number_of_pixels)
    random_pixel_y = random.choices(range(0, image.shape[1]), k=number_of_pixels)
    for i, j in zip(random_pixel_x, random_pixel_y):
        pixel = Pixel(image[i, j])
        pixel_list.append(pixel)
        graph.scatter(pixel.R, pixel.G, pixel.B, c=pixel.normalize().array(), marker="o", depthshade=False)
    graph.set_xlabel('Red Value')
    graph.set_ylabel('Green Value')
    graph.set_zlabel('Blue Value')
    graph.set_xbound(0, 255)
    graph.set_ybound(0, 255)
    graph.set_zbound(0, 255)

    return figure,


def animate(i):
    graph.view_init(elev=10., azim=i)
    return figure,


def main():
    anim = animation.FuncAnimation(figure, animate, init_func=init_graph, frames=360, interval=20, blit=True)
    anim.save('./Figures/test_anim.mp4', fps=30, extra_args=['-vcodec', 'libx264'])


if __name__ == "__main__":
    figure = plot.figure()
    graph = Axes3D(figure)
    main()
