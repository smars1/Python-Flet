# devices/widgets/gauge_widget.py
from devices.widgets.base_widget import BaseWidget
import flet as ft

class GaugeWidget(BaseWidget):
    def __init__(self, name, value=0):
        super().__init__(name)
        self.value = value

    def build(self):
        # Flet no tiene un widget de gauge por defecto, pero puedes usar una barra de progreso circular como alternativa
        return
