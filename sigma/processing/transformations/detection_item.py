from typing import Optional
from dataclasses import dataclass
from sigma.processing.transformations.base import (
    DetectionItemTransformation,
)
from sigma.rule import SigmaDetection, SigmaDetectionItem


@dataclass
class DropDetectionItemTransformation(DetectionItemTransformation):
    """Deletes detection items. This should only used in combination with a detection item
    condition."""

    class DeleteSigmaDetectionItem(SigmaDetectionItem):
        """Class is used to mark detection item as to be deleted. It's just for having all the
        detection item functionality available."""

        @classmethod
        def create(cls):
            return cls(None, [], [])

    def apply_detection_item(
        self, detection_item: SigmaDetectionItem
    ) -> Optional[SigmaDetectionItem]:
        """This function only marks detection items for deletion."""
        return self.DeleteSigmaDetectionItem.create()

    def apply_detection(self, detection: SigmaDetection):
        super().apply_detection(detection)
        detection.detection_items = list(
            filter(
                lambda d: not isinstance(d, self.DeleteSigmaDetectionItem),
                detection.detection_items,
            )
        )
