import importlib.util

import pytest


@pytest.fixture
def solution(request):
    """Загружает solution.py из папки теста и возвращает экземпляр Solution."""
    path = request.path.parent / "solution.py"
    spec = importlib.util.spec_from_file_location(f"solution_{path.parent.name}", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.Solution()
