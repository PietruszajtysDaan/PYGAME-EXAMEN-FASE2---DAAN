# Voorbeeldtests voor het Pygame-project (gebruik pytest)
# Plaats deze bestanden in een map 'tests/' binnen je project.

# ----- tests/test_json_manager.py -----
import os
import json
import pytest
from data.json_manager import JSONManager

@pytest.fixture(autouse=True)
def chdir_tmp(tmp_path, monkeypatch):
    # Zorg dat alle JSON-bestanden in een schone tmp map komen
    monkeypatch.chdir(tmp_path)

def test_load_missing_file_returns_empty_list():
    assert JSONManager.load_data('nonexistent.json') == []

def test_save_and_load_roundtrip(tmp_path):
    data = [{'name':'Test','score': 42}]
    JSONManager.save_data('scores.json', data)
    loaded = JSONManager.load_data('scores.json')
    assert loaded == data

def test_load_corrupt_json_raises_error():
    # Maak map en corrupt bestand aan
    os.makedirs('data', exist_ok=True)
    path = os.path.join('data','bad.json')
    with open(path, 'w') as f:
        f.write('{invalid: json')
    with pytest.raises(json.JSONDecodeError):
        JSONManager.load_data('bad.json')


