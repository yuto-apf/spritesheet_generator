from PIL import Image
import math
import os


def generate_spritesheet(img_folder, sheet_name, sprite_width, sprite_height, num_per_line):
    files = [f for f in os.listdir(img_folder) if f.endswith('.png')]
    imgs  = [Image.open(os.path.join(img_folder, f)) for f in files]

    sheet_width  = min([num_per_line, len(imgs)]) * sprite_width
    sheet_height = math.ceil(len(imgs) / num_per_line) * sprite_height
    spritesheet = Image.new('RGBA', (sheet_width, sheet_height))

    i = 0
    for y in range(sheet_height // sprite_height):
        for x in range(num_per_line):
            if i >= len(imgs):
                break
            spritesheet.paste(imgs[i], (x * sprite_width, y * sprite_height))
            i += 1

    spritesheet.save(os.path.join(img_folder, sheet_name))


def main():
    img_folder_path = './sprites'
    sheet_name      = 'spritesheet.png'
    sprite_width    = int(input("Each sprite's width >> "))
    sprite_height   = int(input("Each sprite's height >> "))
    num_per_line    = int(input("sheet / row >> "))
        
    generate_spritesheet(img_folder_path, sheet_name, sprite_width, sprite_height, num_per_line)
    print(f'Spritesheet is generated and saved to {img_folder_path}.')


if __name__ == '__main__':
    main()
