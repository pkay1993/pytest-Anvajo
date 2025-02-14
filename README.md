# Setup

- use your default python installation
- you have to install `pytest` in your applicable version
- running `python3 -m pytest` from the repository-root should be enough to run tests

# Tasks

1. Resolve Tests / Patch Implemenation
   - Resolve all issues until all tests are passing.
   - Each test explains the specification, assumption, task and optionally a hint.
2. Resolve all "TODO"s
3. Explain how logging is implemented
   - `src` implemented some logging mechanism
   - explain how it works
      - Logging is used fore further information during the tests and for debugging
      - Therefore we have functions like LOGGER.info for simple prints or LOGGER.debug for  values of variables (there is also WARNING, ERROR and CRITICAL)
4. Enable test report generation
   - modify so that a report.xml (JUnit-style) is generated on a test run
   - either use pytest configurations, VS Code settings or a specific command
      - python -m pytest --junitxml=report.xml
