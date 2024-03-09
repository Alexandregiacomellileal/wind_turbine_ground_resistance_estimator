# Integrated approach for wind turbine grounding resistance estimation: Bridging clamp-on ground meter, computational simulations, and machine learning.

<img width="1666" alt="image" src="https://github.com/Alexandregiacomellileal/Update-computacional-tool/assets/96079504/d40874aa-487c-4722-abfe-1cff32cfbd77">

## Associated research paper
Integrated approach for wind turbine grounding resistance estimation: Bridging clamp-on ground meter, computational simulations, and machine learning


## Files attached to this repository

1. [[methodology_flowchart.pdf](https://github.com/Alexandregiacomellileal/Update-computacional-tool/blob/main/methodology_flowchart.pdf)]
    - Flowchart of the proposed methodology.

2. [[Proposed_solution.py](https://github.com/Alexandregiacomellileal/Update-computacional-tool/blob/main/Proposed_solution.py)]
  
    - This Python algorithm comprises three modules designed for generating, analyzing, and forecasting grounding resistance in electrical circuits using the Alternative Transient Program (ATP) and machine learning techniques.
      
    - Module 1 is designed to streamline the generation and control of extensive simulations of electrical circuits through a Python algorithm integrated with the Alternative Transient Program (ATP). The algorithm facilitates the creation of *.atp* simulation files, executes simulations, and transforms resulting waveforms *.pl4* files into MATLAB *.mat* files. The algorithm systematically generates parameter vectors P, which are subsequently introduced into the clamp-on ground meter measurement equivalent electric circuit. It orchestrates the automation of data entry and extraction steps within the ATP software. All input-output vector pairs [**P** ; **Z**<sub>med </sub>] are cataloged in a dedicated database. Notably, the vectors **Z**<sub>med </sub> and **R**<sub>f</sub> ($n$ elements of **P**) assume a pivotal role as a foundational repository for Module 2, where machine learning models are developed based on this comprehensive dataset.

    - Module 2 introduces a Python algorithm leveraging advanced machine learning techniques to forecast turbine grounding resistance based on clamp-on meter readings. This algorithm capitalizes on the database established in Module 1, employing it for tasks such as data preprocessing, model training, and the assessment of evaluation metrics to enhance predictive accuracy. Within the machine learning pipeline, 70% of the vector pairs [**Z**<sub>med </sub> ; **R**<sub>f</sub>] from the Module 1 database are allocated for training the model, ensuring a robust foundation for learning. The remaining 30% is reserved for testing the trained model, evaluating its performance, and constructing boxplot error graphs. These graphs depict the outcomes of implementing the Clamp-on Ground Meter Method (CGM) and the Proposed Method in the São Bento Complex (SBC) grounding system, providing a comparative analysis of their effects.

    - Module 3 features a Python algorithm designed to efficiently generate and manage extensive simulations of electrical circuits using ATP. This module is capable of creating .atp simulation files, executing simulations, and converting resulting waveforms *.pl4* files into MATLAB files *.mat*. Specifically tailored for the testing set separated in Module 2, the algorithm loads the **P** electrical parameter sample vectors, sequentially introducing them into the High-frequency ground meter measurement circuit. It then automates the essential steps of data insertion and extraction within the ATP software. All resulting input-output pairs are stored in a dedicated database, forming the foundation for comprehensive analysis. The algorithm's outcomes are visually represented through a box plot error graph. This graph encapsulates the results obtained from implementing the High-Frequency Method (HFM) in the São Bento Complex (SBC) grounding system, providing a clear comparative assessment of its impact.


    - To utilize this algorithm, users are required to download and install three essential software components: ATP, the pl42mat.exe converter, and Python. 
   
3. [[Database.xlsx](https://github.com/Alexandregiacomellileal/Update-computacional-tool/blob/main/Database.xlsx)]
    - Excel spreadsheet featuring an extensive dataset designed for training, validation, and testing machine learning models. The dataset consists of 11,000 solution vectors, formed by concatenating the **P** vectors with their respective **Z**<sub>med</sub> vectors. In the machine learning pipeline, 70% of these solution vectors are allocated for training the model, ensuring a robust foundation for learning. The remaining 30% of vectors are dedicated to testing the trained model, as well as assessing the performance of the CGM and HFM measurement methods within the SBC framework. This division allows for a comprehensive evaluation of both the model's predictive capabilities and the effectiveness of measurement techniques in the specified context. 

4. [[HFM.acp](https://github.com/Alexandregiacomellileal/Update-computacional-tool/blob/main/HFM.acp)]
   - ATP file for computer simulation of the high-frequency method in case study's grounding system.

5. [[CGM.acp](https://github.com/Alexandregiacomellileal/Update-computacional-tool/blob/main/CGM.acp)]
    - ATP file for computer simulation of the clamp-on ground meter method in case study's grounding system.

6. [[HFM_circuit.pdf](https://github.com/Alexandregiacomellileal/Update-computacional-tool/blob/main/HFM_circuit.pdf)]
   - PDF file with the equivalent circuit's figure for the high-frequency measurement method in case study's grounding system.

7. [[CGM_circuit.pdf](https://github.com/Alexandregiacomellileal/Update-computacional-tool/blob/main/CGM_circuit.pdf)]
   - PDF file with the equivalent circuit's figure for the clamp-on ground meter measurement method in case study's grounding system.

8. [[MAPE_results.xlsx](https://github.com/Alexandregiacomellileal/Update-computacional-tool/blob/main/MAPE_results.xlsx)]
   - Excel spreadsheet containing the final results.

9. [[Error_Boxplot.pdf](https://github.com/Alexandregiacomellileal/Update-computacional-tool/blob/main/Error_Boxplot.pdf)]
    - Error boxplot graphs illustrating the performance variations among the clamp-on ground meter, high-frequency, and a proposed method when applied in the context of estimating the SBC's grounding resistance turbines. These boxplots provide a visual representation of the errors associated with each method, facilitating a comprehensive comparison and analysis between them.

10. [[Supporting files](https://github.com/Alexandregiacomellileal/Update-computacional-tool/tree/main/supporting%20files)]
   - This directory contains sub-algorithms and Excel spreadsheet files with data frames used by the authors in developing the proposed solution. Each module (sub-algorithm) performs a specific task, and when combined, the modules form the complete algorithm named [[Proposed_solution.py](https://github.com/Alexandregiacomellileal/Update-computacional-tool/blob/main/Proposed_solution.py)]. Similarly, all the Excel files contain data frames that collectively contribute to the formatting of the [[Database.xlsx](https://github.com/Alexandregiacomellileal/Update-computacional-tool/blob/main/Database.xlsx)] file.

## Usage

To apply this systematic approach to your wind farm grounding system analysis, follow the steps outlined in the respective sections of the codebase. Detailed instructions for each file can be found within their specific directories.

________________________________________________________________________________________________________________________

## Contact us:
Please send an email to: alexgiacomelli@yahoo.com

________________________________________________________________________________________________________________________

## Contributors:
Federal University of Technology - Parana (UTFPR)

________________________________________________________________________________________________________________________

<p align="center">

________________________________________________________________________________________________________________________

<p align="center">
  <img src="https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2FAlexandregiacomellileal%2FWind-Turbine-Grounding-Resistance-Estimator&label=Visitors&labelColor=%23697689&countColor=%23ff8a65" alt="Visitors Badge">
</p>


