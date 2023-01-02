import smtplib, ssl

def send_email():
    
    smtp_server = "SMTP SERVER"
    port = 587  # For starttls
    sender_email = "USER"
    password = 'PASSWORD'
    receiver_email = "E-MAIL THAT WILL RECEIVE THE EMAIL"
    message = """\
    Subject: Payslip is ON

    This message is sent from Python:

    The new payslip is ON.

    GOOD LUCK"""

# Create a secure SSL context
    context = ssl.create_default_context()

# Try to log in to server and send email
    try:
        server = smtplib.SMTP(smtp_server,port)
        server.ehlo() # Can be omitted
        server.starttls(context=context) # Secure the connection
        server.ehlo() # Can be omitted
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
    # TODO: Send email here
    except Exception as e:
        # Print any error messages to stdout
        print(e)
    finally:
        server.quit()

