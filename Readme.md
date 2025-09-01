# Integrated Image Segmentation-Based Solution for Object Collision Detection in 2D Simulation Environments

This repository contains the source code and documentation for the research paper: **"INTEGRATED IMAGE SEGMENTATION-BASED SOLUTION FOR OBJECT COLLISION DETECTION IN 2D SIMULATION ENVIRONMENTS"**.

**Submission for:** UEH Young Researcher Award 2025

**Field:** Information Technology: Computer Science

---

## 📝 Introduction

This study investigates image segmentation-based methods for object collision detection in 2D simulation environments. Collision detection is a pivotal component in numerous fields, including robotics, virtual reality, and autonomous systems, where accurate modeling of object interactions is essential.

This paper focuses on the evaluation and comparison of three key segmentation algorithms:
* The Watershed Algorithm
* The Active Contour Snake (ACM) Model
* The Chan-Vese Model

The objective is to identify the most optimal algorithm in terms of efficiency and stability, while also providing practical recommendations for applications in fields like gaming, robotics, and automation.

## 🛠️ Methodology

The research was conducted in two main phases: segmentation-based research and simulation-based research, applied to six experimental videos with varying conditions (monochrome/polychrome, number of objects).

### 1. Segmentation Algorithms
* **Watershed:** Based on mathematical morphology, this algorithm is effective for separating overlapping objects but is prone to over-segmentation.
* **Active Contour Snake (ACM):** This model uses a deformable curve to fit object boundaries, adapting well to complex shape changes but requiring high computational cost and precise initialization.
* **Chan-Vese:** As a region-based method, this model performs well in low-contrast and noisy environments, but its iterative optimization process can hinder real-time applications.

### 2. Simulation Environment
A 2D simulation environment was developed using Python and OpenCV, allowing for the customization of parameters such as the number of balls, frame rate, and duration. Collisions between the balls were handled to accurately reflect physical behavior.

### 3. Evaluation
The performance of the models was evaluated based on the following criteria:
* Execution Time 
* Average Time Per Frame 
* Number of Collision Detections

## 📊 Key Results

The analysis of the experimental results revealed the following:

* **The Chan-Vese model** demonstrated **superior efficiency and stability**, particularly when processing polychromatic (multi-colored) images. The algorithm maintained stable processing times even as the number of objects increased or collisions occurred.
* The combination of the **Watershed and Active Contour Model (ACM)** exhibited a higher average processing time and greater variability, especially with monochromatic images or an increased number of objects.
* The performance of the algorithms was influenced by object color; polychromatic images helped reduce processing time by leveraging color information to separate objects.

## 🚀 Limitations and Future Directions

### Limitations
* **2D Scope:** The study is confined to 2D simulation environments, which does not capture the complexity of real-world 3D interactions.
* **Accuracy:** The algorithms sometimes failed to accurately pinpoint the exact frame of a collision, especially with overlapping or fast-moving objects.
* **Computational Resources:** Certain algorithms (especially Watershed and ACM) are computationally intensive, posing a challenge for real-time applications.

### Future Research
* Extend the research to 3D environments.
* Develop hybrid models that combine the strengths of these algorithms to mitigate their individual weaknesses.
* Integrate machine learning techniques to optimize the algorithms for faster and more efficient processing.

## 📜 Citation

If you use this research in your work, please refer to the original paper.

```
@article{huy2025integrated,
  title={Integrated image segmentation-based solution for object collision detection in 2D simulation environments},
  author={Huy, Trần Viết Gia and {\DJ}{\^o}ng, Dương Quang and Nhựt, Nguyễn Minh and Hưởng, Nguyễn Trọng and Thiện, Nguyễn Ngọc},
  year={2025},
  publisher={University of Economics Ho Chi Minh City}
}
```
