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

"Dropping and Cleaning for the Dataset"
# Math
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

# Biology
biology_papers = examination_dataset[["Biology"]]
biology_papers

biology_dataset_cleaned = biology_papers.dropna()
biology_dataset_cleaned

# Literature
literature_papers = examination_dataset[["Literature"]]
literature_papers

literature_dataset_cleaned = literature_papers.dropna()
literature_dataset_cleaned

# History
history_papers = examination_dataset[["History"]]
history_papers

history_dataset_cleaned = history_papers.dropna()
history_dataset_cleaned

# Geography
geography_papers = examination_dataset[["Geography"]]
geography_papers

geography_dataset_cleaned = geography_papers.dropna()
geography_dataset_cleaned

# Civic Education
civic_education_papers = examination_dataset[["Civic_Education"]]
civic_education_papers

civic_education_dataset_cleaned = civic_education_papers.dropna()
civic_education_dataset_cleaned

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

# Round the score to the 2nd point
math_round_score = round(math_average, 2)
physics_round_score =  round(physics_average, 2)
chemistry_round_score = round(chemistry_average, 2)
biology_round_score = round(biology_average, 2)
english_round_score = round(english_average, 2)
literature_round_score = round(literature_average, 2)
history_round_score = round(history_average, 2)
geography_round_score = round(geography_average, 2)
civic_education_round_score = round(civic_education_average, 2)

labels_average = ["Math", "Literature", "English", "Physics", "Chemistry", "Biology", "History",
                    "Geography", "Civic Education"]
counts_average_round = [math_round_score, literature_round_score, english_round_score, physics_round_score, chemistry_round_score,
                        biology_round_score, history_round_score, geography_round_score, civic_education_round_score]

plt.figure(figsize = (20, 15))
sns.set(font_scale = 1.35)
score_average = plt.bar(labels_average, counts_average_round, color = "#00FFB4")

for counts_10 in score_average.patches:
  height = counts_10.get_height()
  label_x = counts_10.get_x() + counts_10.get_width() / 2
  label_y = counts_10.get_y() / height + height
  plt.text(label_x, label_y, s = f"{height:}", ha='center', va='bottom', color = "black", size = 15)

plt.xlabel("Subjects")
plt.ylabel("Occurences")
plt.title("GPA for each papers")

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

# Count the occurence of Math score
plt.figure(figsize = (28, 20))
sns.set(font_scale = 1.5)
math_sns = sns.countplot(examination_dataset.Math)
math_sns.set_xticklabels(math_sns.get_xticklabels(), rotation = 45)

for counts in math_sns.patches:
  height = counts.get_height()
  label_x = counts.get_x() + counts.get_width() / 2
  label_y = counts.get_y() / height + height
  plt.text(label_x, label_y, s = f"{height:}", ha='center', va='bottom', color = "black", size = 15, rotation = 90)

plt.xlabel("Score", fontsize = 20.5)
plt.ylabel("Occurrences", fontsize = 20.5)
plt.title("Math Score Distribution", fontsize = 22.5)

# Count the occurence of Literature score
## Literature is conducted as an essay exam so its point unit is 0.25
x = 0.0
lit_score = []
lit_occurences = []

while (x <= 10.0):
  lit_score.append(x)
  if (x in examination_dataset.Literature.values):
    lit_count = examination_dataset.Literature.value_counts()[x].item()
    
    lit_occurences.append(lit_count)
    x = x + 0.25
  else:
    
    lit_occurences.append(0)
    x = x + 0.25

#Literature score distribution
fig, ax = plt.subplots(figsize = (28, 20))
plt.bar(lit_score, lit_occurences, color = "#FF2AD6", edgecolor = "#000000", width = 0.2)
plt.title("Literature Score Distribution", fontsize = 22.5)
plt.xlabel("Score", fontsize = 20.5)
plt.ylabel("Occurences", fontsize = 20.5)
plt.show()

# Count the occurence of English score
plt.figure(figsize = (28, 20))
sns.set(font_scale = 1.5)
english_sns = sns.countplot(examination_dataset.English)
english_sns.set_xticklabels(english_sns.get_xticklabels(), rotation = 45)
plt.xlabel("Occurrences", fontsize = 22.5)
plt.ylabel("Score", fontsize = 22.5)
plt.title("English Score Distribution", fontsize = 22.5)

