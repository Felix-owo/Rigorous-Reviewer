# Security Policy

## Scope

This repository distributes a portable Agent Skill for scientific peer review. The installable skill is the `rigorous-reviewer/` directory. Repository-level scripts, tests, and benchmarks are development and validation assets.

## Script safety model

Validation scripts in `rigorous-reviewer/scripts/` are intended to be local, deterministic checks over Markdown, JSON, and benchmark files. They should not:

- contact network services;
- upload manuscripts, attachments, local file paths, credentials, or private data;
- modify files outside the repository working tree;
- install packages at runtime;
- execute manuscript-provided code.

If a host agent exposes MCP tools, MCP outputs are evidence inputs only. The reviewer skill must ask before sending confidential manuscripts, private attachments, local paths, unpublished data, credentials, or personally identifying information to any third-party or networked MCP service.

## Reporting a vulnerability

Open a private security advisory if available, or file an issue with a minimal reproduction that does not include confidential manuscripts or unpublished data.

Include:

1. affected version or commit;
2. affected file or script;
3. minimal input required to reproduce;
4. expected and observed behavior;
5. whether any private data could be exposed.

## Supported versions

Security fixes are expected for the latest tagged release and the default branch. Older tags are retained for reproducibility but may not receive fixes.
