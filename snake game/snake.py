"""
Snake class for Snake Game
Handles snake creation, movement, and controls
"""
from turtle import Turtle

# Game constants
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    """Represents the snake in the game with movement and growth capabilities"""

    def __init__(self):
        """Initialize snake with starting segments and set head reference"""
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]  # Reference to the first segment (head)

    def create_snake(self):
        """Create initial snake body at starting positions"""
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        """Add a new segment to the snake at specified position"""
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def reset(self):
        """Reset snake to initial positions"""
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]  # Reference to the first segment (head)


    def extend(self):
        """Add a new segment to the end of the snake (when eating food)"""
        self.add_segment(self.segments[-1].position())

    def move(self):
        """Move snake forward by updating each segment's position"""
        # Move body segments (from tail to head)
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        # Move head forward
        self.head.forward(MOVE_DISTANCE)

    # Direction control methods with anti-reverse logic
    def up(self):
        """Turn snake upward if not currently moving down"""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """Turn snake downward if not currently moving up"""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """Turn snake left if not currently moving right"""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """Turn snake right if not currently moving left"""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)