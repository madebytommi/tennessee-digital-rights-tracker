# Discovery state

`seen.json` is durable machine state for the Tennessee Rights Scout. It records source items the scout has already processed so GitHub Issues are not opened twice.

This file is not a Tracker entry, not evidence, and not a publication queue. Humans still decide whether a lead becomes research or a published entry.

Do not store sensitive personal information here. Keep records limited to source URLs, titles, candidate IDs, scores, and issue numbers.

Live GitHub Actions state is stored on the `scout-state` branch, not on protected `main`. The copy in this directory on `main` is a seed for local runs. Do not merge `scout-state` into `main`.
