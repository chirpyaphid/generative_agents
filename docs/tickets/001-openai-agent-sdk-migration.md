# Ticket 001 – Introduce OpenAI Agents SDK

**Goal:** Add the Agents SDK as a dependency and prototype a basic agent.

- [ ] Add `openai-agents` to `requirements.txt`.
- [ ] Create a wrapper around the existing `Persona` class using `agents.Agent`.
- [ ] Demonstrate a simple call with `Runner.run_sync` in a new example script.
- [ ] Document setup in `README.md`.

---

# Ticket 002 – Convert cognitive modules to tools

**Goal:** Expose key functions as `@function_tool` for agent access.

- [ ] Map planning, perception, memory retrieval and conversation functions to tools.
- [ ] Register these tools with the new agent wrapper.
- [ ] Add unit tests to cover tool invocation via the SDK.

---

# Ticket 003 – Implement handoffs and specialized agents

**Goal:** Split functionality across multiple agents and use handoffs for control flow.

- [ ] Define specialized agents (e.g., PlannerAgent, ChatAgent) with tailored instructions.
- [ ] Configure handoffs between agents based on simulation state.
- [ ] Ensure tracing captures handoff events.

---

# Ticket 004 – Update simulation and documentation

**Goal:** Integrate the SDK-based agents into the existing simulation flow.

- [ ] Replace direct OpenAI API calls in the simulation server with the new agents.
- [ ] Update existing tests and add coverage for agent loops and handoffs.
- [ ] Expand `README.md` with new instructions and troubleshooting tips.

