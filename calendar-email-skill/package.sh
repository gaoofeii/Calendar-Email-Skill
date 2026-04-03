#!/bin/bash

echo "=== Packaging Calendar Email Skill ==="
echo ""

# Create zip file
ZIP_FILE="calendar-email-skill-v1.0.0.zip"

echo "1. Creating zip archive: $ZIP_FILE"
zip -r "$ZIP_FILE" . \
  -x "*.zip" \
  -x "*.git*" \
  -x "package.sh" \
  -x "__pycache__/*" \
  -x "*.pyc"

echo ""
echo "2. File structure in archive:"
unzip -l "$ZIP_FILE" | head -20

echo ""
echo "3. Skill size:"
du -sh "$ZIP_FILE"
du -sh .

echo ""
echo "4. Skill contents:"
echo "   Main file: calendar_email_skill.py"
echo "   Documentation: README.md, USAGE.md"
echo "   Examples: examples/"
echo "   Tests: tests/"
echo "   Configuration: config/"

echo ""
echo "5. Usage instructions:"
echo "   Download and extract, then:"
echo "   litert-lm run gemma-4-E2B-it.litertlm \\"
echo "     --preset=calendar_email_skill.py \\"
echo "     --prompt=\"Schedule meeting on 2024-12-25\""

echo ""
echo "✅ Skill packaged successfully: $ZIP_FILE"
echo "📦 Ready for distribution!"