import numpy as np
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import ttk
import math

def taylor_sine(x, n_terms):
    """Calculate sine using the Taylor series approximation."""
    sine_approx = 0
    for n in range(n_terms):
        term = ((-1)**n * x**(2*n + 1)) / math.factorial(2*n + 1)
        sine_approx += term
    return sine_approx

def taylor_cosine(x, n_terms):
    """Calculate cosine using the Taylor series approximation."""
    cosine_approx = 0
    for n in range(n_terms):
        term = ((-1)**n * x**(2*n)) / math.factorial(2*n)
        cosine_approx += term
    return cosine_approx

def calculate_errors(angle_rad, n_terms):
    """Calculate the absolute and relative errors."""
    true_sine = math.sin(angle_rad)
    true_cosine = math.cos(angle_rad)
    
    approx_sine = taylor_sine(angle_rad, n_terms)
    approx_cosine = taylor_cosine(angle_rad, n_terms)
    
    error_sine_abs = abs(true_sine - approx_sine)
    error_cosine_abs = abs(true_cosine - approx_cosine)
    
    error_sine_rel = error_sine_abs / abs(true_sine) if true_sine != 0 else 0
    error_cosine_rel = error_cosine_abs / abs(true_cosine) if true_cosine != 0 else 0
    
    return (error_sine_abs, error_cosine_abs, error_sine_rel, error_cosine_rel)

def plot_errors(angle_rad):
    """Plot errors against the number of terms."""
    terms = np.arange(1, 21)
    errors_sine = [calculate_errors(angle_rad, n)[0] for n in terms]
    errors_cosine = [calculate_errors(angle_rad, n)[1] for n in terms]
    
    plt.figure(figsize=(10, 5))
    plt.plot(terms, errors_sine, label='Sine Absolute Error', marker='o')
    plt.plot(terms, errors_cosine, label='Cosine Absolute Error', marker='x')
    plt.xlabel('Number of Terms')
    plt.ylabel('Absolute Error')
    plt.title('Taylor Series Approximation Error')
    plt.legend()
    plt.grid(True)
    plt.show()

def compute_and_display():
    """Compute values and display results."""
    try:
        angle = float(entry_angle.get())
        n_terms = int(entry_terms.get())
        angle_rad = np.radians(angle)
        
        approx_sine = taylor_sine(angle_rad, n_terms)
        approx_cosine = taylor_cosine(angle_rad, n_terms)
        errors = calculate_errors(angle_rad, n_terms)
        
        result_sine.set(f"Sine Approximation: {approx_sine:.6f}")
        result_cosine.set(f"Cosine Approximation: {approx_cosine:.6f}")
        error_abs.set(f"Absolute Errors: Sine {errors[0]:.6f}, Cosine {errors[1]:.6f}")
        error_rel.set(f"Relative Errors: Sine {errors[2]:.6f}, Cosine {errors[3]:.6f}")
        
        plot_errors(angle_rad)
    
    except ValueError:
        result_sine.set("Invalid input!")
        result_cosine.set("")
        error_abs.set("")
        error_rel.set("")

# Setting up the GUI
root = Tk()
root.title("Taylor Series Approximation")
root.geometry("400x300")

frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(N, W, E, S))

ttk.Label(frame, text="Angle (degrees):").grid(row=1, column=1, sticky=W)
entry_angle = ttk.Entry(frame, width=10)
entry_angle.grid(row=1, column=2, sticky=(W, E))

ttk.Label(frame, text="Number of Terms:").grid(row=2, column=1, sticky=W)
entry_terms = ttk.Entry(frame, width=10)
entry_terms.grid(row=2, column=2, sticky=(W, E))

ttk.Button(frame, text="Compute", command=compute_and_display).grid(row=3, column=2, sticky=W)

result_sine = StringVar()
ttk.Label(frame, textvariable=result_sine).grid(row=4, column=1, columnspan=2, sticky=W)

result_cosine = StringVar()
ttk.Label(frame, textvariable=result_cosine).grid(row=5, column=1, columnspan=2, sticky=W)

error_abs = StringVar()
ttk.Label(frame, textvariable=error_abs).grid(row=6, column=1, columnspan=2, sticky=W)

error_rel = StringVar()
ttk.Label(frame, textvariable=error_rel).grid(row=7, column=1, columnspan=2, sticky=W)

root.mainloop()
