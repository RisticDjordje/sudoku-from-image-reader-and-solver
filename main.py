from os import listdir

import numpy as np
from PIL.Image import new, open, BILINEAR

if __name__ == '__main__':
    path = input()
    files = [f for f in listdir(path) if f.endswith('.png')]
    img = open(f"{path}/{files[0]}").convert('1')
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

    # left, top, right, bottom

    subimages = []

    # counter = 0
    for i in range(9):
        for j in range(9):
            left = (j - (j // 3)) * small_line_width + j * cell_size + j // 3 * big_line_width
            top = (i - (i // 3)) * small_line_width + i * cell_size + i // 3 * big_line_width
            right = left + cell_size
            bottom = top + cell_size

            subimage = crop_image.crop((left, top, right, bottom))
            subimages.append(subimage)
            # subimage.save(f"subimages\{counter}.png")
            # counter += 1


    def rgba_to_1(rgba):
        rgb = new("RGB", rgba.size, (255, 255, 255))
        rgb.paste(rgba, mask=rgba.split()[3])
        return rgb.convert('1')


    samples = []
    for f in listdir(f"{path}/digits/"):
        img = open(f"{path}/digits/{f}")
        if img.mode == "RGBA":
            samples.append(rgba_to_1(img).resize((cell_size, cell_size), BILINEAR))
        elif img.mode == "1":
            samples.append(img.resize((cell_size, cell_size), BILINEAR))


    def compare_images(img1, img2):

        img1 = np.array(img1)
        img2 = np.array(img2)
        err = np.sum((img1.astype("float") - img2.astype("float")) ** 2)
        err /= float(img1.shape[0] * img2.shape[1])

        # return the MSE, the lower the error, the more "similar"
        # the two images are
        return err


    def diff_sizes(img, px):
        cell_height = img.size[0]
        empty_img = new("1", (cell_height, cell_height), True)
        resized_img = img.resize((cell_height - px, cell_height - px), BILINEAR)
        empty_img.paste(resized_img, (px // 2, px // 2))
        # empty_img.show()
        return empty_img


    for cell in subimages:
        if len(cell.getcolors()) != 1:
            base_example = cell
            break

    min = float('inf')
    for rotation_index in range(4):
        for sample_digit_index in range(9):
            for size in range(cell_size - 5):
                difference = compare_images(base_example.rotate(rotation_index * 90),
                                            diff_sizes(samples[sample_digit_index], size))
                if difference < min:
                    min = difference
                    best_rotation = rotation_index * 90
                    best_size = size

    results = []
    perfectly_sized_samples = [diff_sizes(sample, best_size) for sample in samples]
    perfectly_rotated_cells = [subimage.rotate(best_rotation) for subimage in subimages]

    for cell_index in range(81):
        if len(perfectly_rotated_cells[cell_index].getcolors()) == 1:
            results.append(0)
        else:
            min = float('inf')
            for sample_index in range(len(perfectly_sized_samples)):
                difference = compare_images(perfectly_rotated_cells[cell_index], perfectly_sized_samples[sample_index])
                if difference < min:
                    min = difference
                    number = sample_index + 1
            results.append(number)

    results_2d = []

    for i in range(9):
        results_2d.append(results[i * 9:(i + 1) * 9])


        def find_next_cell_to_fill(grid, i, j):
            for x in range(i, 9):
                for y in range(j, 9):
                    if grid[x][y] == 0:
                        return x, y
            for x in range(0, 9):
                for y in range(0, 9):
                    if grid[x][y] == 0:
                        return x, y
            return -1, -1


    def is_valid(grid, i, j, e):
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


    def solve_sudoku(grid, i=0, j=0):
        i, j = find_next_cell_to_fill(grid, i, j)
        if i == -1:
            return True
        for e in range(1, 10):
            if is_valid(grid, i, j, e):
                grid[i][j] = e
                if solve_sudoku(grid, i, j):
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


    def rotate(matrix):
        temp_matrix = []
        column = len(matrix) - 1
        for column in range(len(matrix)):
            temp = []
            for row in range(len(matrix) - 1, -1, -1):
                temp.append(matrix[row][column])
            temp_matrix.append(temp)
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                matrix[i][j] = temp_matrix[i][j]
        return matrix


    if best_rotation == 270:
        rotated_solution = rotate(results_2d)
        print_2d(results_2d)
    elif best_rotation == 180:
        rotated_solution = rotate(rotate(results_2d))
        print_2d(results_2d)
    elif best_rotation == 90:
        rotated_solution = rotate(rotate(rotate(results_2d)))
        print_2d(results_2d)
    else:
        print_2d(results_2d)

    solve_sudoku(results_2d)
    print_2d(results_2d)