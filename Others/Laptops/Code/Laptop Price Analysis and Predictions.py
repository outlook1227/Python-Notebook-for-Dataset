# Import the libraries
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

# Read dataset
laptop_dataset = pd.read_csv("/content/Cleaned_Laptop_data.csv")
laptop_dataset

"Checking the dataset"
# Check for the dataset (missing data)
laptop_dataset.isna().sum()

# Check information of dataset
laptop_dataset.info()

laptop_dataset.describe()

# Check the dataset is full
list(pd.isna(laptop_dataset).any(axis=1)).count(False)

"Visualization the dataset with Heatmap"
sns.set(font_scale = 1.45)
plt.figure(figsize = (20, 15))
sns.heatmap(laptop_dataset[["graphic_card_gb", "display_size", "warranty", "latest_price", "old_price",
                            "discount", "star_rating", "ratings", "reviews"]].corr(), cmap="GnBu_r", annot = True)
plt.title("Heatmap for the Laptop dataset", fontsize = 17)
plt.show()

"Visualization with the information of dataset"
# 1: Count of the brand of computer
plt.figure(figsize = (20, 15))
sns.set(font_scale = 1.35)
count_brand = sns.countplot(laptop_dataset["brand"])
count_brand.set_xticklabels(count_brand.get_xticklabels(), rotation = 90)

for counts in count_brand.patches:
  bar_height = counts.get_height()
  label_x = counts.get_x() + counts.get_width() / 2
  label_y = counts.get_y() / bar_height + bar_height
  plt.text(label_x, label_y, s = f"{bar_height:}", ha='center', va='bottom', color = "black", size = 15)

plt.xlabel("Brand")
plt.ylabel("Count")
plt.title("The list of Brand Computer in dataset")
plt.show()

# 2: Count of the processor band of computer
plt.figure(figsize = (20, 15))
sns.set(font_scale = 1.35)
count_process_brand = sns.countplot(laptop_dataset["processor_brand"])
count_process_brand.set_xticklabels(count_process_brand.get_xticklabels())

for counts in count_process_brand.patches:
  bar_height = counts.get_height()
  label_x = counts.get_x() + counts.get_width() / 2
  label_y = counts.get_y() / bar_height + bar_height
  plt.text(label_x, label_y, s = f"{bar_height:}", ha='center', va='bottom', color = "black", size = 15)

plt.xlabel("Processor Brand")
plt.ylabel("Count")
plt.title("The list of Computer Brand")
plt.show()

# 3: Count the processor name of computer
plt.figure(figsize = (23, 15))
sns.set(font_scale = 1.4)
count_process_name = sns.countplot(laptop_dataset["processor_name"])
count_process_name.set_xticklabels(count_process_name.get_xticklabels(), rotation = 90)

for counts in count_process_name.patches:
  bar_height = counts.get_height()
  label_x = counts.get_x() + counts.get_width() / 2
  label_y = counts.get_y() / bar_height + bar_height
  plt.text(label_x, label_y, s = f"{bar_height:}", ha='center', va='bottom', color = "black", size = 15)

plt.xlabel("Processor Name")
plt.ylabel("Count")
plt.title("The list of Processor Name in Dataset")
plt.show()

# 4: Count the processor generations of computer
plt.figure(figsize = (20, 15))
sns.set(font_scale = 1.35)
count_process_gnrtn = sns.countplot(laptop_dataset["processor_gnrtn"])
count_process_gnrtn.set_xticklabels(count_process_gnrtn.get_xticklabels())

for counts in count_process_gnrtn.patches:
  bar_height = counts.get_height()
  label_x = counts.get_x() + counts.get_width() / 2
  label_y = counts.get_y() / bar_height + bar_height
  plt.text(label_x, label_y, s = f"{bar_height:}", ha='center', va='bottom', color = "black", size = 15)

plt.xlabel("Processor Generations")
plt.ylabel("Count")
plt.title("The list of Processor Generations")
plt.show()
