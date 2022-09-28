# Import the libraries
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

# Read and show the dataset
examination_dataset = pd.read_csv("/content/VN_Graduation_Examination_2021.csv")
examination_dataset

"Data missing and Data Cleaning"
# Check missing, outlier, information in the dataset
examination_dataset.isna().sum()
examination_dataset.info()
examination_dataset.describe()

"Visualization for the information of dataset with graph"
# Check heatmap for the dataset
plt.figure(figsize = (20, 15))
sns.set(font_scale = 1.3)
sns.heatmap(examination_dataset[["id_examinee","Math", "Physics", "Chemistry", "History", "Biology", "Geography", 
                        "Literature", "Civic_Education", "English", "German", "Chinese", "Russian", "Japanese", "French"]].corr(), 
            cmap = "GnBu_r", annot = True)
plt.title("Heatmap for the dataset of columns")
plt.show()

# Select the continuous features
Math = examination_dataset["Math"]
Physics = examination_dataset["Physics"]
Chemistry = examination_dataset["Chemistry"]
Biology = examination_dataset["Biology"]
History = examination_dataset["History"]
Geography = examination_dataset["Geography"]
Literature = examination_dataset["Literature"]
Civic_Education = examination_dataset["Civic_Education"]
English = examination_dataset["English"]
German = examination_dataset["German"]
Chinese = examination_dataset["Chinese"]
Russian = examination_dataset["Russian"]
French = examination_dataset["French"]
Japanese = examination_dataset["Japanese"]

# Visualizing for all columns
plt.figure(figsize = (20, 15))
sns.set(font_scale = 1.4)
dataset = pd.DataFrame(data = examination_dataset, columns = ["Math", "Physics", "Chemistry", "History", "Biology", "Geography", 
                        "Literature", "Civic_Education", "English"])
boxplot_dataset = sns.boxplot(x="variable", y="value", data=pd.melt(dataset), showfliers = False)
boxplot_dataset.set_xlabel("Subjects")
boxplot_dataset.set_ylabel("Marks")
plt.title("Destiny for mark of the Graduation Examination")
plt.show()

# Visualizing for columns of foreign language
plt.figure(figsize = (20, 15))
sns.set(font_scale = 1.4)
dataset = pd.DataFrame(data = examination_dataset, columns = ["English", "German", "Chinese", "Russian", "Japanese", "French"])
boxplot_dataset = sns.boxplot(x="variable", y="value", data=pd.melt(dataset), showfliers = False)
boxplot_dataset.set_xlabel("Subjects")
boxplot_dataset.set_ylabel("Marks")
plt.title("Boxplot for Foreign Languages")
plt.show()

"Dropping Data"
# Drooping and Cleaning the dataset of columns Math
math_papers = examination_dataset[["Math"]]
math_papers

math_dataset_cleaned = math_papers.dropna()
math_dataset_cleaned

# Physics
physics_papers = examination_dataset[["Physics"]]
physics_papers

physics_dataset_cleaned = physics_papers.dropna()
physics_dataset_cleaned

# English
english_papers = examination_dataset[["English"]]
english_papers

english_dataset_cleaned = english_papers.dropna()
english_dataset_cleaned

# Chemistry
chemistry_papers = examination_dataset[["Chemistry"]]
chemistry_papers

chemistry_dataset_cleaned = chemistry_papers.dropna()
chemistry_dataset_cleaned

"Count the none-null value in Social Sciene, Natural Science, and null values"
# Natural Science
sum_of_NS = sum((examination_dataset.Physics >= 0) | (examination_dataset.Chemistry >= 0) | (examination_dataset.Biology >= 0))
print("Natural Science:",sum_of_NS)

# Social Science
sum_of_SS = sum((examination_dataset.History >= 0) | (examination_dataset.Geography >= 0) | (examination_dataset.Civic_Education >= 0))
print("Social Science:", sum_of_SS)

# Null information
sum_of_Null = sum(examination_dataset.id_examinee >= 0) - sum_of_NS - sum_of_SS
print("Null:", sum_of_Null)
