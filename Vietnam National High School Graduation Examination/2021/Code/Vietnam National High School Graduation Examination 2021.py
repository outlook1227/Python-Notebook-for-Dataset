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

# Bar chart for combination exam selection
labels = ["Social Science", "Natural Science", "Null"]
count = [sum_of_SS, sum_of_NS, sum_of_Null]
colors = ["#0AFF3F", "#059DF3" ,"#939393"]

plt.figure(figsize = (15, 10))
counts_grouped = plt.bar(labels, count, color = colors)

for counts in counts_grouped.patches:
  bar_height = counts.get_height()
  label_x = counts.get_x() + counts.get_width() / 2
  label_y = counts.get_y() / bar_height + bar_height
  plt.text(label_x, label_y, s = f"{bar_height:}", ha='center', va='bottom', color = "black", size = 15)

plt.xlabel("Combination")
plt.ylabel("Number of students took the exam")
plt.title("Bar Chart of Combination Exam Selection")

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

labels_10_score = ["Math", "Literature", "English", "Physics", "Chemistry", "Biology", "History",
                    "Geography", "Civic Education"]
counts_10_score = [math_10_score, literature_10_score, english_10_score, physics_10_score, chemistry_10_score,
                    biology_10_score, history_10_score, geography_10_score, civic_education_10_score]

# Visualization for score maximum
plt.figure(figsize = (20, 15))
sns.set(font_scale = 1.35)
score_10_grouped = plt.bar(labels_10_score, counts_10_score, color = "#00A3FF")

for counts_10 in score_10_grouped.patches:
  height = counts_10.get_height()
  label_x = counts_10.get_x() + counts_10.get_width() / 2
  label_y = counts_10.get_y() / height + height
  plt.text(label_x, label_y, s = f"{height:}", ha='center', va='bottom', color = "black", size = 15)

plt.xlabel("Subjects")
plt.ylabel("Occurences")
plt.title("10 Point Distributions")

# Count of the current of English score
plt.figure(figsize = (28, 20))
sns.set(font_scale = 1.5)
english_sns = sns.countplot(examination_dataset.English)
english_sns.set_xticklabels(english_sns.get_xticklabels(), rotation = 45)
plt.xlabel("Occurrences", fontsize = 22.5)
plt.ylabel("Score", fontsize = 22.5)
plt.title("English Score Distribution", fontsize = 22.5)

# Count of the current of Physics score
plt.figure(figsize = (28, 20))
sns.set(font_scale = 1.45)
physics_sns = sns.countplot(examination_dataset.Physics)
physics_sns.set_xticklabels(physics_sns.get_xticklabels(), rotation = 45)
plt.xlabel("Occurrences", fontsize = 22.5)
plt.ylabel("Score", fontsize = 22.5)
plt.title("Physics Score Distribution", fontsize = 22.5)

# Count of the current of Chemistry score
plt.figure(figsize = (28, 20))
sns.set(font_scale = 1.45)
chemistry_sns = sns.countplot(examination_dataset.Chemistry)
chemistry_sns.set_xticklabels(chemistry_sns.get_xticklabels(), rotation = 45)
plt.xlabel("Occurrences", fontsize = 22.5)
plt.ylabel("Score", fontsize = 22.5)
plt.title("Chemistry Score Distribution", fontsize = 22.5)

# Count of the current of History score
plt.figure(figsize = (28, 20))
sns.set(font_scale = 1.45)
history_sns = sns.countplot(examination_dataset.History)
history_sns.set_xticklabels(history_sns.get_xticklabels(), rotation = 45)

for counts in history_sns.patches:
  height = counts.get_height()
  label_x = counts.get_x() + counts.get_width() / 2
  label_y = counts.get_y() / height + height
  plt.text(label_x, label_y, s = f"{height:}", ha='center', va='bottom', color = "black", size = 15, rotation = 90)

plt.xlabel("Occurrences", fontsize = 20.5)
plt.ylabel("Score", fontsize = 20.5)
plt.title("History Score Distribution", fontsize = 22.5)

# Count of the current of Geography score
plt.figure(figsize = (28, 20))
sns.set(font_scale = 1.45)
geography_sns = sns.countplot(examination_dataset.Geography)
geography_sns.set_xticklabels(geography_sns.get_xticklabels(), rotation = 45)

for counts in geography_sns.patches:
  height = counts.get_height()
  label_x = counts.get_x() + counts.get_width() / 2
  label_y = counts.get_y() / height + height
  plt.text(label_x, label_y, s = f"{height:}", ha='center', va='bottom', color = "black", size = 15, rotation = 90)

plt.xlabel("Occurrences", fontsize = 20.5)
plt.ylabel("Score", fontsize = 20.5)
plt.title("Geography Score Distribution", fontsize = 22.5)

# Count the examiee has failed for Graduation Examination
math_failed = sum(examination_dataset.Math <= 1.0)
literature_failed = sum(examination_dataset.Literature <= 1.0)
english_failed = sum(examination_dataset.English <= 1.0)
physics_failed = sum(examination_dataset.Physics <= 1.0)
chemistry_failed = sum(examination_dataset.Chemistry <= 1.0)
biology_failed = sum(examination_dataset.Biology <= 1.0)
history_failed = sum(examination_dataset.History <= 1.0)
geography_failed = sum(examination_dataset.Geography <= 1.0)
civic_education_failed = sum(examination_dataset.Civic_Education <= 1.0)

list_failed = ["Math", "Literature", "English", "Physics", "Chemistry", "Biology",
              "History", "Geography", "Civic Education"]

counts_failed = [math_failed, literature_failed, english_failed, physics_failed, chemistry_failed,
                 biology_failed, history_failed, geography_failed, civic_education_failed]

plt.figure(figsize = (20, 15))
sns.set(font_scale = 1.45)
failed_grouped = plt.bar(list_failed, counts_failed, color = "#8296A2")

for counts_nope in failed_grouped.patches:
  list_height = counts_nope.get_height()
  label_x = counts_nope.get_x() + counts_nope.get_width() / 2
  label_y = counts_nope.get_y() / list_height + list_height
  plt.text(label_x, label_y, s = f"{list_height:}", ha='center', va='bottom', color = "black", size = 15)

plt.xlabel("Subjects", fontsize = 22.5)
plt.ylabel("Occurences", fontsize = 22.5)
plt.title("Failure Point Distributions", fontsize = 22.5)
