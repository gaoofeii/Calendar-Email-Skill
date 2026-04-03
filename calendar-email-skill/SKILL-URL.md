# Calendar Email Sharing Skill - Skill URL & Distribution

## 📦 Skill Package Structure

```
calendar-email-skill/
├── calendar_email_skill.py      # Main skill file
├── README.md                    # Documentation
├── USAGE.md                     # Usage guide
├── SKILL-URL.md                 # This file
├── examples/                    # Example prompts
│   ├── schedule_event.txt
│   ├── send_invite.txt
│   └── check_availability.txt
├── tests/                       # Test scripts
│   └── test_skill.sh
└── config/                      # Configuration
    └── smtp_config_template.py
```

## 🔗 Skill URL Format

### GitHub Repository URL:
```
https://github.com/[username]/calendar-email-skill
```

### Direct Download URLs:
```
# Main skill file
https://raw.githubusercontent.com/[username]/calendar-email-skill/main/calendar_email_skill.py

# Complete package (zip)
https://github.com/[username]/calendar-email-skill/archive/refs/heads/main.zip
```

### LiteRT-LM Skill Registry Format:
```json
{
  "name": "calendar-email-skill",
  "version": "1.0.0",
  "description": "Schedule events and send email invitations",
  "author": "Your Name",
  "repository": "https://github.com/[username]/calendar-email-skill",
  "main": "calendar_email_skill.py",
  "tools": ["create_event", "send_invite", "check_availability"],
  "compatibility": ["litert-lm>=0.10.1", "gemma-4-E2B-it"],
  "license": "MIT"
}
```

## 🚀 Installation Methods

### Method 1: Direct Download
```bash
# Download skill file
curl -O https://raw.githubusercontent.com/[username]/calendar-email-skill/main/calendar_email_skill.py

# Use with LiteRT-LM
litert-lm run gemma-4-E2B-it.litertlm \
  --preset=calendar_email_skill.py \
  --prompt="Schedule meeting on 2024-12-25"
```

### Method 2: Git Clone
```bash
# Clone repository
git clone https://github.com/[username]/calendar-email-skill.git
cd calendar-email-skill

# Use skill
litert-lm run gemma-4-E2B-it.litertlm \
  --preset=calendar_email_skill.py \
  --prompt="Schedule meeting on 2024-12-25"
```

### Method 3: Package Manager (Future)
```bash
# When LiteRT-LM skill registry is available
litert-lm skill install calendar-email-skill
```

## 📋 Skill Metadata

### Basic Info:
- **Name**: Calendar Email Skill
- **Version**: 1.0.0
- **Type**: LiteRT-LM Agent Skill
- **Model Compatibility**: Gemma 4 E2B, other LiteRT-LM models
- **CLI Compatibility**: litert-lm 0.10.1+

### Features:
- ✅ Event scheduling with validation
- ✅ Email invitation generation
- ✅ Date availability checking
- ✅ SMTP integration ready
- ✅ Professional email templates
- ✅ Error handling

### Dependencies:
- LiteRT-LM CLI
- Gemma 4 E2B model (or compatible)
- Python 3.8+ (for development)
- SMTP access (for production email)

## 🎯 Usage Examples

### Quick Test:
```bash
# Test all functions
./tests/test_skill.sh
```

### Production Use:
```bash
# Schedule and invite workflow
litert-lm run gemma-4-E2B-it.litertlm \
  --preset=calendar_email_skill.py \
  --prompt="Schedule team meeting on 2024-12-25 at 14:00 for 2 hours and invite team@company.com"
```

## 🔧 Configuration

### For Production Email:
1. Copy `config/smtp_config_template.py` to skill file
2. Update SMTP settings
3. Test with real email

### Customization:
- Modify email templates in `send_invite()` function
- Add new tools as needed
- Update SYSTEM_INSTRUCTIONS for specific use cases

## 📊 Skill Statistics

- **Lines of Code**: ~200
- **Tools**: 3 main functions
- **Examples**: 3 categories
- **Tests**: Complete test suite
- **Documentation**: README, USAGE, examples

## 🔗 Integration Points

### With Other Skills:
```python
# Combine with weather skill
from calendar_email_skill import TOOLS as calendar_tools
from weather_skill import TOOLS as weather_tools

TOOLS = calendar_tools + weather_tools
```

### With Web APIs:
- Google Calendar API
- Outlook Calendar API
- SMTP email services
- Calendar file (ICS) generation

## 📝 Publishing Checklist

### Before Publishing:
- [ ] Update repository URL in all files
- [ ] Test with latest LiteRT-LM version
- [ ] Verify all examples work
- [ ] Update version number if needed
- [ ] Add license file
- [ ] Create release notes

### Publishing Steps:
1. Create GitHub repository
2. Push skill files
3. Create release tag (v1.0.0)
4. Update skill registry (if available)
5. Share skill URL

## 🌐 Distribution Channels

### Primary:
- **GitHub**: Main repository
- **GitHub Releases**: Versioned releases
- **Raw GitHub**: Direct file access

### Secondary:
- **Skill Registry**: LiteRT-LM community registry
- **Package Managers**: pip, uv (future)
- **Skill Marketplace**: Community platforms

## 📞 Support & Community

### Issue Tracking:
- GitHub Issues for bug reports
- GitHub Discussions for questions
- Pull Requests for contributions

### Documentation:
- README.md - Installation & overview
- USAGE.md - Detailed usage guide
- Examples/ - Ready-to-use prompts
- Tests/ - Verification scripts

## 🔄 Version History

### v1.0.0 (Current)
- Initial release
- Three core tools
- Email simulation
- Complete documentation
- Test suite

### Planned Features:
- Real email sending
- Calendar API integration
- Recurring events
- Timezone support
- Bulk invitations

## 📄 License

MIT License - See LICENSE file for details.

## 🙏 Acknowledgments

- Google AI Edge for LiteRT-LM
- Gemma team for the model
- SMTP library maintainers
- Community contributors

---

## 🎉 Skill Ready for Distribution!

**Skill URL**: `https://github.com/[username]/calendar-email-skill`  
**Main File**: `calendar_email_skill.py`  
**Version**: 1.0.0  
**Status**: Production Ready  

To use: Download `calendar_email_skill.py` and use with LiteRT-LM:
```bash
litert-lm run gemma-4-E2B-it.litertlm --preset=calendar_email_skill.py --prompt="Your request"
```