import unittest
from elizabeth.builtins import JapanSpecProvider


class JapanTest(unittest.TestCase):
    def setUp(self):
        self.jp = JapanSpecProvider()

    def tearDown(self):
        del self.jp

    def test_full_to_half(self):
        # test full to half
        self.assertEqual(self.jp.full_to_half('パーフェクトでないこと'),
                         'ﾊﾟｰﾌｪｸﾄでないこと')
        self.assertEqual(self.jp.full_to_half('０１８９：；＠Ｇｍ＿ａｉＬＣＯＭ'),
                         '0189:;@Gm_aiLCOM')
        self.assertEqual(self.jp.full_to_half('test_2０ｴｰらー'), 'test_20ｴｰらｰ')

        # test full to half with alnum = Faise
        self.assertEqual(self.jp.full_to_half('パーフェクトでないこと', alnum=False),
                         'ﾊﾟｰﾌｪｸﾄでないこと')
        self.assertEqual(self.jp.full_to_half('０１８９：；＠Ｇｍ＿ａｉＬＣＯＭ', alnum=False),
                         '０１８９:;@Ｇｍ_ａｉＬＣＯＭ')
        self.assertEqual(self.jp.full_to_half('test_2０ｴｰらー', alnum=False),
                         'test_2０ｴｰらｰ')

    def test_half_to_full(self):
        # test half to full
        self.assertEqual(self.jp.half_to_full('ﾊﾟｰﾌｪｸﾄでないこと'),
                         'パーフェクトでないこと')
        self.assertEqual(self.jp.half_to_full('0189:;@Gm_aiLCOM'),
                         '０１８９：；＠Ｇｍ＿ａｉＬＣＯＭ')
        self.assertEqual(self.jp.half_to_full('ｔｅｓｔ＿２0エーらｰ'),
                         'ｔｅｓｔ＿２０エーらー')

        # test half to full with alnum = False
        self.assertEqual(self.jp.half_to_full('ﾊﾟｰﾌｪｸﾄでないこと', alnum=False),
                         'パーフェクトでないこと')
        self.assertEqual(self.jp.half_to_full('0189:;@Gm_aiLCOM', alnum=False),
                         '0189：；＠Gm＿aiLCOM')
        self.assertEqual(self.jp.half_to_full('ｔｅｓｔ＿２0エーらｰ', alnum=False),
                         'ｔｅｓｔ＿２0エーらー')
