import os

import numpy as np
from PIL import Image

if __name__ == '__main__':
    path = input()
    files = [f for f in os.listdir(path) if f.endswith('.png')]
    img = Image.open(f"{path}\{files[0]}").convert('1')
    numpy_arr = np.array(img)

    for row in range(numpy_arr.shape[0]):
        for column in range(numpy_arr.shape[1]):
            if numpy_arr[row][column]:
                left, top = column, row
                break
        else:
            continue  # only executed if the inner loop did NOT break
        break

    for row in range(numpy_arr.shape[0] - 1, -1, -1):
        for column in range(numpy_arr.shape[1] - 1, -1, -1):
            if numpy_arr[row][column]:
                right, bottom = column + 1, row + 1
                break
        else:
            continue  # only executed if the inner loop did NOT break
        break

    crop_image = img.crop((left, top, right, bottom))
    numpy_crop_image = np.array(crop_image)

    for column in range(numpy_crop_image.shape[0]):
        if not numpy_crop_image[0][column]:
            cell_size = column
            break

    for i in range(cell_size, numpy_crop_image.shape[0]):
        if numpy_crop_image[0][i]:
            small_line_width = i - cell_size
            break

    for i in range(cell_size * 3 + small_line_width * 2, numpy_crop_image.shape[0]):
        if numpy_crop_image[0][i]:
            big_line_width = i - (cell_size * 3 + small_line_width * 2)
            break

    subimages = []

    counter = 0

    for i in range(9):
        for j in range(9):
            left = (j - (j // 3)) * small_line_width + j * cell_size + j // 3 * big_line_width
            top = (i - (i // 3)) * small_line_width + i * cell_size + i // 3 * big_line_width
            right = left + cell_size
            bottom = top + cell_size

            subimage = crop_image.crop((left, top, right, bottom))
            subimages.append(subimage)
            counter += 1

            # subimage.save(f"subimages\{counter}.png")


    def rgba_to_1(rgba):
        rgb = Image.new("RGB", rgba.size, (255, 255, 255))
        rgb.paste(rgba, mask=rgba.split()[3])
        return rgb.convert('1')


    samples = []
    for f in os.listdir("digits/"):
        img = Image.open(f"digits/{f}")
        if img.mode == "RGBA":
            samples.append(rgba_to_1(img).resize((cell_size, cell_size), Image.BILINEAR))
        elif img.mode == "1":
            samples.append(img.resize((cell_size, cell_size), Image.BILINEAR))


    def compare_images(img1, img2):
        pairs = zip(img1.getdata(), img2.getdata())
        dif = sum(abs(p1 - p2) for p1, p2 in pairs)
        ncomponents = img1.size[0] * img1.size[1] * 3
        return (dif / 255.0 * 100) / ncomponents


    def diff_sizes(img, px, cell_height):
        empty_img = Image.new("1", (cell_height, cell_height), True)
        resized_img = img.resize((cell_height - px, cell_height - px), Image.BILINEAR)
        empty_img.paste(resized_img, (px // 2, px // 2))
        return empty_img


    sample_rotations = []
    for i in range(len(samples)):
        sample_rotations.append([samples[i], samples[i].rotate(90), samples[i].rotate(180), samples[i].rotate(270)])

    cell_1_diff_sizes = [subimages[0]]
    for px in range(1, cell_size - 5):
        cell_1_diff_sizes.append(diff_sizes(subimages[0], px, cell_size))

    min = float('inf')
    for i in range(9):  # rotations
        for j in range(4):
            for k in range(len(cell_1_diff_sizes)):
                if compare_images(sample_rotations[i][j], cell_1_diff_sizes[k]) < min:
                    min = compare_images(sample_rotations[i][j], cell_1_diff_sizes[k])
                    rotation, size = j, k

    results = []
    final_different_size_cells = [diff_sizes(cell, size, cell_size) for cell in subimages]

    for cell in final_different_size_cells:
        if len(cell.getcolors()) == 1:
            results.append(0)
        else:
            min = float('inf')
            for i in range(len(sample_rotations)):
                if compare_images(sample_rotations[i][rotation], cell) < min:
                    min = compare_images(sample_rotations[i][rotation], cell)
                    number = i + 1
            results.append(number)

    results_2d = []

    for i in range(9):
        results_2d.append(results[i * 9:(i + 1) * 9])


    def findNextCellToFill(grid, i, j):
        for x in range(i, 9):
            for y in range(j, 9):
                if grid[x][y] == 0:
                    return x, y
        for x in range(0, 9):
            for y in range(0, 9):
                if grid[x][y] == 0:
                    return x, y
        return -1, -1


    def isValid(grid, i, j, e):
        rowOk = all([e != grid[i][x] for x in range(9)])
        if rowOk:
            columnOk = all([e != grid[x][j] for x in range(9)])
            if columnOk:
                # finding the top left x,y co-ordinates of the section containing the i,j cell
                secTopX, secTopY = 3 * (i // 3), 3 * (j // 3)  # floored quotient should be used here.
                for x in range(secTopX, secTopX + 3):
                    for y in range(secTopY, secTopY + 3):
                        if grid[x][y] == e:
                            return False
                return True
        return False


    def solveSudoku(grid, i=0, j=0):
        i, j = findNextCellToFill(grid, i, j)
        if i == -1:
            return True
        for e in range(1, 10):
            if isValid(grid, i, j, e):
                grid[i][j] = e
                if solveSudoku(grid, i, j):
                    return True
                # Undo the current cell for backtracking
                grid[i][j] = 0
        return False


    def print_2d(results):
        for row in range(9):
            for val in range(9):
                if val == 8:
                    print(results[row][val])
                else:
                    print(results[row][val], end=',')

    print_2d(results_2d)
    solveSudoku(results_2d)
    print_2d(results_2d)
