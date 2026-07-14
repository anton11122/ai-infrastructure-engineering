# 00 — Roadmap & Learning Operating System

This is the control center for the entire handbook. Everything about **what to learn, in what order, to what depth, and how it's assessed** lives here.

---

## Documents In This Folder

| Document | Purpose |
|----------|---------|
| [`module-catalog.md`](./module-catalog.md) | Every one of the 40 modules: objective, background, key skills, dependencies, project. |
| [`knowledge-graph.md`](./knowledge-graph.md) | Mermaid dependency graphs: what must be learned first, critical path, optional/advanced/expert paths. |
| [`learning-paths.md`](./learning-paths.md) | Curated routes (Fast Track, Serving Specialist, Platform Architect, Agents Specialist, Full Master). |
| [`difficulty-levels.md`](./difficulty-levels.md) | The six-level ladder from Beginner to Principal Engineer, with per-level expectations. |
| [`assessment-framework.md`](./assessment-framework.md) | How each module is evaluated: exams, interviews, code reviews, incidents. |
| [`progress.md`](./progress.md) | Living build + personal-progress tracker. |
| [`templates/`](./templates/) | Canonical module, lab, project, ADR, and assessment templates. |

---

## The 12–18 Month Plan

This curriculum is designed as a **12–18 month** deep program (≈10–15 hrs/week). It is organized into six phases that map onto the modules.

```mermaid
gantt
    title AI Infrastructure Engineer — 12–18 Month Program
    dateFormat  YYYY-MM-DD
    axisFormat  %b

    section Phase 1: Foundations
    01 AI Foundations            :p1a, 2026-01-01, 20d
    02 Python for AI             :p1b, after p1a, 20d
    03 ML Fundamentals           :p1c, after p1b, 25d
    04 Deep Learning             :p1d, after p1c, 30d

    section Phase 2: Core AI
    05 Transformers              :p2a, after p1d, 20d
    06 LLMs                      :p2b, after p2a, 25d
    07 Prompt Engineering        :p2c, after p2b, 12d
    08 Embeddings                :p2d, after p2c, 12d

    section Phase 3: Data, RAG & Agents
    09 Vector Databases          :p3a, after p2d, 15d
    10 RAG                       :p3b, after p3a, 20d
    11-16 Agents & MCP           :p3c, after p3b, 45d
    17 AI Evaluation             :p3d, after p3c, 15d

    section Phase 4: Serving & Infra
    18 LLMOps                    :p4a, after p3d, 15d
    19 Model Serving             :p4b, after p4a, 15d
    20 GPU Infrastructure        :p4c, after p4b, 20d
    21 K8s for AI                :p4d, after p4c, 20d
    22-28 Ray/KServe/vLLM/...    :p4e, after p4d, 60d

    section Phase 5: Ops, Security, Platform
    29 Observability             :p5a, after p4e, 15d
    30 AI Security               :p5b, after p5a, 20d
    31 Platform Engineering      :p5c, after p5b, 25d
    32 Enterprise Architecture   :p5d, after p5c, 20d
    33-37 Cloud & Multi-Agent    :p5e, after p5d, 40d

    section Phase 6: Capstone & Career
    38 Capstone                  :p6a, after p5e, 45d
    39 Interview Prep            :p6b, after p6a, 15d
    40 Career Growth             :p6c, after p6b, 10d
```

---

## Phase Overview

| Phase | Modules | Theme | Outcome |
|-------|---------|-------|---------|
| **1. Foundations** | 01–04 | Speak AI/ML fluently; understand tensors, training, DL. | Can read papers and reason about models. |
| **2. Core AI** | 05–08 | Transformers, LLMs, prompting, embeddings. | Understand how modern models work end-to-end. |
| **3. Data, RAG & Agents** | 09–17 | Vector DBs, RAG, agent frameworks, MCP, evaluation. | Build production RAG + multi-agent systems. |
| **4. Serving & Infra** | 18–28 | LLMOps, serving engines, GPUs, K8s, distributed inference. | Serve thousands of RPS on GPU clusters. |
| **5. Ops, Security, Platform** | 29–37 | Observability, security, platform + enterprise architecture, cloud. | Design & operate enterprise AI platforms. |
| **6. Capstone & Career** | 38–40 | Integrate everything; get hired; grow. | Ship a full platform; pass staff-level interviews. |

---

## Ground Rules

1. **Never skip the dependency graph.** If a module lists prerequisites, complete them first.
2. **Do the labs.** Reading is not learning here; the labs and projects are the curriculum.
3. **Assess honestly.** Do not advance until you pass the module's practical exam and design interview.
4. **Keep it running.** Every project must be reproducible from scratch, and every cloud/GPU resource must be torn down.
5. **Improve as you go.** When you learn something new, update earlier modules — this is a living handbook.

---

## Next Step

Read the **[Module Catalog](./module-catalog.md)** → choose a **[Learning Path](./learning-paths.md)** → begin **`/01-ai-foundations`** (built in Phase 2, after approval).
