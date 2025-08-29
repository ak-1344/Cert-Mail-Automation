import smtplib
import ssl
from email.message import EmailMessage
import pandas as pd

# -----------------------
# Configuration
# -----------------------
SENDER_EMAIL = "example@gmaiol.com"
APP_PASSWORD = "gggg gggg gggg gggg"  # Gmail App Password

# Department group links
DEPT_GROUP_LINKS = {
    "Frontend": "https://chat.whatsapp.com/jskdfhjidsknsdjnjs",
    "Backend": "https://chat.whatsapp.com/sdagsdagfdfgfdgfddfgg",
    "AiMl": "https://chat.whatsapp.com/sadfrgtregfdfvserfgrtedfg",
    "Design": "https://chat.whatsapp.com/sfefrsdddfgregtgfdfdgfd",
    "Social Media": "https://chat.whatsapp.com/ddddddddddddddddd",
    "Management": "https://chat.whatsapp.com/ssssssssssefrfgfgrgrg"
}

# -----------------------
# Send Email Function
# -----------------------
def send_group_invite(to_email, name, reg_number, department):
    subject = f"Welcome to {department} Department - Join Your Group!"

    group_link = DEPT_GROUP_LINKS.get(department, "Group link not available")

    body = f"""Dear {name} ({reg_number}),

Congratulations on being selected to join the Nexus Club in the {department} Department!

To start collaborating with your peers, please join your department group using the link below:

{group_link}

We look forward to your active participation and contributions in the {department} Department.

Best regards,
Who?
President
"""

    # Prepare email
    msg = EmailMessage()
    msg['From'] = SENDER_EMAIL
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.set_content(body)

    # Send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(SENDER_EMAIL, APP_PASSWORD)
        server.send_message(msg)
        print(f"✅ Invite sent to {to_email} for {department} Department")

# -----------------------
# Main
# -----------------------
def main():
    df = pd.read_csv("recruitment.csv")  # CSV must have columns: Name, Registration, Email, Position
    for _, row in df.iterrows():
        name = row["Name"].strip()
        reg_number = str(row["Registration"]).strip()
        email = row["Email"].strip()
        department = row["Position"].strip()  # Must match keys in DEPT_GROUP_LINKS

        send_group_invite(email, name, reg_number, department)

if __name__ == "__main__":
    main()
