
<div align="center">
    <h1>Virtual Cube</h1>
    <p><strong>Virtual 3D Rubik's Cube using pygame</strong></p>


![image](https://github.com/user-attachments/assets/8eb2a847-7a48-48b1-9dea-5e6f74b70cba)
</div>
<hr>  

> [!IMPORTANT]
> You need to have Python installed on your system in order to run Virtual Cube.  
> You can download it [here](https://www.python.org/downloads/).  
> If you are still unable to run it, try specfically downloading version 3.12.4.

Requires modules pygame and numpy. If they are not already installed, the program will install them on your system with `os.system()`.  

`config.py` contains the constants needed to run `main.py`. To change any settings of Virutal Cube, you can edit `config.py`'s settings to your desire.

### Instructions  
<ul>
  <li>Click and drag with your mouse/touchpad/touchscreen to rotate/look around the cube</li>
  <li>Use the F, B, L, R, U, and D keys to move</li>
  <li>F = Front, B = Back, L = Left, R = Right, U = Up, D = Down</li>
  <li>Each move is clockwise when looking directly at the face you are turning</li>
  <li>To execute a prime move (counterclockwise move), hold shift while moving a face</li>
  <li>Adding support for slice moves (M, E, and S) soon</li>
</ul>
 
### Report Issues  
If you encounter an issue with Virtual Cube, open an issue on Github.  
If you are unsure on how to open a issue, see [this link](https://docs.github.com/en/issues/tracking-your-work-with-issues/quickstart).

### How does it work?

Virtual Cube uses raycasting to generate a 2D projection of the 3D rubik's cube.

[Rotation matrices source](https://en.wikipedia.org/wiki/Rotation_matrix#In_three_dimensions)  
[Raycasting source](https://en.wikipedia.org/wiki/Ray_casting)  
[Projection diagram](https://en.wikipedia.org/wiki/Ray_tracing_(graphics)#/media/File:Ray_trace_diagram.svg)

To calculate projections, these formulas are used:  

$$ \text{projected x} = \frac{\text{focal length }(\text{vertex x} - \text{camera x})}{\text{focal length} + \text{vertex z}} + \text{camera x} $$  
  
$$ \text{projected y} = \frac{\text{focal length }(\text{vertex y} - \text{camera y})}{\text{focal length} + \text{vertex z}} + \text{camera y} $$  

All projections are calculated AFTER rotation (below).

To rotate the cube/faces, this formula is used:  

$$
\begin{bmatrix}
x' & y' & z'
\end{bmatrix} = 
\left( 
\begin{bmatrix}
x & y & z
\end{bmatrix} - 
\begin{bmatrix}
r_x & r_y & r_z
\end{bmatrix} 
\right) \cdot 
\begin{bmatrix}
1 & 0 & 0 \\
0 & \cos(\theta_x) & -\sin(\theta_x) \\
0 & \sin(\theta_x) & \cos(\theta_x)
\end{bmatrix} \cdot 
\begin{bmatrix}
\cos(\theta_y) & 0 & \sin(\theta_y) \\
0 & 1 & 0 \\
-\sin(\theta_y) & 0 & \cos(\theta_y)
\end{bmatrix} \cdot 
\begin{bmatrix}
\cos(\theta_z) & -\sin(\theta_z) & 0 \\
\sin(\theta_z) & \cos(\theta_z) & 0 \\
0 & 0 & 1
\end{bmatrix} + 
\begin{bmatrix}
r_x & r_y & r_z
\end{bmatrix}
$$

where $θ_x$, $θ_y$, and $θ_z$ represent rotation in degrees, and $r_x$, $r_y$, and $r_z$ represent the x, y, and z coordinates of the center of rotation.

This works by translating each vertex so that the center of rotation is on the origin, multiplying by all 3 rotation matrices, and then translating the vertex back.

The rubik's cube is represented as 54 squares, each corresponding to a color on the rubik's cube. To draw the cube, the rotation from looking around the cube is applied to each square and saved. Each square is sorted by its average Z coordinate, and then drawn from farthest to closest. Lines are drawn around the square to clearly define borders.  

Turning the faces of the cube is slightly more difficult. There are 26 cubelets on the cube (excluding the middle one), and each cubelet is linked to its corresponding squares. When rotating a face, the program selects which cubelets to rotate, which is used to determine which squares to rotate. The selected squares are rotated
a certain number of times around the middle of the face by a certain number of degrees such that the number of degrees per turn times the number of turns is equal to 90. The squares are rounded to the nearest integer, and the cubelets are also rotated and rounded in one go by 90 degrees.  

Before turning the face, 2 additional squares are added to the rubik's cube that are removed after the turn is complete.
