import os
from PIL import Image, ImageDraw, ImageFont, ImageOps
from tkinter import Tk
from tkinter.filedialog import askdirectory, askopenfilenames


def create_collage(images, output_file, title_text, cell_size=200, border_size=10):
    if not images:
        print("Ошибка: Не выбраны изображения.")
        return

    # Приветственный текст
    font_size = 30
    try:
        font = ImageFont.truetype("arial.ttf", font_size)
    except IOError:
        font = ImageFont.load_default()

    # Определение размера коллажа
    num_images = len(images)
    cols = int(num_images ** 0.5)  # Количество колонок
    rows = (num_images + cols - 1) // cols  # Количество строк

    collage_width = cols * cell_size + (cols + 1) * border_size
    collage_height = rows * cell_size + (rows + 1) * border_size + font_size + border_size

    # Создание фона коллажа
    collage = Image.new('RGB', (collage_width, collage_height), color='grey')
    draw = ImageDraw.Draw(collage)

    # Добавление заголовка
    text_width, text_height = draw.textbbox((0, 0), title_text, font=font)[2:4]
    draw.text(((collage_width - text_width) / 2, border_size), title_text, fill="black", font=font)

    # Обработка изображений
    x_offset = border_size
    y_offset = border_size + font_size + border_size

    for img_path in images:
        img = Image.open(img_path)

        # Масштабируем и обрезаем изображение
        img = ImageOps.fit(img, (cell_size, cell_size), Image.LANCZOS)

        # Вставка изображения на коллаж
        collage.paste(img, (x_offset, y_offset))

        # Переход к следующей позиции
        x_offset += cell_size + border_size

        if x_offset + cell_size > collage_width:  # Переход на следующую строку
            x_offset = border_size
            y_offset += cell_size + border_size

    # Сохранение коллажа
    collage.save(output_file)
    print(f"Коллаж сохранён в файл: {output_file}")


if __name__ == "__main__":
    # Создание окна для выбора файлов
    Tk().withdraw()  # Скрыть главное окно
    input_folder = askdirectory(title="Выберите папку с изображениями")
    
    if not input_folder:
        print("Ошибка: Папка не выбрана.")
    else:
        # Выбор изображений
        images = askopenfilenames(title="Выберите изображения", initialdir=input_folder,
                                   filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])

        # Установка имени выходного файла
        output_file = os.path.join(input_folder, "collage.jpg")  # Имя выходного файла

        # Заголовок
        title_text = "Мой Коллаж"  # Заголовок
        create_collage(images, output_file, title_text)

