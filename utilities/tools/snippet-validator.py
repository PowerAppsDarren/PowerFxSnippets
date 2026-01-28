#!/usr/bin/env python3
"""
T010: Snippet Validator
Validates YAML frontmatter in markdown snippet files.

Usage:
    python snippet-validator.py <file_path>
    python snippet-validator.py --help

Exit codes:
    0 - Valid frontmatter
    1 - Invalid frontmatter or error
"""

import argparse
import re
import sys
from datetime import datetime
from pathlib import Path
from typing import NamedTuple

import yaml


class ValidationError(NamedTuple):
    """Represents a validation error with context."""
    file_path: str
    line_number: int | None
    field: str
    message: str


# Required frontmatter fields
REQUIRED_FIELDS = [
    "title",
    "description",
    "category",
    "subcategory",
    "tags",
    "difficulty",
    "products",
    "author",
    "created",
    "updated",
]

# Valid difficulty levels
VALID_DIFFICULTIES = ["beginner", "intermediate", "advanced"]

# ISO date format regex
ISO_DATE_PATTERN = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def extract_frontmatter(content: str) -> tuple[dict | None, int, int]:
    """
    Extract YAML frontmatter from markdown content.

    Returns:
        Tuple of (frontmatter_dict, start_line, end_line) or (None, 0, 0) if not found.
    """
    lines = content.split("\n")

    # Check for opening ---
    if not lines or lines[0].strip() != "---":
        return None, 0, 0

    # Find closing ---
    end_index = -1
    for i, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            end_index = i
            break

    if end_index == -1:
        return None, 0, 0

    # Extract and parse YAML
    yaml_content = "\n".join(lines[1:end_index])
    try:
        frontmatter = yaml.safe_load(yaml_content)
        return frontmatter, 1, end_index + 1
    except yaml.YAMLError:
        return None, 1, end_index + 1


def find_field_line(content: str, field: str, start_line: int, end_line: int) -> int | None:
    """Find the line number where a field is defined in frontmatter."""
    lines = content.split("\n")
    pattern = re.compile(rf"^{re.escape(field)}:")

    for i, line in enumerate(lines[start_line:end_line], start=start_line + 1):
        if pattern.match(line):
            return i
    return None


def validate_frontmatter(
    file_path: Path,
    frontmatter: dict,
    content: str,
    start_line: int,
    end_line: int
) -> list[ValidationError]:
    """
    Validate frontmatter against required schema.

    Returns:
        List of ValidationError objects.
    """
    errors: list[ValidationError] = []
    file_str = str(file_path)

    # Check for required fields
    for field in REQUIRED_FIELDS:
        if field not in frontmatter or frontmatter[field] is None:
            errors.append(ValidationError(
                file_path=file_str,
                line_number=start_line,
                field=field,
                message=f"Missing required field: {field}"
            ))

    # If we're missing required fields, some validations can't proceed
    if not frontmatter:
        return errors

    # Validate difficulty
    if "difficulty" in frontmatter and frontmatter["difficulty"] is not None:
        difficulty = frontmatter["difficulty"]
        if difficulty not in VALID_DIFFICULTIES:
            line_num = find_field_line(content, "difficulty", start_line, end_line)
            errors.append(ValidationError(
                file_path=file_str,
                line_number=line_num,
                field="difficulty",
                message=f"Invalid difficulty '{difficulty}'. Must be one of: {', '.join(VALID_DIFFICULTIES)}"
            ))

    # Validate tags is an array
    if "tags" in frontmatter and frontmatter["tags"] is not None:
        if not isinstance(frontmatter["tags"], list):
            line_num = find_field_line(content, "tags", start_line, end_line)
            errors.append(ValidationError(
                file_path=file_str,
                line_number=line_num,
                field="tags",
                message="Tags must be an array/list"
            ))

    # Validate products is an array
    if "products" in frontmatter and frontmatter["products"] is not None:
        if not isinstance(frontmatter["products"], list):
            line_num = find_field_line(content, "products", start_line, end_line)
            errors.append(ValidationError(
                file_path=file_str,
                line_number=line_num,
                field="products",
                message="Products must be an array/list"
            ))

    # Validate date fields (ISO format YYYY-MM-DD)
    for date_field in ["created", "updated"]:
        if date_field in frontmatter and frontmatter[date_field] is not None:
            date_value = frontmatter[date_field]
            line_num = find_field_line(content, date_field, start_line, end_line)

            # Handle datetime.date objects from YAML parser
            if isinstance(date_value, datetime):
                date_str = date_value.strftime("%Y-%m-%d")
            elif hasattr(date_value, 'isoformat'):  # datetime.date
                date_str = date_value.isoformat()
            else:
                date_str = str(date_value)

            if not ISO_DATE_PATTERN.match(date_str):
                errors.append(ValidationError(
                    file_path=file_str,
                    line_number=line_num,
                    field=date_field,
                    message=f"Invalid date format '{date_value}'. Must be ISO format (YYYY-MM-DD)"
                ))
            else:
                # Validate it's a real date
                try:
                    datetime.strptime(date_str, "%Y-%m-%d")
                except ValueError:
                    errors.append(ValidationError(
                        file_path=file_str,
                        line_number=line_num,
                        field=date_field,
                        message=f"Invalid date '{date_value}'. Not a valid calendar date."
                    ))

    # Validate title and description are non-empty strings
    for str_field in ["title", "description", "category", "subcategory", "author"]:
        if str_field in frontmatter and frontmatter[str_field] is not None:
            value = frontmatter[str_field]
            if not isinstance(value, str) or not value.strip():
                line_num = find_field_line(content, str_field, start_line, end_line)
                errors.append(ValidationError(
                    file_path=file_str,
                    line_number=line_num,
                    field=str_field,
                    message=f"Field '{str_field}' must be a non-empty string"
                ))

    return errors


