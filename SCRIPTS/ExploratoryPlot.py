'''
Fruit Image Exploratory Histograms
    The purpose of this script is to generate initial exploratory plots for each fruit in the dataset. It generates histograms for each fruit that demonstrate the degrees of freshness
    or spoiledness. 
    To run this code, you need the cv2, os, numpy, and matplotlib libraries, as well as have the fresh and spoiled folders for each fruit downloaded in the specified folder.
'''

import cv2 #install using pip install opencv-python==4.5.5.64
import os
import numpy as np
import matplotlib.pyplot as plt

data_dir = "data"
output_dir = "output/exploratory"
os.makedirs(output_dir, exist_ok=True)

fruit_types = ["banana", "lemon", "lulo", "mango", "orange", "strawberry", "tamarillo", "tomato"]
freshness_types = ["fresh", "spoiled"]

# Function to compute average color channels for a single image
def calculate_average_color(image_path):
    image = cv2.imread(image_path)
    # Convert BGR (OpenCV default) to RGB
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    # Compute mean of each channel (R, G, B)
    avg_color_per_channel = np.mean(image_rgb, axis=(0, 1))
    return avg_color_per_channel

# Dictionary to store average color values by fruit type and freshness
average_colors = {fruit: {freshness: [] for freshness in freshness_types} for fruit in fruit_types}

# Process each image and store average color values
for fruit in fruit_types:
    for freshness in freshness_types:
        folder_path = os.path.join(data_dir, fruit, freshness)
        for filename in os.listdir(folder_path):
            image_path = os.path.join(folder_path, filename)
            avg_color = calculate_average_color(image_path)
            average_colors[fruit][freshness].append(avg_color)

# Plot histograms for each fruit type and freshness and save them to the output folder
for fruit in fruit_types:
    # Create a new figure for each fruit
    plt.figure(figsize=(8, 6))
    
    # Prepare RGB averages for fresh and spoiled samples
    fresh_colors = np.array(average_colors[fruit]["fresh"])
    spoiled_colors = np.array(average_colors[fruit]["spoiled"])

    # Plot histogram for each color channel
    plt.hist(fresh_colors[:, 0], bins=30, color='red', alpha=0.5, label='Fresh - Red')
    plt.hist(spoiled_colors[:, 0], bins=30, color='darkred', alpha=0.5, label='Spoiled - Red')
    plt.hist(fresh_colors[:, 1], bins=30, color='green', alpha=0.5, label='Fresh - Green')
    plt.hist(spoiled_colors[:, 1], bins=30, color='darkgreen', alpha=0.5, label='Spoiled - Green')
    plt.hist(fresh_colors[:, 2], bins=30, color='blue', alpha=0.5, label='Fresh - Blue')
    plt.hist(spoiled_colors[:, 2], bins=30, color='darkblue', alpha=0.5, label='Spoiled - Blue')

    plt.title(f"Average Color Histogram for {fruit.capitalize()}")
    plt.xlabel("Average Color Intensity")
    plt.ylabel("Frequency")
    plt.legend(loc='upper right')
    
    # Save the plot
    plt.tight_layout()
    output_path = os.path.join(output_dir, f"{fruit}_average_color_histogram.png")
    plt.savefig(output_path)
    plt.close()  # Close the plot to save memory

print("Histograms saved in the output folder.")
