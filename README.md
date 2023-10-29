# ML-based Covid Detection with FCS Data
## About the project
> This project is processed on Python 3.11 with a Spyder (Anaconda) editor. The FCS data is read with FlowCal 1.2.1 and analyzed with sci-kit learn 1.3.0.

FCS data is the standard data format to store information collected with flow cytometry.

In this project, each raw FCS file consists of 35 channels, including a time measurement, 6 light scatter measurements, and 28 fluorescence measurements. Only 31 channels are selected for analyzation by matching the mapping table.

With functions provided by FlowCal.stats, 7 types of statistical features are utilized. A total of 187 features are extracted from each sample. The feature array is contained in a dictionary variable with the data_feature key. Dictionary variables of all samples are grouped together as a list variable samples_info.

To detect whether the sample is covid-positive or not, an SVM classifier provided by sci-kit learn is applied. This project applies K-fold cross-validation method to train and validate the model. K as 5 is selected. Recall, precision, accuracy, and confusion matrix of each fold is calculated and printed to evaluate the detection performance.


## Bonus Question
1. Please explain the fundamental principles of flow cytometry and walk through the step-by-step process of how it works? Additionally, highlight some common applications of flow cytometry in scientific research and clinical settings.
Ans. 

2. Below are plots of selected cell surface biomarkers of blood cell samples. Researchers are interested in picking out cells marked in yellow (accupying a high-density chunk at the bottom-right) for further analysis. How would you suggest a method to automatically identify these cells?
Ans. 
