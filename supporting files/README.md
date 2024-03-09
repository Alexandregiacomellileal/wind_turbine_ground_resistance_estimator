# Integrated approach for wind turbine grounding resistance estimation: Bridging clamp-on ground meter, computational simulations, and machine learning.

## Overview
This directory contains sub-algorithms and Excel spreadsheet files with data frames used by the authors in developing the proposed solution. Each module (sub-algorithm) performs a specific task, and when combined, the modules form the complete algorithm named [[Proposed_solution.py](https://github.com/Alexandregiacomellileal/Update-computacional-tool/blob/main/Proposed_solution.py)]. Similarly, all the Excel files contain data frames that collectively contribute to the formatting of the [[Database.xlsx](https://github.com/Alexandregiacomellileal/Update-computacional-tool/blob/main/Database.xlsx)] file.

## Files

1. [[sbn_varia_Rf_e_Rp_e_k_com_mutua_all_cap_111143.py](https://github.com/Alexandregiacomellileal/Update-computacional-tool/blob/main/supporting%20files/sbn_varia_Rf_e_Rp_e_k_com_mutua_all_cap_111143.py)]
    - Python algorithm to automate data insertion and removal in ATP software for clamp-on ground meter measurement circuit simulation (Module 1 of Proposed_solution.py).

2. [[sbnallmutuacap.acp](https://github.com/Alexandregiacomellileal/Update-computacional-tool/blob/main/supporting%20files/sbnallmutuacap.acp)]
    - ATP file for the computer simulation of the clamp-on ground meter method within the grounding system of the case study. This file is intended for use by the algorithm 'sbn_varia_Rf_e_Rp_e_k_com_mutua_all_cap_111143.py'.

3. [[dataframe_sbn_mutua_varia_rf_e_rp.xlsx](https://github.com/Alexandregiacomellileal/Update-computacional-tool/blob/main/supporting%20files/dataframe_sbn_mutua_varia_rf_e_rp.xlsx)]
   - Excel spreadsheet with 11000 samples of input and output vectors from the clamp-on ground meter method simulation in case study's grounding system. This file is intended for use by the algorithm 'sbn_varia_Rf_e_Rp_e_k_com_mutua_all_cap_111143.py'.

4. [[sbn_varios_algoritmos_error_boxplot_mutua_variando_rf_e_rp.py](https://github.com/Alexandregiacomellileal/Update-computacional-tool/blob/main/supporting%20files/sbn_varios_algoritmos_error_boxplot_mutua_variando_rf_e_rp.py)]
    - Python sub-algorithm containing machine learning techniques to predict turbine grounding resistance from clamp-on meter readings (Module 2 of Proposed_solution.py). 

5. [[sbn_error_boxplot_high_frequency_cap.py](https://github.com/Alexandregiacomellileal/Update-computacional-tool/blob/main/supporting%20files/sbn_error_boxplot_high_frequency_cap.py)]
   - Python algorithm to automate data insertion and removal in ATP software for high-frequency measurement circuit simulation (Module 3 of Proposed_solution.py).

6. [[allat25khz_capac.acp](https://github.com/Alexandregiacomellileal/Update-computacional-tool/blob/main/supporting%20files/allat25khz_capac.acp)]
   - ATP file for the computer simulation of the High-frequency method within the grounding system of the case study. This file is intended for use by the algorithm 'sbn_error_boxplot_high_frequency_cap.py.py'.
  
7. [[allat25khzcap_sbn_results.xlsx](https://github.com/Alexandregiacomellileal/Update-computacional-tool/blob/main/supporting%20files/allat25khzcap_sbn_results.xlsx)]
   - Excel spreadsheet with 3300 samples of input and output vectors from the high-frequency method simulation in case study's grounding system. This file is intended for use by the algorithm 'sbn_error_boxplot_high_frequency_cap.py.py'.


________________________________________________________________________________________________________________________

## Usage

To apply this systematic approach to your wind farm grounding system analysis, follow the steps outlined in the respective sections of the codebase. Detailed instructions for each file can be found within their specific directories.

________________________________________________________________________________________________________________________

## Contact us:
Please send an email to: alexgiacomelli@yahoo.com

________________________________________________________________________________________________________________________

## Contributors:
Federal University of Technology – Parana (UTFPR) and Institute of Technology for Development (LACTEC)



