# Nexus Club Certificate & Email Automation

This repository contains Python scripts to automate the generation of certificates for new members of the Nexus Club and send them via email. It also includes functionality to send department-specific WhatsApp group invitations.

---

## File Structure

```
repo/
│
├── GeneratedCertificates/        # Folder where generated certificate images are saved
│   ├── 24BAI1096.png
│   ├── 24BCE1145.png
│   └── ...
│
├── fonts/                        # Fonts used for certificate generation
│   ├── StoryScript-Regular.ttf
│   └── Merriweather-Regular.ttf
│
├── CertGenerator.py              # Script to generate certificates from CSV data
├── cert_template.png             # Certificate template image
├── certificate_data.csv          # CSV file containing member information for certificate generation
├── send-email.py                 # Script to send certificates via email
└── send-email WhatsApp-Links.py  # Script to send WhatsApp group links for each department
```

> **Note:** All code files are hidden for security. You will need to feed your specific data (emails, registration numbers, department names, etc.) to make the scripts functional.

---

## Prerequisites

Make sure you have Python 3 installed along with the required libraries.

Install dependencies using pip:

```bash
pip install pandas pillow
```

> `pandas` is used for reading CSV files.
>
> `pillow` (PIL) is used for image manipulation and drawing text on certificates.

---

## Usage

### 1. Generate Certificates

Make sure `certificate_data.csv` contains the following columns:
`Name, Registration, Position`

Run the script:

```bash
python3 CertGenerator.py
```

Certificates will be generated and saved in the `GeneratedCertificates/` folder.

### 2. Send Certificates via Email

Update the `send-email.py` script with your email credentials (sender email and Gmail App Password).

Ensure `certificate_data.csv` contains the following columns:
`Name, Registration, Email, Department`

Run the script:

```bash
python3 send-email.py
```

Emails with personalized certificates will be sent to each recipient.

### 3. Send WhatsApp Group Links

Update `send-email WhatsApp-Links.py` if necessary with department-specific group links.

Ensure `recruitment.csv` contains the following columns:
`Name, Registration, Email, Position`

Run the script:

```bash
python3 send-email\ WhatsApp-Links.py
```

Each member will receive a personalized email with their department group link.

---

## Notes

* Make sure fonts used in `CertGenerator.py` exist in the `fonts/` folder.
* Department names in CSV must exactly match the keys in the scripts (`Frontend`, `Backend`, `AiMl`, `Design`, `Social Media`, `Management`).
* Always use Gmail App Password for sending emails securely.
* The scripts do **not** handle errors for invalid email addresses or missing files; ensure all required files and data are present.

---

## Author

Aditya
VIT Chennai
