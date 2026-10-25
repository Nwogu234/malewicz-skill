# malewicz-skill

Transcript fetch helper. Transcripts are third-party content and must never be committed to `main`.

## Task for a cloud session

Download auto-caption transcripts for the 20 videos in `missing-videos.txt` (`videoId|durationSeconds|title` per line).

1. `pip install -r requirements.txt`
2. `mkdir -p transcripts && python scripts/fetch.py missing-videos.txt transcripts/` (skips existing files, retries with backoff, paces requests). Output: `transcripts/<videoId>.txt`, starting with TITLE and URL lines.
3. If everything fails with IpBlocked/RequestBlocked, try `pip install yt-dlp`, then for each video `yt-dlp --skip-download --write-auto-subs --sub-langs en --sub-format vtt -o "transcripts/%(id)s" <url>`. Convert the .vtt to plain text (strip timestamps and tags, dedupe repeated lines) in the same TITLE/URL + text format.
4. Create branch `transcripts-drop` from main, `git add -f transcripts/*.txt` (the folder is gitignored on purpose), commit, and push `transcripts-drop`. Don't commit transcripts to `main`, and don't change other files.

Done = `transcripts-drop` pushed. Report which IDs succeeded and which failed (with the error type). If YouTube blocks this machine too, give up after about 15 minutes of blocking and say so.
