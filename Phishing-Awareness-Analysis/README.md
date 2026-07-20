# Project 3: Phishing Awareness & Triage Analysis

## 1. Objective
This project documents the detailed security analysis of three simulated phishing attacks. The goal is to isolate critical indicators of compromise (IoCs), explain the underlying risks of each message, and provide an actionable, non-expert triage checklist and decision tree to strengthen the "human firewall" within an organization.


## 2. Red Flag Triage Checklist
Use this 10-point checklist to evaluate any unexpected incoming communication before interacting with it:

* **Sender Mismatch:** The display name does not align with the actual underlying domain or email address.
* **Artificial Urgency:** Pressuring language demanding immediate action to avoid negative consequences.
* **Lookalike Domains:** Typosquatting or combosquatting designed to mimic trusted brands (e.g., using zeros for 'O's or adding extra hyphens).
* **Requests for Secrecy:** Demands to bypass regular reporting lines or keep the communication strictly confidential.
* **Sensitive Info Harvesters:** Prompts for credentials, multi-factor authentication (MFA) codes, or financial transactions.
* **Obfuscated Links:** Hyperlinks where the display text differs from the actual destination URL revealed on hover.
* **Unusual Attachments:** Unexpected files or dangerous extensions (e.g., `.iso`, `.js`, `.scr`).
* **Generic Greetings:** Phrasing like "Dear User" instead of a personalized name, often accompanied by poor grammar[cite: 1].
* **Unsolicited Channels:** Business communications arriving via unexpected vectors like SMS or personal messaging apps[cite: 1].
* **High-Emotion Triggers:** Promises of massive rewards or sudden threats designed to bypass critical thinking[cite: 1].


## 3. Simulated Message Deep Dives

### Sample 1: Credential-Harvesting Email
* **From:** IT Security Team `<support@decodelabs-secure-login.com>`
* **Subject:** URGENT: Your password expires in 2 hours
* **True Destination URL:** `http://decodelabs-secure-login.com.acc0unt-verify.net/reset`
* **Verdict:** 🔴 **MALICIOUS**
* **Security Risk:** This is a credential-harvesting attempt. Interacting with the link directs users to a spoofed login interface designed to steal corporate credentials.

[ Red Flags Identified ]

Combosquatting domain (decodelabs-secure-login.com) trying to look official.

Severe time pressure (2-hour limit) to force panic.

Generic "Dear User" greeting.

Hidden destination domain (acc0unt-verify.net) buried at the end of a long URL string.

### Sample 2: Business Email Compromise (CEO Fraud)
* **From:** Rohan Mehta (CEO) `<r.mehta.ceo@executive-office-update.com>`
* **Subject:** CONFIDENTIAL — Immediate wire transfer needed
* **Verdict:** 🔴 **MALICIOUS**

[ Red Flags Identified ]

Display name spoofing utilizing an external, unrecognized domain.

Executive impersonation combined with a strict financial deadline.

Explicit instruction to bypass standard financial compliance and validation policies.

Isolation tactic ("can't talk", "closed-door meeting") to prevent out-of-band verification.

* **Security Risk:** This is a classic Business Email Compromise (BEC) macro-attack. It relies entirely on social engineering and authority to execute unauthorized financial transactions.

### Sample 3: Package Delivery Smishing
* **From:** `+1 (302) 555-0199`
* **Message:** Incomplete address delivery failure warning
* **URL:** `bit.ly/pkg-updt3x`
* **Verdict:** 🟡 **SUSPICIOUS**

[ Red Flags Identified ]

Unsolicited text message from an unverified, generic mobile phone number.

The use of a link shortener (bit.ly) to completely obscure the final landing domain.

Employs a low-level urgency hook (24-hour return-to-sender deadline).

* **Security Risk:** Smishing attacks shift the target to mobile devices where email filters cannot protect the user. The hidden page likely targets personal identity details or credit card data.


## 4. Operational Triage Decision Tree
Every suspicious message should be systematically filtered into one of three action paths:

| Classification | Indicators | Required Action |
| :--- | :--- | :--- |
| **SAFE** | 0–1 Red Flags; Verified sender identity & clean links. | Close and proceed normally. |
| **SUSPICIOUS** | 2–3 Red Flags; Unverified sender details or shortened links. | **Pause & Verify:** Validate the request via an independent, known channel (e.g., official phone extension). |
| **MALICIOUS** | 4+ Red Flags; Confirmed lookalike domains or urgent credential requests. | **Block & Escalate:** Do not click. Report immediately via the internal IT security reporting tool. |


## 5. Conclusion
Defending an enterprise network requires combining automated technology filters with strong psychological awareness. By deploying this structured triage model, organizations can effectively transform employees from passive targets into active defensive assets.
