# Supermarket

## Use

### To create an invoice click on "New invoice"

![image](https://user-images.githubusercontent.com/28797741/137647785-357215f3-3890-455f-bc12-6b95273bc80c.png)

Enter the client data code is optional. On the right side you can search for products and add them. In the center section you can change the quantity to buy of each product. Once finished press the generate button

![image](https://user-images.githubusercontent.com/28797741/137647821-44f59ff1-adb9-436c-ac49-0e4c8caef0da.png)

That will show you the generated invoice, you can print it by clicking the "Print" button

![image](https://user-images.githubusercontent.com/28797741/137648043-40fcad2d-3d4c-427e-84cf-5c904305d996.png)

You can check the generated invoices in "list"

![image](https://user-images.githubusercontent.com/28797741/137648094-677cdf1b-59da-4887-85d4-3932045063ff.png)

There, all the generated invoices will be shown, by clicking on one you will see its details

![image](https://user-images.githubusercontent.com/28797741/137648153-3b110539-8a63-4f71-829f-16f8e5f55644.png)

## Setup

Download: `git clone https://github.com/kuronosu/supermarket.git`

Move to the project folder: `cd supermarket`

Create virtual environment: `python -m venv venv`

Actiave virtual environment:
- Windows: `.\venv\Scripts\activate`
- Linux: `./venv/bin/activate`

Install dependencies: `pip install -r .\requirements.txt`

Create environment variable SECRET_KEY:

- Windows: `$env:SECRET_KEY="your-secret-key"`
- Linux: `export SECRET_KEY="your-secret-key"`

Run migrations: `python manage.py migrate`

Create superuser: `python manage.py createsuperuser`

Start server: `python manage.py runserver`

Note:

In each new terminal you must create the environment variable, you can do that and start the server with a single command

- Windows:  `$env:SECRET_KEY="your-secret-key" & python.exe manage.py runserver`
- Linux:  `SECRET_KEY="your-secret-key"; python.exe manage.py runserver`
