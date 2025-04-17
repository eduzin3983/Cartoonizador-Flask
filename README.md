# 🖼️ Image Cartoonizer with Flask + OpenCV

This project is a web application that allows users to:  
- Upload an image 📤  
- Generate a black-and-white cartoonized version 🖌️  
- View a gallery of uploaded images 🖼️  
- Access details of each image (date, URLs, etc.)

---

## 📚 Practical Project — *Introduction to Cloud Computing*  
**AiotLab — PUC-Campinas**

This project was developed as a practical part of the course **"Introduction to Cloud Computing"**, offered by **AiotLab / PUC-Campinas** 🎓.

It also served as an opportunity to apply knowledge of **REST API development with Flask** and to gain experience deploying applications to cloud environments. Key practices covered include:

- Handling file uploads via POST requests  
- Configuring dynamic routes  
- Serving static files and rendering HTML templates  
- Containerizing the application using Docker for portability and consistency 
- Running the application in isolated environments using Docker containers  
- Preparing the project for deployment in cloud infrastructure (e.g., AWS, Azure, etc.)

---

## 🚀 Features

✅ Image upload (.jpg, .png, .jpeg...)  
✅ Automatic detection of duplicate names  
✅ Application of black-and-white cartoon-style filter  
✅ Gallery view  
✅ Individual details for each image  
✅ Data logging  
✅ Responsive layout with animated background (video)

---

## 🌐 Application Routes

| Route                   | Method | Function                                                               |
|-------------------------|--------|------------------------------------------------------------------------|
| `/`                     | GET    | Home page with upload form                                             |
| `/upload`               | POST   | Receives the image, processes it, saves it, and redirects with a flash message |
| `/imagens`              | GET    | Displays a gallery of uploaded images                                  |
| `/image/<filename>`     | GET    | Details page for the original and cartoonized image                    |
| `/uploads/<filename>`   | GET    | Serves the original image directly                                     |
| `/cartooned/<filename>` | GET    | Serves the cartoonized image directly                                  |

---

## 🛠️ How to Run Locally
### 1. Clone the repository
```bash
git clone https://github.com/eduzin3983/Flask-Cartoonizer.git
```
```bash
cd Flask-Cartoonizer/
```
### 2. Create and activate a virtual environment
```bash
python -m venv .venv
```
```bash
source venv/bin/activate  # On Linux/Mac
```
```bash
venv\Scripts\activate   # On Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```
### 4. Start the server
```bash
python app.py
```

### 5. Access in your browser:
```bash
http://localhost:5000
```

---

# 🐳 Docker Setup

> If you prefer running the project inside a Docker container, follow the steps below:

### 1. Clone the repository
```bash
git clone https://github.com/eduzin3983/Flask-Cartoonizer.git
```
```bash
cd Flask-Cartoonizer/
```

### 2. Build the Docker Image
```bash
docker build -t flask-cartoonizer .
```

### 3. Run the Docker Container
```bash
docker run --rm -p 5000:5000 --name cartoonizer-app flask-cartoonizer
```

### 5. Access in your browser:
```bash
http://localhost:5000
```

---

## 🧪 Technologies Used

- [Python 3](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/)
- [OpenCV](https://opencv.org/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Docker](https://www.docker.com/)
- HTML5, CSS3, JavaScript
- Local SQLite database

---

## 📂 Project Structure

```
.  
├── app.py                  # Main Flask application  
├── requirements.txt        # Python dependencies  
├── database.db             # SQLite database (auto-generated)
├── uploads/                # Original uploaded images (auto-generated)
├── cartooned/              # Processed cartoonized images (auto-generated)
├── static/                 # Static assets  
│   ├── style.css  
│   └── background/              
├── templates/              # HTML templates  
│   ├── index.html  
│   ├── gallery.html  
│   └── image_detail.html  
├── .dockerignore           # Docker context exclusions  
├── Dockerfile              # Docker build instructions  
└── README.md               # Project documentation
```

---

## 📸 Interface Overview

- **Home Page**: Upload form with file input and submit button  
- **Gallery Page**: Displays a grid of uploaded images with preview buttons  
- **Details Page**: Shows the original and cartoonized versions side by side, along with image metadata (filename, upload date, etc.)

---

## 📬 Contact

For questions or suggestions, feel free to open an issue or get in touch.  
If you'd like to contribute, you are very welcome! 🤝