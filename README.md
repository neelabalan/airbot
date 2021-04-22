# airbot (All India Radio bot) :radio:
> telegram bot for sending today's news in audio format 


## Setup

* Requirements

    * [Telegram bot token](https://core.telegram.org/bots) 
    * Adding the bot to a public channel with admin priveleges


The app can be deployed in [Heroku](https://devcenter.heroku.com) or whichever platform is comfortable and set the environment variables **TOKEN** with API token and **CHANNEL** with the channel name in format `@channel`

For Heroku I am using the [scheduler addon](https://devcenter.heroku.com/articles/scheduler) to run it everyday at a specified time


> The [`config.ini`](https://github.com/neelabalan/airbot/blob/master/config.ini) file is where the preferences are set 


## List of available AIR Stations 
> can be added in the `config.ini`


| Local                       | National  |   
| :-------------------------- | :-------- |
|                             |           |
| chennai-tamil               | english   |
| tiruchirapalli-tamil        | hindi     |
| agartala-kokborok           | sanskrit  |
| agartala-bengali            | tamil     |
| ahmedabad-gujarati          | urdu      |
| ahmedabad-sindhi            | assamese  |
| aizawl-mizo                 | bengali   |
| aurangabad-marathi          | dogri     |
| aurangabad-urdu             | gujarati  |
| bangalore-kannada           | kannada   |
| bhopal-hindi                | kashmiri  |
| bhuj-gujarati               | konkani   |
| calicut-malayalam           | malayalam |
| chandigarh-hindi            | marathi   |
| chandigarh-punjabi          | nepali    |
| cuttack-odia                | odia      |
| dehradun-hindi              | punjabi   |
| dharwad-kannada             | telugu    |
| dibrugarh-assamese          |
| gangtok-nepali              |
| gangtok-lepcha              |
| gangtok-bhutia              |
| gorakhpur-hindi             |
| gorakhpur-bhojpuri          |
| guwahati-assamese           |
| guwahati-karbi              |
| guwahati-nepali             |
| guwahati-bodo               |
| hyderabad-telugu            |
| hyderabad-urdu              |
| imphal-manipuri             |
| itanagar-hindi              |
| itanagar-english            |
| jaipur-hindi                |
| jaipur-rajasthani           |
| jammu-gojri                 |
| jammu-dogri                 |
| kohima-nagamese             |
| kohima-english              |
| kolkata-bengali             |
| kurseong-nepali             |
| leh-ladakhi                 |
| lucknow-hindi               |
| lucknow-urdu                |
| mumbai-marathi              |
| nagpur-marathi              |
| panaji-konkani              |
| patna-hindi                 |
| patna-maithili              |
| pudducherry-tamil           |
| pune-marathi                |
| raipur-chhatisgar           |
| raipur-hindi                |
| ranchi-hindi                |
| sambalpur-sambalpuri        |
| shillong-jaintia            |
| shillong-english            |
| shillong-khasi              |
| shillong-garo               |
| shimla-hindi                |
| silchar-bengali             |
| thiruvanantapuram-malayalam |
| vijayawada-telugu           |
| visakhapatnam-telugu        |


## Deploy

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)



## Screenshot

<img src="assets/screenshot.jpg" alt="screenshot" style="zoom: 50%;" />

