from biosimulators_utils.config import get_config
from biosimulators_utils.combine.io import CombineArchiveReader
from biosimulators_utils.combine.utils import get_sedml_contents
from biosimulators_utils.log.data_model import CombineArchiveLog
from biosimulators_utils.sedml.data_model import Report, Plot2D, Plot3D
from biosimulators_utils.sedml.io import SedmlSimulationReader
import importlib
import numpy
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

        config = get_config()
        config.COLLECT_COMBINE_ARCHIVE_RESULTS = True
        config.COLLECT_SED_DOCUMENT_RESULTS = True
        config.DEBUG = True

        results, log = api.exec_sedml_docs_in_combine_archive(archive_filename, out_dir, config=config)

        archive_dirname = os.path.join(self.tmp_dirname, 'archive')
        archive = CombineArchiveReader().run(archive_filename, archive_dirname)
        sedml_contents = get_sedml_contents(archive)

        self.assertIsInstance(results, dict)
        self.assertEquals(set(results.keys()), set(sedml_content.location for sedml_content in sedml_contents))
        for sedml_content in sedml_contents:
            sed_doc = SedmlSimulationReader().run(os.path.join(archive_dirname, sedml_content.location))

            doc_results = results[sedml_content.location]
            self.assertIsInstance(doc_results, dict)
            self.assertEquals(set(doc_results.keys()), set(output.id for output in sed_doc.outputs))

            for output in sed_doc.outputs:
                output_results = doc_results[output.id]
                self.assertIsInstance(output_results, dict)
                if isinstance(output, Report):
                    data_set_ids = set(data_set.id for data_set in output.data_sets)

                elif isinstance(output, Plot2D):
                    data_set_ids = set()
                    for curve in output.curves:
                        data_set_ids.add(curve.x_data_generator.id)
                        data_set_ids.add(curve.y_data_generator.id)

                elif isinstance(output, Plot3D):
                    data_set_ids = set()
                    for surface in output.surfaces:
                        data_set_ids.add(surface.x_data_generator.id)
                        data_set_ids.add(surface.y_data_generator.id)
                        data_set_ids.add(surface.z_data_generator.id)

                else:
                    raise NotImplementedError('Outputs of type `{}` are not supported'.format(output.__class__.__name__))

                self.assertEquals(set(output_results.keys()), data_set_ids)

                for data_set_id in data_set_ids:
                    data_set_results = output_results[data_set_id]
                    self.assertIsInstance(data_set_results, numpy.ndarray)
                    self.assertGreater(data_set_results.size, 0)
                    self.assertFalse(numpy.any(numpy.isnan(data_set_results)))

        self.assertGreater(len(results), 0)
        self.assertIsInstance(log, CombineArchiveLog)

        # exec_sed_doc
        if not hasattr(api, 'exec_sed_doc'):
            raise NotImplementedError('API must have a `exec_sed_doc` callable')
        if not callable(api.exec_sed_doc):
            raise ValueError('`exec_sed_doc` must be a callable, not `{}`'.format(
                api.exec_sed_doc.__class__.__name__))

        # exec_sed_task
        if not hasattr(api, 'exec_sed_task'):
            raise NotImplementedError('API must have a `exec_sed_task` callable')
        if not callable(api.exec_sed_task):
            raise ValueError('`exec_sed_task` must be a callable, not `{}`'.format(
                api.exec_sed_task.__class__.__name__))

        # preprocess_sed_task
        if not hasattr(api, 'preprocess_sed_task'):
            raise NotImplementedError('API must have a `preprocess_sed_task` callable')
        if not callable(api.preprocess_sed_task):
            raise ValueError('`preprocess_sed_task` must be a callable, not `{}`'.format(
                api.preprocess_sed_task.__class__.__name__))
