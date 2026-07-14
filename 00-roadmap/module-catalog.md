# Module Catalog

The complete catalog of all 40 modules. Each entry lists: **objective**, **required background**, **key skills**, **prerequisites** (module numbers), **difficulty band**, and the **capstone project** the module ends with.

Legend for difficulty bands: `B` Beginner · `I` Intermediate · `A` Advanced · `E` Expert · `S` Staff · `P` Principal.

---

## Phase 1 — Foundations

### 01 · AI Foundations
- **Objective:** Build accurate mental models of AI/ML/DL/GenAI; kill the hype; understand the compute/data/model triad and where infrastructure fits.
- **Background:** None (AI); your DevOps expertise is the lens.
- **Key skills:** AI vs ML vs DL vs GenAI, training vs inference, the ML lifecycle, hardware landscape (CPU/GPU/TPU/accelerators), the modern AI stack.
- **Prerequisites:** —
- **Difficulty:** `B→I`
- **Project:** AI system teardown — reverse-engineer and diagram a real AI product's infrastructure.

### 02 · Python for AI
- **Objective:** Become productive in the Python/AI toolchain from an engineer's standpoint (not a data scientist's).
- **Background:** General programming.
- **Key skills:** NumPy, pandas, PyTorch basics, `uv`/poetry, packaging, async, FastAPI, profiling, GPU-aware Python, notebooks in production.
- **Prerequisites:** 01
- **Difficulty:** `B→I`
- **Project:** A production-grade Python inference microservice (FastAPI + batching + metrics).

### 03 · Machine Learning Fundamentals
- **Objective:** Understand classical ML so you can operate, evaluate, and reason about models.
- **Background:** 01, 02
- **Key skills:** supervised/unsupervised, features, train/val/test, overfitting, metrics, gradient descent, bias/variance, data leakage.
- **Prerequisites:** 01, 02
- **Difficulty:** `I`
- **Project:** End-to-end ML pipeline with experiment tracking + a model service.

### 04 · Deep Learning
- **Objective:** Understand neural networks deeply enough to make infra decisions (memory, precision, parallelism).
- **Background:** 03
- **Key skills:** backprop, optimizers, CNN/RNN, activations, regularization, mixed precision, GPU memory math, checkpoints.
- **Prerequisites:** 03
- **Difficulty:** `I→A`
- **Project:** Train + serve a DL model on GPU with autoscaling and observability hooks.

---

## Phase 2 — Core AI

### 05 · Transformers
- **Objective:** Master the transformer architecture — the substrate of all modern AI infra.
- **Key skills:** attention, KV cache, positional encodings, tokenization, context windows, FlashAttention, memory/compute scaling laws.
- **Prerequisites:** 04
- **Difficulty:** `A`
- **Project:** Instrument a transformer to measure KV-cache growth and attention cost vs context length.

### 06 · LLMs
- **Objective:** Understand LLM training/finetuning/inference lifecycle and the levers infra engineers control.
- **Key skills:** pretraining vs SFT vs RLHF/DPO, quantization (GPTQ/AWQ/FP8), LoRA/QLoRA, decoding strategies, throughput vs latency, model formats (safetensors/GGUF).
- **Prerequisites:** 05
- **Difficulty:** `A`
- **Project:** Quantize + benchmark an open model across precisions; publish a latency/throughput/cost report.

### 07 · Prompt Engineering
- **Objective:** Engineer prompts as versioned, tested, observable artifacts.
- **Key skills:** system/user/tool messages, few-shot, CoT, structured output/JSON mode, prompt injection basics, prompt versioning & A/B testing.
- **Prerequisites:** 06
- **Difficulty:** `I→A`
- **Project:** A prompt management service with versioning, evals, and rollout controls.

### 08 · Embeddings
- **Objective:** Understand embeddings as the bridge to retrieval and semantic infra.
- **Key skills:** embedding models, similarity metrics, dimensionality, chunking, normalization, embedding drift, batch embedding pipelines.
- **Prerequisites:** 06
- **Difficulty:** `I→A`
- **Project:** A scalable embedding pipeline (batch + streaming) with caching and re-embedding strategy.

---

## Phase 3 — Data, RAG & Agents

