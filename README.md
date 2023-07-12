# Algebra Distance Calculator

This Python program calculates the minimum distance between two points in a given set of points in a two-dimensional plane using the distance formula.

## How to Use

1. Ensure that you have Python 3 installed on your machine.

2. Clone this repository or download the source code file.

3. Open the terminal or command prompt and navigate to the project directory.

4. Run the `distance_calculator.py` file using the Python interpreter.

5. Modify the `points` list within the code to include the points for which you want to calculate the minimum distance. Each point should be represented as a tuple of the form `(x, y)`.

6. After running the program, it will print the coordinates of the two points (`p1` and `p2`) that have the minimum distance, along with the calculated minimum distance.

## Distance Formula

The distance between two points `(x1, y1)` and `(x2, y2)` in a two-dimensional plane can be calculated using the distance formula:

```
distance = sqrt((x2 - x1)^2 + (y2 - y1)^2)
```

The program uses the `dist` function to calculate the distance between two points based on this formula.

## Example

The program includes an example input in the `distance` function. Modify the `points` list to include your own points to calculate the minimum distance.

Here's an example of calculating the minimum distance between two points:

```python
print(distance([(1, 2), (4, 6)]))
```

The program will output the coordinates of the two points (`p1` and `p2`) that have the minimum distance, along with the calculated minimum distance.

## Contributions

Contributions to this project are welcome. If you find any issues or have suggestions for improvement, please feel free to submit a pull request.
