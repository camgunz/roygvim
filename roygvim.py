import enum
import textwrap


TRANSPARENT = 'none'


class Attr(enum.Flag):

    Normal = enum.auto()
    Bold = enum.auto()
    Underline = enum.auto()
    Undercurl = enum.auto()
    Strikethrough = enum.auto()
    Reverse = enum.auto()
    Inverse = enum.auto()
    Italic = enum.auto()
    Standout = enum.auto()
    NoCombine = enum.auto()

    @property
    def attr_name(self):
        name = str(self.name)
        return 'none' if name == 'Normal' else name.lower()

    def __str__(self):
        return ','.join([
            v.attr_name for n, v in Attr.__members__.items() if self & v
        ])


COLOR_TABLE = [
    '#000000', '#800000', '#008000', '#808000', # 0-3
    '#000080', '#800080', '#008080', '#c0c0c0', # 4-7
    '#808080', '#ff0000', '#00ff00', '#ffff00', # 8-11
    '#0000ff', '#ff00ff', '#00ffff', '#ffffff', # 12-15
    '#000000', '#00005f', '#000087', '#0000af', '#0000d7', '#0000ff', # 16-21
    '#005f00', '#005f5f', '#005f87', '#005faf', '#005fd7', '#005fff', # 22-27
    '#008700', '#00875f', '#008787', '#0087af', '#0087d7', '#0087ff', # 28-33
    '#00af00', '#00af5f', '#00af87', '#00afaf', '#00afd7', '#00afff', # 34-39
    '#00d700', '#00d75f', '#00d787', '#00d7af', '#00d7d7', '#00d7ff', # 40-45
    '#00ff00', '#00ff5f', '#00ff87', '#00ffaf', '#00ffd7', '#00ffff', # 46-51
    '#5f0000', '#5f005f', '#5f0087', '#5f00af', '#5f00d7', '#5f00ff', # 52-57
    '#5f5f00', '#5f5f5f', '#5f5f87', '#5f5faf', '#5f5fd7', '#5f5fff', # 58-63
    '#5f8700', '#5f875f', '#5f8787', '#5f87af', '#5f87d7', '#5f87ff', # 64-69
    '#5faf00', '#5faf5f', '#5faf87', '#5fafaf', '#5fafd7', '#5fafff', # 70-75
    '#5fd700', '#5fd75f', '#5fd787', '#5fd7af', '#5fd7d7', '#5fd7ff', # 76-81
    '#5fff00', '#5fff5f', '#5fff87', '#5fffaf', '#5fffd7', '#5fffff', # 82-87
    '#870000', '#87005f', '#870087', '#8700af', '#8700d7', '#8700ff', # 88-93
    '#875f00', '#875f5f', '#875f87', '#875faf', '#875fd7', '#875fff', # 94-99
    '#878700', '#87875f', '#878787', '#8787af', '#8787d7', '#8787ff', # 100-105
    '#87af00', '#87af5f', '#87af87', '#87afaf', '#87afd7', '#87afff', # 106-111
    '#87d700', '#87d75f', '#87d787', '#87d7af', '#87d7d7', '#87d7ff', # 112-117
    '#87ff00', '#87ff5f', '#87ff87', '#87ffaf', '#87ffd7', '#87ffff', # 118-123
    '#af0000', '#af005f', '#af0087', '#af00af', '#af00d7', '#af00ff', # 124-129
    '#af5f00', '#af5f5f', '#af5f87', '#af5faf', '#af5fd7', '#af5fff', # 130-135
    '#af8700', '#af875f', '#af8787', '#af87af', '#af87d7', '#af87ff', # 136-141
    '#afaf00', '#afaf5f', '#afaf87', '#afafaf', '#afafd7', '#afafff', # 142-147
    '#afd700', '#afd75f', '#afd787', '#afd7af', '#afd7d7', '#afd7ff', # 148-153
    '#afff00', '#afff5f', '#afff87', '#afffaf', '#afffd7', '#afffff', # 154-159
    '#d70000', '#d7005f', '#d70087', '#d700af', '#d700d7', '#d700ff', # 160-165
    '#d75f00', '#d75f5f', '#d75f87', '#d75faf', '#d75fd7', '#d75fff', # 166-171
    '#d78700', '#d7875f', '#d78787', '#d787af', '#d787d7', '#d787ff', # 172-177
    '#d7af00', '#d7af5f', '#d7af87', '#d7afaf', '#d7afd7', '#d7afff', # 178-183
    '#d7d700', '#d7d75f', '#d7d787', '#d7d7af', '#d7d7d7', '#d7d7ff', # 184-189
    '#d7ff00', '#d7ff5f', '#d7ff87', '#d7ffaf', '#d7ffd7', '#d7ffff', # 190-195
    '#ff0000', '#ff005f', '#ff0087', '#ff00af', '#ff00d7', '#ff00ff', # 196-201
    '#ff5f00', '#ff5f5f', '#ff5f87', '#ff5faf', '#ff5fd7', '#ff5fff', # 202-207
    '#ff8700', '#ff875f', '#ff8787', '#ff87af', '#ff87d7', '#ff87ff', # 208-213
    '#ffaf00', '#ffaf5f', '#ffaf87', '#ffafaf', '#ffafd7', '#ffafff', # 214-219
    '#ffd700', '#ffd75f', '#ffd787', '#ffd7af', '#ffd7d7', '#ffd7ff', # 220-225
    '#ffff00', '#ffff5f', '#ffff87', '#ffffaf', '#ffffd7', '#ffffff', # 226-231
    '#080808', '#121212', '#1c1c1c', '#262626', '#303030', '#3a3a3a', # 232-237
    '#444444', '#4e4e4e', '#585858', '#626262', '#6c6c6c', '#767676', # 238-243
    '#808080', '#8a8a8a', '#949494', '#9e9e9e', '#a8a8a8', '#b2b2b2', # 244-249
    '#bcbcbc', '#c6c6c6', '#d0d0d0', '#dadada', '#e4e4e4', '#eeeeee', # 250-255
]


