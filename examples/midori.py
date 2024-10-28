#!/usr/bin/env python

import enum

from roygvim import Attr, ColorScheme, Highlight


class Colors(enum.IntEnum):

    BrightRed = 1       # #800000
    BrightGreen = 2     # #008000
    ForestGreen = 22    # #005f00
    Teal = 23           # #005f5f
    GreenPaint = 28     # #008700
    SteelcaseGreen = 29 # #00875f
    SteelcaseBlue = 30  # #008787
    LimeGreen = 34      # #00af00
    Aquamarine = 37     # #00afaf
    DriedBlood = 52     # #5f0000
    Aubergine = 53      # #5f005f
    LightBlue = 66      # #5f8787
    SeaFoamGreen = 72   # #5faf87
    TomatoSoup = 88     # #870000
    Violet = 89         # #87005f
    Purple = 90         # #870087
    Lavender = 96       # #875f87
    RedPaint = 124      # #af0000
    OtherPurple = 127   # #af00af
    BrightPurple = 128  # #af00d7
    Mauve = 132         # #af5f87
    Gloop = 133         # #af5faf
    Fuchsia = 162       # #d70087
    HotPink = 200       # #ff00d7
    Peach = 223         # #ffd7af
    Black = 0           # #000000
    Grey1 = 232         # #080808
    Grey2 = 234         # #1c1c1c
    Grey3 = 235         # #262626
    Grey4 = 236         # #303030
    Grey5 = 238         # #444444
    Grey6 = 240         # #585858
    Grey7 = 59          # #5f5f5f
    Grey8 = 242         # #6c6c6c
    Grey9 = 245         # #8a8a8a
    Grey10 = 247        # #9e9e9e
    Grey11 = 248        # #a8a8a8
    Grey12 = 249        # #b2b2b2
    Grey13 = 250        # #bcbcbc
    Grey14 = 7          # #c0c0c0
    Grey15 = 252        # #d0d0d0
    Grey16 = 255        # #eeeeee
    White = 15          # #ffffff

DARK_FOREGROUND = Colors.White
DARK_BACKGROUND = Colors.Black

LIGHT_FOREGROUND = Colors.Black
LIGHT_BACKGROUND = Colors.White

