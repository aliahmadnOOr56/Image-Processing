import os
import csv
import numpy as np
from skimage import io, color, filters, morphology, measure, segmentation
from skimage.transform import rotate

RAW_BASE_DIR = "../RawImages/"
OUTPUT_DIR = "../GrainImages/"
os.makedirs(OUTPUT_DIR, exist_ok=True)

FEATURES_CSV = os.path.join("../", "metadata.csv")

PIXEL_TO_MM = 0.1  

with open(FEATURES_CSV, mode="w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow([
        "Grain_Name", "Variety", "Image_Base",
        "Height_mm", "Width_mm", "Orientation_deg",
        "Mean_Gray", "Mean_R", "Mean_G", "Mean_B"
    ])

grain_count = 0  

for variety in os.listdir(RAW_BASE_DIR):
    variety_path = os.path.join(RAW_BASE_DIR, variety)

    if not os.path.isdir(variety_path):
        continue

    img_list = [f for f in os.listdir(variety_path) if f.lower().endswith((".jpg", ".png", ".jpeg"))]
    total_images = len(img_list)

    for img_idx, img_name in enumerate(img_list, 1):
        image_path = os.path.join(variety_path, img_name)
        image_base = os.path.splitext(img_name)[0]  # remove extension

        image = io.imread(image_path)
        gray = color.rgb2gray(image)

        thresh = filters.threshold_otsu(gray)
        binary = gray > thresh

        if np.mean(binary) > 0.5:
            binary = ~binary

        binary = morphology.remove_small_objects(binary, min_size=400)
        binary = morphology.remove_small_holes(binary, area_threshold=400)

        binary = segmentation.clear_border(binary)

        labels = measure.label(binary)
        regions = measure.regionprops(labels)

        if len(regions) == 0:
            print(f"variety: {variety} | image {img_idx}/{total_images} | total extraction: {grain_count}")
            continue

        # Identify coin (largest area)
        areas = [r.area for r in regions]
        coin_index = np.argmax(areas)

        grains_in_image = 0
        for i, region in enumerate(regions):
            if i == coin_index:
                continue
            if region.area < 500:
                continue
            if region.eccentricity < 0.8:
                continue

            minr, minc, maxr, maxc = region.bbox
            grain_gray = gray[minr:maxr, minc:maxc]

            height_mm = (maxr - minr) * PIXEL_TO_MM
            width_mm = (maxc - minc) * PIXEL_TO_MM
            orientation_deg = -region.orientation * (180 / np.pi)

            grain_rotated = rotate(grain_gray, orientation_deg, resize=True)

            margin = 5
            r_min = max(0, 0 + margin)
            r_max = grain_rotated.shape[0] - margin
            c_min = max(0, 0 + margin)
            c_max = grain_rotated.shape[1] - margin
            grain_rotated_cropped = grain_rotated[r_min:r_max, c_min:c_max]

            if len(image.shape) == 3 and image.shape[2] == 3:
                grain_rgb = image[minr:maxr, minc:maxc]
                mean_r = np.mean(grain_rgb[:, :, 0])
                mean_g = np.mean(grain_rgb[:, :, 1])
                mean_b = np.mean(grain_rgb[:, :, 2])
            else:
                mean_r = mean_g = mean_b = np.mean(grain_gray)

            grain_count += 1
            grains_in_image += 1
            grain_name = f"{image_base}_Grain_{grain_count:04d}.jpg"
            io.imsave(
                os.path.join(OUTPUT_DIR, grain_name),
                (grain_rotated_cropped * 255).astype(np.uint8)
            )

            with open(FEATURES_CSV, mode="a", newline="") as f:
                writer = csv.writer(f)
                writer.writerow([
                    grain_name, variety, image_base,
                    height_mm, width_mm, orientation_deg,
                    np.mean(grain_rotated_cropped), mean_r, mean_g, mean_b
                ])

        print(f"variety: {variety} | image {img_idx}/{total_images} | total extraction: {grain_count}")

print("\nTotal grains extracted:", grain_count)
print(f"Features saved in: {FEATURES_CSV}")
