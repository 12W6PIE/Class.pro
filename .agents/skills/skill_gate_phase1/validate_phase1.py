#!/usr/bin/env python3
import sys
import re
from pathlib import Path

def resolve_workspace_root():
    current_file = Path(__file__).resolve()
    for parent in current_file.parents:
        if parent.name.startswith("Class.pro-TMPL-"):
            prime_root = parent.parent
            x_pros = prime_root.parent
            return x_pros.parent if x_pros.name.lower() in ["_x_pros", "_x_pro"] else prime_root.parent

    for parent in current_file.parents:
        if (parent / ".git").exists() or (parent / "AGENTS.md").exists():
            return parent

    return current_file.parents[3] if len(current_file.parents) > 3 else current_file.parents[2]

def validate_latex(content: str):
    if "\\documentclass" not in content or "\\end{document}" not in content:
        print("[SKILL_FAIL] Invalid LaTeX structure: missing \\documentclass or \\end{document}.", file=sys.stderr)
        sys.exit(1)

    required_sections = [
        (r"\\section\*?\{.*Working Titles.*\}", "Working Titles Section"),
        (r"\\section\*?\{.*Motivation.*\}", "Motivation Section"),
        (r"\\section\*?\{.*Bounded Domain.*\}", "Bounded Domain & SOTA Delta Section"),
        (r"\\section\*?\{.*Developmental Delta.*\}", "Developmental Delta Section"),
        (r"\\section\*?\{.*Tooling.*\}", "Tooling Architecture Section"),
        (r"\\section\*?\{.*Deliverables Mapping.*\}", "Course Deliverables Mapping Section"),
        (r"\\section\*?\{.*Publishing Level Assessment.*\}", "Publishing Level Assessment Section"),
    ]
    return required_sections

def validate_markdown(content: str):
    required_sections = [
        (r"(?im)^#{1,3}\s+.*Working Titles.*", "Working Titles Section"),
        (r"(?im)^#{1,3}\s+.*Motivation.*", "Motivation Section"),
        (r"(?im)^#{1,3}\s+.*Bounded Domain.*", "Bounded Domain & SOTA Delta Section"),
        (r"(?im)^#{1,3}\s+.*Developmental Delta.*", "Developmental Delta Section"),
        (r"(?im)^#{1,3}\s+.*Tooling.*", "Tooling Architecture Section"),
        (r"(?im)^#{1,3}\s+.*Deliverables Mapping.*", "Course Deliverables Mapping Section"),
        (r"(?im)^#{1,3}\s+.*Publishing Level Assessment.*", "Publishing Level Assessment Section"),
    ]
    return required_sections

def validate_phase_1():
    workspace_root = resolve_workspace_root()
    deliverables_dir = workspace_root / "_Deliverables"

    tex_path = deliverables_dir / "1-Page-Brief.tex"
    md_path = deliverables_dir / "1-Page-Brief.md"

    target_path = None
    is_markdown = False

    if md_path.exists() and not tex_path.exists():
        target_path = md_path
        is_markdown = True
    elif tex_path.exists() and not md_path.exists():
        target_path = tex_path
        is_markdown = False
    elif tex_path.exists() and md_path.exists():
        tex_content = tex_path.read_text(encoding="utf-8", errors="ignore")
        md_content = md_path.read_text(encoding="utf-8", errors="ignore")
        if "[INSERT" not in md_content and "[INSERT" in tex_content:
            target_path = md_path
            is_markdown = True
        else:
            target_path = tex_path
            is_markdown = False
    else:
        print(f"[SKILL_FAIL] Neither 1-Page-Brief.tex nor 1-Page-Brief.md found in {deliverables_dir}", file=sys.stderr)
        sys.exit(1)

    print(f"[skill_gate_phase1] Validating deliverable: {target_path.name}")
    content = target_path.read_text(encoding="utf-8")

    if is_markdown:
        required_sections = validate_markdown(content)
    else:
        required_sections = validate_latex(content)

    missing = [name for pattern, name in required_sections if not re.search(pattern, content)]
    placeholder_matches = re.findall(r"\[(?:INSERT|YES/NO|TODO|CHOOSE)\b.*?\]", content, re.IGNORECASE)

    if missing:
        print(f"[SKILL_FAIL] Missing required sections in {target_path.name}:", file=sys.stderr)
        for item in missing:
            print(f"  - {item}", file=sys.stderr)
        sys.exit(2)

    if placeholder_matches:
        print(f"[SKILL_FAIL] Found {len(placeholder_matches)} unreplaced placeholders in {target_path.name}:", file=sys.stderr)
        for ph in placeholder_matches[:5]:
            print(f"  - {ph}", file=sys.stderr)
        sys.exit(3)

    print(f"[SKILL_PASS] {target_path.name} passed all Phase 1 structural and content checks.")
    sys.exit(0)

if __name__ == "__main__":
    validate_phase_1()
