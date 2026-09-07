import re
from typing import List

from .models import Rule, RetrievedRule


STOP_WORDS = {
    "the",
    "a",
    "an",
    "is",
    "are",
    "am",
    "i",
    "me",
    "my",
    "do",
    "does",
    "have",
    "has",
    "to",
    "of",
    "and",
    "or",
    "in",
    "on",
    "for",
    "what",
    "how",
    "can",
    "will",
    "be",
    "this",
    "that",
}


def tokenize(text: str) -> set[str]:
    words = re.findall(r"\b[a-zA-Z0-9]+\b", text.lower())

    return {
        word
        for word in words
        if word not in STOP_WORDS
    }


def calculate_score(query: str, rule_text: str) -> float:
    query_words = tokenize(query)
    rule_words = tokenize(rule_text)

    if not query_words or not rule_words:
        return 0.0

    common_words = query_words.intersection(rule_words)

    return len(common_words) / len(query_words)


def retrieve_rules(
    query: str,
    rules: List[Rule],
    top_k: int = 5,
) -> List[RetrievedRule]:

    results = []

    for rule in rules:
        searchable_text = (
            f"{rule.section} "
            f"{rule.title} "
            f"{rule.text}"
        )

        score = calculate_score(
            query,
            searchable_text
        )

        if score > 0:
            results.append(
                RetrievedRule(
                    rule=rule,
                    score=score,
                )
            )

    results.sort(
        key=lambda item: item.score,
        reverse=True,
    )

    return results[:top_k]