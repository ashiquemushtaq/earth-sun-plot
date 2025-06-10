# Solar Motion Simulator

A Python script that generates an animated visualization of Earth's orbit around the Sun as it moves through space. This project aims to provide a more dynamic and conceptually accurate alternative to common static orrery models.

## About The Project

Standard planetary models often depict a stationary Sun with planets orbiting around it. While useful, this can create a misconception about the nature of our solar system, which is constantly moving through the Milky Way galaxy at immense speed.

This simulator addresses this by modeling the Sun's linear motion. It visualizes Earth's resulting trajectory not as a simple ellipse, but as the complex, wave-like helical path it actually traces through space.

The final animation depicts an "edge-on" perspective. A key feature is the use of a pseudo-3D effect (dynamic layering and sizing) to solve the visual "collision" that occurs in a simple 2D projection, showing the Earth passing realistically in front of and behind the Sun.

### Key Features

* **Dynamic Visualization:** Animates both the Sun's linear motion and Earth's orbit simultaneously.
* **Edge-On Perspective:** Shows the solar system from the side, a common and intuitive viewpoint for this concept.
* **Pseudo-3D Effect:** Prevents visual collisions by adjusting the layering (`z-order`) and size of the Earth to simulate depth and perspective.
* **Built with Python:** Leverages the power of `Matplotlib` for plotting and animation, and `NumPy` for efficient calculations.
* **Customizable:** Easily adjust parameters like orbital radius, speed, and object sizes directly in the script.

## Technologies Used

* [Python](https://www.python.org/)
* [Matplotlib](https://matplotlib.org/)
* [NumPy](https://numpy.org/)

## Getting Started

To get a local copy up and running, follow these simple steps.

### Prerequisites

Make sure you have Python installed. You will need `pip` to install the required libraries.

### Installation & Usage

1.  **Clone the repository:**
    ```sh
    git clone [https://github.com/your-username/your-repository-name.git](https://github.com/your-username/your-repository-name.git)
    ```
2.  **Navigate to the project directory:**
    ```sh
    cd your-repository-name
    ```
3.  **Install required packages:**
    ```sh
    pip install matplotlib numpy
    ```
4.  **Run the script:**
    ```sh
    python solar_motion_simulator.py
    ```
    An interactive window should appear displaying the animation.

## License

Distributed under the MIT License. See `LICENSE` for more information.
