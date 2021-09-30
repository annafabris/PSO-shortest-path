import math

class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y

class Obstacle_Circle:
    """
    This is a class to implement an obstacle of circular shape.
      
    Attributes:
        r (int): the radius of the circle.
        C (Point): Center of the circle.

    """

    def __init__(self, r, C):
         self.r = r
         self.C = C

    def inside_circle(self, p):
        """
        The function to check if point p lies inside the circle.
  
        Parameters:
            p (Point): Point to check.
          
        Returns:
            boolean: Wheter the point is inside the circle or not.
        """

        return (p.x - self.C.x)**2 + (p.y - self.C.y)**2 <= self.r**2
    
    def how_to_exit_y(self, y):
        """
        The function helps the point inside the circe to exit (coordiante y).
  
        Parameters:
            y (int): Coordinate y of point to check.
          
        Returns:
            int: y distance between point and center.
        """

        return y - self.C.y
    
    def how_to_exit_x(self, x):
        """
        The function helps the point inside the circe to exit (coordiante x).
         
        Parameters:
            x (int): Coordinate x of point to check.
        
        Returns:
            int: x distance between point and center.
        """

        return x - self.C.x    

    def segment_in_circle(self, p, q):
        """
        The function checks if the segment intersect the circle.
         
        Parameters:
            p (int): The first vertex of the segment.
            q (int): The second vertex of the segment.
        
        Returns:
            boolean: if the segment intersect the circle.
        """

        a, b, c = lineFromPoints(p, q)

        # Checking if the distance of line from the center is less than the radius.
        if (self.r > ((abs(a * self.C.x + b * self.C.y + c)) / math.sqrt(a * a + b * b))):
            return True
        else:
            return False
    
def lineFromPoints(p, q):
    """
    The function checks if the segment intersect the circle.
     
    Parameters:
        p (Point): The first vertex of the segment.
        q (Point): The second vertex of the segment.
    
    Returns:
        boolean: if the segment intersect the circle
        boolean: if the segment intersect the circle
        boolean: if the segment intersect the circle
    """

    a = q.y - p.y
    b = p.x - q.x
    c = a*(p.x) + b*(p.y)
    return a, b, c
