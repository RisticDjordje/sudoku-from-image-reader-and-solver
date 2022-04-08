# Sudoku from images reader and solver

This is my full solution to the Sudoku problem given in the test for [PSI:ML 8](https://psiml.petlja.org/).

---

<br>

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
>The resulting table should be printed to the standard output, one row per line. Each line should be printed in csv format (as 9 comma-separated digits). Empty tiles should be represented with a zero. <br><br>The following 9 lines should contain the solved sudoku, in the same format. Each value 0 from the previous 9 lines should be replaced with a correct digit.

#### Scoring
>Each test case brings a maximum of 100 points. Full correctly detected sudoku table brings 50 points per test case. The correct sudoku solution brings additional 50 points only if there are no errors in the previous output.

#### Datasets
>There are two data sets:<br>
>- Public data set is used for developing your solution. After you submit your solution, you will be able to see how well your solution performs against this data set. Public data set is not used for calculating the final score. Public data set is available here.<br>
>- Private data set is used for testing your solution. The final score will be measured against this data set. Private data set and the final score will be available after the homework finishes. Private data set contains different data than the public data set, but the type of data is roughly the same (the same constraints apply).

#### Limitations
>The time limit for task execution is 1 second per input image.<br>
Allowed python packages: numpy, PIL, all packages from the standard python library

<br>

---

## Examples 

<br>

<img src="/public/set/08/08.png" width="300">

Input: `public/set/08/`

Output:<br>

4,8,1,2,6,3,9,5,7<br>
0,5,7,0,8,1,2,6,3<br>
2,6,3,9,5,7,4,8,1<br>
0,3,4,5,7,2,8,1,9<br>
8,1,9,6,3,4,5,7,2<br>
5,7,2,8,1,9,6,3,4<br>
3,4,8,7,0,6,1,9,5<br>
1,9,5,3,4,0,7,2,6<br>
0,2,6,1,9,5,3,0,8<br>
4,8,1,2,6,3,9,5,7<br>
9,5,7,4,8,1,2,6,3<br>
2,6,3,9,5,7,4,8,1<br>
6,3,4,5,7,2,8,1,9<br>
8,1,9,6,3,4,5,7,2<br>
5,7,2,8,1,9,6,3,4<br>
3,4,8,7,2,6,1,9,5<br>
1,9,5,3,4,8,7,2,6<br>
7,2,6,1,9,5,3,4,8<br>

______

<img src="/public/set/02/02.png" width="350">

Input: `public/set/02/`<br>

Output:<br>

8,5,9,3,2,1,4,7,6<br>
4,7,6,8,5,9,3,2,0<br>
0,2,1,4,7,6,8,5,9<br>
1,8,2,6,0,7,0,4,5<br>
9,4,5,1,8,2,6,3,7<br>
6,3,7,9,4,5,1,8,2<br>
2,9,8,7,0,3,5,6,4<br>
5,6,4,2,9,8,7,1,3<br>
7,1,3,5,6,4,2,9,8<br>
8,5,9,3,2,1,4,7,6<br>
4,7,6,8,5,9,3,2,1<br>
3,2,1,4,7,6,8,5,9<br>
1,8,2,6,3,7,9,4,5<br>
9,4,5,1,8,2,6,3,7<br>
6,3,7,9,4,5,1,8,2<br>
2,9,8,7,1,3,5,6,4<br>
5,6,4,2,9,8,7,1,3<br>
7,1,3,5,6,4,2,9,8<br>

_______

<img src="/public/set/07/07.png" width="350">

Input: `public/set/07/`<br>

Output: <br>
3,9,2,4,5,1,0,0,7<br>
4,5,1,6,8,7,3,9,2<br>
6,8,0,3,9,2,4,5,1<br>
2,4,9,1,6,5,7,3,8<br>
1,6,5,7,3,8,2,4,9<br>
7,3,8,2,4,9,1,6,5<br>
9,1,4,5,7,6,8,0,3<br>
5,0,6,8,0,3,9,1,4<br>
8,2,0,9,1,4,5,7,6<br>
3,9,2,4,5,1,6,8,7<br>
4,5,1,6,8,7,3,9,2<br>
6,8,7,3,9,2,4,5,1<br>
2,4,9,1,6,5,7,3,8<br>
1,6,5,7,3,8,2,4,9<br>
7,3,8,2,4,9,1,6,5<br>
9,1,4,5,7,6,8,2,3<br>
5,7,6,8,2,3,9,1,4<br>
8,2,3,9,1,4,5,7,6<br>


________

<img src="/public/set/05/05.png" width="350">

Input: `public/set/05/`<br>

Output: <br>

5,6,3,8,1,9,2,4,7<br>
8,1,9,2,4,7,5,0,3<br>
2,4,7,5,6,3,8,1,9<br>
0,3,5,6,9,8,1,7,2<br>
6,9,8,1,7,2,4,3,5<br>
1,7,2,4,3,5,6,9,8<br>
3,8,6,9,2,1,0,5,0<br>
9,2,1,7,5,4,0,8,6<br>
7,0,4,3,0,6,9,2,1<br>
5,6,3,8,1,9,2,4,7<br>
8,1,9,2,4,7,5,6,3<br>
2,4,7,5,6,3,8,1,9<br>
4,3,5,6,9,8,1,7,2<br>
6,9,8,1,7,2,4,3,5<br>
1,7,2,4,3,5,6,9,8<br>
3,8,6,9,2,1,7,5,4<br>
9,2,1,7,5,4,3,8,6<br>
7,5,4,3,8,6,9,2,1<br>
