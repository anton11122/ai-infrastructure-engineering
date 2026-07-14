# AI Infrastructure Engineering — The Complete Handbook

> A living engineering curriculum that transforms an experienced **Senior DevOps Engineer** into a **world-class AI Infrastructure / Platform Engineer** capable of designing, building, deploying, securing, scaling, and operating enterprise-grade AI platforms.
>
> Equivalent scope: a Master's degree **plus** several years of production AI-platform experience, delivered as a hands-on, project-driven repository.

---

## Who This Is For

This handbook assumes you are **already an expert** in the following, and it deliberately **leverages** these skills instead of reteaching them:

`Linux` · `Kubernetes` · `Docker` · `Terraform` · `AWS` · `CI/CD` · `GitOps` · `Networking` · `Security` · `Monitoring` · `Platform Engineering`

It assumes **zero prior AI/ML knowledge** and teaches every AI concept from first principles.

**Target outcome:** be hireable and effective as an AI Infrastructure Engineer at companies such as OpenAI, Anthropic, Google DeepMind, NVIDIA, Meta, Microsoft, Amazon, Databricks, Snowflake, Cloudflare, Scale AI, HuggingFace, Cohere, Mistral, xAI — or building enterprise AI platforms internally.

---

## How To Use This Repository

This repository is your **permanent learning operating system**. Treat it like a codebase you own and continuously improve.

1. **Start at [`/00-roadmap`](./00-roadmap/README.md).** Read the roadmap, the [knowledge graph](./00-roadmap/knowledge-graph.md), and pick a [learning path](./00-roadmap/learning-paths.md).
2. **Work one module at a time.** Do not skip. Each module builds on prior ones per the dependency graph.
3. **80% hands-on / 20% theory.** Read the theory, then live in the labs and projects.
4. **Prove mastery.** Every module ends with a practical exam, system-design interview, troubleshooting interview, code review, and a production incident.
5. **Evolve the projects.** Every project ships in versions: `v1 → v2 → v3 → enterprise → cloud → HA → multi-region → production`.
6. **Capstone.** The entire curriculum culminates in building a complete enterprise AI platform.

> **Learning philosophy:** Always understand **WHY before HOW**. Compare technologies, weigh trade-offs, study failure modes, and design for scale, security, cost, and operability.

---

## Curriculum Map (40 Modules)

| # | Module | Track |
|---|--------|-------|
| 00 | [Roadmap](./00-roadmap/) | Orientation |
| 01 | AI Foundations | Foundations |
| 02 | Python for AI | Foundations |
| 03 | Machine Learning Fundamentals | Foundations |
| 04 | Deep Learning | Foundations |
| 05 | Transformers | Core AI |
| 06 | LLMs | Core AI |
| 07 | Prompt Engineering | Core AI |
| 08 | Embeddings | Core AI |
| 09 | Vector Databases | Data & Retrieval |
| 10 | RAG | Data & Retrieval |
| 11 | Agentic AI | Agents |
| 12 | MCP (Model Context Protocol) | Agents |
| 13 | LangChain | Agents |
| 14 | LangGraph | Agents |
| 15 | CrewAI | Agents |
| 16 | AutoGen | Agents |
| 17 | AI Evaluation | Quality |
| 18 | LLMOps | Operations |
| 19 | Model Serving | Serving |
| 20 | GPU Infrastructure | Infrastructure |
| 21 | Kubernetes for AI | Infrastructure |
| 22 | Ray | Distributed |
| 23 | KServe | Serving |
| 24 | vLLM | Serving |
| 25 | SGLang | Serving |
| 26 | Triton Inference Server | Serving |
| 27 | TensorRT-LLM | Serving |
| 28 | Distributed Inference | Distributed |
| 29 | AI Observability | Operations |
| 30 | AI Security | Governance |
| 31 | AI Platform Engineering | Platform |
| 32 | Enterprise Architecture | Platform |
| 33 | Cloud AI | Cloud |
| 34 | AWS Bedrock | Cloud |
| 35 | GCP Vertex AI | Cloud |
| 36 | Azure AI | Cloud |
| 37 | Multi-Agent Platforms | Agents |
| 38 | Capstone Projects | Capstone |
| 39 | Interview Preparation | Career |
| 40 | Career Growth | Career |

Full descriptions, objectives, and dependencies: **[Module Catalog](./00-roadmap/module-catalog.md)**.

---

## What Every Module Contains

Each module folder is self-contained and follows a strict structure (see the [Module Template](./00-roadmap/templates/module-template.md)):

```
NN-module-name/
├── README.md            # objectives, background, theory, WHY→HOW
├── theory/              # first-principles explanations + diagrams
├── labs/                # hands-on labs (objective→cleanup)
├── projects/            # mini + large production projects (versioned)
├── design-reviews/      # architecture reviews & ADRs
├── assessments/         # quizzes, exams, interviews, incidents
├── references/          # papers, repos, books, videos, RFCs, benchmarks
├── troubleshooting.md   # symptoms → root cause → fix
├── best-practices.md
├── common-pitfalls.md
└── checklists.md
```

Every module produces: learning objectives, theory, architecture, production use cases, code, labs, mini + large projects, design review, interview questions, troubleshooting, best practices, pitfalls, performance tuning, security, cost optimization, scaling, further reading, and a final exam.

---

## Difficulty Ladder

Every lesson is tagged with a level so you can calibrate depth: **Beginner → Intermediate → Advanced → Expert → Staff Engineer → Principal Engineer**. See the [Difficulty Levels guide](./00-roadmap/difficulty-levels.md).

---

## The Capstone

The curriculum culminates in a **complete enterprise AI platform** integrating: Kubernetes + GPU scheduling, vLLM/SGLang/TensorRT-LLM, Ray, KServe, MLflow, LangSmith, LangFuse, Arize Phoenix, vector databases, RAG, multi-agent systems, an AI gateway, MCP servers, authN/authZ, observability, autoscaling, cost optimization, DR, multi-region, GitOps, CI/CD, security, monitoring, and benchmarking. See [`/38-capstone-projects`](./38-capstone-projects/).

---

## Build Status & Roadmap Progress

This repository is built in **iterative phases**. Content is generated one module at a time and previous modules are continuously improved.

- **Phase 1 — Architecture & Roadmap:** ✅ In this commit.
- **Phase 2 — Module-by-module build:** ⏳ Begins after approval, starting with `01-ai-foundations`.

Progress tracker: **[`/00-roadmap/progress.md`](./00-roadmap/progress.md)**.

---

## Repository Conventions

- **Docs:** Markdown, with Mermaid diagrams for every architecture, flow, sequence, network, and cluster view.
- **IaC:** Terraform for cloud, Helm/Kustomize + GitOps (Argo CD/Flux) for Kubernetes.
- **Labs:** reproducible, with explicit prerequisites, validation, expected output, failure scenarios, and cleanup.
- **Cost safety:** every cloud/GPU lab lists estimated cost and a mandatory teardown step.

---

## License & Contributions

See [`CONTRIBUTING.md`](./CONTRIBUTING.md) for how modules are structured and improved over time. This is a living handbook — issues and improvements are expected as the ecosystem evolves.
