# Developer Documentation

## Installing the source code {#installing-the-source-code}

### Steps

1. **Clone the Repository:**  
     
   ```
   git clone https://github.com/edwardyeung04/commitment-issues.git
   cd commitment-issues
   ```
     
3. **Install Dependencies:**  
     
   **Important:** This program requires OpenAI package version `0.28`.  
     
   `pip install openai==0.28 python-dotenv`
     
   Alternatively, using `requirements.txt`:  
     
   `pip install -r requirements.txt`
     
   **`requirements.txt` Content:**  
   ```
   openai
   python-dotenv  
   pytest  
   Pylint  
   ```
4. **Create a `.env` File:**  
     
   In the project root, create a file named `.env`:  
     
   `touch .env`
     
5. **Add Your OpenAI API Key:**  
     
   Open `.env` and add:  
     
   `OPENAI_API_KEY=your_openai_api_key_here`
     
   **Replace `your_openai_api_key_here` with your actual OpenAI API key.**  
     
   **Note:** The `.gitignore` includes `.env` to keep your API key private.

## Layout of Directory

Currently, we have the following directories in our repository.   
\- `.github/workflows`  
\- `cli\_interface`   
\- `git\_scripts`   
\- `openai\_integration`   
\- `tests`

The source files can be found in the `cli_interface`, `git_scripts`, and `openai_integration` directories. The `cli.py` file is also a source file that is in the root directory. Documentation can be found in the ReadMe in the root directory. Tests will be found in `tests`. The `.github/workflows` directory is for automated linting and testing. 

## How to Run the Project

To run the project, we use the Python interpreter (no “build” required).

`python cli.py [command] [flags]`

## How to Test

### How to run tests

Currently, we have a test suite under the `tests/` folder that has been implemented in Pytest and runs in continuous integration (CI) with GitHub Actions. Because of this, the GitHub Actions workflow runs the existing test suite on any push or pull request. Thus, to test, simply run a push ```git push``` or pull  ```git pull```
to the repository, and the system’s test cases will be run. Before attempting to test, ensure that all source code has been [properly installed](#installing-the-source-code).   
While currently work-in-progress, we plan to have a script to be able to manually run the test suite that is located in the tests/ folder. This section will be updated once the script has been properly set up. 

### How to add new tests

To add new tests, simply add a new test file to the `tests/` folder. Our current testing system is run using Pytest, as our codebase is written in Python. In general, there are no enforced naming conventions, however many tests are written in a file named `test_[insert-functionality]`, with each test file targeting a specific functionality or having a particular purpose when testing. 

**How to Build a Release of the Software**

**1\. Update the Version Number**  
Before building a release, ensure the version number is updated:

* Update the version in the main Python file or `__init__.py` file within your package (e.g., `__version__ = "x.y.z"`).  
* Update any version references in documentation files (like `README.md` or `CHANGELOG.md`).

**2\. Check Dependencies and Sanity Tests**  
Run a quick check to verify all dependencies are listed correctly in your `setup.py` or `pyproject.toml`, and run basic sanity checks:

* Run tests locally (e.g., `pytest`) to confirm everything is working as expected.  
* Use `flake8` or `pylint` to check for any code issues.

**3\. Build the Release**  
Use `setuptools` to build the package:

* Run `python setup.py sdist bdist_wheel` to generate source distributions and wheel files.

**4\. Perform Post-Build Verification**  
After building:

* Verify that the distribution files were created correctly in the `dist/` folder.  
* Test installing the package locally with `pip install dist/your_package_name-x.y.z.tar.gz` or `.whl` to confirm installation runs smoothly.

**5\. Upload to PyPI (Optional)**  
If the release is ready for public distribution:

* Use `twine upload dist/*` to upload the release to PyPI.

