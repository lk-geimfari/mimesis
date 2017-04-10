import pytest

from elizabeth.builtins.ja import JapanSpecProvider


@pytest.fixture
def jp():
    return JapanSpecProvider()


def test_full_to_half(jp):
    # test full to half
    assert jp.full_to_half('パーフェクトでないこと') == 'ﾊﾟｰﾌｪｸﾄでないこと'
    assert jp.full_to_half('０１８９：；＠Ｇｍ＿ａｉＬＣＯＭ') == '0189:;@Gm_aiLCOM'
    assert jp.full_to_half('test_2０ｴｰらー') == 'test_20ｴｰらｰ'

    # test full to half with alnum = Faise
    assert jp.full_to_half('パーフェクトでないこと', alnum=False) == 'ﾊﾟｰﾌｪｸﾄでないこと'
    assert jp.full_to_half('０１８９：；＠Ｇｍ＿ａｉＬＣＯＭ', alnum=False) == '０１８９:;@Ｇｍ_ａｉＬＣＯＭ'
    assert jp.full_to_half('test_2０ｴｰらー', alnum=False) == 'test_2０ｴｰらｰ'


def test_half_to_full(jp):
    # test half to full
    assert jp.half_to_full('ﾊﾟｰﾌｪｸﾄでないこと') == 'パーフェクトでないこと'
    assert jp.half_to_full('0189:;@Gm_aiLCOM') == '０１８９：；＠Ｇｍ＿ａｉＬＣＯＭ'
    assert jp.half_to_full('ｔｅｓｔ＿２0エーらｰ') == 'ｔｅｓｔ＿２０エーらー'

    # test half to full with alnum = False
    assert jp.half_to_full('ﾊﾟｰﾌｪｸﾄでないこと', alnum=False) == 'パーフェクトでないこと'
    assert jp.half_to_full('0189:;@Gm_aiLCOM', alnum=False) == '0189：；＠Gm＿aiLCOM'
    assert jp.half_to_full('ｔｅｓｔ＿２0エーらｰ', alnum=False) == 'ｔｅｓｔ＿２0エーらー'
