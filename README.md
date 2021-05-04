# WG Bars
<!-- ABOUT THE PROJECT -->
## About The Project
WG Bars is a webapp that lets you keep track of items being bought in a WG.

The tables in the Database are:

#### USERS
|ID|Name|
|---|---|
|1|Jose|

The Users table is the table storing the WG members.
The Id is the primary key and it's auto generated.

#### ITEM
|ID|Name|
|---|---|
|1|Toilet Paper|


The Items table stores different items.
The Id is the primary key and it's auto generated.

#### BOUGHT_BY
|ID|User_Id|Item_Id|Date|
|---|---|---|---|
|1|1|1|2020-05-04|

The Bought_by table connects each user with the items that they've bought.
The Id is the primary key and it's auto generated.




### Built With

* Python
* Flask
* SQLite


<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/JocCordova/which-coffee-app.git
   ```
2. Install Flask
   ```sh
   pip install Flask
   ```


<!-- USAGE EXAMPLES -->

## Usage
Flask runs in port 5000 as standard.


1. Run Server 

* (Linux)
   ```sh
   export FLASK_APP=webapp.py
   flask run --host=0.0.0.0
   ```
* (Windows)
  ```sh
   python run.py
  ```

You can now open the Server on

localhost:5000



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


<!-- CONTACT -->
## Contact

Jose Cordova - jacordovah@gmail.com

Project Link: [https://github.com/JocCordova/wg-bars](https://github.com/JocCordova/wg-bars)


