# Free-Mask: A Novel Paradigm of Integration Between the Segmentation Diffusion Model and Image Editing

[**📄 Paper**](https://doi.org/10.1145/XXXXXX.XXXXXX) | [**🔗 Project Page**](https://github.com/gaogao2002/Free-Mask)  
Authors: Bo Gao, Jianhui Wang, Xinyuan Song, Yangfan He, Fangxu Xing, Tianyu Shi

## 📌 Overview

**Free-Mask** is a novel framework for generating high-quality synthetic segmentation datasets via the integration of **segmentation-aware diffusion models** and **image editing techniques**. It enables **multi-instance generation**, **mask refinement**, and **iterative data improvement** without relying on manual annotations.

<p align="center">
  <img src="picture/frame.pdf" />
</p>

## ✨ Key Features

- 🎯 Supports **multi-object composition** with accurate masks.
- 🧠 Introduces **Adaptive Matching Thesaurus** for semantic-aware object placement.
- 📐 Employs **FOPA** for spatially consistent foreground placement.
- 🎨 Integrates **image harmonization** to improve visual consistency.
- 🔁 Proposes a new **adversarial active learning loop** to iteratively filter and optimize data.
- 📈 Outperforms existing methods (e.g., DiffuMask, Dataset Diffusion) in mIoU across multiple benchmarks.

## 📁 Project Structure

```
Free-Mask/
├── single_image_mask_generation/   # Generate single-object images and masks
├── class_relation/                 # Foreground-background relationship mapping
├── FOPA/                           # Object placement module
├── post_refine/                    # Mask refinement via AffinityNet
├── image_harmony/                  # Image harmonization for visual consistency
├── segmentation/                  # Mask2Former training code
├── data/                          # Generated datasets
└── README.md
```

## 🚀 How to Use

### 1. Generate Single-Object Image and Mask

- Use the **single_image_mask_generation** module to generate single-class images and masks.
- This process uses diffusion masks and does not require additional training.

### 2. Foreground-Background Relationship Mapping

- Use a table to map the primary relationships between foreground and background. The code for this is located at: `class_relation`.

### 3. Generate Multi-Object Image and Mask Using FOPA

- Use **FOPA** (Flexible Object Placement Algorithm) to determine the placement of objects. This will convert the original single-object image and mask into multi-object images and masks.

### 4. Image Refinement

- Use **affinity** to refine the generated images. The code for this process is located at: `post_refine`. This step follows the original method described in the paper.

### 5. Harmonious Adjustment of Image and Mask

- Use **image_harmony** to harmonize the generated image. Note: This step may not run on some GPU configurations (e.g., A100, 4090). It is recommended to use a 3090 GPU for this operation.

### 6. Iterative Training

#### 6.1 Configuration

- Use 8 GPUs (3090 or A100) for training, with an estimated training time of about one week.

#### 6.2 Training Process

1. **Generate Images and Masks**: Follow steps 1-5 to generate images (I) and masks (M).
2. **Obtain Segmentation Results**: Use a high-quality segmentation model (e.g., Mask2Former) to segment the images and obtain the Ground Truth (GT).
3. **Calculate IOU**: Compute the Intersection over Union (IOU) between the generated mask (M) and the GT, discarding poor-quality data (samples that do not meet the requirements).
4. **Train the Segmentation Network**: Use the cleaned data (after discarding poor-quality samples) to train Mask2Former.
5. **Iterative Training**: Treat the cleaned data as new samples (I, M, GT) and repeat steps 2-4 for iterative training.

## 🧪 Benchmarks

| Dataset     | Method        | mIoU (%) |
|-------------|---------------|----------|
| VOC 2012    | Free-Mask     | 72.0     |
| Cityscapes  | Free-Mask     | 83.5     |
| ADE20K      | Free-Mask     | 77.2     |

> See full tables and ablation studies in our [paper](https://doi.org/10.1145/XXXXXX.XXXXXX).

## 📦 Dependencies

- Python 3.8+
- PyTorch >= 1.12
- CUDA 11.3+
- OpenCV, scikit-image, SciPy
- NVIDIA APEX (for mixed precision)
- Mask2Former (official repo) for segmentation

## 📜 Citation

```bibtex
@inproceedings{gao2025freemask,
  title={Free-Mask: A Novel Paradigm of Integration Between the Segmentation Diffusion Model and Image Editing},
  author={Bo Gao and Jianhui Wang and Xinyuan Song and Yangfan He and Fangxu Xing and Tianyu Shi},
  booktitle={Proceedings of the 33rd ACM International Conference on Multimedia (ACM MM)},
  year={2025}
}
```

---

© 2025 Bo Gao et al. Licensed under ACM usage policy.
