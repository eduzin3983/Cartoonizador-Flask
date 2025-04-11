# === Built-in ===
import os
from datetime import datetime

# === Third-party ===
import cv2
from flask import Flask, render_template, request, jsonify, send_file, url_for, flash, redirect
from werkzeug.utils import secure_filename
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# === Flask Config ===
app = Flask(__name__)
app.secret_key = '123456789'

UPLOAD_FOLDER = 'uploads'
CARTOONED_FOLDER = 'cartooned'

# Create folders if they don't exist
for folder in [UPLOAD_FOLDER, CARTOONED_FOLDER]:
    if not os.path.exists(folder):
        os.makedirs(folder)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['CARTOONED_FOLDER'] = CARTOONED_FOLDER

# === SQLAlchemy Config ===
Base = declarative_base()

class ProcessedImage(Base):
    __tablename__ = 'processed_images'

    id = Column(Integer, primary_key=True)
    filename = Column(String, nullable=False)
    image_url = Column(String, nullable=False)
    cartoon_url = Column(String, nullable=False)
    ip = Column(String)
    timestamp = Column(String)

engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

# === Utils ===
def get_unique_filename(directory, filename):
    """
    Generate a unique filename in the specified directory.
    """
    base, ext = os.path.splitext(filename)
    counter = 1
    unique_filename = filename
    while os.path.exists(os.path.join(directory, unique_filename)):
        unique_filename = f"{base}{counter}{ext}"
        counter += 1
    return unique_filename

# === Routes ===

@app.route('/')
def index():
    """
    Render the home page with the upload form.
    """
    return render_template('index.html')

@app.route('/image/<filename>')
def image_details(filename):
    """
    Display details of the uploaded image.
    """
    session = Session()
    imagem = session.query(ProcessedImage).filter_by(filename=filename).first()
    session.close()

    if not imagem:
        return "Imagem não encontrada", 404

    return render_template('detalhe_imagem.html', imagem=imagem)

@app.route('/cartooned/<filename>')
def cartooned_file(filename):
    """
    Serve the cartoonized image by filename.
    """
    file = os.path.join(app.config['CARTOONED_FOLDER'], filename)
    return send_file(file)

@app.route('/upload', methods=['POST'])
def upload_image():
    """
    Handle image upload, process it to apply a cartoon effect, save it, and store metadata in the database.
    """
    if 'image' not in request.files:
        return jsonify({'error': 'No image file uploaded'}), 400

    file = request.files['image']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    # === Save with unique name ===
    original_filename = secure_filename(file.filename)
    filename = get_unique_filename(app.config['UPLOAD_FOLDER'], original_filename)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)

    # --- Cartoon Processing (black & white effect on the whole image) ---
    # Black and white cartoon effect applied to the entire image
    image = cv2.imread(filepath)
    if image is None:
        return jsonify({'error': 'Error processing image'}), 500

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray_blur = cv2.medianBlur(gray, 5)

    # Smooth the image using bilateral filter
    smooth_gray = cv2.bilateralFilter(gray_blur, 9, 75, 75)

    cartoon = cv2.adaptiveThreshold(
        smooth_gray, 255,
        cv2.ADAPTIVE_THRESH_MEAN_C,
        cv2.THRESH_BINARY, 19, 3
    )

    # --- Save cartoon with unique name ---
    cartoon_filename = f'cartoon_{filename}'
    cartoon_filename = get_unique_filename(app.config['CARTOONED_FOLDER'], cartoon_filename)
    cartoon_path = os.path.join(app.config['CARTOONED_FOLDER'], cartoon_filename)
    cv2.imwrite(cartoon_path, cartoon)

    # --- Metadata ---
    ip_address = request.remote_addr
    upload_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    image_url = f'/uploads/{filename}'
    cartoon_url = f'/cartooned/{cartoon_filename}'

    # --- Save in database ---
    session = Session()
    new_record = ProcessedImage(
        filename=filename,
        image_url=image_url,
        cartoon_url=cartoon_url,
        ip=ip_address,
        timestamp=upload_time
    )
    session.add(new_record)
    session.commit()
    session.close()

    flash('Imagem enviada com sucesso!')
    return redirect(url_for('index'))

@app.route('/image')
def imagens():
    """
    Display a gallery of all uploaded images.
    """
    session = Session()
    imagens = session.query(ProcessedImage).order_by(ProcessedImage.id.desc()).all()
    session.close()
    return render_template('galeria.html', imagens=imagens)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    """
    Serve the uploaded original image by filename.
    """
    file = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    return send_file(file)

if __name__ == '__main__':
    app.run(debug=True)
