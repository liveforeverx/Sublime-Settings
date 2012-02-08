import sublime, sublime_plugin, os.path

class RunTetrapakCommand(sublime_plugin.WindowCommand):
    def run(self, task="build", **kwargs):
        current_file = self.window.active_view().file_name()
        for folder in self.window.folders():
            if current_file.startswith(folder):
                kwargs['working_dir'] = folder

        kwargs['cmd'] = ['tetrapak' + ' ' + task]
        kwargs['shell'] = True

        print kwargs

        self.window.run_command("exec", kwargs)

    def is_enabled(self, **kwargs):
        v = self.window.active_view()
        (v is not None) and (v.file_name() is not None) and ExecCommand.is_enabled(self, **kwargs)