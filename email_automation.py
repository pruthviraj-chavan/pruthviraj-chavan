import smtplib
import time
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
 
# Email credentialss
sender_email = "your mail id"
app_password = "add your app password from gmail"  # Use App Password, not normal password
 
# List of recipient emails
email_list = [
"deepali@vedak.com ", "girija.m@vedak.com ", "jaya@vedak.com ", "ankit@vedak.com ", "ranjita.g@vedak.com ", "abhidnya@vedak.com ", "subhasmita.parida@vedak.com ", 
 
#add more mails daily 500
 
]
 
 
# Path to the resume PDF file
resume_file_path = r"C:\pruthviraj_files\lkndn\python_developer.pdf"
 
# Function to extract name from email
def extract_name(email):
    # Split email into local part (before @) and domain part (after @)
    local_part = email.split('@')[0]
    domain_part = email.split('@')[1]
   
    # Check the length of the local part and return a tuple (name, is_domain)
    if len(local_part) <= 3:
        # Use the domain part before the first dot and remove digits
        domain_name = ''.join(filter(lambda x: not x.isdigit(), domain_part.split('.')[0])).capitalize()
        return domain_name, True
   
    # If local part length is greater than 3, proceed with existing logic
    if '.' in local_part:
        name_parts = local_part.split('.')
        if len(name_parts[0]) < 3:
            # Use the last part as the name if first name is less than 3 characters and remove digits
            first_name = ''.join(filter(lambda x: not x.isdigit(), name_parts[-1])).capitalize()
        else:
            # Use the first part as the name and remove digits
            first_name = ''.join(filter(lambda x: not x.isdigit(), name_parts[0])).capitalize()
    else:
        # Use the entire local part if no dot is present and remove digits
        first_name = ''.join(filter(lambda x: not x.isdigit(), local_part)).capitalize()
   
    return first_name, False
 
# Email content template
body_template = """{greeting},
 
I am writing to apply for the Software/Python Developer role. I have hands-on experience in Python, Django, SQL, ML, HTML, CSS, React.js, and databases like MySQL and MongoDB. I’ve built real-time web apps and AI-based projects during my internships and academic journey. Please find my resume attached for your kind consideration.
Thank you for your time.
 
Best regards,
Pruthviraj Chavan
📞 Phone : +91 9404895667
📧 Email : pruthvirajchavan2002@gmail.com
🌐 LinkedIn : linkedin.com/in/pruthviraj-chavan
💾 GitHub : github.com/pruthviraj-chavan
 
 
 
"""
 
# Check if resume file exists
if not os.path.exists(resume_file_path):
    print(f"Error: Resume file '{resume_file_path}' not found.")
    exit(1)
 
# Connect to Gmail SMTP
try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, app_password)
 
    # Initialize counter
    a = 1
 
    # Send emails
    for receiver in email_list:
        # Extract name and check if it's a domain name
        name, is_domain = extract_name(receiver)
       
        # Set the greeting based on whether a domain name was used
        if is_domain:
            greeting = "Hello"
        else:
            greeting = f"Hi {name}"
       
        # Format the body with the appropriate greeting
        body = body_template.format(greeting=greeting)
       
        # Create email message
        msg = MIMEMultipart()
        msg["From"] = sender_email
        msg["To"] = receiver
        msg["Subject"] = "Application For Software Developer Role"
        msg.attach(MIMEText(body, "plain"))
 
        # Attach resume PDF
        with open(resume_file_path, "rb") as f:
            pdf_attachment = MIMEApplication(f.read(), _subtype="pdf")
            pdf_attachment.add_header(
                "Content-Disposition",
                "attachment",
                filename=os.path.basename(resume_file_path)
            )
            msg.attach(pdf_attachment)
 
        # Send email
        text = msg.as_string()
        server.sendmail(sender_email, receiver, text)
        print(f"Email sent to {receiver} with resume attached, Attempt: {a}")
        a += 1
       
        time.sleep(5)  # Wait 5 seconds between emails to avoid rate limits
 
except Exception as e:
    print(f"An error occurred: {e}")
 
finally:
    # Close the server connection
    server.quit()
 
mail automation script
 
