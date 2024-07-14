from flask import Blueprint, render_template, request, send_file, jsonify
from app.utils.pdf_utils import extract_text_from_pdf
from app.utils.scraper import scrape_job_description
from app.utils.cv_generator import generate_cvs
import io

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        job_url = request.form['job_url']
        
        if 'file' not in request.files:
            return jsonify({'error': 'No file part'}), 400
        file = request.files['file']
        
        if file.filename == '':
            return jsonify({'error': 'No selected file'}), 400
        
        if file and file.filename.endswith('.pdf'):
            candidate_info = extract_text_from_pdf(file)
            job_description = scrape_job_description(job_url)
            
            cvs = generate_cvs(job_description, candidate_info)
            
            return jsonify({'cvs': cvs})
        else:
            return jsonify({'error': 'Please upload a PDF file'}), 400
    
    return render_template('index.html')

@main.route('/download', methods=['POST'])
def download():
    cvs = request.json['cvs']
    
    buffer = io.StringIO()
    buffer.write(cvs)
    buffer.seek(0)
    
    return send_file(
        io.BytesIO(buffer.getvalue().encode()),
        mimetype='text/plain',
        as_attachment=True,
        attachment_filename='generated_cvs.txt'
    )