"""Tests for OWON reverse energy sensors."""

from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "custom_components"))

from owon.sensor_321 import ALL_SENSORS


def test_reverse_energy_sensors_are_defined() -> None:
    """Reverse energy sensors should be available for the new protocol."""
    keys = {sensor.key for sensor in ALL_SENSORS}

    assert "reverse_energy_a" in keys
    assert "reverse_energy_b" in keys
    assert "reverse_energy_c" in keys
    assert "reverse_energy_total" in keys


def test_forward_and_reverse_energy_translations_exist() -> None:
    """Forward and reverse energy entities should have localized names."""
    repo_root = Path(__file__).resolve().parents[1]
    translations_dir = repo_root / "custom_components" / "owon" / "translations"

    expected_names = {
        "en": {
            "energy_consumed_a": "Phase A forward energy",
            "reverse_energy_a": "Phase A reverse energy",
            "energy_consumed_b": "Phase B forward energy",
            "reverse_energy_b": "Phase B reverse energy",
            "energy_consumed_c": "Phase C forward energy",
            "reverse_energy_c": "Phase C reverse energy",
            "energy_consumed_total": "Total forward energy",
            "reverse_energy_total": "Total reverse energy",
        },
        "zh-Hans": {
            "energy_consumed_a": "A相正向累计电量",
            "reverse_energy_a": "A相反向累计电量",
            "energy_consumed_b": "B相正向累计电量",
            "reverse_energy_b": "B相反向累计电量",
            "energy_consumed_c": "C相正向累计电量",
            "reverse_energy_c": "C相反向累计电量",
            "energy_consumed_total": "总累计电量",
            "reverse_energy_total": "总反向累计电量",
        },
    }

    for locale, names in expected_names.items():
        payload = json.loads((translations_dir / f"{locale}.json").read_text())
        sensors = payload["entity"]["sensor"]
        for key, expected_name in names.items():
            assert sensors[key]["name"] == expected_name
