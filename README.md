Using the CLI:
If using for the first time, run `pip install openai==0.28`. This program uses a feature that is no longer available on the most recent version, so use version 0.28.
1. Replace the `openai.api_key` with the actual key.
2. Make code changes as usual. Stage changes with a standard `git add` command.
3. Run `python cli.py`. This will output a generated commit message. For now, copy the outputted text. It may be truncated.
4. Prepare to commit your changes. Run `git commit` (without the `-m` flag) and a text editor will appear where the copied commit message can be pasted. Save and exit.
5. Push changes as usual with `git push`. 
