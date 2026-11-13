# hermes-cloudgpu

A [Hermes Agent](https://github.com/NousResearch/hermes-agent) model-provider plugin for [cloudgpu.app](https://cloudgpu.app/api?utm_source=github&utm_medium=referral&utm_campaign=202611_seg04_codingagent&utm_content=hermes_plugin).

Hermes runs its own agent loop against cloudgpu.app's OpenAI-compatible API at `https://cloudgpu.app/v1`, with DeepSeek, Kimi, GLM and MiniMax models on one key. Model prices are on [cloudgpu.app/api](https://cloudgpu.app/api); the balance is topped up by card or USDT.

## Owner-approved connection (candidate)

The connection helper is a candidate integration, not a new model provider or a published PyPI release. Install the reviewed CloudGPU Python SDK from the companion `cloudgpu-app/cloudgpu-mcp` repository's `python/` directory, then run:

```bash
python3 model-providers/cloudgpu/connect.py --spend-limit 5
```

Open the link, sign in with Google, review the cap and approve. If needed, top up on the owner page. The helper writes the returned key to the private shared CloudGPU credential store and, by explicit invocation of this Hermes helper, the private local `~/.hermes/.env`. It never prints the key or makes a payment. The $5 is a key spending cap, not an automatic charge. Pending approval survives restarts. Restart Hermes after successful connection; revocation and limits remain enforced by CloudGPU.

Do not install an unrelated similarly named package while the candidate SDK is not published. Existing manual key setup below remains available. Use an immutable `--ref <commit>` when installing a reviewed release. Runtime installation/registration acceptance is documented below; a new owner Google payment still requires the owner browser flow.

## Existing manual setup

```bash
hermes plugins install cloudgpu-app/hermes-cloudgpu --enable
# Then connect through the reviewed Python SDK, or configure your private Hermes env.
hermes chat --provider cloudgpu -m deepseek-v4.1-flash
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

## Repository layout

The repository root contains the native Hermes `plugin.yaml` and provider entry, so `hermes plugins install cloudgpu-app/hermes-cloudgpu` discovers a real plugin. The nested `model-providers/cloudgpu` copy remains for catalog compatibility; both entries must stay identical. The connector honors `HERMES_HOME` in the reviewed Python SDK and never writes keys into this repository.

## Runtime acceptance (2026-11-13)

Tested the actual upstream Hermes CLI/provider registry at revision `5c1abd257d0cc1b531ffee6e50bef0621aa49dc4` with Python3.12. Repository installation, native provider registration and live public model catalog (42 models at observation) passed. The connection helper resumed real production pending state in a new process, completed existing-owner approval, and wrote0600 credentials only in an isolated HERMES_HOME. The internal test key was revoked afterward; no GPU or model-generation charge occurred. This does not certify every Hermes version, a model conversation, a new Google login/payment, or a PyPI publication.
