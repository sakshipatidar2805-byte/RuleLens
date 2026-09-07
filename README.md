\# RuleLens



\## Explainable University Rule Decision System



RuleLens is an explainable, rule-based academic decision system that converts university regulations into structured rules and evaluates a student's situation against those rules.



Instead of providing only a final decision, RuleLens also explains \*\*why the decision was made\*\* and displays the supporting academic regulations.



The current implementation focuses on \*\*attendance and examination eligibility\*\*.



\---



\## 🎯 Problem Statement



University academic regulations are often lengthy, complex, and difficult for students to interpret.



Students may know their attendance percentage but still be unsure whether they are eligible for examinations, whether a medical concession applies, or which regulation supports the decision.



RuleLens solves this problem by:



\- Converting regulations into structured rules

\- Retrieving relevant rules

\- Evaluating student conditions

\- Producing an explainable decision

\- Showing the regulations supporting that decision



\---



\## ✨ Features



\- ✅ Attendance eligibility checking

\- 📚 Rule ingestion from Markdown documents

\- 🔎 Rule-based retrieval

\- 📊 Relevance scoring

\- 🧠 Explainable decision making

\- 🏥 Medical attendance concession handling

\- 📖 Supporting rule display

\- ⚠️ Warning messages for incomplete conditions

\- 🌐 Web-based interface using Flask

\- 💻 Command-line interface

\- 🧪 Automated testing using pytest



\---



\## 📋 Current Attendance Rules



The current rule corpus contains 10 academic regulation sections:



1\. \*\*ATT-1\*\* - General Attendance Requirement

2\. \*\*ATT-2\*\* - Attendance Calculation

3\. \*\*ATT-3\*\* - Medical Absence

4\. \*\*ATT-4\*\* - Attendance Concession

5\. \*\*ATT-5\*\* - Attendance Shortage

6\. \*\*ATT-6\*\* - Department Review

7\. \*\*ATT-7\*\* - Student Responsibility

8\. \*\*ATT-8\*\* - Attendance and Examination Registration

9\. \*\*ATT-9\*\* - Record Keeping

10\. \*\*ATT-10\*\* - Scope



\### Important Rules



\- Normal examination eligibility requires at least \*\*75% attendance\*\*.

\- Students between \*\*65% and 74.99%\*\* may be considered under the medical concession provision.

\- Medical concession requires a documented and approved medical circumstance.

\- Attendance below the applicable threshold results in a \*\*Not Eligible\*\* decision.



\---



\## 🏗️ System Architecture



```text

University Regulations

&#x20;       │

&#x20;       ▼

Markdown Rule Corpus

&#x20;       │

&#x20;       ▼

Rule Ingestion

&#x20;       │

&#x20;       ▼

Rule Retrieval

&#x20;       │

&#x20;       ▼

Relevance Scoring

&#x20;       │

&#x20;       ▼

Decision Engine

&#x20;       │

&#x20;       ▼

Explainable Decision

&#x20;      / \\

&#x20;     /   \\

&#x20;    ▼     ▼

&#x20;Web UI    CLI

