# Calendar Email Skill

## 🎯 Quick Overview

**Skill Name:** Calendar Email Sharing  
**Version:** 1.0.0  
**Type:** LiteRT-LM Agent Skill  
**Main File:** `calendar_email_skill.py`  
**GitHub:** https://github.com/gaoofeii/Calendar-Email-Skill

## 🔧 Tools Available

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
```

### 2. `send_invite(event_title, event_date, to_email)`
Send calendar invitation via email.

**Parameters:**
- `event_title`: Title of the event
- `event_date`: Date of the event
- `to_email`: Recipient email address

**Example:**
```python
send_invite("Team Meeting", "2024-12-25", "john@example.com")
```

### 3. `check_availability(date)`
Check available time slots on a date.

**Parameters:**
- `date`: Date to check (YYYY-MM-DD)

**Example:**
```python
check_availability("2024-12-25")
```

## 🚀 Quick Start

```bash
# Download skill
git clone https://github.com/gaoofeii/Calendar-Email-Skill.git
cd Calendar-Email-Skill

# Use with LiteRT-LM
litert-lm run gemma-4-E2B-it.litertlm \
  --preset=calendar_email_skill.py \
  --prompt="Schedule team meeting on 2024-12-25 at 14:00"
```

## 📋 Examples

### Schedule Event:
```bash
litert-lm run gemma-4-E2B-it.litertlm \
  --preset=calendar_email_skill.py \
  --prompt="Schedule project review on 2024-06-15 at 09:30 for 1.5 hours"
```

### Send Invitation:
```bash
litert-lm run gemma-4-E2B-it.litertlm \
  --preset=calendar_email_skill.py \
  --prompt="Send invitation for board meeting to alice@company.com"
```

### Check Availability:
```bash
litert-lm run gemma-4-E2B-it.litertlm \
  --preset=calendar_email_skill.py \
  --prompt="What times are available on 2024-12-25?"
```

## 📁 File Structure

```
calendar-email-skill/
├── calendar_email_skill.py    # Main skill file
├── skill.md                   # This file
├── README.md                  # Full documentation
├── USAGE.md                   # Usage guide
├── examples/                  # Example prompts
├── tests/                     # Test scripts
└── config/                    # Configuration
```

## 🔗 Links

- **GitHub Repository:** https://github.com/gaoofeii/Calendar-Email-Skill
- **Direct Download:** https://github.com/gaoofeii/Calendar-Email-Skill/raw/main/calendar-email-skill-v1.0.0.zip
- **Main Skill File:** https://raw.githubusercontent.com/gaoofeii/Calendar-Email-Skill/main/calendar_email_skill.py

## 📞 Support

- **Issues:** GitHub Issues
- **Questions:** Check `USAGE.md` or `examples/`
- **Testing:** Run `tests/test_skill.sh`

---

**Skill Ready for Use!** 🎉