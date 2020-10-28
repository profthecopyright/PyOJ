from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

def create_gif(text, dir_path='.', filename='test.gif', imgsize=(600, 200), bgcolor=(255, 255, 255),
           fgcolor=(102, 8, 116), fontfile='fonts\STXINGKA.ttf', fontsize=60, duration=1000, loop=0):

    img_seed = Image.new('RGB', imgsize, bgcolor)
    font = ImageFont.truetype(fontfile, fontsize)

    ctr = 0
    images = [img_seed]

    for i in range(len(text)):
        images.append(img_seed.copy())

    for frame in images:
        d = ImageDraw.Draw(frame)
        d.text((10, 10), text[:ctr], fill=fgcolor, font=font)
        ctr = ctr + 1

    images[0].save(dir_path + '/' + filename,
            save_all=True, append_images=images[1:], optimize=False, duration=duration, loop=loop)

if __name__ == '__main__':
    create_gif('字体')