
<div align="center">
    <h1>Virtual Cube</h1>
    <p><strong>A virtual 3D Rubik's Cube using pygame without any external 3D engine.</strong></p>


![image](https://github.com/user-attachments/assets/8eb2a847-7a48-48b1-9dea-5e6f74b70cba)
</div>
<hr>  

> [!IMPORTANT]
> You need to have Python installed on your system in order to run Virtual Cube.  
> You can download it [here](https://www.python.org/downloads/).  
> If you are still unable to run it, try specfically downloading version 3.12.4.

Requires modules pygame and numpy. If they are not installed, the program will install them on your system with `os.system()`.  

`config.py` contains the constants needed to run `main.py`. To change any settings of Virutal Cube, you can edit `config.py`'s settings to your desire.

## Instructions
<ul>
  <li>Click and drag with your mouse/touchpad/touchscreen to rotate/look around the cube</li>
  <li>Use the F, B, L, R, U, and D keys to move</li>
  <li>F = Front, B = Back, L = Left, R = Right, U = Up, D = Down</li>
  <li>Each move is clockwise when looking directly at the face you are turning</li>
  <li>To execute a prime move (counterclockwise move), hold shift while moving a face</li>
</ul>

## Download
<ol>
    <li>Download the latest stable version of Python 3.X from https://www.python.org/downloads/ if you haven't already done so. (This was made with Python 3.12.4)</li>
    <li>Download this repository as a .zip file.</li>
    <li>Extract the .zip into a folder.</li>
    <li>Run main.py from the terminal, IDLE, or any other IDE/text editor that supports Python.</li>
</ol>

## How does it work?

*This section might not render properly on some devices.*  

Virtual Cube uses raycasting to generate a 2D projection of the 3D Rubik's cube. 

[Rotation matrices source](https://en.wikipedia.org/wiki/Rotation_matrix#In_three_dimensions)  
[Raycasting source](https://en.wikipedia.org/wiki/Ray_casting)  
[Projection diagram](https://en.wikipedia.org/wiki/Ray_tracing_(graphics)#/media/File:Ray_trace_diagram.svg)

To calculate projections, these formulas are used:  

$$ \text{projected x} = \frac{\text{focal length }(\text{vertex x} - \text{camera x})}{\text{focal length} + \text{vertex z}} + \text{camera x} $$  
  
$$ \text{projected y} = \frac{\text{focal length }(\text{vertex y} - \text{camera y})}{\text{focal length} + \text{vertex z}} + \text{camera y} $$  

To rotate, I used rotation matrices instead of quaternions:

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

where $θ_x$, $θ_y$, and $θ_z$ represent the rotation in degrees, and $r_x$, $r_y$, and $r_z$ represent the x, y, and z coordinates of the center of rotation.  

The rubik's cube is represented as 54 squares, each corresponding to a color on the rubik's cube. To draw the cube, the rotation from looking around the cube is applied to each square and saved. Each square is sorted by its average Z coordinate, and then drawn from farthest to closest. Lines are drawn around the square to clearly define borders.  

*The code for executing a turn is located in `turn()` in `main.py`. The code for drawing the cube, along with other things like the start screen, FPS, and buttons, is located in `drawAll()`.*

Side note: Yes the `cubelets` code is far longer than it needs to be but again I'm too lazy to fix it 💀

## Report Issues  
If you encounter an issue with Virtual Cube, open an issue on Github.  
If you are unsure on how to open a issue, see [this link](https://docs.github.com/en/issues/tracking-your-work-with-issues/quickstart).

