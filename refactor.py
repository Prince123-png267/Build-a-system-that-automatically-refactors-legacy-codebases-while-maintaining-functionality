def find_issues(code):
    issues = []

    if "== None" in code:
        issues.append("Use 'is None' instead of '== None'")

    if "eval(" in code:
        issues.append("Avoid eval() (security risk)")

    if "password =" in code:
        issues.append("Hardcoded password detected")

    return issues


def fix_code(code):
    code = code.replace("== None", "is None")
    code = code.replace('eval("2+2")', "2+2")
    return code


def ai_suggestions(code):
    suggestions = []

    if "range(len(" in code:
        suggestions.append("Use direct iteration (for item in list)")

    if "print(" in code:
        suggestions.append("Use logging instead of print()")

    if "eval(" in code:
        suggestions.append("Avoid eval() for security")

    return suggestions