# Resume And Phase Rules

Use this reference when the next phase is not obvious from the current prompt.

## Resume Precedence

1. Respect an explicit user override such as "resume from dev-review".
2. Prefer stronger workspace evidence over free-form prompt intent.
3. Preserve existing user work instead of restarting earlier phases.

## Dirty Workspace Heuristic

- If implementation files changed and no review exists after them, resume at `dev-review`.
- If the newest artifact is an investigation note and there is no newer plan-driving artifact, continue with `dev-resolve`, `dev-spec`, or `dev-plan`.
- If the newest artifact is an ExecPlan and implementation has not started, continue with `dev-plan` execution.
- If the active run came from an end-to-end `dev-orchestrate` request and there is no stop phase at planning, continue into `dev-plan` execution without asking for another approval.
- If a full cycle already produced walkthrough and recap artifacts, and the new request is narrow, enter follow-up mode instead of starting a new cycle.

## Optional Phase Selection

- Run `dev-resolve` only when unresolved questions could change architecture, scope, or execution order.
- Run `dev-spec` when a crisp requirement boundary will materially improve execution.
- Skip optional phases deliberately. Do not skip `dev-investigate`, `dev-plan`, or post-implementation `dev-review`.
