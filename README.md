# ML-based Covid Detection with FCS Data

## About the project

> This project is processed on Python 3.11 with a Spyder (Anaconda) editor. The FCS data is read with FlowCal 1.2.1 and analyzed with sci-kit learn 1.3.0.

FCS data is the standard data format to store information collected with flow cytometry.

In this project, each raw FCS file consists of 35 channels, including a time measurement, 6 light scatter measurements, and 28 fluorescence measurements. Only 31 channels are selected for analyzation by matching the mapping table.

With functions provided by FlowCal.stats, 7 types of statistical features are utilized. A total of 187 features are extracted from each sample. The feature array is contained in a dictionary variable with the data_feature key. Dictionary variables of all samples are grouped together as a list variable samples_info.

To detect whether the sample is covid-positive or not, an SVM classifier provided by sci-kit learn is applied. This project applies K-fold cross-validation method to train and validate the model. K as 5 is selected. Recall, precision, accuracy, and confusion matrix of each fold is calculated and printed to evaluate the detection performance.

## Bonus Question

### Q1. Please explain the fundamental principles of flow cytometry and walk through the step-by-step process of how it works? Additionally, highlight some common applications of flow cytometry in scientific research and clinical settings.

Ans. 

The fundamental principles of flow cytometry are light scattering and fluorescence emission, which occurs as light from a light source collides with the sample particles. There are three major systems in flow cytometry: fluidics, optics, and electronics. The fluidics system is composed of pressurized sheath fluid to deliver and to focus sample particles to the laser beam. The optics system contains excitation optics and collection optics. The former excites energy as light and strikes the light with particles, while the latter, including photomultiplier tubes, dichroic filters, and bandpass filter, transmits the scattered light and the fluorescence of particles to the electronics system. Finally, the electronics system detects the light signals and converts them into digital signals that can be analyzed by computer software.

Common applications of flow cytometry include immunophenotyping, antigen specific responses, intracellular cytokine analysis, proliferation analysis, apoptosis analysis, fluorescent protein analysis, cell cycle analysis, signal transduction flow cytometry, RNA flow cytometry, and cell sorting.

### Q2. Below are plots of selected cell surface biomarkers of blood cell samples. Researchers are interested in picking out cells marked in yellow (accupying a high-density chunk at the bottom-right) for further analysis. How would you suggest a method to automatically identify these cells?

Ans. 

By using gate methods, cells in a specific region can be chosen and isolated for further analysis. For example, if the target cells are bigger in size, a gate can be set on FSC (parameter for analyzing cell size) versus SSC plot. Additionally, FlowCal library provides gate functions to retain events that satisfy certain criteria but to discard those do not. For instance, an ellipse gate can retain an ellipse area by specifying three parameters. On the other hand, a density gate identifies region with density of events. There is only one parameter (i.e. gate_fraction) that is required for users to control, which is easier than the ellipse gate to define a shape that is more similar in the ungated map.

> The answer of both questions refers to 
