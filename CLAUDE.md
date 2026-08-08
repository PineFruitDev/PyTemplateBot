# CLAUDE.md

Orientation for any Claude session working in this repo. Keep it tight; link out rather than inline.

## Project

PyTemplateBot, the Python Discord bot template. discord.py 2.6+, the Python sibling of
[TSTemplateBot](https://github.com/PineFruitDev/TSTemplateBot). Public repo under `PineFruitDev`.

Same architecture as the TypeScript template, deliberately: a command class pattern with
`src/commands/__init__.py` as the single source of truth registry, `src/core/` for the bot and
command manager, `src/services/` for logging and environment validation.

**Keep the two templates conceptually in step.** If you change a pattern here, check whether
TSTemplateBot needs the same change, and say so in the PR. The point of having siblings is that
someone who knows one can read the other.

**Because this is a template, changes propagate by being copied.** Prefer clarity over cleverness
and keep the example commands genuinely exemplary.

## Commands

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python register.py   # register slash commands with Discord
python main.py       # start the bot
```

There is **no test suite and no linter config**. If you add tests, use `pytest` and put them in
`test/`, and add the dependency to `requirements.txt` rather than assuming a global install.

Environment: `DISCORD_TOKEN` (required), `DEVELOPER_IDS` and `ENVIRONMENT` (optional). See
`.env.example`.

## Deploy model (Sparked Host / Pterodactyl)

The PineFruit bots run on a Pterodactyl Python egg where the startup is locked to `git pull`, a
dependency install, then the entrypoint. Consequences:

- **Boot does a `git pull`.** Whatever is on `main` is what runs, so `main` must always be bootable.
- **Secrets live only in the panel**, on the Startup tab or in `/home/container/.env`. Never commit
  a token, and never put a real value in `.env.example`.
- Registration here is a **separate step** (`register.py`), not automatic on boot. VoiceLoungeBot
  (TypeScript) self-registers on boot instead. If you make this template self-register, copy that
  approach rather than inventing a third one.

## Licensing (read this before assuming)

This repo is **MIT**, not Apache 2.0 with the Commons Clause. That is out of step with the rest of
the public PineFruit set (`TSTemplateBot`, `VoiceLoungeBot`, `Free-Verse` are all Apache 2.0 plus
Commons Clause, which permits use and forking but forbids selling the library itself).

**MIT permits selling.** If the "use, fork, do not sell" intent is meant to apply here, the LICENSE
file has to change; documenting the intent is not enough. Do not relicense on your own initiative,
and do not describe this repo as "no selling" while the MIT text says otherwise. Raise it with Sky.

Branch protection on `main`: PR required, admins included, zero approvals needed.

## House rules

- **Never commit to `main`.** Branch, open a PR, squash-merge with `--delete-branch`. This holds for
  one-line doc fixes too.
- **No em dashes** anywhere: code, comments, docs, commit messages, PR bodies, UI strings, embed
  copy. Use a comma, a colon, or parentheses.
- **No AI-collaboration tells.** No `Co-Authored-By` trailer, no "Generated with", no mention of
  Claude or any assistant in commit messages, PR bodies, code comments, or docs. This repo is public
  and part of Sky's portfolio; it reads as his own work.
- **Check the other repos before building something new.** `TSTemplateBot` is the sibling,
  `ServerTagRewardBot` exists in both Python and TypeScript form. Prior art is the norm here, not
  the exception.
- Stage explicit paths. No `git add -A` and no `git add .`.

## Constraints

- Do not commit secrets or a populated `.env`.
- Do not add product-specific features here. Anything only one bot needs belongs in that bot.
- Do not let the Python and TypeScript templates drift apart silently.