class Highlight:

    def __init__(self, syntax, fg, bg, attrs=Attr.Normal,
                 light_fg=None, light_bg=None, light_attrs=None):
        self.syntax = syntax
        self.fg = fg
        self.bg = bg
        self.attrs = attrs
        self.guifg = COLOR_TABLE[0 if self.fg == TRANSPARENT else self.fg]
        self.guibg = COLOR_TABLE[0 if self.bg == TRANSPARENT else self.bg]
        self.light_fg = light_fg if light_fg is not None else bg
        self.light_bg = light_bg if light_bg is not None else fg
        self.light_attrs = light_attrs or attrs
        if self.light_fg == TRANSPARENT:
            self.light_fg = 0
            self.light_guifg = '#000000'
        else:
            self.light_guifg = COLOR_TABLE[self.light_fg]
        if self.light_bg == TRANSPARENT:
            self.light_guibg = '#000000'
        else:
            self.light_guibg = COLOR_TABLE[self.light_bg]

    def render_dark(self):
        return (
            f'  hi {self.syntax:<31} '
            f'ctermfg={self.fg:<4} '
            f'ctermbg={self.bg:<4} '
            f'cterm={self.attrs:<7} '
            f'guifg={self.guifg:<4} '
            f'guibg={self.guibg:<4} '
            f'gui={self.attrs}'
        )

    def render_light(self):
        return (
            f'  hi {self.syntax:<31} '
            f'ctermfg={self.light_fg:<4} '
            f'ctermbg={self.light_bg:<4} '
            f'cterm={self.light_attrs:<7} '
            f'guifg={self.light_guifg:<4} '
            f'guibg={self.light_guibg:<4} '
            f'gui={self.light_attrs}'
        )


class ColorScheme:

    def __init__(self, description, maintainer, version, license, highlights):
        self.description = description
        self.maintainer = maintainer
        self.version = version
        self.license = license
        self.highlights = highlights

    def render(self):
        return '\n'.join([
            textwrap.dedent(
                f"""\
                " {self.description}
                " Maintainer:  {self.maintainer}
                " Version:     {self.version}
                " License:     {self.license}

                if version > 580
                    hi clear
                    if exists("syntax_on")
                      syntax reset
                    endif
                endif

                let g:colors_name = expand("<sfile>:t:r")
                """
            ),
            'if &background == "dark" " set background=dark',
            '\n'.join([cd.render_dark() for cd in self.highlights]),
            'else',
            '\n'.join([cd.render_light() for cd in self.highlights]),
            'endif'
        ])
