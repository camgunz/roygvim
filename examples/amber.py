#!/usr/bin/env python

import enum

from roygvim import Attr, ColorScheme, Highlight, TRANSPARENT


class Colors(enum.IntEnum):

    Black = 0
    DriedBlood = 52
    Mud = 58
    ButterScotch = 94
    RedPaint = 124
    LemonGumdrop = 142
    Carrot = 166
    Papaya = 202
    Amber = 208
    Orange = 214
    Grey = 233
    Grey2 = 234


# olive = 3
# red_leather = 9
# yellow = 11
# tomato_soup = 88
# goldenrod = 100
# squash = 136
# firetruck = 160
# orange_bakelite = 172
# pineapple = 178
# lemon = 184
# red = 196
# yellow_bakelite = 220
# yellow = 226
# grey1 = 232

print(
    ColorScheme(
        description='Glowing amber color scheme',
        version='0.2',
        maintainer='Charlie Gunyon <charles.gunyon@gmail.com>',
        license="Vim license, see :help 'license'",
        highlights=[
            Highlight('Normal', Colors.Amber, TRANSPARENT),
            Highlight('NonText', Colors.Amber, TRANSPARENT),
            Highlight(
                'ColorColumn',
                Colors.Grey,
                Colors.Orange,
                Attr.Reverse,
                light_fg=Colors.Carrot,
                light_bg=Colors.Grey
            ),
            Highlight('Cursor', Colors.Amber, TRANSPARENT, Attr.Reverse),
            Highlight(
                'CursorColumn',
                Colors.Grey,
                Colors.Orange,
                Attr.Reverse,
                light_fg=Colors.Carrot,
                light_bg=Colors.Grey
            ),
            Highlight('CursorIM', Colors.Amber, TRANSPARENT, Attr.Reverse),
            Highlight(
                'CursorLine',
                Colors.Grey,
                Colors.Orange,
                Attr.Reverse,
                light_fg=Colors.Carrot,
                light_bg=Colors.Grey
            ),
            Highlight('CursorLineNr', Colors.Amber, TRANSPARENT),
            Highlight('Directory', Colors.Amber, TRANSPARENT),
            Highlight('ErrorMsg', Colors.Amber, TRANSPARENT),
            Highlight('FoldColumn', Colors.Amber, TRANSPARENT),
            Highlight('Folded', Colors.ButterScotch, Colors.Grey),
            Highlight('Conceal', Colors.Amber, TRANSPARENT),
            Highlight(
                'IncSearch',
                TRANSPARENT,
                Colors.Carrot,
                light_fg=TRANSPARENT,
                light_bg=Colors.Carrot
            ),
            Highlight('LineNr', Colors.Amber, TRANSPARENT),
            Highlight(
                'MatchParen',
                Colors.Grey2,
                Colors.Orange,
                Attr.Bold | Attr.Reverse
            ),
            Highlight('ModeMsg', Colors.Amber, TRANSPARENT),
            Highlight('MoreMsg', Colors.Amber, TRANSPARENT),
            Highlight('Pmenu', Colors.Carrot, Colors.Grey2),
            Highlight('PmenuSel', Colors.Carrot, Colors.Grey2, Attr.Reverse),
            Highlight('PmenuSbar', Colors.DriedBlood, Colors.Grey),
            Highlight(
                'PmenuThumb', Colors.Amber, Colors.RedPaint, Attr.Reverse
            ),
            Highlight('Question', Colors.Amber, TRANSPARENT),
            Highlight(
                'Search',
                TRANSPARENT,
                Colors.Carrot,
                light_fg=TRANSPARENT,
                light_bg=Colors.Carrot
            ),
            Highlight('SignColumn', Colors.Amber, TRANSPARENT),
            Highlight('SpecialKey', Colors.Orange, TRANSPARENT),
            Highlight('StatusLine', Colors.Amber, Colors.Grey, Attr.Reverse),
            Highlight('StatusLineNC', Colors.ButterScotch, Colors.Grey),
            Highlight(
                'StatusLineTerm', Colors.Amber, Colors.Grey, Attr.Reverse
            ),
            Highlight('StatusLineTermNC', Colors.ButterScotch, Colors.Grey),
            Highlight('TabLine', Colors.Amber, TRANSPARENT),
            Highlight('TabLineFill', Colors.Amber, TRANSPARENT),
            Highlight('TabLineSel', Colors.Orange, TRANSPARENT),
            Highlight('Title', Colors.Amber, Colors.Grey2),
            Highlight(
                'VertSplit',
                Colors.ButterScotch,
                Colors.Grey,
                light_fg=Colors.Grey,
                light_bg=Colors.Carrot,
                light_attrs=Attr.Reverse
            ),
            Highlight('vimNumber', Colors.Amber, TRANSPARENT),
            Highlight('vimHiAttrib', Colors.Amber, TRANSPARENT),
            Highlight(
                'Visual',
                TRANSPARENT,
                Colors.Carrot,
                light_fg=0,
                light_bg=Colors.Carrot
            ),
            Highlight('WildMenu', Colors.LemonGumdrop, TRANSPARENT),
            Highlight(
                'Comment',
                Colors.Mud,
                TRANSPARENT,
                light_fg=Colors.Grey,
                light_bg=Colors.Carrot
            ),
            Highlight('Constant', Colors.Amber, TRANSPARENT, Attr.Bold),
            Highlight('String', Colors.Amber, TRANSPARENT),
            Highlight('Character', Colors.Amber, TRANSPARENT),
            Highlight('Number', Colors.Amber, TRANSPARENT),
            Highlight('Boolean', Colors.Amber, TRANSPARENT, Attr.Bold),
            Highlight('Float', Colors.Amber, TRANSPARENT),
            Highlight('Identifier', Colors.Amber, TRANSPARENT),
            Highlight('Function', Colors.Amber, TRANSPARENT),
            Highlight('Statement', Colors.Amber, TRANSPARENT, Attr.Bold),
            Highlight('Conditional', Colors.Amber, TRANSPARENT, Attr.Bold),
            Highlight('Repeat', Colors.Amber, TRANSPARENT, Attr.Bold),
            Highlight('Label', Colors.Amber, TRANSPARENT, Attr.Bold),
            Highlight('Operator', Colors.Amber, TRANSPARENT, Attr.Bold),
            Highlight('Keyword', Colors.Amber, TRANSPARENT, Attr.Bold),
            Highlight('Exception', Colors.Amber, TRANSPARENT, Attr.Bold),
            Highlight('PreProc', Colors.Amber, TRANSPARENT, Attr.Bold),
            Highlight('Include', Colors.Amber, TRANSPARENT, Attr.Bold),
            Highlight('Define', Colors.Amber, TRANSPARENT, Attr.Bold),
            Highlight(
                'Macro',
                Colors.Amber,
                TRANSPARENT,
                Attr.Bold,
                light_fg=Colors.Grey2,
                light_bg=Colors.Amber
            ),
            Highlight('PreCondit', Colors.Amber, TRANSPARENT),
            Highlight('Type', Colors.Amber, TRANSPARENT, Attr.Bold),
            Highlight('StorageClass', Colors.Amber, TRANSPARENT, Attr.Bold),
            Highlight('Structure', Colors.Amber, TRANSPARENT, Attr.Bold),
            Highlight('Typedef', Colors.Amber, TRANSPARENT, Attr.Bold),
            Highlight('Special', Colors.Amber, TRANSPARENT),
            Highlight('SpecialChar', Colors.Amber, TRANSPARENT),
            Highlight('Tag', Colors.Amber, TRANSPARENT),
            Highlight('Delimiter', Colors.Amber, Colors.Grey2),
            Highlight('SpecialComment', Colors.Amber, TRANSPARENT),
            Highlight('Debug', Colors.Amber, TRANSPARENT),
            Highlight('Underlined', Colors.Amber, TRANSPARENT),
            Highlight('Ignore', Colors.Amber, TRANSPARENT),
            Highlight(
                'Error',
                Colors.RedPaint,
                TRANSPARENT,
                Attr.Bold,
                light_fg=Colors.Amber,
                light_bg=Colors.DriedBlood
            ),
            Highlight(
                'Todo',
                Colors.Amber,
                TRANSPARENT,
                light_fg=Colors.Grey2,
                light_bg=Colors.ButterScotch
            ),
            Highlight('DiffAdd', Colors.Papaya, Colors.Grey),
            Highlight('DiffChange', Colors.Amber, Colors.Grey),
            Highlight('DiffDelete', Colors.ButterScotch, Colors.Grey),
            Highlight('DiffText', Colors.Carrot, Colors.Grey),
            Highlight('diffAdded', Colors.Papaya, TRANSPARENT),
            Highlight('diffFile', Colors.Amber, Colors.Grey, Attr.Bold),
            Highlight('diffLine', Colors.Amber, TRANSPARENT),
            Highlight('diffRemoved', Colors.ButterScotch, Colors.Grey),
            Highlight(
                'SpellBad',
                Colors.Black,
                Colors.ButterScotch,
                light_fg=Colors.Amber,
                light_bg=Colors.DriedBlood
            ),
            Highlight(
                'SpellCap',
                Colors.Black,
                Colors.ButterScotch,
                light_fg=Colors.Amber,
                light_bg=Colors.DriedBlood
            ),
            Highlight('htmlBold', Colors.Amber, TRANSPARENT, Attr.Bold),
            Highlight('htmlItalic', Colors.Amber, Colors.Grey2, Attr.Italic),
            Highlight('htmlTitle', Colors.Amber, Colors.Grey2, Attr.Bold),
        ]
    ).render()
)
