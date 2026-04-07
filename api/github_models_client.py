"""GitHub Models client - uses the OpenAI-compatible API at models.inference.ai.azure.com."""

from api.openai_client import OpenAIClient

GITHUB_MODELS_BASE_URL = "https://models.inference.ai.azure.com"


class GitHubModelsClient(OpenAIClient):
    """OpenAI-compatible client for GitHub Models.

    Uses GITHUB_TOKEN as the API key and the GitHub Models inference endpoint.
    """

    def __init__(self, **kwargs):
        super().__init__(
            base_url=GITHUB_MODELS_BASE_URL,
            env_api_key_name="GITHUB_TOKEN",
            **kwargs,
        )
