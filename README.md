# Disease Prediction

A machine learning-based project to predict diseases based on input symptoms. This project leverages data-driven insights to assist in preliminary disease diagnosis, helping users understand potential health issues quickly.

## Features
- Input symptoms and receive predictions of possible diseases.
- Utilizes machine learning models for accurate predictions.
- Interactive user interface for ease of use.

## Technologies Used
- Python
- Pandas and NumPy for data manipulation
- Scikit-learn for building machine learning models
- Flask for the web framework
- HTML and CSS for front-end

## How I Developed This Project
1. **Dataset Collection**:
   - I collected a publicly available dataset that maps symptoms to diseases.
   - The dataset was cleaned and preprocessed using Pandas to handle missing values and inconsistencies.

2. **Model Development**:
   - I used Scikit-learn to build machine learning models, including decision trees and random forests.
   - The model was trained on the dataset to predict diseases based on input symptoms.
   - After training, the model was saved using joblib for later use in the web application.

3. **Web Application Development**:
   - I used Flask to create a simple and interactive web interface.
   - The interface allows users to input symptoms, and the application returns a prediction based on the trained model.
   - HTML and CSS were used for designing the front-end, ensuring a user-friendly experience.

4. **Testing and Optimization**:
   - The application was tested with various inputs to ensure accuracy and reliability.
   - Model performance was evaluated and optimized using techniques like hyperparameter tuning.

5. **Deployment**:
   - The application can be deployed locally by running the Flask server.

## How to Run the Project
1. Clone the repository:
   ```bash
   git clone https://github.com/SurajReddy18/Disease_Prediction.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Disease_Prediction
   ```
3. Install the required dependencies manually (since no `requirements.txt` file is used):
   ```bash
   pip install flask pandas scikit-learn
   ```
4. Run the Flask application:
   ```bash
   python app.py
   ```
5. Open your web browser and visit:
   ```plaintext
   http://127.0.0.1:5000/
   ```

## Dataset
The dataset used for training the model contains various symptoms mapped to their respective diseases. This dataset is processed and used to train machine learning models for predictions.

## Project Structure
- `app.py`: Main Flask application file.
- `templates/`: Contains HTML templates for the user interface.
- `static/`: Contains static files like CSS and JavaScript.
- `model/`: Trained machine learning model files.
- `data/`: Dataset used for training and testing.

## Contributions
Contributions are welcome! Feel free to fork this repository and submit pull requests.

## License
This project is licensed under the **MIT License**. You can view the license [here](https://github.com/SurajReddy18/Disease_Prediction/blob/main/LICENSE).

## Contact
If you have any questions or feedback, feel free to reach out:
- **Email**: surajreddy107@gmail.com
- **GitHub**: [SurajReddy18](https://github.com/SurajReddy18)
