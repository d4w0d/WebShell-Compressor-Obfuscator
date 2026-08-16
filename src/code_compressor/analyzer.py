import re

PATTERNS = {
    "eval": r"\beval\s*\(",
    "exec": r"\bexec\s*\(",
    "system": r"\bsystem\s*\(",
    "shell_exec": r"\bshell_exec\s*\(",
    "passthru": r"\bpassthru\s*\(",
    "proc_open": r"\bproc_open\s*\(",
    "base64_decode": r"\bbase64_decode\s*\(",
}

def analyze_code(code: str) -> dict:
    findings = []
    for name, pattern in PATTERNS.items():
        matches = list(re.finditer(pattern, code, flags=re.IGNORECASE))
        if matches:
            findings.append({
                "pattern": name,
                "count": len(matches),
                "lines": [code.count("\n", 0, m.start()) + 1 for m in matches],
            })

    score = min(100, sum(f["count"] * 15 for f in findings))
    return {
        "risk_score": score,
        "suspicious": [f["pattern"] for f in findings],
        "findings": findings,
        "sha256": __import__("hashlib").sha256(code.encode()).hexdigest(),
    }
