import os
from openai import OpenAI

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])



response = client.chat.completions.create(model="gpt-3.5-turbo",
messages=[{"role": "system", "content": 'You are a code generator for a robot. The robot uses a custom-made position class. Here is the documentation for that. The Position class is a utility for representing and manipulating 3D positions in a Cartesian coordinate system, with methods to initialize, update, and retrieve the position. It has three attributes: x, y, and z, representing the position along the left-right, forward-backward, and up-down axes, respectively. The constructor __init__(self, x=0, y=0, z=0) initializes a new instance with the specified x, y, and z coordinates, defaulting to 0 if not specified. The update method allows updating any of the x, y, or z values; if a value is provided, the corresponding coordinate is updated, while None leaves it unchanged. The get_pos method retrieves the current position as a tuple of its x, y, and z coordinates. The __str__ method provides a human-readable string representation of the object, displaying the values of x, y, and z coordinates. This class is useful in applications requiring 3D spatial representation, such as graphics, simulations, or robotics, though it does not include advanced operations like distance calculations or transformations. Example usage includes creating a new Position object at the origin, updating the position, retrieving and printing the current position, and printing the string representation of the position. You also need to know how to use the move_to_point function. it accepts a position as an argument. You will recieve a set of coordinates, and must return a move_to_point function that has the point passed through it. Example: Passed: Point = (10, 0, 0) Returns: move_to_point(Position(10, 0, 0))'},
          {"role": "user", "content": 'Point = (10, 0, 0)'}
])