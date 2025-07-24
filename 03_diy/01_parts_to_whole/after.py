from trame.app import TrameApp
from trame.decorators import change

from trame.widgets import html
from trame.ui.html import DivLayout


class App(TrameApp):
    def __init__(self, server=None):
        super().__init__(server)

        # Read/Write
        self.state.a = 1
        self.state["b"] = self.state.a * 2

        # Generate UI
        self._build_ui()

    def reset_a(self):
        self.state.a = 10

    def _build_ui(self):
        with DivLayout(self.server) as self.ui:
            html.H1("Events and State")
            html.Div("a={{ a }} and b={{ b }}")

            html.H2("Events")
            html.Button("Reset a", click=self.reset_a)
            html.Button("Reset a & b", click="setAll({ b:2, a:1 })")
            html.Button("Reset log", click="log = ''")

            html.H2("States")
            html.Input(type="range", min=0, max=10, v_model="a")
            html.Input(type="range", min=0, max=30, v_model="b")

            html.Br()

            html.Textarea(
                v_model=("log", ""),
                disabled=True,
                rows=12,
                style="width: 15rem;",
            )

    # Reactivity methods
    @change("a")
    def _on_a_change(self, a, **_):
        self.state.b = int(a) * 2

    @change("a", "b")
    def _on_ab_change(self, **_):
        msg = ["\nChanges to"]
        for var_name in self.state.modified_keys & {"a", "b"}:
            msg.append(f"{var_name}={self.state[var_name]}")

        self.state.log += " ".join(msg)

    @change("log")
    def _trim_log(self, log, **_):
        lines = log.split("\n")
        if len(lines) > 10:
            self.state.log = "\n".join(lines[-10:])


# -----------------------------------------------------------------------------
# In case you want to run it from the CLI
# -----------------------------------------------------------------------------
def main():
    app = App()
    app.server.start()


if __name__ == "__main__":
    main()
