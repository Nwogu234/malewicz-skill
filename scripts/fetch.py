import sys, time, random, pathlib
from youtube_transcript_api import YouTubeTranscriptApi as A
lst, out = sys.argv[1], pathlib.Path(sys.argv[2])
api = A()
for line in open(lst):
    vid, dur, title = line.rstrip("\n").split("|", 2)
    f = out / f"{vid}.txt"
    if f.exists(): continue
    for attempt in range(5):
        try:
            t = api.fetch(vid)
            f.write_text(f"TITLE: {title}\nURL: https://www.youtube.com/watch?v={vid}\n\n" + " ".join(s.text for s in t))
            print("ok", vid, title, flush=True); break
        except Exception as e:
            wait = 60 * (attempt + 1)
            print("fail", vid, type(e).__name__, "retry in", wait, flush=True); time.sleep(wait)
    time.sleep(random.uniform(8, 15))
print("DONE", flush=True)
