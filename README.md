# Causal-Inference-for-Breast-Cancer-Wisconsin-dataset

In this project we are going to use Breast Cancer Wisconsin (Diagnostic) Data Set to preform 
exploratory analysis. Casual graph using different technique is going to be used. 

## Table of Content

- [Introduction](#introduction)
- [Install](#instalation)
- [Data](#data)
- [Notebooks](#notebooks)
- [Scripts](#scripts)
- [Technologies used](#technologies-used)

### Introduction

Most individuals are aware of cause-and-effect links, which is a skill that robots still lack.
And, before we can consider building a system that can understand cause-and-effect in
general, we need to understand cause-and-effect from a statistical standpoint: causal
calculus and causal inference . Statistics is where causality was born from, and in order to
create a high-level causal system, we must return to the fundamentals.

### Instalation

- Install Required Python Modules

git clone https://github.com/maxi1571/Causal-Inference-for-Breast-Cancer-Wisconsin-dataset.git
cd Causal-Inference-for-Breast-Cancer-Wisconsin-dataset.git
pip install -r requirements.txt

- Jupyter Notebook

* cd notebooks
* jupyter notebook


### Data

Data can be found: https://archive.ics.uci.edu/ml/datasets/Breast+Cancer+Wisconsin+%28Diagnostic%29

#### Categorical variables 

      * Diagnosis(Malignant / benign)

#### Continuous variables

      * the circumference (mean of distances from the center to points on the perimeter)
      * the concavity (severity of concave portions of the contour)
      * points that are concave (number of concave portions of the contour)
      * fractal dimension of symmetry (“coastline approximation” — 1)
      * the texture (standard deviation of gray-scale values)
      * Perimeter\s area
      * suppleness (local variation in radius lengths)
      * compactness (area2 / perimeter2 — 1.0)

### Notebooks

- The notebook contains
* A bivariate relationship between the variables.
* A casual graph implemenation of the data 


### Scripts

The causality.py script is the one that was used to make the graph. Jaccard's important antecedent is used to 
examine the sustainability of the association between the independent variables within the graph.


### Analysis insights

  * There are 569 occurrences in all, with 32 properties.
  * Malignant and Benign are the only two distinct values in the Diagnosis Columns 
  * Correlations between dataset have lots of negative correlations and correlation under the values of 
  * 0.5 which creates ambiguity.
  * There are many negative correlations in this dataset .There are many attributes
    with correlation under less than 0.5.
  * A value of 0.91 is achieved by incrementing the data by 10%. But we need a value of 1 to have a stable
    graph that can give us a better output. 
  * The accuracy value found shows that the graph isn’t stable and we need an additional data set to
    determine the significance of the causal graph correlation.


### Technologies used

- [DVC](https://dvc.org/) : Remote Data Storage
- [CML](https://github.com/iterative/cml): Display Model result and usefull information during pull requests