def validate_file(file_path: Path) -> list[ValidationError]:
    """
    Validate a single markdown file's frontmatter.

    Returns:
        List of ValidationError objects.
    """
    errors: list[ValidationError] = []
    file_str = str(file_path)

    # Check file exists
    if not file_path.exists():
        errors.append(ValidationError(
            file_path=file_str,
            line_number=None,
            field="file",
            message="File does not exist"
        ))
        return errors

    # Check it's a markdown file
    if file_path.suffix.lower() not in [".md", ".markdown"]:
        errors.append(ValidationError(
            file_path=file_str,
            line_number=None,
            field="file",
            message="Not a markdown file"
        ))
        return errors

    # Read content
    try:
        content = file_path.read_text(encoding="utf-8")
    except Exception as e:
        errors.append(ValidationError(
            file_path=file_str,
            line_number=None,
            field="file",
            message=f"Could not read file: {e}"
        ))
        return errors

    # Extract frontmatter
    frontmatter, start_line, end_line = extract_frontmatter(content)

    if frontmatter is None:
        errors.append(ValidationError(
            file_path=file_str,
            line_number=1,
            field="frontmatter",
            message="No valid YAML frontmatter found. File must start with '---' delimiter."
        ))
        return errors

    # Validate frontmatter
    errors.extend(validate_frontmatter(file_path, frontmatter, content, start_line, end_line))

    return errors


def format_error(error: ValidationError) -> str:
    """Format a validation error for display."""
    location = f"{error.file_path}"
    if error.line_number:
        location += f":{error.line_number}"
    return f"  {location}: [{error.field}] {error.message}"


def validate_directory(directory: Path) -> tuple[list[ValidationError], int, int]:
    """
    Validate all markdown files in a directory recursively.
    Skips README.md files as they are documentation, not snippets.

    Returns:
        Tuple of (all_errors, total_files, passed_files)
    """
    all_errors: list[ValidationError] = []
    total_files = 0
    passed_files = 0

    for md_file in directory.rglob("*.md"):
        if md_file.name.lower() == "readme.md":
            continue  # Skip README files
        total_files += 1
        errors = validate_file(md_file)
        if errors:
            all_errors.extend(errors)
        else:
            passed_files += 1

    return all_errors, total_files, passed_files


def main() -> int:
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Validate YAML frontmatter in markdown snippet files.",
        epilog="""
Exit codes:
  0 - All validations passed
  1 - Validation failures or errors

Required frontmatter fields:
  title, description, category, subcategory, tags, difficulty,
  products, author, created, updated

Validation rules:
  - difficulty: must be beginner, intermediate, or advanced
  - tags: must be an array
  - products: must be an array
  - created/updated: must be ISO format (YYYY-MM-DD)
        """
    )
    parser.add_argument(
        "file_path",
        type=Path,
        nargs="?",
        help="Path to the markdown file to validate (or directory if --batch)"
    )
    parser.add_argument(
        "--batch",
        action="store_true",
        help="Batch validate all .md files in the specified directory recursively"
    )
    parser.add_argument(
        "-q", "--quiet",
        action="store_true",
        help="Suppress output, only set exit code"
    )
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Show verbose output including success messages"
    )

    args = parser.parse_args()

    if args.batch:
        if not args.file_path:
            print("Error: --batch requires a directory path")
            return 1
        if not args.file_path.is_dir():
            print(f"Error: {args.file_path} is not a directory")
            return 1

        errors, total_files, passed_files = validate_directory(args.file_path)

        if errors:
            if not args.quiet:
                print(f"Batch validation FAILED for: {args.file_path}")
                print(f"Total files: {total_files}, Passed: {passed_files}, Failed: {total_files - passed_files}")
                print(f"Found {len(errors)} error(s):")
                for error in errors:
                    print(format_error(error))
            return 1
        else:
            if not args.quiet:
                print(f"Batch validation PASSED for: {args.file_path}")
                print(f"All {total_files} files passed validation.")
            return 0
    else:
        if not args.file_path:
            parser.print_help()
            return 1

        errors = validate_file(args.file_path)

        if errors:
            if not args.quiet:
                print(f"Validation FAILED for: {args.file_path}")
                print(f"Found {len(errors)} error(s):")
                for error in errors:
                    print(format_error(error))
            return 1
        else:
            if args.verbose and not args.quiet:
                print(f"Validation PASSED for: {args.file_path}")
            return 0


if __name__ == "__main__":
    sys.exit(main())
