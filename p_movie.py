import webbrowser
class p_mv:
    def __init__(self,pmv_name,pmv_line,pmv_poster,pmv_trailer):
        self.pmv_name=pmv_name
        self.pmv_line=pmv_line
        self.pmv_poster=pmv_poster
        self.pmv_trailer=pmv_trailer
    def open_trailer(self):
        webbrowser.open(self.pmv_trailer)
