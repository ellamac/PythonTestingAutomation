# EX 1
## Practice 1 - Python unit testing 

PythonTestingAutomation

Log in to GitHub and create a new public repository (you can delete or make it private afterwards) named "PythonTestingAutomation".

1. Create a local Git repository (for example, by using "git clone") that contains Python source code, for example from practice 1 earlier today. Your code can include unit tests, but this is not mandatory.
2. Then, commit and push your code to GitHub.
3. Make sure you can see the files in your web browser after Git push command (you might need to reload your page).

4. Then, create a GitHub Action that builds or lints and
5. optionally unit tests your source code. When creating the Action, you can use the
   ready-made workflow templates for Python, such as the one named "Python application".

6. Investigate how you can run your Action in GitHub.
7. How do you collect the results of the exection?

maybe done?

# EX 2
## Practice 2 - GitHub Actions and PyTest

PyTest is an alternative unit testing tool for Python, that is similar but slightly different than the built-in "unittest" module.

Take existing testing code from https://github.com/jani-jarvinen-itt/PythonTestingAutomation (or use your own code from yesterday)
and modify the testing code so that is compatible with PyTest: https://docs.pytest.org/en/7.4.x/.

Tip: PyTest requires testable files to use the naming convention "test_*.py" or "*_test.py".

Install PyTest locally, and run the tests to see if they succeed. Then, commit and push your changes to your own GitHub repository.
This "git push" should trigger the GitHub Action to run both Flake8 linting tool and the PyTest unit tests.

How can you verify that your unit tests were correctly executed?
