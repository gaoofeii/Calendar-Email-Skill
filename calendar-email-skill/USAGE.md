# Calendar Email Skill - Usage Guide

## 🚀 Quick Start

### 1. Install Requirements
```bash
# Install LiteRT-LM CLI
uv tool install litert-lm

# Ensure Gemma 4 E2B is installed
litert-lm list  # Should show gemma-4-E2B-it.litertlm
```

### 2. Use the Skill
```bash
export PATH="$HOME/.local/bin:$PATH"

# Basic usage
litert-lm run gemma-4-E2B-it.litertlm \
  --preset=calendar_email_skill.py \
  --prompt="Your calendar request here"
```

## 📋 Common Commands

### Schedule Events
```bash
# Schedule a meeting
litert-lm run gemma-4-E2B-it.litertlm \
  --preset=calendar_email_skill.py \
  --prompt="Schedule team meeting on 2024-12-25 at 14:00 for 2 hours"

# Schedule with specific title
litert-lm run gemma-4-E2B-it.litertlm \
  --preset=calendar_email_skill.py \
  --prompt="Schedule 'Project Review' on 2024-06-15 at 09:30 for 1.5 hours"
```

### Send Invitations
```bash
# Send single invitation
litert-lm run gemma-4-E2B-it.litertlm \
  --preset=calendar_email_skill.py \
  --prompt="Send invitation for team meeting on 2024-12-25 to john@example.com"

# Send to multiple (one at a time)
litert-lm run gemma-4-E2B-it.litertlm \
  --preset=calendar_email_skill.py \
  --prompt="Send invitation for board meeting to alice@company.com"
```

### Check Availability
```bash
# Check specific date
litert-lm run gemma-4-E2B-it.litertlm \
  --preset=calendar_email_skill.py \
  --prompt="Check availability on 2024-12-25"

# Check with context
litert-lm run gemma-4-E2B-it.litertlm \
  --preset=calendar_email_skill.py \
  --prompt="What morning slots are available on 2024-12-25?"
```

## 🔄 Complete Workflows

### Workflow 1: Schedule & Invite
```bash
# Step 1: Schedule event
litert-lm run gemma-4-E2B-it.litertlm \
  --preset=calendar_email_skill.py \
  --prompt="Schedule weekly team sync on 2024-01-08 at 10:00 for 1 hour"

# Step 2: Send invitations
litert-lm run gemma-4-E2B-it.litertlm \
  --preset=calendar_email_skill.py \
  --prompt="Send invitation for weekly team sync on 2024-01-08 to team@company.com"
```

### Workflow 2: Check & Schedule
```bash
# Step 1: Check availability
litert-lm run gemma-4-E2B-it.litertlm \
  --preset=calendar_email_skill.py \
  --prompt="Check availability on 2024-12-25"

# Step 2: Schedule based on availability
litert-lm run gemma-4-E2B-it.litertlm \
  --preset=calendar_email_skill.py \
  --prompt="Schedule Christmas party on 2024-12-25 at 18:00 for 3 hours"
```

## ⚙️ Configuration

### Date/Time Formats
- **Date**: `YYYY-MM-DD` (e.g., `2024-12-25`)
- **Time**: `HH:MM` (24-hour, e.g., `14:00` for 2 PM)
- **Duration**: Decimal hours (e.g., `1.5` for 1 hour 30 minutes)

### Email Setup (Optional)
For real email sending:
1. Copy `config/smtp_config_template.py` settings
2. Update `calendar_email_skill.py` with your SMTP details
3. Test with a real email address

## 🐛 Troubleshooting

### Common Issues

**Issue**: "Invalid date/time format"
```bash
# Wrong format
litert-lm run ... --prompt="Schedule meeting on Dec 25 2024"

# Correct format
litert-lm run ... --prompt="Schedule meeting on 2024-12-25"
```

**Issue**: Tool not being called
```bash
# Vague prompt (may not trigger tool)
litert-lm run ... --prompt="Meeting on Friday"

# Specific prompt (will trigger tool)
litert-lm run ... --prompt="Schedule meeting on 2024-12-25 at 14:00"
```

**Issue**: Email not sending
- By default, email is simulated
- Configure SMTP for real sending
- Check `config/smtp_config_template.py`

### Debug Mode
Add to `calendar_email_skill.py`:
```python
DEBUG = True

if DEBUG:
    print(f"Tool: {tool_name}")
    print(f"Params: {params}")
```

## 📚 Advanced Usage

### Combine with Other Skills
```python
# Create combined skill
from calendar_email_skill import TOOLS as calendar_tools
from weather_skill import TOOLS as weather_tools

TOOLS = calendar_tools + weather_tools
SYSTEM_INSTRUCTIONS = "You are a multi-functional assistant..."
```

### Custom Email Templates
Modify the `send_invite()` function in `calendar_email_skill.py`:
```python
# Add custom templates
TEMPLATES = {
    "business": "...",
    "casual": "...",
    "reminder": "..."
}
```

### Integration with APIs
```python
# Add Google Calendar integration
import google_calendar_api

def create_google_event(title, date, time):
    # Integrate with Google Calendar API
    pass
```

## 🧪 Testing

### Run Test Suite
```bash
cd calendar-email-skill
chmod +x tests/test_skill.sh
./tests/test_skill.sh
```

### Manual Testing
```bash
# Test each function
litert-lm run gemma-4-E2B-it.litertlm \
  --preset=calendar_email_skill.py \
  --prompt="Test: create_event"

litert-lm run gemma-4-E2B-it.litertlm \
  --preset=calendar_email_skill.py \
  --prompt="Test: send_invite"

litert-lm run gemma-4-E2B-it.litertlm \
  --preset=calendar_email_skill.py \
  --prompt="Test: check_availability"
```

## 🔗 Integration Examples

### With Scripts
```bash
#!/bin/bash
# schedule_meeting.sh

EVENT_TITLE="Team Meeting"
EVENT_DATE="2024-12-25"
EVENT_TIME="14:00"
DURATION="2.0"
EMAIL="team@company.com"

litert-lm run gemma-4-E2B-it.litertlm \
  --preset=calendar_email_skill.py \
  --prompt="Schedule $EVENT_TITLE on $EVENT_DATE at $EVENT_TIME for $DURATION hours"

litert-lm run gemma-4-E2B-it.litertlm \
  --preset=calendar_email_skill.py \
  --prompt="Send invitation for $EVENT_TITLE on $EVENT_DATE to $EMAIL"
```

### With Python
```python
import subprocess

def schedule_meeting(title, date, time, duration, email):
    cmd = [
        "litert-lm", "run", "gemma-4-E2B-it.litertlm",
        "--preset", "calendar_email_skill.py",
        "--prompt", f"Schedule {title} on {date} at {time} for {duration} hours"
    ]
    subprocess.run(cmd, check=True)
```

## 📞 Support

- **Issues**: Check `examples/` folder
- **Debugging**: Enable debug mode in skill file
- **Customization**: Modify `calendar_email_skill.py`
- **Integration**: See `config/smtp_config_template.py`

## 🎯 Best Practices

1. **Be Specific**: Use exact date/time formats
2. **Test First**: Try examples before custom prompts
3. **Check Output**: Verify tools are being called
4. **Configure SMTP**: For production email sending
5. **Backup**: Keep original skill file before modifying

---

**Ready to use!** Start with the examples and customize as needed.