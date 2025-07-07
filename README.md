
# FiniteDifferenceMethodSphere
Solving heat conduction equation (PDE) on a sphere using the Finite Difference Method (FDM) method


<p>
  The heat equation in Cartesian coordiantes reads as:
  <img src="images/Heat equation.png" alt="Heat equation Cartesian Coordinates" width="300" align="center" style="margin-left: 20px; margin-bottom: 10px;" />
  
  
</p>

If we project it to spherical coordinates (assuming u=0):
  <img src="images/Energy equation in Spherical coordinates.png" alt="Heat equation Spherical Coordinates" width="300" align="center" style="margin-left: 20px; margin-bottom: 10px;" />






This script was coded using PyCharm using Python 3.12. It uses basic libraries such as numpy, math and matplotlib.

Requirements:
Python 3.12 or higher installed on your machine
Numpy, math and matplotlib

If some of these libraries weren't available on your system, try typing:

Numpy: pip install numpy
Math: pip install math
Matplotlib: pip install matplotlib

To execute the code:
Open a terminal on the location of the script and type: python '.\temperature distribution of a sphere.py'
If this doesn't work, try typing: python temp (and press Tab)

To change the different constants:
Open the script on your text editor or IDE of choice and change the values encapsulated in the Parameters section of the
code. Then save the script and rerun it.
