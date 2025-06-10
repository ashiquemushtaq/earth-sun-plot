import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

orbit_radius = 5.0
sun_size = 150
earth_size = 40
animation_frames = 720
animation_interval = 20
sun_initial_x = -orbit_radius * 4
sun_velocity_x = 0.08

# To trace Earth's absolute path
earth_path_x = []
earth_path_y = []

# --- Set up the figure and axis ---
fig, ax = plt.subplots(figsize=(14, 7))
ax.set_aspect('equal', 'box')
ax.set_ylim(-orbit_radius * 2.5, orbit_radius * 2.5)

# Set a wide, static background that does NOT move
total_sun_travel = sun_velocity_x * animation_frames
ax.set_xlim(sun_initial_x - orbit_radius, sun_initial_x + total_sun_travel + orbit_radius * 2)

ax.set_title("Earth's Orbit Around a Moving Sun (Pseudo-3D View)")
ax.set_xlabel("X-coordinate (Direction of Solar System Travel)")
ax.set_ylabel("Y-coordinate (Apparent 'Up/Down' Motion)")
ax.grid(True, linestyle='--', alpha=0.7)

# --- Sun (initial position) ---
# zorder=5 means the Sun is on layer 5
sun, = ax.plot([sun_initial_x], [0], marker='o', markersize=np.sqrt(sun_size), color='gold', label="Sun", zorder=5)
sun_current_x = sun_initial_x

# --- Earth (initial position) ---
earth, = ax.plot([sun_current_x], [orbit_radius], marker='o', markersize=np.sqrt(earth_size), color='dodgerblue', label="Earth", zorder=10)

# --- Earth's absolute path line ---
earth_absolute_path_line, = ax.plot([], [], color='cyan', linestyle='-', linewidth=1.0, label="Earth's Absolute Path", zorder=2)

# --- Animation function ---
def animate(i):
    global sun_current_x

    # Update Sun's position
    sun_current_x += sun_velocity_x
    sun.set_data([sun_current_x], [0])

    # Update Earth's position relative to the Sun
    angle = (i / (animation_frames / 2)) * 2 * np.pi
    earth_current_x = sun_current_x
    earth_current_y = orbit_radius * np.cos(angle)
    earth.set_data([earth_current_x], [earth_current_y])
    
    # Simulate a 3rd dimension (depth) using another trigonometric function
    # sin(angle) will be -1 or 1 when cos(angle) is 0 (at the 'collision' point)
    z_dimension = np.sin(angle)
    
    if z_dimension > 0:
        # Earth is "in front" of the Sun
        earth.set_zorder(10) # Render on a layer above the Sun (zorder=5)
        earth.set_markersize(np.sqrt(earth_size) * 1.1) # Appear slightly larger
    else:
        # Earth is "behind" the Sun
        earth.set_zorder(4) # Render on a layer below the Sun
        earth.set_markersize(np.sqrt(earth_size) * 0.9) # Appear slightly smaller

    # Append to Earth's absolute path
    earth_path_x.append(earth_current_x)
    earth_path_y.append(earth_current_y)
    earth_absolute_path_line.set_data(earth_path_x, earth_path_y)

    return sun, earth, earth_absolute_path_line,

# --- Create and run the animation ---
ax.legend(loc='upper right')
ani = animation.FuncAnimation(fig, animate, frames=animation_frames,
                              interval=animation_interval, blit=True, repeat=False)

plt.tight_layout()
plt.show()
