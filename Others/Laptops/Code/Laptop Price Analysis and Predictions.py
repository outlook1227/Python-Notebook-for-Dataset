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

# 2: Count of the processor brand of computer
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

# 5: Count the RAM GB of brand computer
plt.figure(figsize = (20, 15))
sns.set(font_scale = 1.35)
count_process_gnrtn = sns.countplot(laptop_dataset["ram_gb"].str.replace('GB GB','GB'))
count_process_gnrtn.set_xticklabels(count_process_gnrtn.get_xticklabels())

for counts in count_process_gnrtn.patches:
  bar_height = counts.get_height()
  label_x = counts.get_x() + counts.get_width() / 2
  label_y = counts.get_y() / bar_height + bar_height
  plt.text(label_x, label_y, s = f"{bar_height:}", ha='center', va='bottom', color = "black", size = 15)

plt.xlabel("RAM - GB")
plt.ylabel("Count")
plt.title("Random Access Memory")
plt.show()

# 6: Count number of RAM Type
plt.figure(figsize = (20, 15))
sns.set(font_scale = 1.35)
count_ram_type = sns.countplot(laptop_dataset["ram_type"])
count_ram_type.set_xticklabels(count_ram_type.get_xticklabels())

for counts in count_ram_type.patches:
  bar_height = counts.get_height()
  label_x = counts.get_x() + counts.get_width() / 2
  label_y = counts.get_y() / bar_height + bar_height
  plt.text(label_x, label_y, s = f"{bar_height:}", ha='center', va='bottom', color = "black", size = 15)

plt.xlabel("RAM Type")
plt.ylabel("Count")
plt.title("The Type of Random Access Memory")
plt.show()

# 7: Count number of SSD Hardware
plt.figure(figsize = (20, 15))
sns.set(font_scale = 1.35)
count_ssd = sns.countplot(laptop_dataset["ssd"])
count_ssd.set_xlabel(count_ssd.get_xticklabels())

for counts in count_ssd.patches:
  bar_height = counts.get_height()
  label_x = counts.get_x() + counts.get_width() / 2
  label_y = counts.get_y() / bar_height + bar_height
  plt.text(label_x, label_y, s = f"{bar_height:}", ha='center', va='bottom', color = "black", size = 15)

plt.xlabel("SSD - GB")
plt.ylabel("Count")
plt.title("SSD Hardware")
plt.show()

# 8: Count number of HDD Hardware
plt.figure(figsize = (20, 15))
sns.set(font_scale = 1.35)
count_ssd = sns.countplot(laptop_dataset["hdd"])
count_ssd.set_xlabel(count_ssd.get_xticklabels())

for counts in count_ssd.patches:
  bar_height = counts.get_height()
  label_x = counts.get_x() + counts.get_width() / 2
  label_y = counts.get_y() / bar_height + bar_height
  plt.text(label_x, label_y, s = f"{bar_height:}", ha='center', va='bottom', color = "black", size = 15)

plt.xlabel("HDD - GB")
plt.ylabel("Count")
plt.title("HDD Hardware")
plt.show()

# 9: Operating Systems (OS) of Computer
plt.figure(figsize = (18, 12))
sns.set(font_scale = 1.35)
count_os = sns.countplot(laptop_dataset["os"])
count_os.set_xlabel(count_os.get_xticklabels())

for counts in count_os.patches:
  bar_height = counts.get_height()
  label_x = counts.get_x() + counts.get_width() / 2
  label_y = counts.get_y() / bar_height + bar_height
  plt.text(label_x, label_y, s = f"{bar_height:}", ha='center', va='bottom', color = "black", size = 15)

plt.xlabel("OS")
plt.ylabel("Count")
plt.title("Operating Systems of Computer")
plt.show()

# 10: Touchscreen of Computers
plt.figure(figsize = (18, 12))
sns.set(font_scale = 1.35)
count_touchscreen = sns.countplot(laptop_dataset["Touchscreen"])
count_touchscreen.set_xlabel(count_touchscreen.get_xticklabels())

for counts in count_touchscreen.patches:
  bar_height = counts.get_height()
  label_x = counts.get_x() + counts.get_width() / 2
  label_y = counts.get_y() / bar_height + bar_height
  plt.text(label_x, label_y, s = f"{bar_height:}", ha='center', va='bottom', color = "black", size = 15)

plt.xlabel("Touchscreen")
plt.ylabel("Count")
plt.title("Touchscreen of Computer")
plt.show()

"Visualization for the price with component of computer"
# The Computer Brand 
plt.figure(figsize = (18, 12))
brand_price = sns.boxplot(x = laptop_dataset["brand"], y = laptop_dataset["latest_price"], showfliers = False)
brand_price.set_xticklabels(brand_price.get_xticklabels(), rotation = 90)
plt.xlabel("Brand of Computer")
plt.ylabel("Price")
plt.show()

# The Computer Brand Processor
plt.figure(figsize = (18, 12))
processor_brand_price = sns.boxplot(x = laptop_dataset["processor_brand"], y = laptop_dataset["latest_price"], showfliers = False)
processor_brand_price.set_xticklabels(processor_brand_price.get_xticklabels())
plt.xlabel("Processor Brand of Computer")
plt.ylabel("Price")
plt.show()

# The Computer Operating Systems
plt.figure(figsize = (18, 12))
sns.set(font_scale = 1.35)
os_price = sns.boxplot(x = laptop_dataset["os"], y = laptop_dataset["latest_price"], showfliers = False)
os_price.set_xticklabels(processor_brand_price.get_xticklabels())
plt.xlabel("Operating Systems")
plt.ylabel("Price")
plt.show()

# The RAM Storage 
plt.figure(figsize = (18, 12))
sns.set(font_scale = 1.35)
ram_price = sns.boxplot(x = laptop_dataset["ram_gb"], y = laptop_dataset["latest_price"], showfliers = False)
ram_price.set_xticklabels(ram_price.get_xticklabels())
plt.xlabel("RAM Storage")
plt.ylabel("Price")
plt.show()

# The RAM Type
plt.figure(figsize = (18, 12))
sns.set(font_scale = 1.35)
ram_price = sns.boxplot(x = laptop_dataset["ram_type"], y = laptop_dataset["latest_price"], showfliers = False)
ram_price.set_xticklabels(ram_price.get_xticklabels())
plt.xlabel("RAM Type")
plt.ylabel("Price")
plt.show()

"Train data and test data"
def train_test_split(x, y, train_size = 0.8):
    # Set split data into training and set test
    train_size = int(len(x1) * train_size)

    x_train = x1[:train_size]
    y_train = x2[:train_size]

    x_test = x1[train_size:]
    y_test = x2[train_size:]

    return x_train, y_train, x_test, y_test

"Implement the function to compute the loss and error of dataset"
# Mean Squared Error (MSE)
def mean_squared_error(y_prediction, y_true):
  MSE = np.average((y_true - y_prediction) ** 2)
  return MSE

# Mean Absolute Error (MAE)
def mean_absolute_error(y_prediction, y_true):
  MAE = np.average(np.abs(y_prediction - y_true))
  return MAE
