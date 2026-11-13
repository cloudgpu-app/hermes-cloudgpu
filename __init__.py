"""cloudgpu.app model provider for Hermes Agent.

Hermes drives models served by cloudgpu.app over the OpenAI-compatible API at
https://cloudgpu.app/v1 with a CLOUDGPU_API_KEY. The model list comes live
from GET /v1/models (public, no key needed); fallback_models is the static
list Hermes shows when that call fails.
"""

from providers import register_provider
from providers.base import ProviderProfile

cloudgpu = ProviderProfile(
    name="cloudgpu",
    aliases=("cloudgpu-app", "cloudgpu.app"),
    display_name="CloudGPU",
    description="cloudgpu.app: DeepSeek, Kimi, GLM and MiniMax on one OpenAI-compatible API",
    signup_url="https://cloudgpu.app/api",
    env_vars=("CLOUDGPU_API_KEY", "CLOUDGPU_BASE_URL"),
    base_url="https://cloudgpu.app/v1",
    auth_type="api_key",
    default_aux_model="deepseek-v4.1-flash",
    # [0] is the setup default; the live catalog at /v1/models lists the rest.
    fallback_models=(
        "deepseek-v4.1-flash",
        "deepseek-v4-pro",
        "kimi-k3",
        "kimi-k2.7-code",
        "glm-5.2",
        "minimax-m3",
    ),
)

register_provider(cloudgpu)
