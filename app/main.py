import argparse
import sys

from config import ConfigError, load_settings
from notion_client import NotionClient, extract_source_text
from prompt_engine import generate_prompt_candidates
from scorer import pick_top_prompts, score_pack


def run_generate() -> int:
    try:
        settings = load_settings()
    except ConfigError as exc:
        print(f"[ERROR] {exc}")
        return 1

    notion = NotionClient(settings.notion_token, settings.notion_db_id)
    pages = notion.fetch_idea_records(limit=10)

    if not pages:
        print("No records found with Status=idea")
        return 0

    print(f"Found {len(pages)} idea records")
    updated = 0

    for page in pages:
        page_id = page.get("id", "")
        source_text = extract_source_text(page)
        prompts = generate_prompt_candidates(source_text, total=12)
        score = score_pack(prompts)
        top_prompts = pick_top_prompts(prompts, top_n=3)

        prompt_pack_text = "\n".join(f"{i + 1}. {prompt}" for i, prompt in enumerate(prompts))
        top_prompt_text = "\n".join(f"{i + 1}. {prompt}" for i, prompt in enumerate(top_prompts))

        notion.update_record(
            page_id=page_id,
            prompt_pack=prompt_pack_text,
            top_prompts=top_prompt_text,
            score=score,
            status="generated",
        )
        updated += 1
        print(f"[OK] Updated page={page_id} score={score}")

    print(f"Done. Updated {updated}/{len(pages)} records.")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Romantic Kitchen Prompt Factory CLI")
    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser("generate", help="Generate prompt packs for idea records")
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command == "generate":
        return run_generate()

    parser.print_help()
    return 1


if __name__ == "__main__":
    sys.exit(main())
