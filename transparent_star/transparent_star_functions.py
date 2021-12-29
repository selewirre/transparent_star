from PIL import Image, ImageDraw
import numpy as np


def get_transparent_star(image_filename, luminance_stop=90, transparency_power_decay=0.9):
    image = Image.open(image_filename).convert('RGB')

    r, g, b = image.split()
    image_gray = image.convert('L')
    alpha = np.array(image_gray)

    alpha[alpha >= luminance_stop] = 255
    alpha[alpha < luminance_stop] = (alpha[alpha < luminance_stop] / luminance_stop) ** transparency_power_decay * 255
    alpha[alpha[:, :] > 210] = 255
    alpha[alpha[:, :] < 20] = 0

    alpha = Image.fromarray(alpha)
    image_new = Image.merge('RGBA', (r, g, b, alpha))

    return image_new


def get_logos(image_filename, inverted=False):
    image_new = get_transparent_sol(image_filename)
    new_image_array = np.array(image_new.convert('LA'))
    new_image_array[:, :, 0] = 255
    image_new = Image.fromarray(new_image_array, 'LA')
    draw = ImageDraw.Draw(image_new)
    center_x = np.linspace(700, 3200, 9)

    def cy_func(x, start, stop):
        breadth = stop - start
        return stop - ((x - start) / breadth) ** 1.8 * breadth

    center_y = cy_func(center_x, 700, 3200)
    radii = list(np.linspace(20, 150, 5)) + list(np.linspace(150, 20, 5)[1:])
    for (x, y, radius) in zip(np.flip(center_y), center_y, radii):
        xmin = x - radius
        xmax = x + radius
        ymin = y - radius
        ymax = y + radius
        draw.ellipse((xmin, ymin, xmax, ymax), fill='black', outline='black')

    if inverted:
        new_image_inverted_array = np.array(image_new)
        new_image_inverted_array[:, :, 0] = 255 - new_image_inverted_array[:, :, 0]
        image_new = Image.fromarray(new_image_inverted_array, 'LA')

    return image_new


# image_new.save('logo.ico', sizes=[(256, 256)])
# new_image_inverted.save('logo_inverted.ico', sizes=[(256, 256)])
# plt.imshow(image_new.convert('LA'))
# plt.gca().set_facecolor('xkcd:salmon')
# plt.show()
