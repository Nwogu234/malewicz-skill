# malewicz-skill

Raw material for a Claude skill on web design and conversion psychology, based on designer Michal Malewicz's YouTube channel (@MalewiczHype).

**This repo is public. Never commit transcripts to it** (they're third-party content). Only paraphrased notes go here.

## Task for a cloud session

### 1. Fetch the transcripts (they stay on this machine only)
`missing-videos.txt` lists 20 videos (`videoId|durationSeconds|title`).

    pip install -r requirements.txt
    mkdir -p transcripts && python scripts/fetch.py missing-videos.txt transcripts/

If everything fails with IpBlocked/RequestBlocked, try `pip install yt-dlp`, then for each video `yt-dlp --skip-download --write-auto-subs --sub-langs en --sub-format vtt -o "transcripts/%(id)s" <url>`, and convert the .vtt to plain text. If YouTube blocks this machine too, give up after about 15 minutes of blocking and say so.

### 2. Extract principles into `extracted/batch2.md`
Read every fetched transcript in full (auto-captions, so expect errors). Merge repeats across videos into one entry that lists all its source IDs. **Paraphrase everything. No quotes longer than a few words.**

For each principle, rule or "do this, not that":

    ### <short name>
    - **Rule:** in your own words
    - **Why (psychology):** how the brain or user reacts, per his reasoning
    - **Apply when designing:** a concrete instruction
    - **Check when auditing:** a yes/no or scored test runnable on a page or screenshot
    - **Example:** a brief example he uses
    - **Sources:** video IDs
    - **Strength:** core (stressed or repeated) or minor

Then add these sections: **Named methods** (with steps), **Anti-patterns**, **Numbers/specifics** (sizes, ratios, colour rules such as 60-30-10, results), and **Off-topic** (one line each). At the top, list the IDs you processed and the IDs that failed.

### 3. Deliver
Create branch `batch2-notes`, commit **only** `extracted/batch2.md` (`git add -f extracted/batch2.md`; the folder is gitignored), and push. Never `git add` the `transcripts/` folder. If you can't push, print the whole of `batch2.md` in your final message instead.
