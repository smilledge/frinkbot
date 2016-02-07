# -*- coding: utf-8 -*-
import unittest
from lib.utils import parse_command_text


class CommandParserTest(unittest.TestCase):

    def test_parse_search_query(self):
        cmds = (
            ('d\'oh', 'd\'oh'),
            ('don\'t you hate pants?', 'don\'t you hate pants?'),
            (u'Aurora borealis.', u'Aurora borealis.'),
            ('nothing at all!', 'nothing at all!'),
            ('     Checkmate, Mr. Trampoline.     ', 'Checkmate, Mr. Trampoline.')
        )
        for cmd in cmds:
            query, caption = parse_command_text(cmd[0])
            self.assertEqual(query, cmd[1])
            self.assertIsNone(caption)

    def test_parse_caption(self):
        cmds = (
            ('nothing at all "Nothing at all..."  " ...  ', ('nothing at all', 'Nothing at all...')),
            ('   Aurora borealis. "At this time of year"   ', (u'Aurora borealis.', 'At this time of year')),
            (u'trampoline "Checkmate, Mr Trampoline"', (u'trampoline', u'Checkmate, Mr Trampoline'))
        )
        for cmd in cmds:
            query, caption = parse_command_text(cmd[0])
            self.assertEqual(query, cmd[1][0])
            self.assertEqual(caption, cmd[1][1])

    def test_parse_linebreaks(self):
        cmds = (
            ('nothing at all "Nothing at all... | Nothing at all... | Nothing at all..."  " ...  ', ('nothing at all', 'Nothing at all...\nNothing at all...\nNothing at all...')),
            ('am I out of touch "Am I out of touch? No it\'s the children who are wrong."', ('am I out of touch', 'Am I out of touch? No\nit\'s the children who are\nwrong.'))
        )
        for cmd in cmds:
            query, caption = parse_command_text(cmd[0])
            self.assertEqual(query, cmd[1][0])
            self.assertEqual(caption, cmd[1][1])

    def test_parse_special_quotes(self):
        query, caption = parse_command_text(u'trampoline “Checkmate, Mr Trampoline"')
        self.assertEqual(caption, u'Checkmate, Mr Trampoline', u'Did not convert curly quotes wrapping caption')
