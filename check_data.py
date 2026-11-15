from pathlib import Path

# Find the data folder inside our project
DATA_FOLDER = Path(__file__).resolve().parent / "data"

# Find every .txt file in the data folder
meeting_files = sorted(DATA_FOLDER.glob("*.txt"))

print("=== DecisionTrace AI: Data Validation ===")

# Check that all three meeting files exist
if len(meeting_files) != 3:
    raise ValueError(
        f"Expected 3 meeting files, found {len(meeting_files)}"
    )

# Read each meeting file and validate the content
for file_path in meeting_files:
    content = file_path.read_text(encoding="utf-8")

    if not content.strip():
        raise ValueError(f"{file_path.name} is empty")

    required_sections = ["Meeting Date:", "Decisions:", "Status:"]

    for section in required_sections:
        if section not in content:
            raise ValueError(
                f"{file_path.name} is missing: {section}"
            )

    print(f"PASS: {file_path.name} ({len(content.split())} words)")

print("SUCCESS: All 3 meeting files are valid!")