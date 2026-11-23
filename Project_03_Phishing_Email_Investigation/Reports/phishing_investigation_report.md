# Phishing Email Investigation Report

## 1. Project Overview

**Project:** Phishing Email Investigation




**Role:** Junior SOC Analyst (Training Simulation)




**Tools Used:** Python, PowerShell




**Environment:** Controlled synthetic email investigation

## 2. Investigation Objective

The objective was to examine a suspicious email, analyse its headers and content, identify potential phishing indicators, and recommend appropriate security response actions.

A synthetic email was used to practise phishing investigation techniques safely.

## 3. Email Details

| Field | Extracted Information |
|---|---|
| Displayed Sender | support@company.example |
| Recipient | employee@company.example |
| Reply-To | helpdesk@external-mail.example |
| Return-Path | bounce@external-mail.example |
| Subject | Urgent: Your Mailbox Will Be Disabled |
| SPF | Fail |
| DKIM | None |
| DMARC | Fail |
| Suspicious URL | http://mailbox-check.example/verify |

## 4. Investigation Methodology

A Python email analysis script was used to:

1. Load the sample email.
2. Extract important email headers.
3. Examine the sender, Reply-To and Return-Path.
4. Retrieve reported authentication results.
5. Extract URLs from the email body.
6. Identify suspicious language and indicators.
7. Generate an investigation summary.

The suspicious URL was inspected as text only and was not opened.

## 5. Investigation Findings

Seven suspicious indicators were identified.

### Finding 1: Sender and Reply-To Mismatch

The displayed sender was support@company.example, while the Reply-To address was helpdesk@external-mail.example.

**Analysis:** The reply address uses a different domain from the claimed organisation. This may indicate an attempt to redirect replies to an external party.

### Finding 2: External Return-Path

The Return-Path was bounce@external-mail.example.

**Analysis:** The return address differs from the displayed sender domain and warrants further investigation.

### Finding 3: SPF Failure

The reported SPF result was fail.

**Analysis:** The reported authentication result indicates that the sending host did not pass the SPF check.

### Finding 4: Missing DKIM

The reported DKIM result was none.

**Analysis:** No DKIM signature was reported.

### Finding 5: DMARC Failure

The reported DMARC result was fail.

**Analysis:** The reported DMARC check failed, providing another reason to investigate the message's authenticity.

### Finding 6: Urgent and Threatening Language

The subject stated: "Urgent: Your Mailbox Will Be Disabled."

The body threatened loss of email access unless the recipient acted immediately.

**Analysis:** Creating urgency and fear is a common social engineering technique.

### Finding 7: Suspicious Verification Link

The message contained:

http://mailbox-check.example/verify

**Analysis:** The message encouraged the recipient to verify an account through a link. The destination was not opened, and its legitimacy remains unverified.

## 6. Risk Assessment

**Assessment: Suspicious — High Priority for Investigation**

The combination of sender inconsistencies, failed reported authentication checks, urgent language and an account-verification link creates a strong phishing pattern.

The message should not be trusted without further verification.

This assessment identifies suspicious indicators; it does not independently establish malicious intent or successful account compromise.

## 7. Recommended SOC Response

As a Junior SOC Analyst, I would recommend:

1. Quarantine the email to prevent further interaction.
2. Identify other recipients who may have received the message.
3. Search email security logs for similar sender addresses, subjects and URLs.
4. Block the sender or URL if confirmed malicious, following organisational procedures.
5. Notify affected users and advise them not to click the link or reply.
6. If credentials were submitted, initiate the account-compromise response process.
7. Escalate the investigation to a senior analyst where necessary.
8. Document findings and response actions in the incident management system.

## 8. Evidence Collected

- Data/sample_phishing_email.eml — Synthetic suspicious email.
- Scripts/phishing_analyzer.py — Python email analysis script.
- Evidence/01_phishing_analysis_output.png — Screenshot of successful analysis.

## 9. Investigation Limitations

- The email was synthetic and created for training.
- SPF, DKIM and DMARC values were read from the sample Authentication-Results header. They were not independently verified.
- The destination URL was not opened or tested.
- No live email server, DNS records or threat intelligence platform was queried.
- The findings demonstrate indicators requiring investigation, not confirmed compromise.

## 10. Conclusion

The investigation demonstrated how Python can automate the extraction and examination of suspicious email information.

Seven suspicious indicators were identified, including sender inconsistencies, reported email authentication failures, urgent language and a verification link.

The exercise strengthened practical skills in email header analysis, phishing detection, Python scripting, evidence collection, risk assessment and SOC incident documentation.

**Project Status:** Completed — Synthetic Training Investigation.
