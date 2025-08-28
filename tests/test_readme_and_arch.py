import os

def test_readme_exists():
    assert os.path.exists('README.md'), 'README.md must exist'

def test_architecture_exists():
    assert os.path.exists('architecture_detailed.png') or os.path.exists('architecture_polished.png'), 'Architecture image must exist'
