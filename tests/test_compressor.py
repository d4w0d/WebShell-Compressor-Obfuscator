from code_compressor import CodeCompressor
from code_compressor.analyzer import analyze_code


def test_round_trip():
    source = "def add(a, b):\n    return a + b\n"
    c = CodeCompressor()
    assert c.decompress(c.compress(source)) == source


def test_analysis():
    result = analyze_code("x = eval(user_input)")
    assert "eval" in result["suspicious"]
    assert result["risk_score"] > 0
