# Incident Response Playbook: SSH Brute-Force & Unauthorized Access

## 📌 1. Overview & Purpose
* **Incident Type:** Automated Brute-Force Attack / Credential Stuffing against Secure Shell (SSH).
* **Objective:** Standardized operating procedure (SOP) for Security Operations Center (SOC) analysts to detect, triage, contain, and remediate unauthorized SSH access attempts.
* **Framework Alignment:** NIST SP 800-61 Rev. 2 (Computer Security Incident Handling Guide).

---

## 🔍 Phase 1: Identification & Triage
When an alert triggers for suspicious login spikes or failed authentication thresholds:

1. **Acknowledge & Log:** Note the timestamp, source IP, target account, and volume of failures.
2. **Examine Authentication Logs:** Access the target system and review live or historical auth logs:
   ```bash
   sudo grep "Failed password" /var/log/auth.log
