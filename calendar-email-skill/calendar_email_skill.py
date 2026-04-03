"""
Calendar Email Sharing Skill for LiteRT-LM
Version: 1.0.0

A skill that enables LiteRT-LM models to:
1. Create calendar events with dates, times, and durations
2. Send email invitations for scheduled events
3. Check availability on specific dates

Usage with LiteRT-LM:
  litert-lm run gemma-4-E2B-it.litertlm \
    --preset=calendar_email_skill.py \
    --prompt="Schedule meeting on 2024-12-25 at 14:00"
"""

import datetime
from typing import Dict, Any, List


def clean_param(param: str) -> str:
    """Clean parameter from LiteRT-LM formatting.
    
    LiteRT-LM sends parameters like: "<|\"|>value<|\"|>"
    This function extracts the actual value.
    """
    if isinstance(param, str):
        # Remove the wrapping
        if param.startswith('<|"|>') and param.endswith('<|"|>'):
            return param[5:-5]
    return param


def create_event(
    title: str,
    date: str,
    time: str = "14:00",
    duration: float = 1.0
) -> Dict[str, Any]:
    """Create a calendar event.
    
    Args:
        title: Event title (e.g., "Team Meeting")
        date: Event date in YYYY-MM-DD format (e.g., "2024-12-25")
        time: Start time in HH:MM format (24-hour, e.g., "14:00" for 2 PM)
        duration: Duration in hours (e.g., 2.0 for 2 hours)
    
    Returns:
        Dictionary with event details and status
    
    Example:
        create_event("Team Sync", "2024-12-25", "14:00", 1.5)
    """
    # Clean parameters from LiteRT-LM formatting
    title = clean_param(title)
    date = clean_param(date)
    time = clean_param(time)
    
    try:
        # Parse date and time
        start_datetime = datetime.datetime.strptime(f"{date} {time}", "%Y-%m-%d %H:%M")
        end_datetime = start_datetime + datetime.timedelta(hours=duration)
        
        event_details = {
            "title": title,
            "date": date,
            "day_of_week": start_datetime.strftime("%A"),
            "start_time": time,
            "end_time": end_datetime.strftime("%H:%M"),
            "duration_hours": duration,
            "status": "scheduled"
        }
        
        return {
            "success": True,
            "message": f"✅ Event '{title}' scheduled for {date} at {time} ({duration} hours)",
            "event": event_details,
            "next_steps": [
                "Event is ready to be shared",
                "Use send_invite() to email invitations",
                "Event can be added to calendar apps"
            ]
        }
        
    except ValueError as e:
        return {
            "success": False,
            "error": f"Invalid format: {str(e)}",
            "required_format": "Date: YYYY-MM-DD, Time: HH:MM (24-hour)",
            "examples": [
                "Date: 2024-12-25",
                "Time: 14:00 (for 2 PM)",
                "Time: 09:30 (for 9:30 AM)"
            ]
        }


def send_invite(
    event_title: str,
    event_date: str,
    to_email: str
) -> Dict[str, Any]:
    """Send calendar invitation via email.
    
    Args:
        event_title: Title of the event (e.g., "Team Meeting")
        event_date: Date of the event in YYYY-MM-DD format
        to_email: Recipient email address
    
    Returns:
        Dictionary with email details and status
    
    Example:
        send_invite("Team Sync", "2024-12-25", "john@example.com")
    """
    # Clean parameters
    event_title = clean_param(event_title)
    event_date = clean_param(event_date)
    to_email = clean_param(to_email)
    
    # Generate professional email template
    email_content = f"""Subject: Calendar Invitation: {event_title}

Dear Colleague,

You are invited to: {event_title}

📅 Date: {event_date}
⏰ Time: To be confirmed (please check calendar invite)
📍 Location: Virtual Meeting

Please save the date and add this to your calendar.

Best regards,
Calendar Assistant
"""
    
    email_details = {
        "to": to_email,
        "subject": f"Calendar Invitation: {event_title}",
        "body": email_content.strip(),
        "event_title": event_title,
        "event_date": event_date,
        "status": "ready_to_send"
    }
    
    return {
        "success": True,
        "message": f"📧 Invitation for '{event_title}' prepared for {to_email}",
        "email": email_details,
        "notes": [
            "Email is ready to send",
            "Configure SMTP settings for actual sending",
            "Template can be customized as needed"
        ]
    }


