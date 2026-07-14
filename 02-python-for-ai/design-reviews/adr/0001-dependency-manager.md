# ADR-0001: Standardize on uv for Python Environments & Packaging

- **Status:** Accepted
- **Date:** 2026-01-01
- **Deciders:** AI Platform Engineer (you)
- **Difficulty context:** `A`

## Context
Our AI services need reproducible Python environments across dev, CI, and production, including the fragile `torch`/CUDA chain. We must pick a standard env/dependency tool for the handbook and the platform. Inconsistent tooling across teams causes irreproducible builds and slow CI.

## Decision Drivers
- Reproducibility (lockfiles with the full resolved tree).
- Speed (dependency resolution + install time in CI).
- Compatibility with the `pip`/PyPI ecosystem and torch CUDA wheels.
- Simplicity of the toolchain (fewer moving parts).
- Ability to handle occasional non-Python/system libs.

## Options Considered
### Option A — uv
- **Pros:** extremely fast resolves/installs; native lockfile; pip-compatible; single static binary; great in Docker layer caching.
- **Cons:** newer; smaller (but rapidly growing) track record.

### Option B — poetry
- **Pros:** mature; nice UX; lockfile; widely used.
- **Cons:** slower resolves; heavier; occasional friction with torch index URLs.

### Option C — pip + venv + pip-tools
- **Pros:** ubiquitous; minimal; transparent.
- **Cons:** manual locking; more custom scripting; slower.

### Option D — conda/mamba
- **Pros:** manages non-Python + CUDA system libraries.
- **Cons:** heavy, slow, large images; overkill unless we need system-level scientific libs.

## Decision
**Standardize on `uv`** as the default env/dependency/packaging tool, with committed `uv.lock`. Pin `torch` to an explicit CUDA build. Reserve **conda** for the rare service that genuinely needs system-level scientific/CUDA libraries `pip` can't provide.

## Consequences
- **Positive:** fast, reproducible CI; small cache-friendly images; one tool to teach.
- **Negative / debt:** dependence on a younger tool; teams familiar with poetry need a short ramp.
- **Follow-ups:** enable hash-locked installs + CVE scanning in CI (Module 30); define the CUDA base image standard (Module 20).

## Validation
CI builds are reproducible from `uv.lock`; a clean machine can `uv sync --frozen` to an identical env. Docker dependency layers cache across code-only changes. Revisit if uv blocks a required use case or if a platform standard changes.
