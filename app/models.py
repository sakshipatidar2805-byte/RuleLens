from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Rule:
    rule_id: str
    section: str
    title: str
    text: str


@dataclass
class RetrievedRule:
    rule: Rule
    score: float


@dataclass
class Decision:
    eligible: bool
    status: str
    explanation: str
    supporting_rules: List[RetrievedRule]
    warnings: Optional[List[str]] = None