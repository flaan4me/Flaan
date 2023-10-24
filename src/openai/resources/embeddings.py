# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import base64
from typing import List, Union, cast
from typing_extensions import Literal

from ..types import CreateEmbeddingResponse, embedding_create_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import is_given, maybe_transform
from .._extras import numpy as np
from .._extras import has_numpy
from .._resource import SyncAPIResource, AsyncAPIResource
from .._base_client import make_request_options

__all__ = ["Embeddings", "AsyncEmbeddings"]


class Embeddings(SyncAPIResource):
    def create(
        self,
        *,
        input: Union[str, List[str], List[int], List[List[int]]],
        model: Union[str, Literal["text-embedding-ada-002"]],
        encoding_format: Literal["float", "base64"] | NotGiven = NOT_GIVEN,
        user: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> CreateEmbeddingResponse:
        """
        Creates an embedding vector representing the input text.

        Args:
          input: Input text to embed, encoded as a string or array of tokens. To embed multiple
              inputs in a single request, pass an array of strings or array of token arrays.
              The input must not exceed the max input tokens for the model (8192 tokens for
              `text-embedding-ada-002`) and cannot be an empty string.
              [Example Python code](https://cookbook.openai.com/examples/how_to_count_tokens_with_tiktoken)
              for counting tokens.

          model: ID of the model to use. You can use the
              [List models](https://platform.openai.com/docs/api-reference/models/list) API to
              see all of your available models, or see our
              [Model overview](https://platform.openai.com/docs/models/overview) for
              descriptions of them.

          encoding_format: The format to return the embeddings in. Can be either `float` or
              [`base64`](https://pypi.org/project/pybase64/).

          user: A unique identifier representing your end-user, which can help OpenAI to monitor
              and detect abuse.
              [Learn more](https://platform.openai.com/docs/guides/safety-best-practices/end-user-ids).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        params = {
            "input": input,
            "model": model,
            "user": user,
            "encoding_format": encoding_format,
        }
        if not is_given(encoding_format) and has_numpy():
            params["encoding_format"] = "base64"

        response = self._post(
            "/embeddings",
            body=maybe_transform(params, embedding_create_params.EmbeddingCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreateEmbeddingResponse,
        )

        if is_given(encoding_format):
            # don't modify the response object if a user explicitly asked for a format
            return response

        for embedding in response.data:
            data = cast(object, embedding.embedding)
            if not isinstance(data, str):
                # numpy is not installed / base64 optimisation isn't enabled for this model yet
                continue

            embedding.embedding = np.frombuffer(  # type: ignore[no-untyped-call]
                base64.b64decode(data), dtype="float32"
            ).tolist()

        return response


class AsyncEmbeddings(AsyncAPIResource):
    async def create(
        self,
        *,
        input: Union[str, List[str], List[int], List[List[int]]],
        model: Union[str, Literal["text-embedding-ada-002"]],
        encoding_format: Literal["float", "base64"] | NotGiven = NOT_GIVEN,
        user: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> CreateEmbeddingResponse:
        """
        Creates an embedding vector representing the input text.

        Args:
          input: Input text to embed, encoded as a string or array of tokens. To embed multiple
              inputs in a single request, pass an array of strings or array of token arrays.
              The input must not exceed the max input tokens for the model (8192 tokens for
              `text-embedding-ada-002`) and cannot be an empty string.
              [Example Python code](https://cookbook.openai.com/examples/how_to_count_tokens_with_tiktoken)
              for counting tokens.

          model: ID of the model to use. You can use the
              [List models](https://platform.openai.com/docs/api-reference/models/list) API to
              see all of your available models, or see our
              [Model overview](https://platform.openai.com/docs/models/overview) for
              descriptions of them.

          encoding_format: The format to return the embeddings in. Can be either `float` or
              [`base64`](https://pypi.org/project/pybase64/).

          user: A unique identifier representing your end-user, which can help OpenAI to monitor
              and detect abuse.
              [Learn more](https://platform.openai.com/docs/guides/safety-best-practices/end-user-ids).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        params = {
            "input": input,
            "model": model,
            "user": user,
            "encoding_format": encoding_format,
        }
        if not is_given(encoding_format) and has_numpy():
            params["encoding_format"] = "base64"

        response = await self._post(
            "/embeddings",
            body=maybe_transform(params, embedding_create_params.EmbeddingCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreateEmbeddingResponse,
        )

        if is_given(encoding_format):
            # don't modify the response object if a user explicitly asked for a format
            return response

        for embedding in response.data:
            data = cast(object, embedding.embedding)
            if not isinstance(data, str):
                # numpy is not installed / base64 optimisation isn't enabled for this model yet
                continue

            embedding.embedding = np.frombuffer(  # type: ignore[no-untyped-call]
                base64.b64decode(data), dtype="float32"
            ).tolist()

        return response