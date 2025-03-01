from typing import Dict
from typing import List
from typing import Union

from cata.run.cata_config_template import CataConfigTemplate
from config_manager import base_configuration


class StudentTeacherConfig(base_configuration.BaseConfiguration):
    def __init__(self, config: Union[str, Dict], changes: List[Dict] = []) -> None:
        super().__init__(
            configuration=config,
            template=CataConfigTemplate.base_config_template,
            changes=changes,
        )
        self._validate_configuration()

    def _validate_configuration(self):
        """Method to check for non-trivial associations
        in the configuration.
        """
        pass
        # if self.teacher_configuration == constants.BOTH_ROTATION:
        #     assert self.scale_forward_by_hidden == True, (
        #         "In both rotation regime, i.e. mean field limit, "
        #         "need to scale forward by 1/K."
        #     )
        # else:
        #     assert self.scale_forward_by_hidden == False, (
        #         "When not in both rotation regime, i.e. mean field limit, "
        #         "no need to scale forward by 1/K."
        #     )
