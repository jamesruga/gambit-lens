============================= test session starts ==============================
platform android -- Python 3.14.6, pytest-9.1.1, pluggy-1.6.0 -- /data/data/com.termux/files/usr/bin/python3.14
cachedir: .pytest_cache
rootdir: /data/data/com.termux/files/home/GambitLens
configfile: pytest.ini
collecting ... collected 7 items

tests/test_agent.py::test_tactical_agent_fallback PASSED                 [ 14%]
tests/test_features.py::test_compute_centipawn_loss PASSED               [ 28%]
tests/test_features.py::test_empty_dataframe_features PASSED             [ 42%]
tests/test_ingestion.py::test_parse_pgn_to_dataframe PASSED              [ 57%]
tests/test_ingestion.py::test_ingestion_empty_pgn PASSED                 [ 71%]
tests/test_model.py::test_blunder_classifier_training PASSED             [ 85%]
tests/test_visuals.py::test_generate_centipawn_drift_svg PASSED          [100%]

=============================== warnings summary ===============================
../../usr/lib/python3.14/site-packages/chess/engine.py:66
  /data/data/com.termux/files/usr/lib/python3.14/site-packages/chess/engine.py:66: DeprecationWarning: 'asyncio.AbstractEventLoopPolicy' is deprecated and slated for removal in Python 3.16
    class EventLoopPolicy(asyncio.AbstractEventLoopPolicy):

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
========================= 7 passed, 1 warning in 2.21s =========================
