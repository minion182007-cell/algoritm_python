import importlib.util

import pytest


def pytest_generate_tests(metafunc):
    """Запускает каждый тест для всех файлов solution*.py в папке задачи."""
    if "solution" in metafunc.fixturenames:
        paths = sorted(metafunc.definition.path.parent.glob("solution*.py"))
        metafunc.parametrize("solution", paths, ids=[p.stem for p in paths], indirect=True)


@pytest.fixture
def solution(request):
    """Загружает файл решения и возвращает экземпляр Solution."""
    path = request.param
    spec = importlib.util.spec_from_file_location(f"{path.stem}_{path.parent.name}", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.Solution()
