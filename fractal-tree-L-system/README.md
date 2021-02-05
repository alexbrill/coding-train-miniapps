# Fractal Tree

Visualization of L-system 

![](https://camo.githubusercontent.com/33112f9269a876af00e8bf63af3b9eb6f2f70dd43a2678aa557d01f84c2b204e/68747470733a2f2f70702e757365726170692e636f6d2f633834353031372f763834353031373731312f39643231352f71686436485541624d4c302e6a7067)

| Case | |
| ----- | -----|
| 1 | variables : X F <br> constants : + − [ ] <br> start : X <br> rules : (X → F+[[X]-X]-F[-FX]+X), (F → FF) <br> angle : 25°|
| 2 | case 2: variables : F <br> constants : + − [ ] <br> start : F <br> rules : FF+[+F-F-F]-[-F+F+F] <br> angle : 25° <br> |

* F means "draw forward"
* − means "turn left 25°"
* , and + means "turn right 25°"
* X does not correspond to any drawing action
  and is used to control the evolution of the curve.
* The square bracket "[" corresponds to saving the current 
  values for position and angle, which are restored when 
  the corresponding "]" is executed.
  
### Controls

* Space - start





