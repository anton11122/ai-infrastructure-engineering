# Knowledge Graph — Dependencies & Critical Path

This is the dependency map for the entire curriculum. Use it to decide **what to learn first**, **what the critical path is**, and **which branches are optional vs advanced vs expert**.

> Rule: never start a module before its prerequisite edges are satisfied.

---

## Master Dependency Graph

```mermaid
graph TD
    subgraph P1["Phase 1 · Foundations"]
        M01[01 AI Foundations]
        M02[02 Python for AI]
        M03[03 ML Fundamentals]
        M04[04 Deep Learning]
    end

    subgraph P2["Phase 2 · Core AI"]
        M05[05 Transformers]
        M06[06 LLMs]
        M07[07 Prompt Eng]
        M08[08 Embeddings]
    end

    subgraph P3["Phase 3 · Data/RAG/Agents"]
        M09[09 Vector DBs]
        M10[10 RAG]
        M11[11 Agentic AI]
        M12[12 MCP]
        M13[13 LangChain]
        M14[14 LangGraph]
        M15[15 CrewAI]
        M16[16 AutoGen]
        M17[17 AI Evaluation]
    end

    subgraph P4["Phase 4 · Serving/Infra"]
        M18[18 LLMOps]
        M19[19 Model Serving]
        M20[20 GPU Infra]
        M21[21 K8s for AI]
        M22[22 Ray]
        M23[23 KServe]
        M24[24 vLLM]
        M25[25 SGLang]
        M26[26 Triton]
        M27[27 TensorRT-LLM]
        M28[28 Distributed Inference]
    end

    subgraph P5["Phase 5 · Ops/Sec/Platform"]
        M29[29 Observability]
        M30[30 AI Security]
        M31[31 Platform Eng]
        M32[32 Enterprise Arch]
        M33[33 Cloud AI]
        M34[34 AWS Bedrock]
        M35[35 GCP Vertex]
        M36[36 Azure AI]
        M37[37 Multi-Agent Platforms]
    end

    subgraph P6["Phase 6 · Capstone/Career"]
        M38[38 Capstone]
        M39[39 Interview Prep]
        M40[40 Career Growth]
    end

    M01 --> M02 --> M03 --> M04 --> M05 --> M06
    M06 --> M07
    M06 --> M08 --> M09 --> M10
    M07 --> M11
    M10 --> M11 --> M12
    M11 --> M13 --> M14
    M14 --> M15
    M14 --> M16
    M10 --> M17
    M11 --> M17
    M06 --> M18
    M17 --> M18
    M06 --> M19
    M04 --> M19
    M04 --> M20 --> M21 --> M22
    M21 --> M23
    M19 --> M24
    M20 --> M24 --> M25
    M19 --> M26
    M24 --> M27
    M26 --> M27
    M24 --> M28
    M22 --> M28
    M17 --> M29
    M24 --> M29
    M11 --> M30
    M12 --> M30
    M18 --> M31
    M23 --> M31
    M29 --> M31
    M30 --> M31 --> M32
    M28 --> M33 --> M34
    M33 --> M35
    M33 --> M36
    M14 --> M37
    M15 --> M37
    M16 --> M37
    M31 --> M37
    M32 --> M38
    M37 --> M38
    M28 --> M38
    M29 --> M38
    M30 --> M38
    M38 --> M39 --> M40
```

---

## Critical Path (shortest route to "can build a serving platform")

The minimum spine you must complete in order — everything else hangs off it:

```mermaid
graph LR
    A[01→02→03→04] --> B[05 Transformers] --> C[06 LLMs]
    C --> D[19 Model Serving]
    C --> E[20 GPU Infra]
    E --> F[21 K8s for AI]
    D --> G[24 vLLM]
    F --> G
    G --> H[28 Distributed Inference]
    H --> I[31 Platform Eng]
    I --> J[38 Capstone]
```

**Critical path modules:** `01 → 02 → 03 → 04 → 05 → 06 → 19 → 20 → 21 → 24 → 28 → 31 → 38`.

---

## Branch Classification

| Branch | Modules | When to take |
|--------|---------|--------------|
| **Core (required)** | 01–06, 09, 10, 17, 18, 19, 20, 21, 24, 28, 29, 30, 31, 32, 38 | Everyone. Non-negotiable spine. |
| **Agents (specialization)** | 07, 11, 12, 13, 14, 15, 16, 37 | If targeting agent/RAG platform roles. |
| **Serving depth (advanced)** | 22, 23, 25, 26, 27 | If targeting inference/performance roles. |
| **Cloud (optional-by-employer)** | 33, 34, 35, 36 | Pick the cloud(s) your target employer uses. |
| **Career** | 39, 40 | Final phase, before/during job search. |

---

## Path Overlays

### Optional path
Modules you can defer without blocking the critical path: `13 LangChain`, `15 CrewAI`, `16 AutoGen`, `25 SGLang`, `26 Triton`, one or more of `34/35/36`.

### Advanced path
Deepen here once core is solid: `22 Ray`, `23 KServe`, `27 TensorRT-LLM`, `28 Distributed Inference`, `29 Observability`.

### Expert path
Staff/Principal-level integration: `30 Security`, `31 Platform Eng`, `32 Enterprise Arch`, `37 Multi-Agent Platforms`, `38 Capstone`.

---

## Skill → Module Traceability

Where each headline skill from the mission is built:

| Skill | Primary modules |
|-------|-----------------|
| Deploy LLMs | 06, 19, 24 |
| Operate GPU clusters | 20, 21 |
| Build AI platforms / IDP for AI | 31, 32 |
| Scale inference / thousands of RPS | 24, 28 |
| Deploy AI agents / multi-agent | 11, 14, 15, 16, 37 |
| Production RAG | 10 |
| Vector DB infrastructure | 09 |
| Evaluate AI systems | 17 |
| AI observability | 29 |
| Inference cost optimization | 20, 24, 28, 31 |
| GPU scheduling | 20, 21 |
| AI security & governance | 30 |
| Prompt management | 07 |
| Evaluation pipelines | 17 |
| Model registries / routing | 18 |
| MCP servers / AI gateways | 12, 31 |
| Distributed inference | 28 |
| Autoscaling | 21, 23, 24 |
| KServe / Ray / vLLM / SGLang / Triton / TensorRT-LLM | 23, 22, 24, 25, 26, 27 |
| MLflow / LangSmith / LangFuse / Phoenix / W&B | 18, 29 |
| Kubeflow / Airflow | 18, 31 |
| Distributed vector databases | 09 |
| Enterprise AI architecture / lead teams | 32, 40 |
