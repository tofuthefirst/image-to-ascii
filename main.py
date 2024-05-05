from typer import Argument, Option, run
from PIL import Image
from pathlib import Path
from typing_extensions import Annotated


def main(path: Annotated[str, Argument(help="Specify the path to the input image")] = "image.png",
         downscale: Annotated[int, Option("--downscale", "-d", "-D", help="Specify the downscale factor")] = 4,
         output_path: Annotated[
             str, Option("--output-path", "-o", "-O", help="Specify the path to the output file")] = None,
         print_in_console: Annotated[bool, Option("--console", "-c", "-C",
                                                  help="Specify whether to print in console or output file.")] = False):
    image = Image.open(Path(path))
    width, height = [dimension // downscale for dimension in image.size]
    image = image.resize((width, height))
    pixels = image.load()
    output = []
    for y in range(height):
        output.append([])
        for x in range(width):
            brightness = sum(pixels[x, y])
            if brightness == 0:
                output[y].append(" ")
            elif brightness in range(1, 100):
                output[y].append("'")
            elif brightness in range(100, 200):
                output[y].append("(")
            elif brightness in range(200, 300):
                output[y].append("/")
            elif brightness in range(300, 400):
                output[y].append("+")
            elif brightness in range(400, 500):
                output[y].append("*")
            elif brightness in range(500, 600):
                output[y].append("&")
            elif brightness in range(600, 700):
                output[y].append("%")
            elif brightness in range(700, 750):
                output[y].append("X")
            else:
                output[y].append("#")
    if print_in_console:
        for row in output:
            print(''.join(row) + '\n')
    else:
        output_path = '.'.join([path.split('.')[0], 'txt']) if not output_path else output_path
        output_file = open(output_path, 'w')
        for row in output:
            output_file.write(''.join(row) + '\n')


if __name__ == "__main__":
    run(main)