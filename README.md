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



### Scripts




### data exploration insights

* There are 569 occurrences in all, with 32 properties.

* Malignant and Benign are the only two distinct values in the Diagnosis Columns.

* Diagnosis, Radius_mean, perimeter_mean, Concavity_mean, points_mean, perimeter_worst,area_worst,radius_se, area_mean, compactness_mean, perimeter_se, area_se,radius_worst, compactness_worst,concavity_worst, concave points_worst are the highly correlated columns.

* Correlations between dataset have lots of negative correlations and correlation under the values of 0.5 which creates ambiguity.

* The displots shows, the radius mean,texture mean, perimeter mean, area mean, smoothness mean, compactness mean, concavity mean, concave points mean, symmetry mean and the fractal dimension mean significantly vary in the different types of tumors.

* There are many negative correlations in this dataset .There are many attributes with correlation under less than 0.5.

### Technologies used

- [DVC](https://dvc.org/) : Remote Data Storage
- [CML](https://github.com/iterative/cml): Display Model result and usefull information during pull requests
