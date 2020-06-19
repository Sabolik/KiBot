from pcbnew import PLOT_FORMAT_DXF
from .error import KiPlotConfigurationError
from .out_base import (BaseOutput)
from .out_any_layer import (AnyLayer)


class DXF(AnyLayer):
    def __init__(self, name, type, description):
        super(DXF, self).__init__(name, type, description)
        self._plot_format = PLOT_FORMAT_DXF
        # Options
        self.use_aux_axis_as_origin = False
        self._drill_marks = 'full'
        self.polygon_mode = True
        self.sketch_plot = True

    @property
    def drill_marks(self):
        return self._drill_marks

    @drill_marks.setter
    def drill_marks(self, val):
        if val not in self._drill_marks_map:
            raise KiPlotConfigurationError("Unknown drill mark type: {}".format(val))
        self._drill_marks = val

    def config(self, outdir, options, layers):
        super().config(outdir, options, layers)
        self._drill_marks = self._drill_marks_map[self._drill_marks]

    def _configure_plot_ctrl(self, po, output_dir):
        super()._configure_plot_ctrl(po, output_dir)
        po.SetDXFPlotPolygonMode(self.polygon_mode)


# Register it
BaseOutput.register('dxf', DXF)
