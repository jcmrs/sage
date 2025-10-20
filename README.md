# SAGE (Spec-Agentic Guidance Environment)

Proposed Concept for Intended Agent (SAGE)
LLM-agnostic open-source AI-powered mentorship system with specialized agents providing expert guidance across ideation, product design, user research, UX/UI, strategy, AI integration, and leadership. Built for synergy between Human and AI to accelerate learning through personalized, hands-on mentorship and go from ideation to putting everything in place for Product and Project Development utilising Spec Driven Development methodology. Runs out-of-the-box with Claude Code (Subscription) and Gemini CLI (0Auth) (gemini-2.5-pro) as well as remote API Keys and local AI (Ollama, LM Studio). Features integrated local Git + Repository Management and remote GitHub Management incorporating advanced Git/GitHub Protocols (inspired by [Conventional Commits](https://www.conventionalcommits.org/) and enhanced to serve as "process memory" of the project, creating a Git-based memory graph for AI).

## Local Working Directory

C:\Development\sage

## Remote GitHub Repository
https://github.com/jcmrs/sage

## Source GitHub Projects

### Primary

product-design-agent
https://github.com/jmlusiardo/product-design-agent

### Potentials for Pattern Analysis

git-memory-mcp-server <- high interest
https://github.com/nirutyodjai/git-memory-mcp-server

git-mcp-server <- high interest
https://github.com/cyanheads/git-mcp-server

DiffMem <- high interest
https://github.com/Growth-Kinetics/DiffMem
https://www.xugj520.cn/en/archives/diffmem-git-based-ai-memory-management.html
https://medium.com/data-science-collective/diffmem-why-a-git-repo-might-be-the-most-honest-memory-your-ai-can-have-1951203912ed
https://news.mcan.sh/item/44969622

BaseAI
https://github.com/LangbaseInc/BaseAI
https://baseai.dev/docs/guides/memory-from-git
https://medium.com/data-science-collective/agentic-ai-implementing-long-term-memory-304be62063cc

graph-of-thoughts-mcp
https://github.com/angrysky56/graph-of-thoughts-mcp

persistent-ai-memory
https://github.com/savantskie/persistent-ai-memory

agents
https://github.com/wshobson/agents <- high interest
https://sethhobson.com

memory-journal-mcp
https://github.com/neverinfamous/memory-journal-mcp

gemini-mcp-starter
https://github.com/sonra44/gemini-mcp-starter

AIPM
https://github.com/getHarshOnline/AIPM

mem-mcp-server
https://github.com/memovai/mem-mcp-server

github-copilot-with-memory-bank
https://github.com/phillip1029/github-copilot-with-memory-bank

Creative-Agent
https://github.com/uv-yuval-cohen/Creative-Agent

claude-code-architect-copilot
https://github.com/casper7995/claude-code-architect-copilot

ideation-agent
https://github.com/brianmeyer/ideation-agent

AI-Agent-Ideation-Chatbot-System-Prompt
https://github.com/danielrosehill/AI-Agent-Ideation-Chatbot-System-Prompt

Claude-Code-Git-Ask
https://github.com/ihainan/Claude-Code-Git-Ask

agent-rules
https://github.com/steipete/agent-rules

## Foundational Concepts

Configurability
Modularity
Extensibility
Integration
Automation

## Constraints

LLM-agnostic
No Servers of any kind
No NPM

### Tokens and auto-compact:

No skipping things or leaving things out, learn to manage context windows properly



---

Based on the Claude documentation, there are several approaches for managing context windows in Claude Code more effectively:

## Multi-Context Window Workflows

For long-running tasks that span multiple context windows, Claude Sonnet 4.5 excels at state management across sessions [(1)](https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/claude-4-best-practices#general-principles). The recommended approach is to use structured state tracking rather than relying solely on compaction [(1)](https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/claude-4-best-practices#general-principles).

## Context Awareness Features

Claude Sonnet 4.5 includes context awareness, which allows the model to track its remaining context window throughout a conversation [(1)](https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/claude-4-best-practices#general-principles). To optimize this behavior in agent environments, you can add this guidance to your prompts [(1)](https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/claude-4-best-practices#general-principles):

```
Your context window will be automatically compacted as it approaches its limit, allowing you to continue working indefinitely from where you left off. Therefore, do not stop tasks early due to token budget concerns. As you approach your token budget limit, save your current progress and state to memory before the context window refreshes. Always be as persistent and autonomous as possible and complete tasks fully, even if the end of your budget is approaching. Never artificially stop any task early regardless of the context remaining.
```
[(1)](https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/claude-4-best-practices#general-principles)

## Best Practices for State Management

Instead of relying on compaction, consider these strategies [(1)](https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/claude-4-best-practices#general-principles):

1. **Use structured formats for state data**: Track information in JSON or other structured formats [(1)](https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/claude-4-best-practices#general-principles)
2. **Use git for state tracking**: Git provides logs and checkpoints that can be restored across sessions [(1)](https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/claude-4-best-practices#general-principles)
3. **Starting fresh vs compacting**: Consider starting with a brand new context window rather than compaction, as Sonnet 4.5 is effective at discovering state from the local filesystem [(1)](https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/claude-4-best-practices#general-principles)

## Context Editing (Beta)

There's a newer context editing feature available with the `context-management-2025-06-27` beta header that provides more automated context management [(2)](https://docs.claude.com/en/docs/build-with-claude/context-editing). This feature can automatically clear tool results when conversation context grows beyond configured thresholds [(2)](https://docs.claude.com/en/docs/build-with-claude/context-editing).

## Cost Tracking

You can monitor token usage with the `/cost` command to better understand your context consumption patterns [(3)](https://docs.claude.com/en/docs/claude-code/costs#reduce-token-usage).

The documentation suggests that structured state management and leveraging Claude's context awareness capabilities may be more reliable than depending on traditional compaction methods for long-running coding sessions.





You're right - the specific issue of Claude Code interrupting test routines due to auto-compact is addressed through hooks. Here's how to manage this:

## PreCompact Hook

You can use the `PreCompact` hook to control when Claude Code compacts its context [(1)](https://docs.claude.com/en/docs/claude-code/hooks#hook-events). This hook runs before Claude Code is about to run a compact operation and supports these matchers [(1)](https://docs.claude.com/en/docs/claude-code/hooks#hook-events):

- `manual` - Invoked from `/compact`
- `auto` - Invoked from auto-compact (due to full context window)

## Hook Configuration

Configure the hook in your settings files [(1)](https://docs.claude.com/en/docs/claude-code/hooks#hook-events):

```json
{
  "hooks": {
    "PreCompact": [
      {
        "matcher": "auto",
        "hooks": [
          {
            "type": "command",
            "command": "your-test-check-script.sh"
          }
        ]
      }
    ]
  }
}
```
[(1)](https://docs.claude.com/en/docs/claude-code/hooks#hook-events)

## Hook Decision Control

The `PreCompact` hook can use exit codes to control behavior [(2)](https://docs.claude.com/en/docs/claude-code/hooks#hook-events):

- **Exit code 0**: Allow compaction to proceed
- **Exit code 2**: Block the compaction operation and show stderr to the user

## Hook Input Data

The hook receives JSON data including the trigger type [(2)](https://docs.claude.com/en/docs/claude-code/hooks#hook-events):

```json
{
  "session_id": "abc123",
  "transcript_path": "~/.claude/projects/.../00893aaf-19fa-41d2-8238-13269b9b3ca0.jsonl",
  "hook_event_name": "PreCompact",
  "trigger": "auto",
  "custom_instructions": ""
}
```
[(2)](https://docs.claude.com/en/docs/claude-code/hooks#hook-events)

This allows you to create a script that checks if tests are running and blocks auto-compact when they are, preventing the interruption you're experiencing.

There's also a known GitHub issue where context window tracking shows zero context remaining incorrectly, causing premature auto-compaction [(3)](https://github.com/anthropics/claude-code/issues/2523). This suggests the problem you're encountering may be related to a bug in context window calculation.

