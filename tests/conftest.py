import pytest

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result() 
    test_fn = item.obj
    docstring = getattr(test_fn, '__doc__')
    if docstring:
        report.nodeid = docstring

@pytest.hookimpl(optionalhook=True)
def pytest_html_results_table_row(report, cells):
    for cell in cells:
        if cell.attr.class_ == "col-name":
            if hasattr(report, "docstring"):
                cell[0] = report.docstring
            break
