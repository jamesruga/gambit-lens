============================= test session starts ==============================
platform android -- Python 3.14.6, pytest-9.1.1, pluggy-1.6.0 -- /data/data/com.termux/files/usr/bin/python3.14
cachedir: .pytest_cache
rootdir: /data/data/com.termux/files/home/gambit-lens
configfile: pytest.ini
collecting ... collected 7 items

tests/test_agent.py::test_tactical_agent_fallback PASSED                 [ 14%]
tests/test_features.py::test_compute_centipawn_loss PASSED               [ 28%]
tests/test_features.py::test_empty_dataframe_features PASSED             [ 42%]
tests/test_ingestion.py::test_parse_pgn_to_dataframe PASSED              [ 57%]
tests/test_ingestion.py::test_ingestion_empty_pgn PASSED                 [ 71%]
tests/test_model.py::test_blunder_classifier_training PASSED             [ 85%]
tests/test_visuals.py::test_generate_centipawn_drift_svg FAILED          [100%]

=================================== FAILURES ===================================
______________________ test_generate_centipawn_drift_svg _______________________

tmp_path = PosixPath('/data/data/com.termux/files/usr/tmp/pytest-of-u0_a376/pytest-8/test_generate_centipawn_drift_0')

>   ???
E   assert 'GambitLens' in '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 360" width="100%" height="100%" style="background-color: #0d1117; border-radius: 10px; border: 1px solid #30363d;">\n    <path d="M 60.0,115.4 L 60.0,113.5 L 293.3,111.7 L 526.7,143.1 L 760.0,115.4 L 760.0,115.4 Z" fill="#58a6ff" fill-opacity="0.2" />\n    <path d="M 60.0,113.5 L 293.3,111.7 L 526.7,143.1 L 760.0,115.4" fill="none" stroke="#58a6ff" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>\n    <circle cx="60.0" cy="113.5" r="5" fill="#58a6ff" stroke="#0d1117" stroke-width="1.5"/><circle cx="293.3" cy="111.7" r="5" fill="#58a6ff" stroke="#0d1117" stroke-width="1.5"/><circle cx="526.7" cy="143.1" r="7" fill="#f85149" stroke="#ffffff" stroke-width="2"/><circle cx="760.0" cy="115.4" r="7" fill="#f85149" stroke="#ffffff" stroke-width="2"/><text x="60.0" y="335" fill="#8b949e" font-size="11" text-anchor="middle" font-family="sans-serif">e4</text><text x="293.3" y="335" fill="#8b949e" font-size="11" text-anchor="middle" font-family="sans-serif">e5</text><text x="526.7" y="335" fill="#8b949e" font-size="11" text-anchor="middle" font-family="sans-serif">g4</text><text x="760.0" y="335" fill="#8b949e" font-size="11" text-anchor="middle" font-family="sans-serif">Qh4#</text>\n</svg>'

/data/data/com.termux/files/home/GambitLens/tests/test_visuals.py:15: AssertionError
=============================== warnings summary ===============================
../../usr/lib/python3.14/site-packages/chess/engine.py:66
  /data/data/com.termux/files/usr/lib/python3.14/site-packages/chess/engine.py:66: DeprecationWarning: 'asyncio.AbstractEventLoopPolicy' is deprecated and slated for removal in Python 3.16
    class EventLoopPolicy(asyncio.AbstractEventLoopPolicy):

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
=========================== short test summary info ============================
FAILED tests/test_visuals.py::test_generate_centipawn_drift_svg - assert 'Gam...
==================== 1 failed, 6 passed, 1 warning in 2.08s ====================
