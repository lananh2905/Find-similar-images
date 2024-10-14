# Import lib
import numpy as np
import pandas as pd
import cv2
import os

#-----------------------------------------------------------------------
# Function

# Load data from folder
def load_dataset(data_dir):
    X = []
    y = []
    X_path = []
    image_size = (128, 128)
    
    for label_dir in os.listdir(data_dir):
        
        for img_file in os.listdir(os.path.join(data_dir, label_dir)):
            img_path = os.path.join(data_dir, label_dir, img_file)
            image = cv2.imread(img_path)
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            image = cv2.resize(image, image_size)
            X_path.append(img_file)
            X.append(image)
            y.append(label_dir)
            
    return X_path, np.array(X), y


# Extract histogram from a image
def extract_histogram(image, bin_size):
    row, column, channel = image.shape[:3]
    size = row * column
    
    feature = np.zeros(channel * bin_size)
    for k in range(channel):
        histogram = cv2.calcHist([image], [k], None, [bin_size], [0, 256]).flatten()
        histogram /= size  # Normalize histogram
        feature[k * bin_size:(k + 1) * bin_size] = histogram
    return feature

# Extract histogram features vector
def extract_features(X):
    X_features = []
    for image in X:
        features = extract_histogram(image, BIN_SIZE)
        
        X_features.append(features)
    
    return X_features

#---------------------------------------------------------------------------------
# Main program

seg_path = 'static/dataset/seg'
seg_test_path = 'static/dataset/seg_test'
BIN_SIZE = 256;

# Load data
X_seg_path, X_seg, y_seg = load_dataset(seg_path)
X_seg_test_path, X_seg_test, y_seg_test = load_dataset(seg_test_path)

# Extract and save into 'X_hist_features.npy'
X_hist_features = np.array(extract_features(X_seg))
np.save('database/X_hist_features.npy', X_hist_features)

# Create histogram and save into 'seg_path.csv'
df_seg_path = pd.DataFrame({
    "Path": X_seg_path,
    "Name": y_seg
})
df_seg_path.to_csv('database/seg_path.csv')

# Create histigram and save into 'seg_test_path.csv'
df_seg_test_path = pd.DataFrame({
    "Path": X_seg_test_path,
    "Name": y_seg_test
})
df_seg_test_path.to_csv('database/seg_test_path.csv')