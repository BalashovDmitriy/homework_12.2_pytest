import utils.dicts


def test_get_val():
    # {"vcs": "mercurial"}
    assert utils.dicts.get_val({"vcs": "mercurial"}, "vcs") == "mercurial"
    assert utils.dicts.get_val({"vcs": "mercurial"}, "vcs", "git") == "mercurial"
    # {}
    assert utils.dicts.get_val({}, "vcs", "git") == "git"
    assert utils.dicts.get_val({}, "vcs", "bazaar") == "bazaar"
