# SETUP
In order for this script to run you will need to do the following:
1. You will need python installed on your machine (you can get that from [here](https://www.python.org/)) and an IDE of your choice I use [PyCharm](https://www.jetbrains.com/pycharm/)
2. Clone this repo
3. Set up your virtual enviornment, [here](https://realpython.com/python-virtual-environments-a-primer/) is a great guide on this from the guys at Real Python (NOTE: this is not completely necessary however, it is recommended with python to have your dependecies tied to the project rather than your system)
4. install the following dependencies:
  * ``` pip install requests ```
  * ``` pip install python-dotenv ```

5. Now you need to create a .env file in the root directory (I did this to keep the API Key and Address private)
6. inside the .env file store the API credentials as DscoAuth and the API address as DscoURL (This wouldnt typically be neccessary but I did not want to expose these keys/addresses)
7. Now run the ItemStatus.py script

You should have the upc and quantityAvailable printed to the screen. This screenshot shows the output.
![Screenshot from 2021-06-14 14-20-14](https://user-images.githubusercontent.com/17036585/121954298-d5d13200-cd1b-11eb-883e-59c86e5ab301.png)
