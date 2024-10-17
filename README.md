Using the CLI:
If using for the first time, run `pip install openai==0.28`. This program uses a feature that is no longer available on the most recent version, so use version 0.28.
Also, you'll need to create a file called `.env` that stores our private keys. Create a version of this file in your local repo. Copy and paste this line of code: `OPENAI_API_KEY=[insert Edward's key here]` where you should replace the right side of the equals symbol with the actual key. This .env file should only contain this single line of code for now.
If you're wondering, the .gitignore lists the .env file, so it will never be committed to the remote repo. It stays in your local repo so you can run and test locally.

Now, for the usual steps:
1. Make code changes as usual. Stage changes with a standard `git add` command.
2.  Run `python cli.py`. This will generate a commit message (current token limit is 500) and **automatically** run `git commit -m` for you, including this generated message. The commit message is displayed to the terminal for your reference.
3.  Push changes as usual with `git push`. 
