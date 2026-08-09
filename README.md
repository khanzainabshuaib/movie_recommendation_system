# 🎬 Movie Recommendation System

A **Machine Learning-based Movie Recommendation System** built using **Python and Flask**. The application recommends movies based on the movie selected by the user and provides the results through a simple and user-friendly web interface.

## 🚀 Features

* 🎬 Movie recommendations based on similarity
* 🤖 Machine Learning-based recommendation engine
* 🌐 Flask web application
* 🔎 Easy movie selection
* ⚡ Fast recommendation results
* 📊 TMDB movie dataset
* 🎨 Simple and responsive web interface
* 💾 Pre-trained recommendation model generated locally

## 🛠️ Technologies Used

* **Python**
* **Flask**
* **Pandas**
* **NumPy**
* **Scikit-learn**
* **PyArrow**
* **Pickle**
* **HTML**
* **CSS**
* **Jinja2**

## 📂 Project Structure

```text
movie_recommendation_system/
│
├── app.py
├── recommendation.py
├── train_model.py
├── movies.csv
├── tmdb_5000_movies.csv
├── tmdb_5000_credits.csv
├── requirements.txt
│
├── model/
│   └── (Generated .pkl files)
│
├── static/
│   └── css/
│       └── style.css
│
├── templates/
│   ├── index.html
│   └── result.html
│
├── .gitignore
└── README.md
```

## 🧠 How the System Works

The system uses movie information from the **TMDB 5000 Movies and Credits datasets**.

The workflow is:

```text
User Selects a Movie
        ↓
Flask Web Interface
        ↓
Recommendation Function
        ↓
Movie Feature Processing
        ↓
Similarity Calculation
        ↓
Find Similar Movies
        ↓
Display Recommended Movies
```

The recommendation system calculates the similarity between movies and returns movies that are most similar to the selected movie.

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/khanzainabshuaib/movie_recommendation_system.git
```

### 2. Open the Project Folder

```bash
cd movie_recommendation_system
```

### 3. Install Dependencies

```bash
py -m pip install -r requirements.txt
```

If you don't have a `requirements.txt` file or a package is missing, install:

```bash
py -m pip install flask pandas numpy scikit-learn pyarrow
```

## 🏗️ Generate the Model

The large `.pkl` model files are **not stored in this GitHub repository** because GitHub has a 100 MB file-size limit.

The project includes `train_model.py`, which can generate the required model files locally.

Run:

```bash
py train_model.py
```

After successful execution, the required files should be created inside:

```text
model/
├── movies.pkl
└── similarity.pkl
```

> Make sure these files are generated before starting the Flask application.

## ▶️ Run the Application

Start the Flask server:

```bash
py app.py
```

You should see something similar to:

```text
Running on http://127.0.0.1:5000
```

Open your browser and visit:

```text
http://127.0.0.1:5000
```

## 🎯 Example

### Input

```text
Selected Movie: Avatar
```

### Output

The system displays a list of movies similar to the selected movie.

Example:

```text
Recommended Movies:

1. Guardians of the Galaxy
2. Star Trek
3. John Carter
4. Avengers
5. Interstellar
```

> Recommendations may vary depending on the generated model and dataset.

## 📊 Dataset

This project uses the **TMDB 5000 Movie Dataset**, containing information about movies such as:

* Movie titles
* Genres
* Keywords
* Cast
* Crew
* Overview
* Popularity
* Release information

Dataset files included in the project:

```text
tmdb_5000_movies.csv
tmdb_5000_credits.csv
```

## 🔐 Large Model Files

The following files are intentionally excluded from GitHub:

```text
model/movies.pkl
model/similarity.pkl
```

This is because:

* `movies.pkl` is approximately **73 MB**
* `similarity.pkl` is approximately **176 MB**
* GitHub has a **100 MB maximum file size** for regular Git repositories.

They are excluded using `.gitignore`:

```text
model/*.pkl
```

Generate them locally using:

```bash
py train_model.py
```

## 📦 Requirements

Main Python libraries:

```text
Flask
Pandas
NumPy
Scikit-learn
PyArrow
```

Install everything using:

```bash
py -m pip install -r requirements.txt
```

## 🔮 Future Improvements

* 🎞️ Add movie posters
* ⭐ Add movie ratings
* 🎭 Add genre-based filtering
* 👤 Add personalized user recommendations
* 🔐 Add user authentication
* 🌐 Deploy the application online
* 📱 Improve mobile responsiveness
* 🔗 Integrate the TMDB API
* 🧠 Implement collaborative filtering
* 🚀 Improve recommendation accuracy

<img width="1919" height="967" alt="image" src="https://github.com/user-attachments/assets/111b2063-c643-4a17-88fd-ae77a7ebe3b1" />

## 👨‍💻 Author

**Khanzainabshuaib**

GitHub:

https://github.com/khanzainabshuaib

## ⭐ GitHub Repository

https://github.com/khanzainabshuaib/movie_recommendation_system

If you find this project useful, please consider giving it a ⭐ on GitHub.
