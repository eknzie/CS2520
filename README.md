# Taylor Series Approximation for Sine and Cosine

This repository contains a Python application that demonstrates the Taylor series approximation for sine and cosine functions. The program calculates approximations, computes errors, and visualizes the convergence of the Taylor series using a graphical user interface (GUI) built with Tkinter.

## Features
- **Compute Taylor Series Approximation**: Approximates sine and cosine values based on user-defined input.
- **Error Calculation**: Displays absolute and relative errors compared to Python's built-in `math.sin` and `math.cos`.
- **Graphical Visualization**: Plots the absolute errors against the number of terms used in the approximation.
- **Interactive GUI**: Users can enter angle values and the number of terms for computation.

## Installation
Ensure you have Python installed on your system (Python 3 recommended). Then, install the required dependencies:

```bash
pip install numpy matplotlib
```

## Usage
Run the script using:

```bash
python taylor_series_gui.py
```

### Inputs:
- **Angle (degrees)**: The angle for which sine and cosine approximations will be calculated.
- **Number of Terms**: The number of terms in the Taylor series expansion.

### Outputs:
- Approximated sine and cosine values.
- Absolute and relative errors.
- A plot showing the absolute error convergence.

## Example
If you input:
- Angle: `30`
- Number of Terms: `5`

The program will compute and display:
```
Sine Approximation: 0.499674
Cosine Approximation: 0.866753
Absolute Errors: Sine 0.000326, Cosine 0.000257
Relative Errors: Sine 0.000653, Cosine 0.000297
```
Additionally, a plot will be generated showing how the approximation error decreases as more terms are included.

## File Structure
```
├── taylor_series_gui.py   # Main script
├── README.md             # Documentation
```

## License
This project is open-source and available under the MIT License.

## Contributions
Contributions and suggestions are welcome! Feel free to submit pull requests or issues to improve the program.

## Author
Developed by Kenzie.
