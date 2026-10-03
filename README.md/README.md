->Recommended Execution Order

->For a complete fresh run, use this order:

->Step 1 — Generate dataset
python data/generate_dataset.py
->Step 2 — Generate SQL outputs
python part1_sql/run_queries.py
->Step 3 — Run Part 2 tests
python -m pytest part2_engine/test_growth_engine.py
->Step 4 — Run Part 3 tests
python -m pytest part3_narrative/test_masking.py
->Step 5 — Run Part 4 tests
python -m pytest part4_agent/test_mock_agent_runner.py
->Step 6 — Run the complete test suite
python -m pytest