### 09 · Vector Databases
- **Objective:** Design and operate vector database infrastructure at scale.
- **Key skills:** HNSW/IVF/PQ indexes, ANN trade-offs, pgvector/Qdrant/Milvus/Weaviate, sharding, replication, hybrid search, filtering.
- **Prerequisites:** 08
- **Difficulty:** `A→E`
- **Project:** Distributed vector DB deployment with sharding, HA, and hybrid search.

### 10 · RAG
- **Objective:** Build production RAG systems that are accurate, fast, and observable.
- **Key skills:** ingestion pipelines, chunking strategies, retrievers, rerankers, query rewriting, evaluation (faithfulness/relevance), caching.
- **Prerequisites:** 09
- **Difficulty:** `A→E`
- **Project:** **Production RAG** platform (versioned v1→enterprise) with evals + observability.

### 11 · Agentic AI
- **Objective:** Understand agent architectures and their infra/operational implications.
- **Key skills:** tool calling, ReAct, planning, memory, reflection, loops/guardrails, cost/latency control, sandboxing.
- **Prerequisites:** 07, 10
- **Difficulty:** `A→E`
- **Project:** A safe, observable single-agent service with tool sandboxing and budget limits.

### 12 · MCP (Model Context Protocol)
- **Objective:** Deploy and operate MCP servers as first-class platform components.
- **Key skills:** MCP spec, transports, tools/resources/prompts, auth, multi-tenant MCP, security posture.
- **Prerequisites:** 11
- **Difficulty:** `A→E`
- **Project:** **Enterprise MCP Platform** — multi-tenant MCP servers with authN/Z and observability.

### 13 · LangChain
- **Objective:** Use LangChain effectively while understanding its runtime/operational cost.
- **Key skills:** chains, runnables, LCEL, callbacks/tracing, integrations, when NOT to use it.
- **Prerequisites:** 11
- **Difficulty:** `I→A`
- **Project:** Refactor a naive LangChain app into an observable, cost-controlled service.

### 14 · LangGraph
- **Objective:** Build stateful, durable agent graphs suitable for production.
- **Key skills:** graph state, checkpoints, human-in-the-loop, persistence, resumability, concurrency.
- **Prerequisites:** 13
- **Difficulty:** `A→E`
- **Project:** A durable, resumable multi-step agent workflow with persistence.

### 15 · CrewAI
- **Objective:** Orchestrate role-based multi-agent teams and understand their trade-offs.
- **Key skills:** roles, tasks, delegation, coordination patterns, failure handling.
- **Prerequisites:** 14
- **Difficulty:** `A`
- **Project:** A role-based multi-agent crew with guardrails and cost tracking.

### 16 · AutoGen
- **Objective:** Build conversational multi-agent systems; compare frameworks objectively.
- **Key skills:** conversable agents, group chat, termination, tool use, framework comparison matrix.
- **Prerequisites:** 14
- **Difficulty:** `A`
- **Project:** A multi-agent system + a rigorous CrewAI/AutoGen/LangGraph comparison report.

### 17 · AI Evaluation
- **Objective:** Evaluate AI systems rigorously — the backbone of AI quality engineering.
- **Key skills:** offline/online evals, LLM-as-judge, golden datasets, regression testing, RAG/agent metrics, red-teaming, statistical rigor.
- **Prerequisites:** 10, 11
- **Difficulty:** `A→E`
- **Project:** **Evaluation Platform** with CI-integrated eval pipelines and dashboards.

---

## Phase 4 — Serving & Infrastructure

### 18 · LLMOps
- **Objective:** Operationalize the full LLM lifecycle (the AI analog of your DevOps expertise).
- **Key skills:** model registry, CI/CD for models/prompts, canary/shadow, rollback, data/version management, MLflow.
- **Prerequisites:** 06, 17
- **Difficulty:** `A→E`
- **Project:** **Model Registry** + LLMOps pipeline with GitOps promotion flows.

### 19 · Model Serving
- **Objective:** Understand serving fundamentals and choose the right engine.
- **Key skills:** batching (dynamic/continuous), streaming, concurrency, latency budgets, engine comparison, autoscaling basics.
- **Prerequisites:** 06, 04
- **Difficulty:** `A→E`
- **Project:** A serving benchmark harness comparing engines under identical load.

