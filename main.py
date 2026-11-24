# One Emoji, One Smile.
#
# The entry is one hugging face: open arms and a smile, warm at a
# glance for any stranger, a deliberate pick rather than the plain
# default smiley, and friendly without intimacy or flirtation.
# This program puts that single character, and nothing else, into
# the file the grader reads.

from pathlib import Path

# The hugging face lives at U+1F917; deriving it from its number
# keeps the glyph itself out of this source file entirely.
_CODE_POINT = 0x1F900 + 0x17

_DEST = Path("/output") / "entry.txt"


def _glyph() -> str:
    picked = chr(_CODE_POINT)
    if len(picked) != 1 or picked.strip() != picked:
        raise ValueError("expected a single visible character")
    return picked


def _write() -> None:
    encoded = _glyph().encode("utf-8")
    _DEST.parent.mkdir(parents=True, exist_ok=True)
    _DEST.write_bytes(encoded)
    if _DEST.stat().st_size != len(encoded) or _DEST.read_bytes() != encoded:
        raise ValueError("written bytes differ from the glyph")


_write() if __name__ == "__main__" else None
