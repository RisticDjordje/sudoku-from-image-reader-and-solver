# Sudoku from images reader and solver

This is my full solution to the Sudoku problem given in the test for [PSI:ML 8](https://psiml.petlja.org/).

---


## The problem

Your little cousin has just learned how to solve a sudoku. He finds the game interesting but is still not good at it, so he often sends you an image asking for your help. You don’t always have time to help him, so you want to automatize this task.

<br>

### Task 1: Read the table

> You are given an image of a standard 9x9 sudoku table. You already have the images of your cousin’s usual handwriting, and you can assume he writes all 9 digits fairly consistently, but you know you can encounter several problems:

> - He is taking the pictures carefully, so the table is perfectly aligned, but you can expect the image you receive to be rotated by 180 degrees, or by 90 degrees in either direction.
>- The sudoku table is not the same size each time, and the borders can be of slightly different widths.
>- The table can be in different parts of the image.
>- Although the digits are always centered, they can vary in size and take up different portions of the tiles.
>- Knowing all of this, you want to recognize all digits in the sudoku table, as well as the positions of the empty tiles.



>Additional notes: 
>- All images are in PNG format. 
>- Each tile is a square with a side of at least 32 and up to 64 pixels.
>- The sudoku table is always white, and your cousin colors the rest of the image in black before sending it.
>- He is always using a black marker for writing.
<br>

### Task 2: Check the solution

>You want to help him finish his game. You can assume that most of the numbers are already written, with up to 11 empty tiles. Find the numbers to enter in the empty tiles to make solved sudoku. <br><br>
Note: In the solved sudoku no rows, columns, or sub-boxes contain the same digit.

---
<br>

#### Input format
>Your program should read a single line through standard input. The input is a path to a folder that contains another folder and one png image. The png is the image of unsolved sudoku and the subfolder contains the sample digits written in your cousin’s handwriting.

#### Output format
>The resulting table should be printed to the standard output, one row per line. Each line should be printed in csv format (as 9 comma-separated digits). Empty tiles should be represented with a zero. The following 9 lines should contain the solved sudoku, in the same format. Each value 0 from the previous 9 lines should be replaced with a correct digit.

#### Scoring
>Each test case brings a maximum of 100 points. Full correctly detected sudoku table brings 50 points per test case. The correct sudoku solution brings additional 50 points only if there are no errors in the previous output.

#### Datasets
>There are two data sets:
>Public data set is used for developing your solution. After you submit your solution, you will be able to see how well your solution performs against this data set. Public data set is not used for calculating the final score. Public data set is available here.
>Private data set is used for testing your solution. The final score will be measured against this data set. Private data set and the final score will be available after the homework finishes. Private data set contains different data than the public data set, but the type of data is roughly the same (the same constraints apply).

#### Limitations
>The time limit for task execution is 1 second per input image.<br>
Allowed python packages: numpy, PIL, all packages from the standard python library