### 20 · GPU Infrastructure
- **Objective:** Operate GPU clusters like a pro — scheduling, sharing, topology, cost.
- **Key skills:** NVIDIA drivers/CUDA, MIG, time-slicing, NVLink/NVSwitch, GPU Operator, DCGM, GPU cost models, spot strategies.
- **Prerequisites:** 04
- **Difficulty:** `E→S`
- **Project:** **GPU Cluster** with scheduling, sharing (MIG/time-slice), monitoring, and cost dashboards.

### 21 · Kubernetes for AI
- **Objective:** Extend your K8s expertise to AI-specific scheduling and operators.
- **Key skills:** device plugins, node pools, taints/affinity, Kueue/Volcano, gang scheduling, priority/preemption, topology-aware scheduling.
- **Prerequisites:** 20
- **Difficulty:** `E→S`
- **Project:** An AI-optimized K8s cluster with gang scheduling and GPU-aware autoscaling.

### 22 · Ray
- **Objective:** Use Ray for distributed AI workloads (data, train, serve).
- **Key skills:** Ray core, Ray Serve, Ray Data, autoscaling, KubeRay, placement groups.
- **Prerequisites:** 21
- **Difficulty:** `E`
- **Project:** A Ray Serve deployment on KubeRay with autoscaling + fault tolerance.

### 23 · KServe
- **Objective:** Standardize model serving on Kubernetes with KServe.
- **Key skills:** InferenceService, serverless/raw, transformers, canary, ModelMesh, autoscaling to zero.
- **Prerequisites:** 21
- **Difficulty:** `E`
- **Project:** KServe-based serving with canary rollout and scale-to-zero.

### 24 · vLLM
- **Objective:** Master vLLM — the workhorse LLM inference engine.
- **Key skills:** PagedAttention, continuous batching, tensor parallelism, prefix caching, speculative decoding, OpenAI-compatible server, tuning.
- **Prerequisites:** 19, 20
- **Difficulty:** `E→S`
- **Project:** A tuned vLLM deployment hitting a target RPS/latency SLO on a GPU cluster.

### 25 · SGLang
- **Objective:** Use SGLang for high-throughput, structured, multi-turn workloads.
- **Key skills:** RadixAttention, structured generation, when SGLang beats vLLM, tuning.
- **Prerequisites:** 24
- **Difficulty:** `E`
- **Project:** SGLang vs vLLM benchmark on structured + multi-turn workloads.

### 26 · Triton Inference Server
- **Objective:** Serve heterogeneous models (not just LLMs) at scale with Triton.
- **Key skills:** backends, model repository, ensembles, dynamic batching, concurrent model execution.
- **Prerequisites:** 19
- **Difficulty:** `E`
- **Project:** A Triton deployment serving mixed model types with ensembles.

### 27 · TensorRT-LLM
- **Objective:** Squeeze maximum performance from NVIDIA GPUs.
- **Key skills:** engine building, FP8/INT4, in-flight batching, Triton+TensorRT-LLM, kernel-level trade-offs.
- **Prerequisites:** 24, 26
- **Difficulty:** `S`
- **Project:** A TensorRT-LLM optimized deployment with a before/after performance report.

### 28 · Distributed Inference
- **Objective:** Serve models too large for one GPU/node; design for scale and resilience.
- **Key skills:** tensor/pipeline/expert parallelism, multi-node inference, disaggregated prefill/decode, KV-cache offloading, routing.
- **Prerequisites:** 24, 22
- **Difficulty:** `S→P`
- **Project:** **Inference Cluster** — multi-node distributed serving with routing + HA.

---

## Phase 5 — Ops, Security, Platform

### 29 · AI Observability
- **Objective:** See everything: traces, metrics, logs, evals, cost — for AI systems.
- **Key skills:** LLM tracing, LangFuse/LangSmith/Phoenix, token/cost metrics, GPU metrics, OpenTelemetry for AI, alerting on quality.
- **Prerequisites:** 17, 24
- **Difficulty:** `E→S`
- **Project:** **AI Monitoring Stack** integrating traces, evals, GPU + cost dashboards.

