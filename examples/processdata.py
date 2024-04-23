# Example Usage
#
# make sure that the package is installed or package directory is on pythonpath.
#
# in case if you are running py files from package git folders using cmd or terminal
# then set pythonpath. 
# for windows: set PYTHONPATH=C:\path\to\copilot4office;%PYTHONPATH%
# verify it by: echo %PYTHONPATH%
# for linux/mac: export PYTHONPATH=/path/to/simple_calculator:$PYTHONPATH
# verify it by: echo $PYTHONPATH 
#
# or from root of project, run it as: python -m examples.createpptx
# in that case the folder path for data shall be: r'examples\data\in\jsn.json' and
# r"examples\data\out\output_presentation.pptx"
#
# if you are using vscode then you can set python path in settings.json as:
    # "terminal.integrated.env.windows": {
    #     "PYTHONPATH": "${workspaceFolder}\\presentation"
    # },
    # "terminal.integrated.env.linux": {
    #     "PYTHONPATH": "${workspaceFolder}/presentation"
    # },
    # "terminal.integrated.env.osx": {
    #     "PYTHONPATH": "${workspaceFolder}/presentation"
    # },
    # "python.analysis.extraPaths": [
    #     "${workspaceFolder}/presentation"
    # ]
#
# Save it and then open new terminal to set the path. 
#
from presentation.presentation_processor import PresentationProcessor  

prsp= PresentationProcessor()
#if you are running python from project root then below shall be the path
#if you are running python from examples folder then path shall be: \data\in\presentation.txt
text =prsp.read_text_from_file(r'examples\data\in\presentation.txt')
jsn = prsp.text_to_json(text)
print(jsn)
#if you are running python from project root then below shall be the path
#if you are running python from examples folder then path shall be: \data\out\presentation.json
r = prsp.save_to_file(jsn, r'examples\data\out\presentation.json')
print(r)

