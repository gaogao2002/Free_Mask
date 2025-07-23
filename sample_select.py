import cv2
import numpy as np
import os

def extract_binary_mask(mask, category):
    """
    Extracts the binary mask for the specified category.
    :param mask: Multi-category mask image
    :param category: Category number
    :return: Binary mask
    """
    return (mask == category).astype(np.uint8)

def calculate_iou(mask1, mask2):
    """
    Calculates the IoU (Intersection over Union) for two binary masks.
    :param mask1: The first binary mask
    :param mask2: The second binary mask
    :return: IoU value
    """
    intersection = np.logical_and(mask1, mask2).sum()
    union = np.logical_or(mask1, mask2).sum()
    return intersection / union if union != 0 else 0.0

def process_masks(mask_path1, mask_path2, image_path, iou_threshold, output_dir, num_classes=20):
    """
    Processes multi-category masks, computes IoU, and decides whether to save the image.
    :param mask_path1: Path to the first mask
    :param mask_path2: Path to the second mask
    :param image_path: Path to the image corresponding to the first mask
    :param iou_threshold: IoU threshold
    :param output_dir: Output directory
    :param num_classes: Total number of categories
    """
    # Read mask images
    mask1 = cv2.imread(mask_path1, cv2.IMREAD_GRAYSCALE)
    mask2 = cv2.imread(mask_path2, cv2.IMREAD_GRAYSCALE)
    
    if mask1 is None or mask2 is None:
        print("Failed to read mask images, please check the paths.")
        return
    
    # Initialize IoU list
    ious = []
    
    # Iterate through all categories and compute IoU for each category
    for category in range(1, num_classes + 1):
        binary_mask1 = extract_binary_mask(mask1, category)
        binary_mask2 = extract_binary_mask(mask2, category)
        
        iou = calculate_iou(binary_mask1, binary_mask2)
        ious.append(iou)
        print(f"IoU for category {category}: {iou:.4f}")
    
    # Decide whether to save the image based on the following strategy:
    # Strategy 1: Save the image if any category's IoU exceeds the threshold
    if any(iou >= iou_threshold for iou in ious):
        print("At least one category's IoU exceeds the threshold, saving the image.")
        save_image = True
    else:
        print("All categories have IoU below the threshold, not saving the image.")
        save_image = False
    
    # Strategy 2: Save the image only if all category IoUs exceed the threshold
    # if all(iou >= iou_threshold for iou in ious):
    #     print("All category IoUs exceed the threshold, saving the image.")
    #     save_image = True
    # else:
    #     print("At least one category's IoU is below the threshold, not saving the image.")
    #     save_image = False
    
    # Strategy 3: Save the image if the weighted average IoU of categories exceeds the threshold
    # avg_iou = np.mean(ious)
    # if avg_iou >= iou_threshold:
    #     print(f"Weighted average IoU {avg_iou:.4f} exceeds the threshold, saving the image.")
    #     save_image = True
    # else:
    #     print(f"Weighted average IoU {avg_iou:.4f} is below the threshold, not saving the image.")
    #     save_image = False
    
    # Save the image if required
    if save_image:
        image = cv2.imread(image_path)
        if image is None:
            print("Failed to read the image, please check the path.")
            return
        
        output_path = os.path.join(output_dir, os.path.basename(image_path))
        cv2.imwrite(output_path, image)
        print(f"Image saved to: {output_path}")

# Example usage
mask_path1 = "path/to/first_mask.png"  # Path to the first mask
mask_path2 = "path/to/second_mask.png"  # Path to the second mask
image_path = "path/to/image.jpg"         # Path to the image corresponding to the first mask
iou_threshold = 0.5                      # IoU threshold
output_dir = "path/to/output"            # Output directory

# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)

process_masks(mask_path1, mask_path2, image_path, iou_threshold, output_dir)
