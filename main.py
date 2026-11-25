"""Write one office-life joke to /output/entry.txt (make.fun program/v1).

The entry is a single line, 1-200 characters, no trailing newline, so the
sealed gate scorer sees exactly one joke and nothing else.
"""

import os

JOKE = (
    "The office plant has survived four rounds of layoffs and two CEOs "
    "\u2014 HR is now asking it to mentor the new hires."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)

    # Gate checks, done before writing anything.
    encoded = JOKE.encode("utf-8")
    assert 1 <= len(JOKE) <= 200, f"joke length {len(JOKE)} outside 1-200"
    assert len(encoded) <= 200, f"joke is {len(encoded)} bytes, over 200"
    assert "\n" not in JOKE and "\r" not in JOKE, "joke must be a single line"
    assert JOKE == JOKE.strip(), "joke must not be only whitespace / padded"

    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(encoded)

    # Read back and confirm the file holds exactly the joke, byte for byte.
    with open(path, "rb") as f:
        assert f.read() == encoded, "entry.txt does not match the joke"


if __name__ == "__main__":
    main()
