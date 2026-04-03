# Calendar Email Sharing Skill for LiteRT-LM

## 📅 Overview

A LiteRT-LM agent skill for creating calendar events and sharing them via email. This skill enables Gemma 4 E2B (or other LiteRT-LM models) to schedule meetings, check availability, and send email invitations.

## 🚀 Quick Start

```bash
# Install LiteRT-LM CLI first (if not already installed)
uv tool install litert-lm

# Run with Gemma 4 E2B
export PATH="$HOME/.local/bin:$PATH"

litert-lm run gemma-4-E2B-it.litertlm \
  --preset=calendar_email_skill.py \
  --prompt="Schedule team meeting on 2024-12-25 at 14:00 for 2 hours"
```

## 📁 Skill Structure

```
calendar-email-skill/
├── calendar_email_skill.py    # Main skill file
├── README.md                  # This file
├── examples/                  # Usage examples
│   ├── schedule_event.txt
│   ├── send_invite.txt
│   └── check_availability.txt
├── tests/                     # Test scripts
│   └── test_skill.sh
└── config/                    # Configuration templates
    └── smtp_config_template.py
```

## 🔧 Available Tools

### 1. **create_event(title, date, time, duration)**
Schedule a calendar event.

**Parameters:**
- `title`: Event title (string)
- `date`: Date in YYYY-MM-DD format
- `time`: Start time in HH:MM format (24-hour)
- `duration`: Duration in hours (float)

**Example:**
```python
create_event("Team Meeting", "2024-12-25", "14:00", 2.0)
```

### 2. **send_invite(event_title, event_date, to_email)**
Send calendar invitation via email.

**Parameters:**
- `event_title`: Title of the event
- `event_date`: Date of the event
- `to_email`: Recipient email address

**Example:**
```python
send_invite("Team Meeting", "2024-12-25", "john@example.com")
```

### 3. **check_availability(date)**
Check available time slots on a date.

**Parameters:**
- `date`: Date to check (YYYY-MM-DD)

**Example:**
```python
check_availability("2024-12-25")
```

## 📧 Email Integration

### Current State: Simulation
The skill currently **simulates** email sending. Email templates are generated but not actually sent.

### For Production Use:
1. **Configure SMTP** in `send_invite()` function
2. **Add authentication** (username/password or OAuth)
3. **Test** with your email service

### SMTP Configuration Template:
```python
# Add to send_invite() function
smtp_config = {
    "server": "smtp.gmail.com",
    "port": 587,
    "username": "your_email@gmail.com",
    "password": "your_app_password",  # Use app password
    "use_tls": True
}
```

## 🧪 Examples

### Example 1: Schedule Event
```bash
litert-lm run gemma-4-E2B-it.litertlm \
  --preset=calendar_email_skill.py \
  --prompt="Schedule project review on 2024-06-15 at 09:30 for 1.5 hours"
```

### Example 2: Send Invitation
```bash
litert-lm run gemma-4-E2B-it.litertlm \
  --preset=calendar_email_skill.py \
  --prompt="Send invitation for board meeting on 2024-06-20 to board@company.com"
```

### Example 3: Check Availability
```bash
litert-lm run gemma-4-E2B-it.litertlm \
  --preset=calendar_email_skill.py \
  --prompt="What times are available on 2024-12-25?"
```

## 🛠️ Installation

### Method 1: Direct Use
```bash
# Clone or download the skill
git clone <skill-url>
cd calendar-email-skill

# Use with LiteRT-LM
litert-lm run gemma-4-E2B-it.litertlm \
  --preset=./calendar_email_skill.py \
  --prompt="Your prompt here"
```

### Method 2: Integration
Copy `calendar_email_skill.py` to your project and import tools as needed.

## 🔍 Testing

Run the test suite:
```bash
chmod +x tests/test_skill.sh
./tests/test_skill.sh
```

Or test manually:
```bash
# Test all functions
python3 -c "
import calendar_email_skill
print('Available tools:', [t.__name__ for t in calendar_email_skill.TOOLS])
print('System instructions:', calendar_email_skill.SYSTEM_INSTRUCTIONS[:200] + '...')
"
```

## 📋 Requirements

- **LiteRT-LM CLI** (version 0.10.1 or higher)
- **Gemma 4 E2B** or other LiteRT-LM compatible model
- **Python 3.8+** (for skill development)
- **SMTP access** (for production email sending)

