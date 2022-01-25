@pytest.fixture(params=['nodict', 'dict'])
def generate_initial_transform_parameters(request, mocker):
    [...]
    mocker.patch.object(outside_module, 'do_something')
    mocker.do_something.return_value(1)
    [...]

@pytest.fixture(params=['nodict', 'dict'])
def generate_initial_transform_parameters1(request, mocker):
    [...]
    mocker.patch.object(outside_module, 'do_something')
    mocker.do_something.side_effect([1, 2])
    [...]


