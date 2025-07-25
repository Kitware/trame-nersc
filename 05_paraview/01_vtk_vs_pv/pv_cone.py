r"""
Installation requirements:
    pip install trame trame-vuetify trame-vtk
"""

from paraview import simple

from trame.app import TrameApp
from trame.decorators import change
from trame.ui.vuetify3 import SinglePageLayout
from trame.widgets import paraview as pv_widgets
from trame.widgets import vuetify3 as v3


class Cone(TrameApp):
    def __init__(self, server_or_name=None):
        super().__init__(server_or_name)
        self._setup_pv()
        self._build_ui()

    def _setup_pv(self):
        self.view = simple.GetActiveViewOrCreate("RenderView")
        self.view.SMProxy.render_window.OffScreenRenderingOn()

        self.cone = simple.Cone()
        simple.Show(self.cone, self.view)

    @change("resolution")
    def on_resolution_change(self, resolution, **_):
        self.cone.Resolution = resolution
        self.ctrl.view_update()

    @property
    def resolution(self):
        return self.state.resolution

    @resolution.setter
    def resolution(self, v):
        with self.state:
            self.state.resolution = v

    def reset_resolution(self):
        self.resolution = 6

    def _build_ui(self):
        with SinglePageLayout(self.server) as self.ui:
            self.ui.title.set_text("ParaView Cone")
            with self.ui.toolbar as toolbar:
                toolbar.density = "compact"
                v3.VSpacer()
                v3.VSlider(
                    v_model=("resolution", 6),
                    min=3,
                    max=60,
                    step=1,
                    hide_details=True,
                    style="max-width: 300px;",
                )
                v3.VBtn(icon="mdi-lock-reset", click=self.reset_resolution)
                v3.VBtn(icon="mdi-crop-free", click=self.ctrl.view_reset_camera)

            with self.ui.content:
                with v3.VContainer(fluid=True, classes="pa-0 fill-height"):
                    view = pv_widgets.VtkRemoteView(self.view)
                    self.ctrl.view_update = view.update
                    self.ctrl.view_reset_camera = view.reset_camera


def main(**kwargs):
    cone = Cone()
    cone.server.start(**kwargs)


if __name__ == "__main__":
    main()
