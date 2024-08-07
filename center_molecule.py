import numpy as np

# Define the input and output file names and box size
input_file = "trajec.xyz"
output_file = "centered_structure.xyz"
box_size = 15.0  # Box size in Å

# Load your structure file (assuming it's in XYZ format)
with open(input_file, "r") as file:
    lines = file.readlines()

# Initialize variables
frames = []
i = 0

# Read through lines to extract frames
while i < len(lines):
    if lines[i].strip().isdigit():  # Number of atoms line
        num_atoms = int(lines[i].strip())
        title = lines[i + 1].strip()
        atom_types = []
        coordinates = []

        for j in range(num_atoms):
            parts = lines[i + 2 + j].split()
            if len(parts) == 4:
                atom_types.append(parts[0])
                x = float(parts[1])
                y = float(parts[2])
                z = float(parts[3])
                coordinates.append([x, y, z])
            else:
                print(f"Warning: Skipping line due to incorrect format: {lines[i + 2 + j].strip()}")

        # Convert coordinates to NumPy array for easier manipulation
        coordinates = np.array(coordinates)

        # Calculate the center of mass of the molecule
        center_of_mass = np.mean(coordinates, axis=0)

        # Calculate the shift needed to center the molecule within the periodic boundary conditions
        shift = np.array([box_size / 2, box_size / 2, box_size / 2]) - center_of_mass

        # Shift coordinates to center the molecule within the periodic boundary conditions
        coordinates_shifted = coordinates + shift

        # Store the frame data
        frames.append((num_atoms, title, atom_types, coordinates_shifted))

        # Move to the next frame
        i += 2 + num_atoms
    else:
        print(f"Warning: Skipping unexpected line: {lines[i].strip()}")
        i += 1

# Save the modified trajectory in XYZ format
with open(output_file, "w") as file:
    for num_atoms, title, atom_types, coordinates_shifted in frames:
        file.write(f"{num_atoms}\n")
        file.write(f"{title}\n")
        for k in range(num_atoms):
            atom_line = f"{atom_types[k]} {coordinates_shifted[k][0]:.3f} {coordinates_shifted[k][1]:.3f} {coordinates_shifted[k][2]:.3f}\n"
            file.write(atom_line)

