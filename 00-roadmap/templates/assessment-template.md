# Assessment Template

> Copy into each module's `assessments/`. One file per assessment type, or a single `README.md` with all seven. See the [assessment framework](../assessment-framework.md) for scoring.

---

## 1. Self-Assessment Quiz
10–15 questions, mixed recall + reasoning. Provide an answer key in a collapsible section or separate `answers.md`.

```
Q1. [question]  `[difficulty]`
...
```

## 2. Practical Exam  `[E]`
- **Task:** [hands-on deliverable]
- **Environment:** [what's provided]
- **Time box:** [minutes]
- **Grading:** automated validation script + rubric.
- **Pass bar:** [explicit criteria].

## 3. Architecture Interview  `[A/S]`
- **Prompt:** "Design [system] for [constraints]."
- **Expected topics:** [what a strong answer covers].
- **Rubric:** correctness, trade-offs, scale, security, cost, operability (see framework).

## 4. Troubleshooting Interview  `[E]`
- **Setup:** a broken system + access.
- **Injected fault:** [hidden root cause].
- **Success:** identifies root cause + proposes correct fix within time box.

## 5. Code Review  `[A]`
- **Artifact:** a PR/diff with planted issues.
- **Planted issues:** [list, hidden from candidate].
- **Success:** finds ≥ [N] of the issues and explains impact + fix.

## 6. Scenario Interview  `[A/S]`
- **Prompt:** open-ended "what would you do if [constraint changes]".
- **Success:** structured reasoning, names trade-offs, states assumptions.

## 7. System Design Interview  `[S/P]`
- **Prompt:** full platform/subsystem design.
- **Deliverable:** design doc + diagrams + ADRs; defend in review.

## 8. Production Incident  `[E]`
- **Alert:** [symptom + metric that paged you].
- **Target MTTR:** [minutes].
- **Injected fault:** [root cause — reveal at debrief].
- **Deliverable:** mitigation + postmortem (impact, timeline, root cause, action items).

## 9. Module Final Exam
Combines a practical task + a design prompt + 5 short-answer questions. Pass bar documented per module.
