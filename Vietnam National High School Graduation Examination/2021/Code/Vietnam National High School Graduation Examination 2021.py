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
boxplot_dataset.set_ylabel("Score")
plt.title("Destiny for mark of the Graduation Examination")
plt.show()

# Visualizing for columns of foreign language
plt.figure(figsize = (20, 15))
sns.set(font_scale = 1.4)
dataset = pd.DataFrame(data = examination_dataset, columns = ["English", "German", "Chinese", "Russian", "Japanese", "French"])
boxplot_dataset = sns.boxplot(x="variable", y="value", data=pd.melt(dataset), showfliers = False)
boxplot_dataset.set_xlabel("Subjects")
boxplot_dataset.set_ylabel("Score")
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

"Calculate the GPA of papers in Graduation Examination"

# Average of each papers
math_average = np.average(math_dataset_cleaned)
physics_average = np.average(physics_dataset_cleaned)
chemistry_average = np.average(chemistry_dataset_cleaned)
english_average = np.average(english_dataset_cleaned)
literature_average = np.average(literature_dataset_cleaned)
history_average = np.average(history_dataset_cleaned)
geography_average = np.average(geography_dataset_cleaned)
civic_education_average = np.average(civic_education_dataset_cleaned)

# Print and result
print("The GPA of Maths: ", round(math_average, 2))
print("The GPA of Physics: ", round(physics_average, 2))
print("The GPA of Chemistry: ", round(chemistry_average, 2))
print("The GPA of English: ", round(english_average, 2))
print("The GPA of Literature: ", round(literature_average, 2))
print("The GPA of History: ", round(history_average, 2))
print("The GPA of Geography: ", round(geography_average, 2))
print("The GPA of Civic Education: ", round(civic_education_average, 2))
"Count the none-null value in Social Sciene, Natural Science, and null values"

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

# Count the number has score 10
math_10_score = sum(examination_dataset.Math == 10)
literature_10_score = sum(examination_dataset.Literature == 10)
english_10_score = sum(examination_dataset.English == 10)
physics_10_score = sum(examination_dataset.Physics == 10)
chemistry_10_score = sum(examination_dataset.Chemistry == 10)
biology_10_score = sum(examination_dataset.Biology == 10)
history_10_score = sum(examination_dataset.History == 10)
geography_10_score = sum(examination_dataset.Geography == 10)
civic_education_10_score = sum(examination_dataset.Civic_Education == 10)

print("Number of examniee take 10 score Math papers:", math_10_score)
print("Number of examniee take 10 score Literature papers:", literature_10_score)
print("Number of examniee take 10 score English papers:", english_10_score)
print("Number of examniee take 10 score Physics papers:", physics_10_score)
print("Number of examniee take 10 score Chemistry papers:", chemistry_10_score)
print("Number of examniee take 10 score Biology papers:", biology_10_score)
print("Number of examniee take 10 score History papers:", history_10_score)
print("Number of examniee take 10 score Geography papers:", geography_10_score)
print("Number of examniee take 10 score Civic Education papers:", civic_education_10_score)