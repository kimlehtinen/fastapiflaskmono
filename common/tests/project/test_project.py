
from common.core.project.project import Project


def test_to_dict__can_convert_to_dict():
    project = Project(title='test', id=1)

    assert project.to_dict() == {'id': 1, 'title': 'test'}
