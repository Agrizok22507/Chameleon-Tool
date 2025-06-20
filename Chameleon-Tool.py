import os
from PIL import Image
from rich import print

def convert_to_png_and_resize(input_path, output_path):
    """Конвертирует изображение в PNG (если нужно) и уменьшает до 512x512."""
    try:
        img = Image.open(input_path)
        if img.format != "PNG":
            img = img.convert("RGBA")
        img.thumbnail((512, 512))
        img.save(output_path, "PNG")
        print(f"Успешно: {input_path} -> {output_path}")
    except Exception as e:
        print(f"Ошибка при обработке {input_path}: {e}")

def process_folder(input_folder, output_folder):
    """Обрабатывает все изображения в папке (включая подпапки)."""
    os.makedirs(output_folder, exist_ok=True)
    
    for root, _, files in os.walk(input_folder):
        for filename in files:
            if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.webp', '.bmp', '.gif')):
                input_path = os.path.join(root, filename)
                
                # Создаем аналогичную структуру папок в output
                relative_path = os.path.relpath(root, input_folder)
                output_dir = os.path.join(output_folder, relative_path)
                os.makedirs(output_dir, exist_ok=True)
                
                # Формируем выходное имя (с заменой расширения на .png)
                output_filename = os.path.splitext(filename)[0] + '.png'
                output_path = os.path.join(output_dir, output_filename)
                
                convert_to_png_and_resize(input_path, output_path)

if __name__ == "__main__":
    chameleon = """
▄█▄     ▄  █ ██   █▀▄▀█ ▄███▄   █     ▄███▄   ████▄    ▄     ▄▄▄▄▀ ████▄ ████▄ █     
█▀ ▀▄  █   █ █ █  █ █ █ █▀   ▀  █     █▀   ▀  █   █     █ ▀▀▀ █    █   █ █   █ █     
█   ▀  ██▀▀█ █▄▄█ █ ▄ █ ██▄▄    █     ██▄▄    █   █ ██   █    █    █   █ █   █ █     
█▄  ▄▀ █   █ █  █ █   █ █▄   ▄▀ ███▄  █▄   ▄▀ ▀████ █ █  █   █     ▀████ ▀████ ███▄  
▀███▀     █     █    █  ▀███▀       ▀ ▀███▀         █  █ █  ▀                      ▀ 
         ▀     █    ▀                               █   ██                           
              ▀                                                                      
"""
    log = os.getlogin()
    print(f"[bold cyan]{chameleon}[/bold cyan]")
    print("[bold cyan]Converter image for stickers tg(png 512px)[bold cyan]")
    print("[bold cyan]Start path with all images, end path for all convertered images(png 512px)[/bold cyan]")
    print(f"[bold cyan]Example of path C:/Users/{log}/Desktop/Images[/bold cyan]")
    input_folder = input("Path to images(jpg, jpeg, png, webp, bmp, gif) : ")
    output_folder = input("Path output : ")
    
    print(f"[bold cyan]Convert image '{input_folder}'...[/bold cyan]")
    process_folder(input_folder, output_folder)
    print(f"[bold cyan]Sucess, check output in : {output_folder}[/bold cyan]")