import cv2
import matplotlib.pyplot as plot
from mpl_toolkits.mplot3d import Axes3D
import random
from Pixel import Pixel


def main():
    figure = plot.figure()
    graph = figure.add_subplot(111, projection='3d')
    graph.set_xlabel('Red Value')
    graph.set_ylabel('Green Value')
    graph.set_zlabel('Blue Value')
    image = cv2.imread("./Images/A_Sunday_on_La_Grande_Jatte,_Georges_Seurat,_1884.png", 1)
    image = image[:, :, ::-1]  # Reverses OpenCV2's BGR color order to more-standard RGB color order
    pixel_list = []
    for [row, i] in zip(image, range(0, len(image))):
        for [column, j] in zip(row, range(0, len(row))):
            pixel = Pixel(column)
            pixel_list.append(pixel)
    for i in range(0, min((image.shape[0] * image.shape[1])/30, 5000)):
        pixel = random.choice(pixel_list)
        graph.scatter(pixel.R, pixel.G, pixel.B, c=pixel.normalize().array(), marker="o", depthshade=False)
        pixel_list.remove(pixel)
    plot.show()


if __name__ == "__main__":
    main()
