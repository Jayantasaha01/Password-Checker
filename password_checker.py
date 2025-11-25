#!/usr/bin/env python3
import re
import sys

COMMON_WORDS = {"password","123456","qwerty","letmein","admin","welcome"}

def score_password(pw: str):
    score = 0
    reasons = []
    if len(pw) >= 12:
        score += 2
    elif len(pw) >= 8:
        score += 1
    else:
        reasons.append("Use at least 8 characters (12+ recommended).")

    if re.search(r'[a-z]', pw) and re.search(r'[A-Z]', pw):
        score += 1
    else:
        reasons.append("Mix upper and lower case letters.")

    if re.search(r'\d', pw):
        score += 1
    else:
        reasons.append("Add digits.")

    if re.search(r'[^A-Za-z0-9]', pw):
        score += 1
    else:
        reasons.append("Add symbols like !@#$%.")

    if pw.lower() in COMMON_WORDS or re.search(r'^(.)\1+$', pw):
        reasons.append("Avoid common or repeated patterns.")
        score = max(0, score-2)

    # Grading scale of the password from 1 to 5
    if score >= 5:
        verdict = "Strong"
    elif score >= 3:
        verdict = "Moderate"
    else:
        verdict = "Weak"

    return {"password":pw, "score":score, "verdict":verdict, "reasons":reasons}

def main():
    if len(sys.argv) > 1:
        pw = sys.argv[1]
        out = score_password(pw)
        print("Password Strength will be Scored from 0 to 5")
        print(f"Password: {out['password']}\nScore: {out['score']}\nVerdict: {out['verdict']}")
        if out['reasons']:
            print("Suggestions:")
            for r in out['reasons']:
                print("-", r)
    else:
        print("Usage: python3 password_checker.py <password>")

if __name__ == "__main__":
    main()
