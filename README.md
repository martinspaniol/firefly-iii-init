# firefly-iii-init

This docker container gives you the possibility to configure [Firefly-III][Firefly-III] with some default values after you have a fresh installation. Basically you can add anything which the [Firefly-III API][Firefly-III API] provides like
* Accounts including Name, IBAN, BIC, opening balance
* Categories with their name and notes
and many more. In theory everything which the official API provides can be added in the configuration.

## Usage

### Step 1: Create a personal access token

To use the REST API of Firefly-III you need a personal access token. You can [create a token as described in the official Firefly-III documentation][Firefly-III Create Token].

### Step 2: Create a configuration file

Next you have to provide the necessary details in the configuration file in json format. An example is provided in this repo [here][example-configuration]. It looks like this:

```json
{
    "settings": {
        "host": "http://firefly:8080", // <<< this is the URL to your Firefly-III installation
        "token": "VeryLongSecretToken" // <<< this is your personal access token
    },
    "accounts": {
        "url": "/api/v1/accounts",
        "accounts": [ // <<< here you can create accounts
            {
                "name": "Bank Account", // <<< just fill in all details you want
                "type": "asset",
                "iban": "DE01234567890123456789",
                "bic": "ABCDEFGHIJK",
                "account_number": "0123456789",
                "opening_balance": "0",
                "opening_balance_date": "2020-01-01",
                "virtual_balance": "0",
                "currency_code": "EUR",
                "order": 1,
                "account_role": "sharedAsset"
            }, // <<< if you want to load more than one account, separate each account with a comma
            {
                "name": "Credit Card Account",
                "type": "asset",
                "iban": "DE01234567890123456789",
                "bic": "ABCDEFGHIJK",
                "account_number": "0123456789",
                "opening_balance": "0",
                "opening_balance_date": "2020-01-01",
                "virtual_balance": "0",
                "currency_code": "EUR",
                "order": 2,
                "account_role": "ccAsset",
                "credit_card_type": "monthlyFull",
                "monthly_payment_date": "2020-01-01"
            }
        ]
    }, // <<< if you want to load other 
    "categories": { // <<< here you can create accounts
        "url": "/api/v1/categories",
        "categories": [
            {
                "name": "Category1",
                "notes": ""
            },
            {
                "name": "Category2",
                "notes": ""
            }
        ]
    }
}
```

Adjust the file for your needs and save it as `init.json`.

### Step 3: Run the container

After you've create the configuration file, you can simply pull and run the container.

### docker example

```shell
docker run -d \
    -v /path/to/your/init.json:/configuration/init.json:ro \
    martinspaniol/firefly-iii-init:latest
```

### docker-compose example

```yaml
version: '3.3'

services:

  ffinit:
    image: martinspaniol/firefly-iii-init:latest
    networks:
      - firefly_iii
    restart: "no"
    volumes:
      - /path/to/your/init.json:/configuration/init.json:ro
```

[Firefly-III]: https://firefly-iii.org/
[Firefly-III API]: https://api-docs.firefly-iii.org/
[example-configuration]: ./configuration/example.json
[Firefly-III Create Token]: https://docs.firefly-iii.org/how-to/firefly-iii/features/api/#personal-access-tokens
