# Copyright (c) 2025 Sethu Pavan Venkata Reddy Pastula
# Licensed under the Apache License, Version 2.0. See LICENSE file for details.
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import logging

from llm_markdownify.logging import get_logger, set_log_level


def test_get_logger_returns_logger():
    """get_logger returns a configured logger."""
    logger = get_logger("test_module")
    assert isinstance(logger, logging.Logger)
    assert logger.name == "test_module"


def test_get_logger_same_instance():
    """get_logger returns the same logger for same name."""
    logger1 = get_logger("test_same")
    logger2 = get_logger("test_same")
    assert logger1 is logger2


def test_set_log_level_quiet():
    """set_log_level('quiet') sets WARNING level."""
    set_log_level("quiet")
    logger = get_logger("llm_markdownify.test_quiet")
    assert logger.level == logging.WARNING


def test_set_log_level_normal():
    """set_log_level('normal') sets INFO level."""
    set_log_level("normal")
    logger = get_logger("llm_markdownify.test_normal")
    assert logger.level == logging.INFO


def test_set_log_level_verbose():
    """set_log_level('verbose') sets DEBUG level."""
    set_log_level("verbose")
    logger = get_logger("llm_markdownify.test_verbose")
    assert logger.level == logging.DEBUG


def test_set_log_level_debug():
    """set_log_level('debug') sets DEBUG level."""
    set_log_level("debug")
    logger = get_logger("llm_markdownify.test_debug")
    assert logger.level == logging.DEBUG
