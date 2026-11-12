# hermes-cloudgpu

A [Hermes Agent](https://github.com/NousResearch/hermes-agent) model-provider plugin for [cloudgpu.app](https://cloudgpu.app/api?utm_source=github&utm_medium=referral&utm_campaign=202611_seg04_codingagent&utm_content=hermes_plugin).

Hermes runs its own agent loop against cloudgpu.app's OpenAI-compatible API at `https://cloudgpu.app/v1`, with DeepSeek, Kimi, GLM and MiniMax models on one key. Model prices are on [cloudgpu.app/api](https://cloudgpu.app/api); the balance is topped up by card or USDT.

## Setup

```bash
hermes plugins install cloudgpu-provider && export CLOUDGPU_API_KEY=cgw-sk-... && hermes chat --provider cloudgpu -m deepseek-v4.1-flash
```

Create the key in the cloudgpu.app console. Put it in `~/.hermes/.env` to keep it; the installer also asks for it.

Before the catalog entry is merged, install from GitHub instead:

```bash
hermes plugins install cloudgpu-app/hermes-cloudgpu/model-providers/cloudgpu
```

Then `hermes model` and pick **CloudGPU**.

## What it does

| | |
|---|---|
| Provider id | `cloudgpu` (aliases `cloudgpu-app`, `cloudgpu.app`) |
| Base URL | `https://cloudgpu.app/v1` (override with `CLOUDGPU_BASE_URL`) |
| Auth | `CLOUDGPU_API_KEY`, sent as `Authorization: Bearer` |
| Model list | live from `GET https://cloudgpu.app/v1/models` (public); if that fails, the fallback list below |
| Default model | `deepseek-v4.1-flash` (also the auxiliary model) |

Fallback models: `deepseek-v4.1-flash`, `deepseek-v4-pro`, `kimi-k3`, `kimi-k2.7-code`, `glm-5.2`, `minimax-m3`.

The plugin registers one provider profile and nothing else: no tools, hooks, middleware or extra dependencies. Prompts, tool schemas and the key go to cloudgpu.app.

## Check it

```bash
hermes plugins validate --install-deps model-providers/cloudgpu
```

## License

MIT.
