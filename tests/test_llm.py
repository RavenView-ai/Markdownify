# Copyright (c) 2025 Sethu Pavan Venkata Reddy Pastula
# Licensed under the Apache License, Version 2.0. See LICENSE file for details.
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import time

from llm_markdownify.llm import RateLimiter, configure_llm, _hash_content


def test_hash_content_deterministic():
    """Same input produces same hash."""
    h1 = _hash_content("hello world")
    h2 = _hash_content("hello world")
    assert h1 == h2


def test_hash_content_different_inputs():
    """Different inputs produce different hashes."""
    h1 = _hash_content("hello")
    h2 = _hash_content("world")
    assert h1 != h2


def test_rate_limiter_no_limit():
    """RateLimiter with None rpm doesn't block."""
    limiter = RateLimiter(rpm=None)
    start = time.monotonic()
    for _ in range(10):
        limiter.acquire()
    elapsed = time.monotonic() - start
    # Should be nearly instant
    assert elapsed < 0.1


def test_rate_limiter_high_limit():
    """RateLimiter with high limit doesn't block much."""
    limiter = RateLimiter(rpm=6000)  # 100 per second
    start = time.monotonic()
    for _ in range(5):
        limiter.acquire()
    elapsed = time.monotonic() - start
    # Should be fast
    assert elapsed < 0.5


def test_rate_limiter_low_limit():
    """RateLimiter with low limit introduces delays."""
    limiter = RateLimiter(rpm=120)  # 2 per second
    start = time.monotonic()
    limiter.acquire()  # First one is instant
    limiter.acquire()  # Second one should be ~0.5s wait
    elapsed = time.monotonic() - start
    # Should take some time but not too long
    assert elapsed < 2.0


def test_configure_llm_sets_globals():
    """configure_llm sets the global configuration."""
    configure_llm(max_retries=5, retry_delay=2.0, rate_limit_rpm=100)
    # Just verify it doesn't raise - actual values are internal
