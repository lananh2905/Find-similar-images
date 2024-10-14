# Import lib
from flask import Flask, request, render_template, redirect
from image_search import find_similar_images
import pandas as pd
import numpy as np

# Create objects
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/dataset/seg_test'
df_seg_test_path = pd.read_csv('database/seg_test_path.csv')


# Show form upload
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)

        file = request.files['file']

        if file.filename == '':
            return redirect(request.url)

        if file:
            # Read image path
            filename = file.filename
            index = df_seg_test_path[df_seg_test_path['Path'] == filename].index[0]
            label = df_seg_test_path.Name[index]
            file_path = 'static/dataset/seg_test' + '/' + label + '/' + filename;
            
            # Call function to find top 10 closest
            similar_images = find_similar_images(file_path)
            return render_template('index.html', uploaded_image=file_path, results=similar_images)
            
    return render_template('index.html')

# Run app
if __name__ == '__main__':
    app.run(debug=True)
