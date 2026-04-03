#!/bin/bash

echo "=== Testing Calendar Email Skill ==="
echo ""

export PATH="$HOME/.local/bin:$PATH"

echo "1. Testing create_event function..."
echo "   Prompt: 'Schedule team meeting on 2024-12-25 at 14:00 for 2 hours'"
echo ""
timeout 10 litert-lm run gemma-4-E2B-it.litertlm \
  --preset=../calendar_email_skill.py \
  --prompt="Schedule team meeting on 2024-12-25 at 14:00 for 2 hours" 2>&1 | grep -A5 -B5 "tool_call\|tool_response\|Event\|success"

echo ""
echo "---"
echo "2. Testing send_invite function..."
echo "   Prompt: 'Send invitation for team meeting on 2024-12-25 to john@example.com'"
echo ""
timeout 10 litert-lm run gemma-4-E2B-it.litertlm \
  --preset=../calendar_email_skill.py \
  --prompt="Send invitation for team meeting on 2024-12-25 to john@example.com" 2>&1 | grep -A5 -B5 "tool_call\|tool_response\|Invitation\|email"

echo ""
echo "---"
echo "3. Testing check_availability function..."
echo "   Prompt: 'Check availability on 2024-12-25'"
echo ""
timeout 10 litert-lm run gemma-4-E2B-it.litertlm \
  --preset=../calendar_email_skill.py \
  --prompt="Check availability on 2024-12-25" 2>&1 | grep -A5 -B5 "tool_call\|tool_response\|availability\|slots"

echo ""
echo "=== Skill Test Complete ==="
echo ""
echo "✅ Skill is working correctly if:"
echo "   1. Tools are being called (tool_call messages)"
echo "   2. Tools return responses (tool_response messages)"
echo "   3. Model presents results clearly"
echo ""
echo "📁 Skill location: ../calendar_email_skill.py"
echo "📚 Examples: ../examples/"
echo "🚀 Ready for use with LiteRT-LM!"