## 🎯 Use Cases

1. **Team Scheduling**: Coordinate meetings across teams
2. **Event Planning**: Schedule and invite to events
3. **Appointment Booking**: Manage client appointments
4. **Project Management**: Schedule project milestones
5. **Personal Calendar**: Manage personal schedule

## 🔄 Workflow Examples

### Complete Workflow:
```bash
# 1. Check availability
litert-lm run gemma-4-E2B-it.litertlm \
  --preset=calendar_email_skill.py \
  --prompt="Check availability on 2024-12-25"

# 2. Schedule event
litert-lm run gemma-4-E2B-it.litertlm \
  --preset=calendar_email_skill.py \
  --prompt="Schedule Christmas party on 2024-12-25 at 18:00 for 3 hours"

# 3. Send invitations
litert-lm run gemma-4-E2B-it.litertlm \
  --preset=calendar_email_skill.py \
  --prompt="Send invitation for Christmas party on 2024-12-25 to team@company.com"
```

## ⚙️ Configuration

### Date/Time Formats:
- **Dates**: `YYYY-MM-DD` (e.g., `2024-12-25`)
- **Times**: `HH:MM` (e.g., `14:00` for 2 PM)
- **Duration**: Decimal hours (e.g., `1.5` for 1 hour 30 minutes)

### Email Templates:
Templates can be customized in the `send_invite()` function:
- Formal business style
- Casual team style
- Brief notification style

## 🐛 Troubleshooting

### Common Issues:

1. **"Invalid date/time format"**
   - Ensure dates are `YYYY-MM-DD`
   - Ensure times are `HH:MM` (24-hour)

2. **Tool not being called**
   - Check SYSTEM_INSTRUCTIONS clarity
   - Ensure prompt includes required parameters

3. **Email not sending**
   - Skill simulates by default
   - Configure SMTP for real sending

### Debug Mode:
```python
# Add to skill file for debugging
DEBUG = True

if DEBUG:
    print(f"Tool called: {tool_name}")
    print(f"Parameters: {params}")
```

## 📚 API Reference

### Skill Interface:
```python
# Required exports
TOOLS = [create_event, send_invite, check_availability]
SYSTEM_INSTRUCTIONS = "Your instructions here"
__all__ = ["TOOLS", "SYSTEM_INSTRUCTIONS"]
```

### Tool Signature:
```python
def tool_name(param1: type, param2: type) -> Dict[str, Any]:
    """Tool description.
    
    Args:
        param1: Description
        param2: Description
    
    Returns:
        Dictionary with results
    """
```

## 🔗 Integration

### With Other Skills:
```python
# Combine with other skills
from calendar_email_skill import TOOLS as calendar_tools
from weather_skill import TOOLS as weather_tools

TOOLS = calendar_tools + weather_tools
```

### With Web APIs:
```python
# Add real calendar API integration
import google_calendar_api  # Example

def create_google_calendar_event(title, date, time):
    # Integrate with Google Calendar API
    pass
```

## 📈 Roadmap

### Planned Features:
1. **Real email sending** with SMTP
2. **Calendar API integration** (Google, Outlook)
3. **Recurring events** support
4. **Timezone handling**
5. **RSVP tracking**
6. **Attachment support** (ICS files)
7. **Bulk invitations**
8. **Template customization**

### Current Version: v1.0.0
- Basic event scheduling
- Email template generation
- Availability checking
- LiteRT-LM integration

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make changes
4. Test thoroughly
5. Submit pull request

### Development Setup:
```bash
# Clone repository
git clone <skill-url>
cd calendar-email-skill

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies (if any)
pip install -r requirements.txt

# Run tests
./tests/test_skill.sh
```

## 📄 License

MIT License - see LICENSE file for details.

## 🙏 Acknowledgments

- **Google AI Edge** for LiteRT-LM
- **Gemma team** for the model
- **Community contributors**

## 📞 Support

- **Issues**: GitHub Issues
- **Questions**: Discussions
- **Contributions**: Pull Requests

---

**Skill URL**: `https://github.com/your-username/calendar-email-skill`  
**Version**: 1.0.0  
**Last Updated**: 2026-04-03  
**Compatibility**: LiteRT-LM 0.10.1+, Gemma 4 E2B