BASIC = {
    'fg': DARK_FOREGROUND,
    'bg': DARK_BACKGROUND,
    'light_fg': LIGHT_FOREGROUND,
    'light_bg': LIGHT_BACKGROUND,
}
CURSOR_LINE = {
    'fg': DARK_FOREGROUND, 'bg': Colors.Grey4,
    'light_fg': LIGHT_FOREGROUND, 'light_bg': Colors.Grey13,
}
CURSOR_LINE_NR = {
    'fg': Colors.Fuchsia, 'bg': Colors.Grey4,
    'light_fg': Colors.Aubergine, 'light_bg': Colors.Grey9,
}
CONCEAL = {
    'fg': Colors.BrightGreen, 'bg': Colors.BrightRed,
    'light_fg': Colors.BrightGreen, 'light_bg': Colors.BrightRed
}
TAG = {
    'fg': Colors.Peach,
    'bg': DARK_BACKGROUND,
    'light_fg': Colors.Black,
    'light_bg': LIGHT_BACKGROUND,
}
DEBUG = {
    'fg': Colors.Peach, 'bg': DARK_BACKGROUND,
    'light_fg': Colors.Peach, 'light_bg': LIGHT_BACKGROUND,
}
VERT_SPLIT = {
    'fg': Colors.Grey1, 'bg': Colors.Grey1,
    'light_fg': Colors.Grey12, 'light_bg': Colors.Grey12,
}
STATUS_LINE = {
    'fg': DARK_BACKGROUND, 'bg': Colors.Grey10,
    'light_fg': LIGHT_FOREGROUND, 'light_bg': Colors.Grey12,
}
STATUS_LINE_REVERSED = {
    'fg': Colors.Grey3, 'bg': Colors.Grey10,
    'light_fg': Colors.Grey1, 'light_bg': Colors.Grey12,
    'attrs': Attr.Reverse
}
IGNORE = {
    'fg': Colors.Grey3, 'bg': DARK_BACKGROUND,
    'light_fg': LIGHT_FOREGROUND, 'light_bg': Colors.Grey3
}
COMMENT = {
    'fg': Colors.Grey6, 'bg': DARK_BACKGROUND, 'attrs': Attr.Bold,
    'light_fg': Colors.SteelcaseGreen, 'light_bg': Colors.Grey16,
    'light_attrs': Attr.Normal
}
TABLINE = {
    'fg': Colors.Grey8, 'bg': Colors.Grey1,
    'light_fg': LIGHT_FOREGROUND, 'light_bg': Colors.Grey12
}
ERROR = {
    'fg': Colors.Grey9, 'bg': Colors.Aubergine,
    'light_fg': Colors.White, 'light_bg': Colors.TomatoSoup
}
TYPE = {
    'fg': Colors.Gloop, 'bg': DARK_BACKGROUND,
    'light_fg': Colors.Purple, 'light_bg': LIGHT_BACKGROUND,
}
SEARCH = {
    'fg': DARK_FOREGROUND, 'bg': Colors.Aubergine,
    'light_fg': Colors.White, 'light_bg': Colors.Violet,
}
INC_SEARCH = {
    'fg': DARK_FOREGROUND, 'bg': Colors.Violet,
    'light_fg': Colors.White, 'light_bg': Colors.Violet,
}
FOLD = {'fg': Colors.Grey11, 'bg': Colors.Grey5}
DIFF_FILE = {
    'fg': Colors.Grey13, 'bg': Colors.ForestGreen,
    'light_fg': LIGHT_FOREGROUND, 'light_bg': Colors.Grey13
}
DIFF_INDEX_LINE = {
    'fg': Colors.Grey13, 'bg': Colors.ForestGreen,
    'light_fg': LIGHT_FOREGROUND, 'light_bg': Colors.Grey13
}
DIFF_TEXT = {
    'fg': DARK_FOREGROUND, 'bg': Colors.Aubergine,
    'light_fg': LIGHT_BACKGROUND, 'light_bg': Colors.Purple
}
DIFF_DELETE = {
    'fg': Colors.Grey13, 'bg': Colors.DriedBlood,
    'light_fg': LIGHT_BACKGROUND, 'light_bg': Colors.DriedBlood
}
DIFF_REMOVED = {
    'fg': Colors.Mauve, 'bg': DARK_BACKGROUND,
    'light_fg': LIGHT_BACKGROUND, 'light_bg': Colors.DriedBlood
}
DIFF_ADDED = {
    'fg': DARK_FOREGROUND, 'bg': Colors.ForestGreen,
    'light_fg': LIGHT_BACKGROUND, 'light_bg': Colors.ForestGreen
}
VISUAL = {
    'fg': Colors.Grey16, 'bg': Colors.ForestGreen,
    'light_fg': Colors.SteelcaseGreen, 'light_bg': Colors.Grey12,
}
GREY19_BOLD = {'fg': Colors.Grey16, 'bg': DARK_BACKGROUND, 'attrs': Attr.Bold}
TITLE = {
    'fg': Colors.GreenPaint, 'bg': DARK_BACKGROUND,
    'light_fg': Colors.GreenPaint, 'light_bg': LIGHT_BACKGROUND,
    'attrs': Attr.Bold
}
GREEN_PAINT = {
    'fg': Colors.GreenPaint, 'bg': DARK_BACKGROUND,
    'light_fg': Colors.ForestGreen, 'light_bg': LIGHT_BACKGROUND,
}
STEELCASE_GREEN = {
    'fg': Colors.SteelcaseGreen, 'bg': DARK_BACKGROUND,
    'light_fg': LIGHT_FOREGROUND, 'light_bg': LIGHT_BACKGROUND,
}
HTML_ITALIC = {
    'fg': Colors.LimeGreen, 'bg': Colors.Grey4,
    'light_fg': Colors.LimeGreen, 'light_bg': LIGHT_BACKGROUND,
}
SPECIAL = {
    'fg': Colors.Gloop, 'bg': DARK_BACKGROUND,
    'light_fg': Colors.Mauve, 'light_bg': LIGHT_BACKGROUND,
}
SPECIAL_CHAR = {
    'fg': Colors.RedPaint, 'bg': DARK_BACKGROUND,
    'light_fg': Colors.RedPaint, 'light_bg': LIGHT_BACKGROUND,
}
SPECIAL_KEY = {
    'fg': Colors.Aquamarine, 'bg': Colors.Grey3,
    'light_fg': Colors.HotPink, 'light_bg': LIGHT_BACKGROUND,
}
DELIMITER = {
    'fg': Colors.Lavender, 'bg': DARK_BACKGROUND,
    'light_fg': Colors.Grey2, 'light_bg': LIGHT_BACKGROUND,
    'attrs': Attr.Bold,
}
DEFINE = {
    'fg': Colors.Purple, 'bg': DARK_BACKGROUND,
    'light_fg': Colors.BrightPurple, 'light_bg': LIGHT_BACKGROUND,
}
MATCH_PAREN = {
    'fg': Colors.Aquamarine, 'bg': Colors.Grey3,
    'light_fg': Colors.SteelcaseBlue, 'light_bg': Colors.Grey13,
}
UNDERLINE = {'fg': Colors.Aquamarine, 'bg': Colors.Grey5}
DIRECTORY = {
    'fg': Colors.Aquamarine, 'bg': DARK_BACKGROUND,
    'light_fg': Colors.Aquamarine, 'light_bg': LIGHT_BACKGROUND,
}
SIGN_COLUMN = {
    'fg': Colors.Grey9, 'bg': DARK_BACKGROUND,
    'light_fg': Colors.Violet, 'light_bg': Colors.Grey14
}
LINE_NUMBER = {'fg': Colors.Grey7, 'bg': Colors.Grey1}
INCLUDE = {
    'fg': Colors.LightBlue, 'bg': DARK_BACKGROUND,
    'light_fg': Colors.SteelcaseBlue, 'light_bg': LIGHT_BACKGROUND,
}
LIGHT_BLUE = {
    'fg': Colors.LightBlue, 'bg': DARK_BACKGROUND,
    'light_fg': Colors.Teal, 'light_bg': LIGHT_BACKGROUND,
}
MACRO = {
    'fg': Colors.LightBlue, 'bg': DARK_BACKGROUND,
    'light_fg': Colors.Teal, 'light_bg': LIGHT_BACKGROUND,
    'attrs': Attr.Bold
}
COLOR_COLUMN = {
    'fg': Colors.LightBlue, 'bg': DARK_BACKGROUND,
    'light_fg': Colors.LightBlue, 'light_bg': LIGHT_BACKGROUND,
    'attrs': Attr.Reverse
}
ERROR_MESSAGE = {
    'fg': LIGHT_BACKGROUND, 'bg': Colors.TomatoSoup,
    'light_fg': Colors.Grey14, 'light_bg': Colors.TomatoSoup
}
LITERAL = {
    'fg': Colors.SteelcaseBlue, 'bg': DARK_BACKGROUND,
    'light_fg': Colors.SteelcaseBlue, 'light_bg': LIGHT_BACKGROUND,
}
STRING = {
    'fg': Colors.SeaFoamGreen, 'bg': DARK_BACKGROUND,
    'light_fg': Colors.SteelcaseGreen, 'light_bg': LIGHT_BACKGROUND,
}
HTML_BOLD = {
    'fg': DARK_FOREGROUND, 'bg': DARK_BACKGROUND,
    'light_fg': LIGHT_FOREGROUND, 'light_bg': LIGHT_BACKGROUND,
    'attrs': Attr.Bold
}
WHITE_REVERSED = {
    'fg': DARK_FOREGROUND, 'bg': DARK_BACKGROUND, 'attrs': Attr.Reverse
}
TODO = {
    'fg': Colors.LightBlue, 'bg': DARK_BACKGROUND,
    'light_fg': Colors.Violet, 'light_bg': Colors.Grey15
}
MENU = {
    'fg': DARK_FOREGROUND, 'bg': Colors.Grey4,
    'light_fg': LIGHT_FOREGROUND, 'light_bg': Colors.Grey10,
}
WILD_MENU = MENU
PMENU_SEL = {
    'fg': DARK_FOREGROUND, 'bg': Colors.Grey4,
    'light_fg': LIGHT_FOREGROUND, 'light_bg': Colors.Grey10,
    'attrs': Attr.Reverse
}
PMENU_SBAR = {'fg': Colors.ForestGreen, 'bg': Colors.Grey1}
PMENU_THUMB = {
    'fg': DARK_FOREGROUND, 'bg': Colors.LimeGreen, 'attrs': Attr.Reverse
}

