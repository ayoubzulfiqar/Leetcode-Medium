def apply_substitutions(text: str, substitutions: dict[str, str]) -> str:
    modified_text = text
    for old_substring, new_substring in substitutions.items():
        if old_substring:
            modified_text = modified_text.replace(old_substring, new_substring)
    return modified_text