
from email import policy
from email.parser import BytesParser
from pathlib import Path
from urllib.parse import urlparse

# Locate the sample email
project_dir = Path(__file__).resolve().parent.parent
email_file = project_dir / "Data" / "sample_phishing_email.eml"

# Read and parse the email
with email_file.open("rb") as file:
    message = BytesParser(policy=policy.default).parse(file)

print("=" * 60)
print("PHISHING EMAIL INVESTIGATION")
print("=" * 60)

# Extract important email details
sender = message.get("From", "Not provided")
reply_to = message.get("Reply-To", "Not provided")
return_path = message.get("Return-Path", "Not provided")
subject = message.get("Subject", "Not provided")
auth_results = message.get("Authentication-Results", "Not provided")

print(f"\nSender: {sender}")
print(f"Reply-To: {reply_to}")
print(f"Return-Path: {return_path}")
print(f"Subject: {subject}")
print(f"Authentication Results: {auth_results}")

# Extract URLs from the email body
body = message.get_body(preferencelist=("plain",))
body_text = body.get_content() if body else ""

urls = [
    word.strip(".,;:()<>")
    for word in body_text.split()
    if word.lower().startswith(("http://", "https://"))
]

print("\nURLs Found:")
if urls:
    for url in urls:
        parsed_url = urlparse(url)
        print(f"- {url}")
        print(f"  Domain: {parsed_url.hostname}")
else:
    print("- No URLs found")

# Identify suspicious indicators
findings = []

if reply_to != "Not provided" and reply_to != sender:
    findings.append("Reply-To address differs from the displayed sender.")

if return_path != "Not provided" and "external-mail.example" in return_path:
    findings.append("Return-Path uses an external domain.")

auth_lower = auth_results.lower()

for result in ("spf=fail", "dkim=none", "dmarc=fail"):
    if result in auth_lower:
        findings.append(f"Email authentication indicator detected: {result.upper()}.")

if any(word in subject.lower() for word in ("urgent", "immediately", "disabled")):
    findings.append("Subject uses urgent or threatening language.")

if urls:
    findings.append("Email contains a link requesting recipient interaction.")

print("\n" + "=" * 60)
print("INVESTIGATION FINDINGS")
print("=" * 60)

for number, finding in enumerate(findings, start=1):
    print(f"{number}. {finding}")

print("\nOverall Assessment: SUSPICIOUS")
print("Note: This is a synthetic training email.")
print("Authentication results are reported headers, not independently verified.")
print("=" * 60)
