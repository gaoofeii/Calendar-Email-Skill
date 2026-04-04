# Calendar Email Skill

**Repository:** https://github.com/gaoofeii/Calendar-Email-Skill  
**Main Skill File:** `calendar-email-skill/calendar_email_skill.py`  
**Full Documentation:** https://github.com/gaoofeii/Calendar-Email-Skill/tree/main/calendar-email-skill

## 🎯 Overview
A LiteRT-LM agent skill for scheduling calendar events and sending email invitations.

## 🔧 Available Tools

### 1. `create_event(title, date, time, duration)`
Schedule a calendar event.

**Parameters:**
- `title`: Event title (string)
- `date`: YYYY-MM-DD format
- `time`: HH:MM format (24-hour)
- `duration`: Hours (float)

**Example:**
```python
create_event("Team Meeting", "2024-12-25", "14:00", 2.0)