def check_availability(date: str) -> Dict[str, Any]:
    """Check available time slots on a specific date.
    
    Args:
        date: Date to check in YYYY-MM-DD format
    
    Returns:
        Dictionary with availability information
    
    Example:
        check_availability("2024-12-25")
    """
    date = clean_param(date)
    
    try:
        # Parse the date
        check_date = datetime.datetime.strptime(date, "%Y-%m-%d")
        today = datetime.datetime.now()
        
        days_difference = (check_date - today).days
        
        # Generate suggested time slots
        morning_slots = ["09:00-10:00", "10:30-11:30"]
        afternoon_slots = ["14:00-15:00", "15:30-16:30"]
        evening_slots = ["17:00-18:00"]
        
        all_slots = morning_slots + afternoon_slots + evening_slots
        
        availability_info = {
            "date": date,
            "day_of_week": check_date.strftime("%A"),
            "is_weekend": check_date.strftime("%A") in ["Saturday", "Sunday"],
            "days_from_today": days_difference,
            "is_past": days_difference < 0,
            "is_today": days_difference == 0,
            "is_future": days_difference > 0,
            "available_slots": all_slots,
            "morning_slots": morning_slots,
            "afternoon_slots": afternoon_slots,
            "evening_slots": evening_slots,
            "recommended_slots": morning_slots if len(morning_slots) > 0 else afternoon_slots
        }
        
        # Add recommendations
        if availability_info["is_weekend"]:
            availability_info["recommendation"] = "Weekend date - consider Monday instead"
        elif availability_info["is_past"]:
            availability_info["recommendation"] = "Date is in the past"
        elif days_difference < 7:
            availability_info["recommendation"] = "Short notice - confirm availability"
        else:
            availability_info["recommendation"] = "Good availability - morning slots recommended"
        
        return {
            "success": True,
            "message": f"📅 Availability for {date} ({availability_info['day_of_week']})",
            "availability": availability_info
        }
        
    except ValueError:
        return {
            "success": False,
            "error": "Invalid date format",
            "required_format": "YYYY-MM-DD",
            "examples": ["2024-12-25", "2024-06-15", "2024-01-01"]
        }


# ==================== SKILL CONFIGURATION ====================

SYSTEM_INSTRUCTIONS = """
You are a Calendar Email Assistant. Your purpose is to help users schedule events and share them via email.

AVAILABLE TOOLS:

1. CREATE_EVENT(title, date, time, duration)
   - Schedule a calendar event
   - Parameters:
     * title: Event title (e.g., "Team Meeting")
     * date: YYYY-MM-DD format (e.g., "2024-12-25")
     * time: HH:MM format (24-hour, e.g., "14:00" for 2 PM)
     * duration: Hours (e.g., 1.5 for 1 hour 30 minutes)

2. SEND_INVITE(event_title, event_date, to_email)
   - Send calendar invitation via email
   - Parameters:
     * event_title: Title of the event
     * event_date: Date of the event
     * to_email: Recipient email address

3. CHECK_AVAILABILITY(date)
   - Check available time slots on a date
   - Parameters:
     * date: YYYY-MM-DD format

HOW TO USE THESE TOOLS:

When user requests to:
- "Schedule a meeting on [date] at [time]" → Use CREATE_EVENT
- "Send invitation for [event] to [email]" → Use SEND_INVITE  
- "Check availability on [date]" → Use CHECK_AVAILABILITY
- "What times are free on [date]?" → Use CHECK_AVAILABILITY

FORMAT REQUIREMENTS:
- Dates must be YYYY-MM-DD (e.g., 2024-12-25)
- Times must be HH:MM (24-hour, e.g., 14:00 for 2 PM)
- Duration is in hours (e.g., 2.0 for 2 hours)

EXAMPLES:
- User: "Schedule team meeting on 2024-12-25 at 14:00 for 2 hours"
  → create_event("Team Meeting", "2024-12-25", "14:00", 2.0)

- User: "Invite john@example.com to meeting on 2024-12-25"
  → send_invite("Meeting", "2024-12-25", "john@example.com")

- User: "What's available on 2024-12-25?"
  → check_availability("2024-12-25")

ALWAYS:
1. Use the exact parameters provided by the user
2. Confirm the event details before creating
3. Present results clearly and helpfully
4. Suggest next steps (e.g., sending invitations)

EMAIL NOTES:
- Email sending is simulated by default
- For real emails, SMTP configuration is needed
- Email templates can be customized
"""

TOOLS = [
    create_event,
    send_invite,
    check_availability,
]

__all__ = ["TOOLS", "SYSTEM_INSTRUCTIONS", "clean_param"]