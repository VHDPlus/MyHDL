# MyHDL
## Setup
For Windows make sure you have Python and pip is installed
- Install Python here: https://www.python.org/downloads/
- Download https://bootstrap.pypa.io/get-pip.py
- Install pip using `python get-pip.py`

Install MyHDL using `pip install myhdl`

## Program
1. Clone or download and extract this repository
2. Open the VHDPlus project and program your code with MyHDL: <br/>
http://www.myhdl.org/docs/examples/ <br/>
http://docs.myhdl.org/en/stable/manual/rtl.html
3. After you finished coding, open `Terminal/New Terminal` in the IDE and convert the python file using `python [filename].py` 
(Check if `Extras/Settings/Detect external file changes` is enabled)
4. The file blinky.vhd is created after running the python file. Import other created vhdl files, if you change the code.
5. If you use the MyHDL code together with VHDP, make sure your file with the `Main` component uses the new updated component and click on `Compile`
