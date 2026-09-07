from pathlib import Path
from typing import List

from .models import Rule


def load_rules(corpus_path: str = "corpus/attendance_rules.md") -> List[Rule]:
    path = Path(corpus_path)

    if not path.exists():
        raise FileNotFoundError(f"Corpus file not found: {path}")

    content = path.read_text(encoding="utf-8")

    rules = []
    current_section = None
    current_title = None
    current_text = []

    for line in content.splitlines():
        line = line.strip()

        # Remove accidental backslashes from Markdown headings
        clean_line = line.lstrip("\\")

        if clean_line.startswith("### Section "):

            if current_section and current_title and current_text:
                rules.append(
                    Rule(
                        rule_id=current_section,
                        section=current_section,
                        title=current_title,
                        text=" ".join(current_text).strip(),
                    )
                )

            section_text = clean_line.replace(
                "### Section ", "", 1
            ).strip()

            if ":" in section_text:
                section_id, title = section_text.split(":", 1)
                current_section = section_id.strip()
                current_title = title.strip()
            else:
                current_section = section_text
                current_title = section_text

            current_text = []

        elif clean_line.startswith("#") or clean_line == "":
            continue

        else:
            current_text.append(clean_line)

    # Add final section
    if current_section and current_title and current_text:
        rules.append(
            Rule(
                rule_id=current_section,
                section=current_section,
                title=current_title,
                text=" ".join(current_text).strip(),
            )
        )

    return rules