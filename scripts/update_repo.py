#!/usr/bin/env python3
"""Fetch latest HD2 catalog, convert to Markdown, commit changed files and push.

The first run can initialize this directory as a git repository; create the EMPTY
remote GitHub repository first. Later runs fast-forward before syncing to avoid
clobbering changes made on GitHub/GitHub Actions.
"""
from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_REMOTE = 'https://github.com/shenjiaqi8/hd2-knowledge-base.git'


def git(*args: str, check: bool = True) -> subprocess.CompletedProcess:
    proc = subprocess.run(['git', *args], cwd=ROOT, capture_output=True, text=True, encoding='utf-8', errors='replace')
    if check and proc.returncode:
        raise RuntimeError(f'git {" ".join(args)} failed ({proc.returncode}):\n{proc.stderr.strip() or proc.stdout.strip()}')
    return proc


def have_commit() -> bool:
    return git('rev-parse', '--verify', 'HEAD', check=False).returncode == 0


def ensure_git(url: str) -> None:
    if not shutil.which('git'):
        raise RuntimeError('Git is not installed or not found in PATH. Please install Git for Windows / git.')
    if git('rev-parse', '--is-inside-work-tree', check=False).returncode != 0:
        git('init', '-b', 'main')
        print('Initialized local git repository.')
    toplevel = Path(git('rev-parse', '--show-toplevel').stdout.strip()).resolve()
    if toplevel != ROOT.resolve():
        raise RuntimeError(f'This folder is nested inside a different git repo: {toplevel}. Move it outside to avoid changing another project.')
    origin = git('remote', 'get-url', 'origin', check=False)
    if origin.returncode:
        git('remote', 'add', 'origin', url)
    elif origin.stdout.strip().removesuffix('.git') != url.removesuffix('.git'):
        raise RuntimeError(f'Existing origin points elsewhere: {origin.stdout.strip()}\nExpected: {url}\nRefusing to change origin automatically.')
    branch = git('branch', '--show-current').stdout.strip()
    if branch and branch != 'main':
        raise RuntimeError(f'Current branch is {branch!r}, but expected main. Switch to main first.')


def prepare_remote() -> None:
    # Distinguish an empty repository from a missing/inaccessible remote.
    check = git('ls-remote', 'origin', 'HEAD', check=False)
    if check.returncode:
        raise RuntimeError('Unable to contact GitHub repository. Create an EMPTY repository at '\
                           'https://github.com/new with the name hd2-knowledge-base, '\
                           'then authenticate Git before retrying.\n' + check.stderr.strip())
    remote_ref = git('ls-remote', '--heads', 'origin', 'main', check=False)
    if remote_ref.returncode:
        raise RuntimeError(remote_ref.stderr.strip())
    if remote_ref.stdout.strip():
        if not have_commit():
            raise RuntimeError('Remote main is not empty but this folder has no local history. '\
                               'Clone your existing repository then copy this starter into it; do not overwrite history.')
        status = git('status', '--porcelain').stdout.strip()
        if status:
            raise RuntimeError('Local uncommitted changes exist; commit or stash them before updating from GitHub. '\
                               'This protects personal notes from accidental overwrites.')
        git('pull', '--ff-only', 'origin', 'main')
    else:
        if have_commit():
            print('Remote main is empty; first push will publish local history.')


def ensure_identity() -> None:
    if git('config', 'user.name', check=False).returncode:
        git('config', 'user.name', 'HD2 Knowledge Sync')
    if git('config', 'user.email', check=False).returncode:
        git('config', 'user.email', 'hd2-sync@users.noreply.github.com')


def main():
    parser = argparse.ArgumentParser(description='Update Markdown and push changed files to GitHub.')
    parser.add_argument('--scope', choices=['gameplay', 'all'], default='gameplay')
    parser.add_argument('--remote', default=DEFAULT_REMOTE)
    parser.add_argument('--no-push', action='store_true')
    args = parser.parse_args()
    ensure_git(args.remote)
    if not args.no_push:
        prepare_remote()
    command = [sys.executable, str(ROOT / 'scripts' / 'hd2_to_markdown.py'),
               '--out', str(ROOT / 'knowledge'), '--scope', args.scope,
               '--aliases-csv', str(ROOT / 'config' / 'aliases_zh.csv')]
    print('Fetching source data and regenerating Markdown...', flush=True)
    proc = subprocess.run(command, cwd=ROOT)
    if proc.returncode:
        raise RuntimeError(f'Collector failed ({proc.returncode}). No changes will be committed or pushed.')

    # Protect already-staged unrelated changes from accidental commits.
    if git('diff', '--cached', '--name-only').stdout.strip():
        raise RuntimeError('There are already staged git changes. Commit/unstage them first to avoid mixing unrelated files.')
    # First commit includes workflow/scripts/docs; subsequent commits touch only knowledge/.
    if have_commit():
        git('add', '-A', '--', 'knowledge')
    else:
        git('add', '-A', '--', '.')
    if git('diff', '--cached', '--quiet', check=False).returncode == 0:
        print('Knowledge base is unchanged; no commit or push required.')
        return
    ensure_identity()
    git('commit', '-m', 'Update HD2 Markdown knowledge base')
    if args.no_push:
        print('Committed locally (push disabled).')
    else:
        git('push', '-u', 'origin', 'main')
        print('Pushed to GitHub. AstrBot will pick up changed Markdown on its next sync check.')


if __name__ == '__main__':
    try:
        main()
    except (RuntimeError, OSError) as exc:
        print('ERROR:', exc, file=sys.stderr)
        sys.exit(1)
