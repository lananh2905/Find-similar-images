# Import lib
import numpy as np
import pandas as pd
import cv2
from scipy.spatial.distance import euclidean

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

# Function find similar images
def find_similar_images(input_image_path):
    
    # Read histogram features vector from database
    X_hist_features = np.load('database\X_hist_features.npy')
    df_seg_path = pd.read_csv('database\seg_path.csv')
    
    # Read and preprocess image
    image_size = (128, 128)
    image = cv2.imread(input_image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = cv2.resize(image, image_size)
    image_arr = np.array(image)
    hist_features = np.array(extract_histogram(image_arr, 256))
    
    # Caculate distance of image uploads with histogram features vector
    distances = [] 

    for index, feature in enumerate(X_hist_features):
        distance = euclidean(feature, hist_features) 
        distances.append((index, distance))
        
        
    # Choice top 10 closest
    distances.sort(key=lambda x: x[1])
    top_10_closest = np.array(distances[:10]).astype(float)
    
    index_closest = top_10_closest[:, 0].astype(int)
    eucli_closest = np.around(top_10_closest[:, 1].astype(float), decimals=2)
    
    # Save output include imge_path and euclidean of top 10 closest
    similar_images = [];
    
    for i, index in enumerate(index_closest):
        img_path = df_seg_path.Name[index] + '/' + df_seg_path.Path[index]
        similar_images.append((img_path, eucli_closest[i]))
    
    return similar_images