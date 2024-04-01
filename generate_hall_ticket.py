from flask import Flask, request, jsonify
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
# CORS(app, resources={r"/api/*": {"origins": "http://localhost:4200"}})

from sqlalchemy import create_engine, text
# @app.route('/api/generate_pdf', methods=['OPTIONS'])
# def handle_options():
#     return '', 200, {
#         'Access-Control-Allow-Origin': 'http://localhost:4200',
#         'Access-Control-Allow-Methods': 'POST',
#         'Access-Control-Allow-Headers': 'Content-Type'
#     }


# @app.route('/generate_pdf', methods=['POST'])
# def generate_certificate_route():
#     data = request.get_json()
#     fullname = data.get('fullname')
#     fathername = data.get('fathername')
#     dob = data.get('date')
#     age = data.get('age')
#     age_group = data.get('age_group')
#     email = data.get('email')
#     # logo_path = data.get('logoPath')
#     filename = 'certificate.pdf'  

#     generate_hall_ticket("AG/EC.123", fullname, age, age_group, fathername,"123456789012", "9876543210", "ExamCentreA", "Country", "hall_ticket.pdf", "10-Mar-2024")
#     return jsonify({'success': True, 'filename': filename})

def generate_hall_ticket(roll_no, name, age, age_group, father_name, aadhar_no, mobile_no,  exam_centre, exam_centre_address, filename, exam_date):
    c = canvas.Canvas(filename, pagesize=(505, 405))  # shorter page size
    c.setStrokeColorRGB(1, 0.5, 0)
    # Draw border for entire document
    c.rect(5, 5, 495, 395)

    # Draw border for main content area
    c.rect(20, 20, 460, 360)

    c.setStrokeColorRGB(1, 0.5, 0)

    # Roll No/Ref No
    c.drawString(30, 350, f"Roll No/Ref No.: {roll_no}")

    # Name
    c.drawString(30, 300, f"Name: {name}")

    # Age
    c.drawString(30, 275, f"Age: {age}")

    # Age Group
    c.drawString(30, 255, f"Age Group: {age_group}")

    # Father's Name
    c.drawString(30, 235, f"Father's Name: {father_name}")

    # Aadhar Card Number
    c.drawString(30, 215, f"Aadhar Card Number: {aadhar_no}")

    # Mobile Number
    c.drawString(30, 195, f"Mobile Number: {mobile_no}")

    # Exam Date
    c.drawString(30, 175, f"Exam Date: {exam_date}")

    # Exam Centre
    c.drawString(30, 155, f"Exam Centre: {exam_centre}")

    # Exam Centre Address
    c.drawString(30, 135, f"Exam Centre Address: {exam_centre_address}")

    # Signature of Participant
    c.drawString(180, 100, "Signature of Participant:")
    c.line(320, 100, 460, 100)

    # Signature of Bible Quiz Convener
    c.drawString(180, 60, "Signature of Bible Quiz Convener:")
    c.line(365, 60, 460, 60)

    # Draw the logo in the top right corner
    c.drawImage('./imyf_landing_page/src/assets/imgs/IMYF_logo.jpg', 400, 315, width=60, height=60)
    c.save()

# Example usage:
generate_hall_ticket("AG/EC.123", "John Doe", "25", "AG", "John Doe Sr.", "1234 5678 9012", "9876543210", "March 15, 2024", "Exam Centre A", "123 Main St, City, Country", "hall_ticket_shorter.pdf")

# def generate_refNo(age_group, exam_centre, mobile_no):
    


if __name__ == '__main__':
    app.run(debug=True)
