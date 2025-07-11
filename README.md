
# FiniteDifferenceMethodSphere
Solving heat conduction equation (PDE) on a sphere using the Finite Difference Method (FDM) method


<p>
  The heat equation in Cartesian coordiantes reads as:
  <img src="images/Heat equation.png" alt="Heat equation Cartesian Coordinates" width="300" align="center" style="margin-left: 20px; margin-bottom: 10px;" />
  
  

If we project it to spherical coordinates (assuming u=0):
  <img src="images/Energy equation in Spherical coordinates.png" alt="Heat equation Spherical Coordinates" width="300" align="center" style="margin-left: 20px; margin-bottom: 10px;" />

The initial conditions are: 
<img src="images/Initial conditions.png" alt="Initial conditions" width="300" align="center" style="margin-left: 20px; margin-bottom: 10px;" />

And as boundary conditions we set that the sphere is subjected to convection in its outer shell, encoded by the equation: 
<img src="images/Boundary conditions (convection).png" alt="Boundary conditions" width="300" align="center" style="margin-left: 20px; margin-bottom: 10px;" />


This script was coded using PyCharm using Python 3.12. It uses basic libraries such as numpy, math and matplotlib.


</p><img width="634" height="691" alt="Flow chart" src="https://github.com/user-attachments/assets/d08a15de-e53e-490c-abf3-aef433ed1c1c" />




To change the different constants:
Open the script on your text editor or IDE of choice and change the values encapsulated in the Parameters section of the
code. Then save the script and rerun it.
