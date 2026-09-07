\# RuleLens



\## Explainable University Rule Decision System



RuleLens is a rule-based academic decision system that analyzes university regulations and provides transparent, explainable decisions.



The current implementation focuses on \*\*attendance and examination eligibility\*\*.



\---



\## Problem Statement



University academic regulations are often lengthy and difficult for students to interpret.



RuleLens converts academic regulations into structured rules and evaluates a student's situation against those rules.



Instead of providing only a final decision, the system also shows the supporting regulations used for that decision.



\---



\## Features



\- Attendance eligibility checking

\- Rule ingestion from Markdown documents

\- Rule-based retrieval

\- Relevance scoring

\- Explainable decisions

\- Medical attendance concession handling

\- Supporting rule display

\- Warning messages for incomplete conditions

\- Web-based interface using Flask

\- Command-line interface

\- Automated testing with pytest



\---



\## Attendance Rules



The current corpus contains 10 academic regulation sections:



1\. ATT-1 - General Attendance Requirement

2\. ATT-2 - Attendance Calculation

3\. ATT-3 - Medical Absence

4\. ATT-4 - Attendance Concession

5\. ATT-5 - Attendance Shortage

6\. ATT-6 - Department Review

7\. ATT-7 - Student Responsibility

8\. ATT-8 - Attendance and Examination Registration

9\. ATT-9 - Record Keeping

10\. ATT-10 - Scope



\### Important Rules



\- Normal examination eligibility requires at least 75% attendance.

\- Students between 65% and 74.99% may be considered under the medical concession provision.

\- Medical concession requires a documented and approved medical circumstance.

\- Attendance below the applicable threshold results in a not-eligible decision.



\---



\## System Architecture



```text

&#x20;               University Regulations

&#x20;                        |

&#x20;                        v

&#x20;               Markdown Rule Corpus

&#x20;                        |

&#x20;                        v

&#x20;                 Rule Ingestion

&#x20;                        |

&#x20;                        v

&#x20;                 Rule Retrieval

&#x20;                        |

&#x20;                        v

&#x20;                Relevance Scoring

&#x20;                        |

&#x20;                        v

&#x20;                 Decision Engine

&#x20;                        |

&#x20;                        v

&#x20;             Explainable Decision

&#x20;                   /          \\

&#x20;                  /            \\

&#x20;                 v              v

&#x20;            Web Interface    CLI Output

