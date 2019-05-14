import getQuote
# Enable emailing
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Read mailing list
def read_mailing_list():
    searching = True
    numUsers = 0
    EMAIL_MAILING_LIST = []

    f = open("emails.txt", 'r')
    lines = f.read().splitlines()

    # Add users to mailing list
    while searching:
        try:
            if lines[0 + numUsers] == "":
                searching = False
            else:
                EMAIL_MAILING_LIST.append(lines[0 + numUsers])
                numUsers += 1
        # If there are no more lines in the mailing list file
        # Then there are no more user to mail to
        except IndexError:
            searching = False

    f.close()

    return EMAIL_MAILING_LIST

# Send quote as email
def email_quote(message, mailing_list):

    # Read email credentials from external file
    f = open("EmailCredentials.txt","r")
    lines = f.read().splitlines()
    print(lines)
    EMAIL_USERNAME = lines[0]
    EMAIL_PASSWORD = lines[1]
    f.close()

    userIndex = 0

    while userIndex < len(mailing_list):

        # Email results to self
        fromaddr = EMAIL_USERNAME
        toaddr = mailing_list[userIndex]

        # Create message container
        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Subject'] = "Daily Philosophy Nugget"

        # Allow Unicode characters to be emailed
        plainText = MIMEText(message, 'plain', 'UTF-8')
        # html = MIMEText(html, 'html')

        msg.attach(plainText)

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(fromaddr, EMAIL_PASSWORD)
        server.sendmail(fromaddr, toaddr, msg.as_string())
        server.quit()

        print("Sent email to", toaddr)
        userIndex += 1

# Main
def send_quote(quote):
    mailing_list = read_mailing_list()
    email_quote(quote, mailing_list)
