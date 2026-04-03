"""
SMTP Configuration Template for Calendar Email Skill

Copy this configuration to calendar_email_skill.py and fill in your details
to enable real email sending.
"""

# SMTP Configuration
SMTP_CONFIG = {
    # Gmail Example
    "gmail": {
        "server": "smtp.gmail.com",
        "port": 587,
        "username": "your_email@gmail.com",
        "password": "your_app_password",  # Use app password, not regular password
        "use_tls": True,
        "sender_name": "Calendar Assistant"
    },
    
    # Outlook Example
    "outlook": {
        "server": "smtp.office365.com",
        "port": 587,
        "username": "your_email@outlook.com",
        "password": "your_password",
        "use_tls": True,
        "sender_name": "Calendar Assistant"
    },
    
    # Custom SMTP Server
    "custom": {
        "server": "smtp.yourdomain.com",
        "port": 587,
        "username": "your_username",
        "password": "your_password",
        "use_tls": True,
        "sender_name": "Calendar Assistant"
    }
}

# Email Templates
EMAIL_TEMPLATES = {
    "formal": """
Subject: Calendar Invitation: {event_title}

Dear {recipient_name},

You are cordially invited to: {event_title}

📅 Date: {event_date}
⏰ Time: {event_time}
📍 Location: {event_location}

{event_description}

Please RSVP at your earliest convenience.

Sincerely,
{organizer_name}
""",
    
    "casual": """
Subject: Invitation: {event_title}

Hi {recipient_name}!

You're invited to: {event_title}

📅 When: {event_date} at {event_time}
📍 Where: {event_location}

{event_description}

Let me know if you can make it!

Cheers,
{organizer_name}
""",
    
    "brief": """
Subject: {event_title}

{event_title}
Date: {event_date}
Time: {event_time}
Location: {event_location}

{event_description}

- {organizer_name}
"""
}

# How to integrate with calendar_email_skill.py:

"""
1. Copy the SMTP configuration above into calendar_email_skill.py
2. Update the send_invite() function to use real SMTP:

def send_invite_with_smtp(event_title, event_date, to_email):
    import smtplib
    from email.mime.text import MIMEText
    
    # Use configuration
    config = SMTP_CONFIG["gmail"]  # or "outlook" or "custom"
    
    # Create email
    msg = MIMEText(EMAIL_TEMPLATES["formal"].format(
        event_title=event_title,
        event_date=event_date,
        event_time="To be confirmed",
        event_location="Virtual Meeting",
        event_description="Please save the date.",
        recipient_name="Colleague",
        organizer_name="Calendar Assistant"
    ))
    
    msg['Subject'] = f"Calendar Invitation: {event_title}"
    msg['From'] = f"{config['sender_name']} <{config['username']}>"
    msg['To'] = to_email
    
    # Send email
    try:
        with smtplib.SMTP(config['server'], config['port']) as server:
            if config['use_tls']:
                server.starttls()
            server.login(config['username'], config['password'])
            server.send_message(msg)
        
        return {"success": True, "message": f"Email sent to {to_email}"}
    except Exception as e:
        return {"success": False, "error": str(e)}

3. Replace the simulated send_invite() with the real version
4. Test with a real email address
"""

# Security Notes:
"""
IMPORTANT SECURITY:
1. Never commit real credentials to version control
2. Use environment variables for sensitive data:
   import os
   username = os.getenv("SMTP_USERNAME")
   password = os.getenv("SMTP_PASSWORD")
3. Use app passwords for Gmail (not regular passwords)
4. Consider OAuth2 for better security
5. Test with a dedicated test email account first
"""

# Environment Variables Example:
"""
# .env file (add to .gitignore)
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
SMTP_USERNAME=your_email@gmail.com
SMTP_PASSWORD=your_app_password
SMTP_SENDER_NAME=Calendar Assistant

# In Python:
import os
from dotenv import load_dotenv

load_dotenv()  # Load from .env file

config = {
    "server": os.getenv("SMTP_SERVER"),
    "port": int(os.getenv("SMTP_PORT")),
    "username": os.getenv("SMTP_USERNAME"),
    "password": os.getenv("SMTP_PASSWORD"),
    "sender_name": os.getenv("SMTP_SENDER_NAME")
}
"""