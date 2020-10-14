import tkinter
from PIL import Image, ImageDraw, ImageTk

def draw_game(grid_resolution, ships, attacks,
              image_size=(400, 400)):

    grid_size = (image_size[0]//grid_resolution[0],
                 image_size[1]//grid_resolution[1])
    
    im = Image.new('RGB', image_size, (0, 0, 100))
    draw = ImageDraw.Draw(im)

    # draw column
    for x in range(0, image_size[0], grid_size[0]):
        draw.line((x, 0, x, image_size[1]),
                  fill='black', width=1)
    # draw row
    for y in range(0, image_size[1], grid_size[1]):
        draw.line((0, y, image_size[0], y),
                  fill='black', width=1)

    def _scale_grid(area):
        tl_x = area[0] * grid_size[0]
        tl_y = area[1] * grid_size[1]
        br_x = (area[2]+1) * grid_size[0]
        br_y = (area[3]+1) * grid_size[1]
        return (tl_x, tl_y, br_x, br_y)
            
    # draw ships
    for s in ships:
        draw.rectangle(_scale_grid(s.area), fill='grey', outline='black')

    # draw attacks
    for a in attacks:
        area = (a[0], a[1], a[0], a[1])
        draw.ellipse(_scale_grid(area), fill='red', outline='black')

    return im


class ShowFrame(tkinter.Frame):
    def __init__(self, master, image):
        tkinter.Frame.__init__(self, master)

        # set up the image
        self.tkim = ImageTk.PhotoImage(image.mode, image.size)
        self.tkim.paste(image)

        # image window
        tkinter.Label(self, image=self.tkim).pack()


def show_image(image):
    window = tkinter.Tk()
    window.title('Grid Battle Ship')
    window.geometry('400x400')
    ShowFrame(window, image).pack()
    # tkinter.Button
    window.mainloop()