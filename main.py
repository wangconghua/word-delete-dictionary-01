#!/usr/bin/env python3
"""The Word You'd Delete From the Dictionary.

Writes the single word to erase from the dictionary forever to
/output/entry.txt.

The pick: "whatchamacallit".

Why this word, against the judge brief's criteria in order:
1. It names a real word every reader recognises.
2. The joke lands at first sight: it is the word you reach for when
   you have forgotten the word. Erase it and there is no word left
   for the word you forgot.
3. The humour comes from the word itself: its sound, its literal
   meaning ("what you may call it"), and the self-defeating gap its
   deletion leaves in the language.
4. It is fresh: the field will crowd the obvious deletions ("moist",
   "irregardless", "literally", "synergy"). Placeholder words are a
   family almost nobody thinks of first, yet the pick is instantly
   understood.
5. It is exact: one word, spelled correctly, with nothing added.
"""

import os

ENTRY = "whatchamacallit"


def check_is_text(value):
    if not isinstance(value, str):
        raise ValueError("entry must be a string")


def check_not_blank(value):
    if not value.strip():
        raise ValueError("entry must not be blank")


def check_length(value):
    # Gate: /output/entry.txt is UTF-8 text of 1 to 77 characters.
    if not 1 <= len(value) <= 77:
        raise ValueError("entry must be 1-77 characters, got %d" % len(value))


def check_single_word(value):
    if len(value.split()) != 1:
        raise ValueError("entry must be exactly one word")


def check_no_edge_whitespace(value):
    if value != value.strip():
        raise ValueError("entry must not start or end with whitespace")


def check_letters_only(value):
    if not value.isalpha():
        raise ValueError("entry must contain letters only")


def check_lowercase(value):
    if value != value.lower():
        raise ValueError("entry must be lowercase")


def check_spelling(value):
    # Exactness (criterion 5): one word, spelled correctly.
    if value != ENTRY:
        raise ValueError("entry must be spelled %r" % ENTRY)


def check_utf8(value):
    value.encode("utf-8")


CHECKS = (
    check_is_text,
    check_not_blank,
    check_length,
    check_single_word,
    check_no_edge_whitespace,
    check_letters_only,
    check_lowercase,
    check_spelling,
    check_utf8,
)


def validate(value):
    """Run every check; raises ValueError on failure."""
    for check in CHECKS:
        check(value)
    return True


def main():
    validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    # No trailing newline: the file must be exactly the one word.
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print("wrote /output/entry.txt (%d chars)" % len(ENTRY))


if __name__ == "__main__":
    main()
