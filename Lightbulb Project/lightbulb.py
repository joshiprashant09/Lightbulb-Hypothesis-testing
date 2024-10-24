from flask import Flask, request, render_template, redirect, url_for
import pandas as pd
import numpy as np
from scipy import stats

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')  
@app.route('/upload', methods=['POST'])
def upload_file():
    try:
        if 'file' not in request.files:
            return redirect(url_for('home'))
        
        file = request.files['file']
        
        if file.filename == '':
            return redirect(url_for('home'))
        
        population_mean = float(request.form['population_mean'])

        data = pd.read_csv(file)

        if 'Hours' not in data.columns:
            return "Error: The dataset must contain a column named 'Hours'."

        sample_size = 25

        sample = data['Hours'].sample(n=sample_size, random_state=1)

        sample_mean = np.mean(sample)
        sample_std = np.std(sample, ddof=1) 


        t_statistic = (sample_mean - population_mean) / (sample_std / np.sqrt(sample_size))
        df = sample_size - 1  
        alpha = 0.05  
        t_critical = stats.t.ppf(1 - alpha / 2, df)  
        

        if abs(t_statistic) > t_critical:
            result = "Reject the null hypothesis. The company's claim is not acceptable."
        else:
            result = "Accecpt null hypothesis. The company's claim is acceptable."


        null_hypothesis = f"H0: The mean lifespan of the bulbs is {population_mean} hours."
        alt_hypothesis = f"H1: The mean lifespan of the bulbs is not {population_mean} hours."


        return render_template('result.html', sample_mean=sample_mean, sample_std=sample_std,
                               t_statistic=t_statistic, t_critical=t_critical,
                               result=result, null_hypothesis=null_hypothesis,
                               alt_hypothesis=alt_hypothesis)
    except Exception as e:

        return f"An error occurred: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True, port=5001)