print(
    ColorScheme(
        description='Color scheme for a 256-color terminal or GUI',
        version='0.6',
        maintainer='Charlie Gunyon <charlie@charlieg.net>',
        license="Vim license, see :help 'license'",
        highlights=[
            Highlight('Normal', **BASIC),
            Highlight('NonText', **BASIC),
            Highlight('ColorColumn', **COLOR_COLUMN),
            Highlight('Cursor', **WHITE_REVERSED),
            Highlight('CursorColumn', **CURSOR_LINE),
            Highlight('CursorIM', **WHITE_REVERSED),
            Highlight('CursorLine', **CURSOR_LINE),
            Highlight('CursorLineNr', **CURSOR_LINE_NR),
            Highlight('Directory', **DIRECTORY),
            Highlight('ErrorMsg', **ERROR_MESSAGE),
            Highlight('FoldColumn', **FOLD),
            Highlight('Folded', **FOLD),
            Highlight('Conceal', **CONCEAL),
            Highlight('IncSearch', **INC_SEARCH),
            Highlight('LineNr', **LINE_NUMBER),
            Highlight('MatchParen', **MATCH_PAREN),
            Highlight('ModeMsg', **BASIC),
            Highlight('MoreMsg', **BASIC),
            Highlight('Pmenu', **MENU),
            Highlight('PmenuSel', **PMENU_SEL),
            Highlight('PmenuSbar', **PMENU_SBAR),
            Highlight('PmenuThumb', **PMENU_THUMB),
            Highlight('Question', **SEARCH),
            Highlight('Search', **SEARCH),
            Highlight('SignColumn', **SIGN_COLUMN),
            Highlight('SpecialKey', **SPECIAL_KEY),
            Highlight('StatusLine', **STATUS_LINE),
            Highlight('StatusLineNC', **STATUS_LINE_REVERSED),
            Highlight('StatusLineTerm', **STATUS_LINE),
            Highlight('StatusLineTermNC', **STATUS_LINE_REVERSED),
            Highlight('TabLine', **TABLINE),
            Highlight('TabLineFill', **TABLINE),
            Highlight('TabLineSel', **BASIC),
            Highlight('Title', **TITLE),
            Highlight('VertSplit', **VERT_SPLIT),
            Highlight('vimNumber', **LITERAL),
            Highlight('vimHiAttrib', **STEELCASE_GREEN),
            Highlight('Visual', **VISUAL),
            Highlight('WildMenu', **MENU),
            Highlight('Comment', **COMMENT),
            Highlight('Constant', **LITERAL),
            Highlight('String', **STRING),
            Highlight('Character', **LITERAL),
            Highlight('Number', **LITERAL),
            Highlight('Boolean', **LITERAL),
            Highlight('Float', **LITERAL),
            Highlight('Identifier', **BASIC),
            Highlight('Function', **BASIC),
            Highlight('Statement', **GREEN_PAINT),
            Highlight('Conditional', **GREEN_PAINT),
            Highlight('Repeat', **GREEN_PAINT),
            Highlight('Label', **GREEN_PAINT),
            Highlight('Operator', **GREEN_PAINT),
            Highlight('Keyword', **GREEN_PAINT),
            Highlight('Exception', **GREEN_PAINT),
            Highlight('PreProc', **LIGHT_BLUE),
            Highlight('Include', **INCLUDE),
            Highlight('Define', **DEFINE),
            Highlight('Macro', **MACRO),
            Highlight('PreCondit', **LIGHT_BLUE),
            Highlight('Type', **TYPE),
            Highlight('StorageClass', **TYPE),
            Highlight('Structure', **TYPE),
            Highlight('Typedef', **TYPE),
            Highlight('Special', **SPECIAL),
            Highlight('SpecialChar', **SPECIAL_CHAR),
            Highlight('Tag', **TAG),
            Highlight('Delimiter', **DELIMITER),
            Highlight('SpecialComment', **DEBUG),
            Highlight('Debug', **DEBUG),
            Highlight('Underlined', **UNDERLINE),
            Highlight('Ignore', **IGNORE),
            Highlight('Error', **ERROR),
            Highlight('Todo', **TODO),
            Highlight('DiffAdd', **DIFF_ADDED),
            Highlight('DiffChange', **BASIC),
            Highlight('DiffDelete', **DIFF_DELETE),
            Highlight('DiffText', **DIFF_TEXT),
            Highlight('diffAdded', **DIFF_ADDED),
            Highlight('diffFile', **DIFF_FILE),
            Highlight('diffIndexLine', **DIFF_INDEX_LINE),
            Highlight('diffLine', **BASIC),
            Highlight('diffRemoved', **DIFF_REMOVED),
            Highlight('SpellBad', **ERROR),
            Highlight('SpellCap', **ERROR),
            Highlight('htmlBold', **HTML_BOLD),
            Highlight('htmlItalic', **HTML_ITALIC),
            Highlight('htmlTitle', **GREY19_BOLD),
        ]
    ).render()
)
