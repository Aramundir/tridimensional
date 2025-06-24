# Poliedro 3D Transformations GUI

A Python project for visualizing and manipulating a 3D polyhedron using Tkinter and Matplotlib. The application allows users to perform geometric transformations such as translation, scaling, and rotation on a predefined 10-point polyhedron.

## Features

- **Interactive GUI** using Tkinter
- **3D Visualization** with Matplotlib
- **Geometric Transformations:**
  - Translate along X, Y, and Z axes
  - Scale independently along X, Y, and Z
  - Rotate around X, Y, or Z axis by any angle
- **Reset** the polyhedron to its original position
- **Exit** the application with a single click

## Structure

The project is split into two main files:

### `portal.py`

- GUI application definition using Tkinter
- Embeds a Matplotlib canvas
- Handles user input and dispatches transformations to the model

### `calculator.py`

- Contains the core logic for 3D transformations
- Defines `Polyhedron` base class
- Implements `TenPointPolyhedron`, a subclass with a specific shape and edges

## Requirements

- Python 3.x
- Tkinter (usually included with Python)
- See `requirements.txt` for specific versions:

```
numpy==1.22.4  
matplotlib==3.5.2
```

## How to Run

1. **Clone or download** this repository.

2. **Create a virtual environment** (optional but recommended):

   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment:**

   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies** using the provided `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```

5. **Run the application:**

   ```bash
   python portal.py
   ```

## Controls

- **Translation:**
  - Enter values for X, Y, and Z
  - Click **"Transladar"**

- **Scaling:**
  - Enter scale factors for X, Y, and Z
  - Click **"Redimensionar"**

- **Rotation:**
  - Enter an angle in degrees
  - Specify axis: `x`, `y`, or `z`
  - Click **"Rotacionar"**

- **Reset:** Click **"Reset"** to restore the original shape

- **Exit:** Click **"Sair"** to close the application

## Notes

- Invalid or empty inputs will default to fallback values.
- The 3D figure is redrawn after every transformation.

## License

This project is provided as-is for educational or personal use. Modify and extend as needed.

```python
# Made with Python
```

