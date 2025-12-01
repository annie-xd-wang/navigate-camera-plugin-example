
from typing import Any, Optional
from navigate.model.devices.camera.base import CameraBase
class MyCamera(CameraBase):
    def __init__(
        self,
        microscope_name: str,
        device_connection: Any,
        configuration: dict[str, Any],
        *args: Optional[Any],
        **kwargs: Optional[Any],
    ) -> None:
        super().__init__(
            microscope_name, device_connection, configuration, *args, **kwargs
        )

    def set_ROI(
        self,
        roi_width: int = 2048,
        roi_height: int = 2048,
        center_x: int = 1024,
        center_y: int = 1024,
    ) -> bool:
        return True
    
    def set_binning(self, binning: str = "1x1") -> bool:
        return True
    
    def set_trigger_mode(self, trigger_source: str = "External") -> None:
        """Set the camera trigger source to external or internal free run mode.

        This abstract method must be implemented by all subclasses.

        Parameters
        ----------
        trigger_source : str
            Trigger source. Options are 'External' or 'Internal'.
        """
        pass

    def set_sensor_mode(self, mode: str) -> None:
        """Set camera sensor mode.

        Parameters
        ----------
        mode : str
            Sensor mode. Options are 'Normal' or 'Light-Sheet'.
        """
        pass

    @property
    def commands(self):
        """Return commands dictionary

        Returns
        -------
        commands : dict
            commands that the device supports
        """
        return {"move_plugin_device": lambda *args: self.move(args[0])}

    def move(self, *args):
        """An example function: to move the device"""
        print("move device", args)
        pass
