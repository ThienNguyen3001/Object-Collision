# **Experiment: Evaluating Execution Time and Collision Detection Performance**

## **Overview**
This experiment involves running two image segmentation algorithms—**Chan-Vese** and **Watershed-ACM**—on video data from the `data/videos/` folder. The goal is to analyze the execution time per frame, calculate the average execution time, and determine the number of collisions detected by each algorithm. The results provide insight into the performance and efficiency of these algorithms under different scenarios.

---

## **Experiment Steps**
1. **Dataset**:  
   - Input videos are located in the `data/videos/` folder. These videos contain various object properties and motion complexities for testing.

2. **Algorithms**:  
   - **Chan-Vese**  
   - **Watershed-ACM**

3. **Execution Process**:  
   - Run the `experiment.ipynb` notebook in the `experiments/` folder.
   - Each cell processes one video from the dataset using both algorithms:
     - Measure the execution time per frame.
     - Calculate the average execution time for the entire video.
     - Count the total number of collisions detected.
   - Results for each video are stored after execution of the corresponding cell.
   
4. **Results Storage**:  
   - Execution time and collision data for each video are saved in CSV files within the respective algorithm's folder:
     - `results/Chan-vese_csv/`
     - `results/Watershed-ACM_csv/`

5. **Visualization**:  
   - Use the stored CSV files to generate plots for execution time trends and comparative analysis of the two algorithms. Plots are saved in `results/plots/`.

---

## **Expected Output**
1. **CSV Files**:
   - Each CSV file contains:
     - **Video Name**: Name of the processed video.
     - **Frame Execution Time**: Execution time for each frame.

2. **Analysis**:
   - A comparison of execution times and collision detection performance between the two algorithms.
   - Insights into the trade-offs between efficiency and accuracy for each algorithm.

---

## **Usage**
1. **Run the Experiment**:
   - Open the `experiment.ipynb` notebook in the `experiments/` folder.
   - Run each cell, which processes one video from the `data/videos/` folder.

2. **Analyze Results**:
   - Open the CSV files in the corresponding algorithm folders (`results/Chan-vese_csv/` and `results/Watershed-ACM_csv/`) to view detailed execution time and collision data.
   - Review the plots in `results/plots/` for visual insights into algorithm performance.

---

## **Conclusion**
This experiment facilitates a detailed evaluation of the execution time and collision detection capabilities of Chan-Vese and Watershed-ACM algorithms, enabling researchers to assess their applicability in real-time simulation environments.

