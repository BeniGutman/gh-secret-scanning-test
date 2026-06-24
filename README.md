# test-secret-scanning

A throwaway repository for verifying that **GitHub secret scanning** detects
committed credentials.

> ⚠️ **No real secrets live here.** Any credential-looking string in this repo
> is a hand-crafted, format-valid *mock* used solely to trigger GitHub's
> scanner. It maps to no real account, service, or test vector.

## What's inside

- `main.py` — contains mock AWS credentials (`AKIA...` access key ID + a
  40-char secret access key) shaped to match the patterns GitHub's secret
  scanning detects.

## How to run the test

1. Create a GitHub repo and add it as a remote:
   ```bash
   gh repo create test-secret-scanning --private --source=. --remote=origin
   ```
2. Commit and push:
   ```bash
   git add -A && git commit -m "Add mock secret for scanning test"
   git push -u origin main
   ```
3. Observe the result:
   - **Push protection** may block the push at commit time.
   - Otherwise, check **Security → Secret scanning alerts** in the repo.

## Notes

- **Public repos** have secret scanning on by default.
- **Private repos** require GitHub Advanced Security to be enabled
  (Settings → Code security).
- AWS's documented example key (`AKIAIOSFODNN7EXAMPLE`) is intentionally
  **not** used here — GitHub allowlists it, so it would never fire.
