import cv2
import matplotlib.pyplot as plot
from matplotlib import animation
from mpl_toolkits.mplot3d import Axes3D
import random
import argparse
import re
import datetime
from Pixel import Pixel


def render_graph():
    if args.outfile is None:
        args.outfile = './Figures/' + re.search(r"^(.:)?(.+\\)*((.+)(\..*))$", args.infile).group(4) + '.png'
    print("Generating image from {}.".format(args.infile))
    generation_started = datetime.datetime.now()
    image = cv2.imread(args.infile, 1)
    image = image[:, :, ::-1]  # Reverses OpenCV2's BGR color order to more-standard RGB color order
    number_of_pixels = min(int((image.shape[0] * image.shape[1])*(1/2)), args.max_samples)
    random_pixel_x = random.choices(range(0, image.shape[0]), k=number_of_pixels)
    random_pixel_y = random.choices(range(0, image.shape[1]), k=number_of_pixels)
    for i, j in zip(random_pixel_x, random_pixel_y):
        pixel = Pixel(image[i, j])
        graph.scatter(pixel.R, pixel.G, pixel.B, c=pixel.normalize().array(), marker="o", depthshade=False)
    graph.set_xlabel('Red Value')
    graph.set_ylabel('Green Value')
    graph.set_zlabel('Blue Value')
    graph.set_xbound(0, 255)
    graph.set_ybound(0, 255)
    graph.set_zbound(0, 255)
    plot.savefig(args.outfile, dpi=300)
    print("Image generated and saved at {}. "
          "This operation took {}".format(args.outfile, datetime.datetime.now() - generation_started))

    return figure,


def animate(i):
    graph.view_init(elev=10., azim=i)
    return figure,


def render_animation():
    anim = animation.FuncAnimation(figure, animate, init_func=render_graph, frames=360, interval=20, blit=True)
    if args.movie_outfile is None:
        args.movie_outfile = './Figures/' + re.search(r"^(.:)?(.+\\)*((.+)(\..*))$", args.infile).group(4) + '.mp4'
    print("Generating animation from {}".format(args.infile))
    generation_started = datetime.datetime.now()
    anim.save(args.movie_outfile, fps=30, extra_args=['-vcodec', 'libx264'])
    print("Animation generated and saved at {}. "
          "This operation took {}".format(args.movie_outfile, datetime.datetime.now() - generation_started))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate 3D scatter plots by color-sampling images.")
    parser.add_argument('infile', help="Path to the input image")
    parser.add_argument('-o', '--outfile', nargs='?', help="Path to output the 3D plot")
    parser.add_argument('-s', '--max_samples', nargs='?', help="Maximum number of sample points to take",
                        type=int, default=5000)
    parser.add_argument('-a', '--animate', action="store_true", help="Render an animation")
    parser.add_argument('-m', '--movie_outfile', nargs='?', help="Path to output the animation")
    args = parser.parse_args()
    figure = plot.figure(tight_layout=True)
    graph = figure.add_subplot(111, projection='3d')
    if args.animate:
        render_animation()
    else:
        render_graph()
