# git_scripts/git_history_analyzer.py

import subprocess
from datetime import datetime

class GitHistoryAnalyzer:
    def __init__(self):
        pass

    def filter_commits(self, change_type=None, impact_area=None, author=None):
        try:
            cmd = ["git", "log", "--pretty=format:%H|%s|%an|%ad", "--date=iso"]
            response = subprocess.run(cmd, capture_output=True, text=True, check=True)
            commits = response.stdout.strip().split('\n')
            filtered = []
            for commit in commits:
                commit_hash, subject, commit_author, commit_date = commit.split('|')
                if change_type and change_type not in subject:
                    continue
                if impact_area and impact_area not in subject:
                    continue
                if author and author != commit_author:
                    continue
                filtered.append({
                    'hash': commit_hash,
                    'subject': subject,
                    'author': commit_author,
                    'date': datetime.fromisoformat(commit_date)
                })
            return filtered
        except subprocess.CalledProcessError as e:
            print(f"Error running git log: {e}")
            return []
        except Exception as e:
            print(f"Unexpected error in filter_commits: {e}")
            return []

    def search_commits(self, keyword):
        try:
            cmd = ["git", "log", "--grep", keyword, "--pretty=format:%H|%s|%an|%ad", "--date=iso"]
            response = subprocess.run(cmd, capture_output=True, text=True, check=True)
            commits = response.stdout.strip().split('\n')
            results = []
            for commit in commits:
                commit_hash, subject, commit_author, commit_date = commit.split('|')
                results.append({
                    'hash': commit_hash,
                    'subject': subject,
                    'author': commit_author,
                    'date': datetime.fromisoformat(commit_date)
                })
            return results
        except subprocess.CalledProcessError as e:
            print(f"Error searching commits: {e}")
            return []
        except Exception as e:
            print(f"Unexpected error in search_commits: {e}")
            return []
