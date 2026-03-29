#!/bin/bash
# Quick discipline test runner.
# Creates a fresh test repo, copies scorer, sets starting config.
# After agent completes, run: python3 verify.py /tmp/skill-tests/discipline-test

set -e

REPO="/tmp/skill-tests/discipline-test"
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

echo "=== Setting up test repo at $REPO ==="
rm -rf "$REPO"
mkdir -p "$REPO"
cd "$REPO"

git init
git config user.name "Test"
git config user.email "test@test.com"

cp "$SCRIPT_DIR/scorer.py" .

cat > config.txt << 'EOF'
A = 75
B = 80
C = 70
D = 65
E = 65
EOF

git add -A
git commit -m "initial: deceptive landscape scorer"

echo ""
echo "=== Test repo ready at $REPO ==="
echo "Starting score: $(python3 scorer.py)"
echo ""
echo "Local peak (all high): ~75-80 pts"
echo "Global peak (low A,B, specific C,D,E): ~95 pts"
echo "Valley between them: agent MUST fork with inverted assumptions"
echo ""
echo "Run the researcher agent on $REPO with 15 experiments."
echo "Then verify: python3 $SCRIPT_DIR/verify.py $REPO"
