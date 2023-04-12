# Dashboards-with-Dash
This workshop is designed to introduce how to create dashboards using [Dash](https://dash.plotly.com/). The dashboard tracks common stock metrics retrieved from the unofficial Yahoo Finance wrapper API, [yahooquery](https://yahooquery.dpguthrie.com/).

Due to limitations of the official jupyter-dash library, which allows us to run Dash app within the notebook itself, this workshop will implement the Dash app in an unconvential way. We will use Jupyter Notebook to work on the files and write the files to a python file. 

### Installation
For both versions, you will need to download a version of Python < 3.10.

### Windows
It is ideal to run this with conda for easier installation.
1. Install anaconda https://docs.anaconda.com/anaconda/install/windows/
2. Open Anaconda Prompt from the Windows search bar and type the following commands
    1. `conda create --name Dash python=3.8` 
    2. `conda activate Dash`
    2. `pip install -r requirements.txt`

### Mac/Linux
It is ideal to run this in a virtual environment. To do this, run the following commands.
1. `pip install virtualenv`
2. `virtualenv venv`
3. `source venv/bin/activate`
4. `pip install -r requirements.txt`
5. `ipython kernel install --user --name=dash`

Then to launch the notebook, run `jupyter-lab` in the directory with the files.

### Workshop Files
* **Dashboard.ipynb** The fully completed version of the workshop notebook. Running this file will create the .py files needed to create the application
* **HandsOn_Dashboard** The uncompleted version of the workshop notebook. Code will be filled in during the workshop

Made for the Data Visualization Lab @ Georgia Tech. 
