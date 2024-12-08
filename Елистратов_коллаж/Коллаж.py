from PIL import Image, ImageDraw, ImageFont, ImageOps
import os
import math

def calculate_grid(num_images):
    # Вычисляет оптимальное количество столбцов и строк для сетки.
    side = int(math.ceil(math.sqrt(num_images)))
    return side, math.ceil(num_images / side)

def center_text(draw, text, font, width, height, padding=10):
    # Центрирует текст в заданной области.
    text_width, text_height = draw.textsize(text, font=font)
    x = (width - text_width) // 2
    y = (height - text_height) // 2 + padding
    return x, y



def create_collage(image_dir, output_filename, title_text):
    # проверка существования папки и изображений 

    cell_size = 200
    border_width = 5
    try:
        title_font = ImageFont.truetype("arial.ttf", 48)
    except IOError:
        title_font = ImageFont.load_default()

    num_images = len(image_files)
    cols, rows = calculate_grid(num_images)


    collage_width = cols * (cell_size + border_width) + border_width
    collage_height = rows * (cell_size + border_width) + border_width + title_font.getsize(title_text)[1]

    collage = Image.new('RGB', (collage_width, collage_height), color='grey')
    draw = ImageDraw.Draw(collage)

    # Центрирование заголовка
    title_x, title_y = center_text(draw, title_text, title_font, collage_width, title_font.getsize(title_text)[1])
    draw.text((title_x, title_y), title_text, font=title_font, fill="black")

    #  добавление изображений 

    collage.save(output_filename, "JPEG")
    print(f"Коллаж сохранен в файл: {output_filename}")


if __name__ == "__main__":

    image_directory = "images" # Ваш путь файла
    output_file = "collage.jpg" # Ваше имя выходного файла
    collage_title = "Мой коллаж" # Ваш загаловок

    try:
        create_collage(image_directory, output_file, collage_title)
    except (FileNotFoundError, ValueError) as e:
        print(f"Ошибка: {e}")

