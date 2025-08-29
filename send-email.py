import smtplib
import ssl
from email.message import EmailMessage
import pandas as pd
import os

# -----------------------
# Configuration
# -----------------------
SENDER_EMAIL = "example@gmail.com"
APP_PASSWORD = "gggg gggg gggg gggg"  # Gmail App Password

# CC recipients per department (list of emails)
CC_MAPPING = {
    "Frontend": ["example@gmail.com", "example@gmail.com", "example@gmail.com", "example@gmail.com"],
    "Backend": ["example@gmail.com", "example@gmail.com", "example@gmail.com", "example@gmail.com"],
    "AiMl": ["example@gmail.com", "example@gmail.com", "example@gmail.com", "example@gmail.com"],
    "Design": ["example@gmail.com", "example@gmail.com"],
    "Social Media": ["example@gmail.com", "example@gmail.com"],
    "Management": ["example@gmail.com", "example@gmail.com", "example@gmail.com", "example@gmail.com"]
}

# Department-specific lines
DEPT_LINES = {
    "Frontend": "bring innovative ideas to our web and UI projects",
    "Backend": "enhance our backend systems and API integrations",
    "AiMl": "drive impactful research and development in AI/ML",
    "Design": "enhance our creative initiatives in design",
    "Social Media": "strengthen our social media outreach and engagement",
    "Management": "support organizational and leadership efforts effectively"
}

# -----------------------
# Send Email Function
# -----------------------
def send_certificate(to_email, name, cert_path, department):
    subject = "Welcome to <name> Club!"

    # Department-specific line
    dept_line = DEPT_LINES.get(department, "contribute effectively to Nexus Club initiatives")

    # Email body template
    # Only include FFCS course line if reg_number starts with '24'
    ffcs_line = ""
    if str(cert_path).split(os.sep)[-1].startswith("24"):
        ffcs_line = "\nIn addition, you also have the chance to enroll in our  course,<Course Code> - <Course Name>, which will help you build valuable skills for your academic and club projects.\n"

    # Remove leading/trailing whitespace and blank lines from the body
    body = f"""Dear {name},

Congratulations on being selected to join the Nexus Club in the {department} Department! We are excited to have you on board and can’t wait to see the energy and fresh ideas you will bring to the team.

As a member of the {department} Department, you are uniquely positioned to {dept_line}. This will be a wonderful opportunity for you to learn, collaborate, and grow alongside like-minded peers.
{ffcs_line}
Attached to this email is your personalized certificate of membership. Please keep it safe as it serves as a testament to your dedication and enthusiasm.

We look forward to your journey with Nexus Club and the positive impact you will make in the community. Once again, congratulations on becoming part of the team!

Best regards,
Who?
President
"""

    # Prepare email
    msg = EmailMessage()
    msg['From'] = SENDER_EMAIL
    msg['To'] = to_email
    msg['Cc'] = ", ".join(CC_MAPPING.get(department, []))
    msg['Subject'] = subject
    msg.set_content(body)

    # Attach certificate
    with open(cert_path, 'rb') as f:
        file_data = f.read()
        file_name = os.path.basename(cert_path)
    msg.add_attachment(file_data, maintype="image", subtype="png", filename=file_name)

    # Send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(SENDER_EMAIL, APP_PASSWORD)
        server.send_message(msg)
        print(f"✅ Sent to {to_email} | CC: {CC_MAPPING.get(department)}")

# -----------------------
# Main
# -----------------------
def main():
    df = pd.read_csv("certificate_data.csv")
    output_dir = "GeneratedCertificates"

    for _, row in df.iterrows():
        name = row["Name"].strip()
        reg_number = str(row["Registration"]).strip()
        email = row["Email"].strip()
        department = row["Position"].strip()  # Must exist in CSV

        cert_path = os.path.join(output_dir, f"{reg_number}.png")
        if os.path.exists(cert_path):
            send_certificate(email, name, cert_path, department)
        else:
            print(f"⚠️ Certificate not found for {name} ({reg_number})")

if __name__ == "__main__":
    main()
