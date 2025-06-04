# OpenAI Agent SDK Integration Plan

This document outlines the steps needed to migrate the existing generative agent
codebase to the [OpenAI Agents SDK](https://github.com/openai/openai-agents-python).

## Background

The Agents SDK is a provider‑agnostic framework that simplifies building
multi‑agent workflows with features such as guardrails, tracing and
handoffs. Key concepts include agents configured with instructions and tools,
handoffs for switching between agents, and built‑in tracing for debugging. The
README from the SDK notes:

- "The OpenAI Agents SDK is a lightweight yet powerful framework for building
  multi-agent workflows."【02a542†L1-L9】
- Core features include agents, handoffs, guardrails and tracing【02a542†L7-L12】.
- Installation is performed via `pip install openai-agents`【02a542†L25-L29】.

Adopting this framework can streamline agent loops and provide better support for
structured output and tool usage.

## Migration Goals

1. **Simplify LLM calls** – replace manual `openai.ChatCompletion` requests with
   the SDK's `Agent` and `Runner` abstractions.
2. **Leverage tools and handoffs** – expose cognitive modules (planning,
   perception, memory retrieval) as tools that can be called by agents and allow
   handing off between specialized agents when appropriate.
3. **Enable tracing and guardrails** – integrate tracing to debug agent
   behavior and apply guardrails for input/output validation.
4. **Maintain existing behaviour** – ensure the simulation continues to function
   as before while using the new agent loop.

## High‑Level Steps

1. **Introduce dependency** – add `openai-agents` to `requirements.txt` and set
   up basic configuration (API key environment variable).
2. **Prototype a single agent** – create an initial wrapper around the existing
   `Persona` to demonstrate responding using `Agent` and `Runner`.
3. **Map cognitive modules to tools** – expose functions like planning,
   conversation and memory retrieval via `@function_tool` so the agent can invoke
   them dynamically.
4. **Implement handoffs** – create specialized agents (e.g., planning agent,
   conversation agent) and define handoffs to transfer control according to the
   conversation or simulation state.
5. **Add tracing hooks** – enable default tracing and document how to visualize
   runs using the SDK's tracing utilities.
6. **Update tests** – refactor existing tests to invoke the new agent API and add
   coverage for tool calls and handoffs.
7. **Update documentation** – describe the new setup, configuration steps and
   developer workflow in `README.md`.

## Considerations

- Review licensing and compatibility of the Agents SDK.
- Ensure the environment server can still run alongside agent logic.
- Provide a fallback for environments without the SDK installed.

This plan serves as the foundation for generating development tickets.
