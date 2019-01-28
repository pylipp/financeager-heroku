## Deploying `financeager` to heroku

This repository demonstrates how to deploy [`financeager`](https://github.com/pylipp/financeager) as flask webservice on heroku.

### Prerequisites

1. Sign up for heroku at https://signup.heroku.com/dc
1. Download the heroku toolbelt from https://toolbelt.heroku.com/

### Setting up the webservice

Clone this repository and change into it.

Login to heroku and create the app:

    heroku login
    heroku create

Trigger building of the app:

    git push heroku master

Check that web processes are running:

    heroku ps:scale web=1

### Using the webservice

Configure `financeager` to use your heroku app by editing `~/.config/financeager/config`. It should contain:

    [SERVICE]
    name = flask

    [SERVICE:FLASK]
    host = <heroku-app-name>.herokuapp.com

`<heroku-app-name>` is the output of `heroku apps`.