### 30 · AI Security
- **Objective:** Secure AI systems against AI-specific and classic threats; implement governance.
- **Key skills:** prompt injection, data exfiltration, jailbreaks, guardrails, PII, secrets, supply chain, model provenance, OWASP LLM Top 10, governance/policy.
- **Prerequisites:** 11, 12
- **Difficulty:** `E→S`
- **Project:** **AI Security Platform** — guardrails, policy engine, red-team harness, audit.

### 31 · AI Platform Engineering
- **Objective:** Build an Internal Developer Platform for AI (self-service golden paths).
- **Key skills:** platform APIs, golden paths, multi-tenancy, quotas, self-service model/agent deploy, developer portal (Backstage), FinOps.
- **Prerequisites:** 18, 23, 29, 30
- **Difficulty:** `S→P`
- **Project:** **Internal AI Developer Platform** — self-service deploy of models/agents/RAG.

### 32 · Enterprise Architecture
- **Objective:** Design enterprise AI architectures and lead the decisions.
- **Key skills:** reference architectures, build vs buy, data governance, compliance, DR, multi-region, capacity planning, TCO, ADRs.
- **Prerequisites:** 31
- **Difficulty:** `S→P`
- **Project:** A full enterprise AI reference architecture + ADR set + design review.

### 33 · Cloud AI
- **Objective:** Understand managed vs self-hosted trade-offs across clouds.
- **Key skills:** managed inference, cloud GPU options, networking/egress cost, hybrid, portability.
- **Prerequisites:** 28
- **Difficulty:** `A→E`
- **Project:** A multi-cloud decision matrix + a portable deployment abstraction.

### 34 · AWS Bedrock
- **Objective:** Build on AWS's managed GenAI stack.
- **Key skills:** Bedrock models, Knowledge Bases, Agents, Guardrails, provisioned throughput, private networking, cost.
- **Prerequisites:** 33
- **Difficulty:** `A→E`
- **Project:** A Bedrock-based RAG + agent app with guardrails and VPC isolation.

### 35 · GCP Vertex AI
- **Objective:** Build on Google's Vertex AI stack.
- **Key skills:** Vertex endpoints, Model Garden, Agent Builder, RAG Engine, TPUs, pipelines.
- **Prerequisites:** 33
- **Difficulty:** `A→E`
- **Project:** A Vertex AI deployment with pipelines + endpoint autoscaling.

### 36 · Azure AI
- **Objective:** Build on Azure's AI stack.
- **Key skills:** Azure OpenAI, AI Foundry, AI Search, content safety, private endpoints, quotas.
- **Prerequisites:** 33
- **Difficulty:** `A→E`
- **Project:** An Azure OpenAI + AI Search RAG app with content safety + private endpoints.

### 37 · Multi-Agent Platforms
- **Objective:** Operate multi-agent systems as a platform capability at scale.
- **Key skills:** agent orchestration at scale, shared memory, message buses, agent registries, cost/safety governance, A2A protocols.
- **Prerequisites:** 14, 15, 16, 31
- **Difficulty:** `S→P`
- **Project:** **Agent Platform** — orchestration, registry, shared memory, governance.

---

## Phase 6 — Capstone & Career

### 38 · Capstone Projects
- **Objective:** Integrate the entire curriculum into a complete enterprise AI platform.
- **Key skills:** everything — end to end.
- **Prerequisites:** all core modules (see knowledge graph).
- **Difficulty:** `S→P`
- **Project:** **Enterprise AI Platform** (see the [capstone spec](../38-capstone-projects/)).

### 39 · Interview Preparation
- **Objective:** Pass staff/principal AI-infra interviews.
- **Key skills:** system design, GPU/serving deep-dives, troubleshooting, behavioral, take-homes.
- **Prerequisites:** 38
- **Difficulty:** `S→P`
- **Project:** A personal interview dossier: design docs, war stories, and a mock-interview log.

### 40 · Career Growth
- **Objective:** Grow from senior to staff/principal and lead AI platform teams.
- **Key skills:** tech leadership, RFC writing, mentoring, roadmap ownership, stakeholder management.
- **Prerequisites:** 39
- **Difficulty:** `S→P`
- **Project:** A 12-month leadership + growth plan with measurable milestones.
