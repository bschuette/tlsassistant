from modules.server.testssl_base import Testssl_base


class Drown(Testssl_base):

    # to override
    def _set_arguments(self):
        self._arguments = ["-D"]

    # to override
    def _worker(self, results):
        return self._obtain_results(results, ["DROWN", "DROWN_hint"])