# Count the occurence of Physics score
plt.figure(figsize = (28, 20))
sns.set(font_scale = 1.45)
physics_sns = sns.countplot(examination_dataset.Physics)
physics_sns.set_xticklabels(physics_sns.get_xticklabels(), rotation = 45)
plt.xlabel("Score", fontsize = 20.5)
plt.ylabel("Occurrences", fontsize = 20.5)
plt.title("Physics Score Distribution", fontsize = 22.5)

# Count the occurence of Chemistry score
plt.figure(figsize = (28, 20))
sns.set(font_scale = 1.45)
chemistry_sns = sns.countplot(examination_dataset.Chemistry)
chemistry_sns.set_xticklabels(chemistry_sns.get_xticklabels(), rotation = 45)
plt.xlabel("Score", fontsize = 20.5)
plt.ylabel("Occurrences", fontsize = 20.5)
plt.title("Chemistry Score Distribution", fontsize = 22.5)

# Count the occurence of Biology score
plt.figure(figsize = (28, 20))
sns.set(font_scale = 1.45)
biology_sns = sns.countplot(examination_dataset.Biology)
biology_sns.set_xticklabels(biology_sns.get_xticklabels(), rotation = 45)

for counts in biology_sns.patches:
  height = counts.get_height()
  label_x = counts.get_x() + counts.get_width() / 2
  label_y = counts.get_y() / height + height
  plt.text(label_x, label_y, s = f"{height:}", ha='center', va='bottom', color = "black", size = 15, rotation = 90)

plt.xlabel("Score", fontsize = 20.5)
plt.ylabel("Occurrences", fontsize = 20.5)
plt.title("Biology Score Distribution", fontsize = 22.5)

# Count the occurence of History score
plt.figure(figsize = (28, 20))
sns.set(font_scale = 1.45)
history_sns = sns.countplot(examination_dataset.History)
history_sns.set_xticklabels(history_sns.get_xticklabels(), rotation = 45)

for counts in history_sns.patches:
  height = counts.get_height()
  label_x = counts.get_x() + counts.get_width() / 2
  label_y = counts.get_y() / height + height
  plt.text(label_x, label_y, s = f"{height:}", ha='center', va='bottom', color = "black", size = 15, rotation = 90)

plt.xlabel("Score", fontsize = 20.5)
plt.ylabel("Occurrences", fontsize = 20.5)
plt.title("History Score Distribution", fontsize = 22.5)

# Count the occurence of Geography score
plt.figure(figsize = (28, 20))
sns.set(font_scale = 1.45)
geography_sns = sns.countplot(examination_dataset.Geography)
geography_sns.set_xticklabels(geography_sns.get_xticklabels(), rotation = 45)

for counts in geography_sns.patches:
  height = counts.get_height()
  label_x = counts.get_x() + counts.get_width() / 2
  label_y = counts.get_y() / height + height
  plt.text(label_x, label_y, s = f"{height:}", ha='center', va='bottom', color = "black", size = 15, rotation = 90)

plt.xlabel("Score", fontsize = 20.5)
plt.ylabel("Occurrences", fontsize = 20.5)
plt.title("Geography Score Distribution", fontsize = 22.5)

# Count the occurence of Civic Education score
plt.figure(figsize = (28, 20))
sns.set(font_scale = 1.45)
civic_education_sns = sns.countplot(examination_dataset.Civic_Education)
civic_education_sns.set_xticklabels(civic_education_sns.get_xticklabels(), rotation = 45)

for counts_civic in civic_education_sns.patches:
  list_height_civic = counts_civic.get_height()
  label_x = counts_civic.get_x() + counts_civic.get_width() / 2
  label_y = counts_civic.get_y() / list_height_civic + list_height_civic
  plt.text(label_x, label_y, s = f"{list_height_civic:}", ha='center', va='bottom', color = "black", size = 15, rotation = 90)

plt.xlabel("Score", fontsize = 20.5)
plt.ylabel("Occurrences", fontsize = 20.5)
plt.title("Civic Education Score Distribution", fontsize = 22.5)

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
