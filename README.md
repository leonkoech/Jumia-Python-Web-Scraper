[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-v2.0%20adopted-ff69b4.svg)](code-of-conduct.md)
[![Python 3.7](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/downloads/release/python-360/)
[![Build status](https://ci.appveyor.com/api/projects/status/pjxh5g91jpbh7t84?svg=true)](https://ci.appveyor.com/project/tygerbytes/resourcefitness)
 [![Coverage Status](https://coveralls.io/repos/github/leonkoech/Jumia-Python-Web-Scraper/badge.svg?branch=master)](https://coveralls.io/github/leonkoech/Jumia-Python-Web-Scraper?branch=master)
# Simple Jumia Webscraping Module

The module scrapes the [Jumia Kenya website](jumia.co.ke) based on user query and dumps the results on a JSON file. The query may be choosing either one of the categories or searching the whole website or even selecting a product to observe for price changes. In all instances the name, the minimum and maximum price value is required to get a rough estimate of the product. User then selects the product to watch by entering it's price.
The background script then runs and sends a notification to devices subscribed to the notification channel. the notification contains the link to the webpage of the product.

The motivation for this product came from a friend who bought an electric iron for clothes for 1ksh(0.0099USD). He did this by constantly watching the price for changes. So I thought it'd be cool if a bot actually did that for you.
# Requirements
This package requires the following to run:

- [git](https://www.digitalocean.com/community/tutorials/how-to-install-git-on-ubuntu-18-04)  
- [python](https://www.python.org/downloads/)>=3.6
# Installation
First you have to clone the repo by writing the following code

 `git clone https://github.com/leonkoech/Jumia-Python-Web-Scraper`

Change directory to jumia python web scraper
 `cd Jumia-Python-Web-Scraper`

Then run  setup.py

`sudo python setup.py install`
# Usage
Change directory to scraper. Because that's where the main python file is
 `cd scraper`

Then run the python file

`python main.py`
# Contribution
You can contribute to this project.
To contribute to this project, clone repo locally and commit your code on a seperate branch.
You can find more details in my [Contributing guide](docs/contibuting.md)  
You can also reach me via [email](mailto:leonkipkip@gmail.com?subject=Python%20Web%29%Scraper) me or better yet, shoot me a [twitter](https://twitter.com/messages/compose?recipient_id=460904371) DM.

# license
Jumia Python Web Scraper is licensed under [MIT](#) license.  

