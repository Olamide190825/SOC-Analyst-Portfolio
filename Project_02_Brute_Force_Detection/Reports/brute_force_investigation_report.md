# SOC Investigation Report: Brute-Force Detection

## 1. Investigation Overview

**Project:** Brute-Force Detection and Authentication Log Analysis

**Investigation Type:** Authentication Log Analysis

**Data Source:** Synthetic authentication log (`authentication_log.csv`)

**Detection Tool:** Python

**Detection Threshold:** Five or more failed login attempts within five minutes

**Assessment:** Suspicious authentication activity - further investigation required

## 2. Objective

The objective was to analyse authentication events, identify repeated failed login attempts, detect potentially suspicious login behaviour, and determine whether a successful authentication occurred after the failed attempts.

## 3. Detection Methodology

A Python script was developed to:

- Read authentication records from a CSV file.
- Group events by username and source IP address.
- Identify five or more failed login attempts within a five-minute window.
- Identify the fifth failed login timestamp.
- Check whether a successful login occurred after the fifth failure within the detection window.

## 4. Investigation Findings

The analysis identified suspicious activity involving the `admin` account.

| Finding | Result |
|---|---|
| Target account | admin |
| Source IP | 192.168.18.25 |
| Failed attempts within window | 8 |
| Fifth failed login | 08:02:00 |
| Successful login | 08:02:30 |
| Additional failed attempts | 3 |

### Authentication Timeline

- 08:00:00 to 08:02:00: Five failed login attempts against the admin account.
- 08:02:30: Successful login from the same source IP.
- 08:04:00 to 08:05:00: Three additional failed login attempts.

The successful login occurred 30 seconds after the fifth failed attempt.

The three additional failures occurred after the successful login.

### Comparison Account

The `john` account recorded one failed login followed by a successful login from `192.168.18.30`.

This activity did not meet the configured detection threshold.

## 5. Risk Assessment

**Assessment:** Suspicious activity; possible brute-force behaviour.

Repeated failed authentication attempts followed by a successful login may indicate that an account was accessed after repeated password attempts.

However, the available synthetic logs do not establish whether the successful login was authorised or whether an account was compromised.

## 6. Recommended SOC Response

1. Verify whether the successful admin login was authorised.
2. Review the source device and relevant endpoint activity.
3. Examine subsequent account activity for suspicious commands, privilege changes, or unusual access.
4. Review authentication logs for additional attempts outside the five-minute detection window.
5. If unauthorised access is confirmed, follow the organisation's incident response process, including appropriate account protection and session revocation.
6. Preserve relevant logs and document the investigation.

## 7. Limitations

- The investigation used synthetic lab data, not production authentication logs.
- The detection rule uses a fixed threshold of five failures within five minutes.
- Slow, distributed, or low-frequency attacks may not trigger this rule.
- The presence of a successful login does not independently prove account compromise.

## 8. Conclusion

The Python detection tool successfully identified repeated failed login attempts against the admin account from `192.168.18.25`, followed by a successful authentication.

The investigation demonstrates practical experience in authentication log analysis, threshold-based detection, event correlation, alert interpretation, and SOC investigation documentation.

The alert should be investigated further before concluding that unauthorised access occurred.
