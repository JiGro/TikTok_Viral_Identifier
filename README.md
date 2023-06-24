# TikTok Insights Scraper

![Logo of the Project](https://cdn.pixabay.com/photo/2016/01/12/10/49/like-1135176_1280.jpg)

This script is used to scrape TikTok insights data from multiple user profiles and looks for viral video ideas.  It saves the results in an Excel file. The code utilizes the BeautifulSoup and Selenium libraries to extract the required information from the TikTok website.

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Installing
1. Make sure you have Python installed on your system (version 3.6 or later).

2. Clone the repository to your local machine
```
git clone https://github.com/JiGro/TikTok_Viral_Identifier.git
```

3. Install the required packages
```
pip install -r requirements.txt
```

4. Set Location and start url
```
########################################################################
INPUT_URL = ["https://www.tiktok.com/@cheatsheets",
             "https://www.tiktok.com/@mtholfsen",
             "https://www.tiktok.com/@informatikmentor",
             "https://www.tiktok.com/@tiffintech",
             "https://www.tiktok.com/@exceltips00"]
########################################################################
```

5. Run the code using the following command:
```
python Identify_Viral_Videos.py
```

## Authors
- **Jimmy (JiGro)** - *Initial work* - [My Github Profile](https://github.com/JiGro)
