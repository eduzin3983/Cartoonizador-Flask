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

Additionally, this project served as a practical opportunity to **develop and implement REST APIs with Flask**, as well as to **host the application in the cloud**. The main practices covered include:

- File upload via POST requests  
- Redirection with flash messages for user feedback  
- Route configuration with dynamic parameters for greater flexibility  
- Returning static files and dynamically rendered HTML pages  
- Integration and execution in cloud environments for scalability and accessibility  

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

```bash
# 1. Clone the repository
git clone https://github.com/your-username/cartoonizer-flask.git
cd cartoonizer-flask
```
```bash
# 2. Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
```

```bash
# 3. Install dependencies
pip install -r requirements.txt
```
```bash
# 4. Start the server
python app.py
```

```bash
# 5. Access in your browser:
http://localhost:5000
```

---

## 🧪 Technologies Used

- [Python 3](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/)
- [OpenCV](https://opencv.org/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- HTML5, CSS3, JavaScript
- Local SQLite database

---

## 📂 Project Structure

```
.  
├── app.py                  # Main application file  
├── database.db             # SQLite database  
├── uploads/                # Original images  
├── cartooned/              # Cartoonized images  
├── static/                 # Static files  
│   ├── style.css           # CSS styles  
│   └── fundo/              # Background resources  
├── templates/              # HTML templates  
│   ├── index.html          # Home page  
│   ├── galeria.html        # Gallery page  
│   └── detalhe_imagem.html # Image details page  
└── README.md               # Project documentation
```

---

## 📸 Interface

- Home page with upload button
- Image gallery with "View processed image" button
- Details page with original image, cartoonized image, and metadata

---

## 📬 Contact

For questions or suggestions, feel free to open an issue or get in touch.  
If you'd like to contribute, you are very welcome! 🤝