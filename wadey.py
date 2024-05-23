import csv
import matplotlib.pyplot as plt
from tkinter import filedialog, Tk

class Point:
    """
    Represents a point in a 2D plane.

    Attributes:
    - x (float): The x-coordinate.
    - y (float): The y-coordinate.
    """

    def __init__(self, x, y):
        """
        Initializes a Point with x and y coordinates.

        Args:
        - x (float): The x-coordinate.
        - y (float): The y-coordinate.
        """
        self.x = x
        self.y = y

    def translate(self, dx, dy):
        """
        Shifts the point by dx units on the x-axis and dy units on the y-axis.

        Args:
        - dx (float): The shift along the x-axis.
        - dy (float): The shift along the y-axis.
        """
        self.x += dx
        self.y += dy

def plot_points(points_list, colors_list):
    """
    Displays points on a scatterplot.

    Args:
    - points_list (list of lists of Point): Lists of points to be plotted.
    - colors_list (list of str): Colors for each list of points.
    """
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Scatter Plot of Points')
    plt.grid(True)
    plt.gca().set_aspect('equal', adjustable='box')
    
    for points, color in zip(points_list, colors_list):
        x_values = [point.x for point in points]
        y_values = [point.y for point in points]
        plt.scatter(x_values, y_values, color=color)

    plt.show()

def read_points_from_csv(file_path):
    """
    Loads points from a CSV file.

    Args:
    - file_path (str): Path to the CSV file.

    Returns:
    - list of Point: Points read from the CSV file.
    """
    points = []
    try:
        with open(file_path, 'r') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)  # Skip the header row
            for row in csv_reader:
                x, y = map(float, row)
                points.append(Point(x, y))
    except FileNotFoundError:
        print("File not found.")
    return points

def main():
    # Initialize a Tkinter root window
    root = Tk()
    root.withdraw()  # Hide the root window

    # Prompt user to select a CSV file
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])

    if file_path:
        # Step 1: Load points from the selected CSV file
        points = read_points_from_csv(file_path)

        if points:
            # Step 2: Shift the points
            dx = 5  # Shift by 5 units on x-axis
            dy = 3  # Shift by 3 units on y-axis
            translated_points = [Point(point.x + dx, point.y + dy) for point in points]

            # Step 3: Plot the original points (blue) and shifted points (red) on the same graph
            plot_points([points, translated_points], ['blue', 'red'])

if __name__ == "__main__":
    main()
