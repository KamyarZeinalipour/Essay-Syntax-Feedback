"""Generate syntax feedback for a CSV of student essays with an OpenAI model.

    OPENAI_API_KEY=... python data_generation/generate_feedback.py essays.csv feedback.csv

The input CSV needs an `essay` column. Progress is saved after every row, so the command can be
re-run to resume. This is how the Essay-Syntax-Instruct dataset was built (GPT-3.5-Turbo,
temperature 0.35).
"""
import argparse
import os
import time
from pathlib import Path

import pandas as pd
from openai import OpenAI
from tqdm.auto import tqdm

from prompts import SYNTAX_FEEDBACK_PROMPT


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("input", help="CSV with an `essay` column.")
    p.add_argument("output")
    p.add_argument("--model", default="gpt-3.5-turbo-0125")
    p.add_argument("--temperature", type=float, default=0.35)
    args = p.parse_args()

    key = os.getenv("OPENAI_API_KEY")
    if not key:
        raise SystemExit("Set OPENAI_API_KEY in your environment (see .env.example).")
    client = OpenAI(api_key=key)

    out = Path(args.output)
    df = pd.read_csv(out if out.exists() else args.input)
    if "feedback" not in df.columns:
        df["feedback"] = None

    for i in tqdm(df.index[df["feedback"].isna()], desc="feedback"):
        prompt = SYNTAX_FEEDBACK_PROMPT.format(essay=df.at[i, "essay"])
        for attempt in range(3):
            try:
                reply = client.chat.completions.create(
                    model=args.model,
                    messages=[{"role": "user", "content": prompt}],
                    temperature=args.temperature,
                )
                df.at[i, "feedback"] = reply.choices[0].message.content
                break
            except Exception as exc:
                print(f"row {i}: {exc}")
                time.sleep(20 * (attempt + 1))
        df.to_csv(out, index=False)
    print(f"Saved {out}")


if __name__ == "__main__":
    main()
