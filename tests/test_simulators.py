import importlib
import os
import parameterized
import requests
import yaml
import shutil
import tempfile
import unittest

with open(os.path.join(os.path.dirname(__file__), 'simulators.yml'), 'r') as file:
    SIMULATORS = yaml.load(file, Loader=yaml.Loader)


EXAMPLES_BASE_URL = 'https://github.com/biosimulators/Biosimulators_test_suite/raw/deploy/examples'


class SimulatorsHaveValidApisTestCase(unittest.TestCase):
    def setUp(self):
        self.tmp_dirname = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.tmp_dirname)

    @parameterized.parameterized.expand(
        (simulator['id'], simulator)
        for simulator in SIMULATORS
    )
    def test(self, id, simulator):
        simulator_module = simulator['api']['module']
        example_combine_archive = simulator['exampleCombineArchive']
        tmp_dirname = self.tmp_dirname

        api = importlib.import_module(simulator_module)

        # __version__
        if not hasattr(api, '__version__'):
            raise NotImplementedError('API must have a `__version__` attribute whose value is a non-empty string (e.g., 1.0.1)')
        if not isinstance(api.__version__, str):
            raise ValueError('API must have a `__version__` attribute whose value is a non-empty string (e.g., 1.0.1), not `{}`'.format(
                api.__version__.__class__.__name__))
        if api.__version__ == '':
            raise ValueError('API must have a `__version__` attribute whose value is a non-empty string (e.g., 1.0.1), not `{}`'.format(
                api.__version__))

        # get_simulator_version
        if not hasattr(api, 'get_simulator_version'):
            raise NotImplementedError('API must have a `get_simulator_version` callable that returns a non-empty string (e.g., 1.0.1)')
        if not callable(api.get_simulator_version):
            raise ValueError('`get_simulator_version` must be a callable that returns a non-empty string (e.g., 1.0.1), not `{}`'.format(
                api.get_simulator_version.__class__.__name__))
        simulator_version = api.get_simulator_version()
        if not isinstance(simulator_version, str):
            raise ValueError('`get_simulator_version` must return a non-empty string (e.g., 1.0.1), not `{}`'.format(
                simulator_version.__class__.__name__))
        if simulator_version == '':
            raise ValueError('`get_simulator_version` must return a non-empty string (e.g., 1.0.1), not `{}`'.format(
                simulator_version))

        # exec_sedml_docs_in_combine_archive
        if not hasattr(api, 'exec_sedml_docs_in_combine_archive'):
            raise NotImplementedError('API must have a `exec_sedml_docs_in_combine_archive` callable')
        if not callable(api.exec_sedml_docs_in_combine_archive):
            raise ValueError('`exec_sedml_docs_in_combine_archive` must be a callable, not `{}`'.format(
                api.exec_sedml_docs_in_combine_archive.__class__.__name__))

        response = requests.get(EXAMPLES_BASE_URL + '/' + example_combine_archive)
        response.raise_for_status()
        archive_filename = os.path.join(tmp_dirname, 'archive.omex')
        with open(archive_filename, 'wb') as file:
            file.write(response.content)
        out_dir = os.path.join(tmp_dirname, 'out')
        results, log = api.exec_sedml_docs_in_combine_archive(archive_filename, out_dir,
                                                              return_results=True,
                                                              report_formats=None, plot_formats=None,
                                                              bundle_outputs=None, keep_individual_outputs=None,
                                                              raise_exceptions=True)

        # exec_sed_task
        if not hasattr(api, 'exec_sed_task'):
            raise NotImplementedError('API must have a `exec_sed_task` callable')
        if not callable(api.exec_sed_task):
            raise ValueError('`exec_sed_task` must be a callable, not `{}`'.format(
                api.exec_sed_task.__class__.__name__))
