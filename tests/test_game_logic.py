from logic_utils import check_guess, get_range_for_difficulty, parse_guess, update_score

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"


# --- get_range_for_difficulty ---

def test_range_easy():
    low, high = get_range_for_difficulty("Easy")
    assert low == 1
    assert high == 20

def test_range_normal():
    low, high = get_range_for_difficulty("Normal")
    assert low == 1
    assert high == 100

def test_range_hard():
    low, high = get_range_for_difficulty("Hard")
    assert low == 1
    assert high == 50


# --- parse_guess ---

def test_parse_guess_valid():
    ok, value, err = parse_guess("42")
    assert ok == True
    assert value == 42
    assert err is None

def test_parse_guess_empty():
    ok, value, err = parse_guess("")
    assert ok == False
    assert value is None
    assert err == "Enter a guess."

def test_parse_guess_none():
    ok, value, err = parse_guess(None)
    assert ok == False
    assert value is None
    assert err == "Enter a guess."

def test_parse_guess_not_a_number():
    ok, value, err = parse_guess("abc")
    assert ok == False
    assert value is None
    assert err == "That is not a number."

def test_parse_guess_float_truncates():
    ok, value, err = parse_guess("7.9")
    assert ok == True
    assert value == 7
    assert err is None


# --- update_score ---

def test_update_score_win_increases_score():
    # A win should increase the score
    new_score = update_score(0, "Win", 1)
    assert new_score > 0

def test_update_score_wrong_guess_no_decrement():
    # A wrong guess should not decrease the score below its starting value
    score_after_too_high = update_score(0, "Too High", 1)
    score_after_too_low = update_score(0, "Too Low", 1)
    assert score_after_too_high >= 0
    assert score_after_too_low >= 0
