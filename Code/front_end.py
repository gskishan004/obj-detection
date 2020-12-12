from flask import Flask, render_template, request
from pathlib import Path
import os 
import subprocess
import shutil
from shutil import copyfile


#################################################################################
#               MAINTAINER : Ishan Khanka (ik1304) 
#################################################################################

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['RESULT_FOLDER'] = 'static/'
app.config['YOLO_RES_FOLDER'] = 'runs/detect/exp'

@app.route('/')
def upload_f():
    return render_template('upload.html')

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if request.form['submit_button'] == 'Predict':
            f = request.files['file']
            f.save(os.path.join(app.config['UPLOAD_FOLDER'],f.filename))
            
            # Prediction for blood cells
            if request.form.get('blood_cell_prediction'):
                print('Using model for blood cells')
                temp_cmd = ['python', 'detect.py', '--source', 'uploads', '--weights', 'runs/train/exp29/weights/best.pt']
                predict_output = subprocess.check_output(temp_cmd).decode('ascii')
                print(predict_output)

            # Prediction for normal YOLO images
            else:
                print('Using model for normal images')
                temp_cmd = ['python', 'detect.py', '--source', 'uploads', '--weights', 'yolov3.pt', '--conf', '0.25']
                predict_output = subprocess.check_output(temp_cmd).decode('ascii')
                print(predict_output)

            # Copy result image to static folder so it can be display in show_result.html 
            copyfile(app.config['YOLO_RES_FOLDER'] +'/'+f.filename, app.config['RESULT_FOLDER'] +f.filename)

            # Remove the src folder for next prediction
            shutil.rmtree(app.config['YOLO_RES_FOLDER'])
            full_filename = os.path.join(app.config['RESULT_FOLDER'], f.filename)
            print(full_filename)

            return render_template("show_result.html", user_image = full_filename)
                

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug = True, host= '0.0.0.0', port = port)