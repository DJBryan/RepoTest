from peewee import *
from decimal import Decimal
from datetime import datetime
from playhouse.postgres_ext import PostgresqlExtDatabase

db = PostgresqlDatabase('claims', user='postgres',password = 'root')

class Claim(Model):
    claim_id = IntegerField(unique=True)
    submitted_amt = DecimalField(max_digits=7, decimal_places=2)
    factored_amt = DecimalField(max_digits=7, decimal_places=2)
    actual_amt = DecimalField(max_digits=7, decimal_places=2)
    min = DecimalField(max_digits=7, decimal_places=2)
    max = DecimalField(max_digits=7, decimal_places=2)
    median = DecimalField(max_digits=7, decimal_places=2)
    mean = DecimalField(max_digits=7, decimal_places=2)
    std_dev = DecimalField(max_digits=7, decimal_places=2)
    MAD_avg = DecimalField(max_digits=7, decimal_places=2)
    count = IntegerField()
    DOS = DateField()
    outliers = IntegerField()
    shortage_amt = DecimalField(max_digits=7, decimal_places=2)
    shortage_recovered = DecimalField(max_digits=7, decimal_places=2)
    shortage_status = CharField(max_length=2)
    claim_status = CharField(max_length=2)
    interest_chg = DecimalField(max_digits=4, decimal_places=2)
    fees = DecimalField(max_digits=4, decimal_places=2)

    class Meta:
        database = db

claims = [
    {'claim_id': 562338654,
     'submitted_amt':  12370.12,
     'min': 0,
     'max':3884.45,
     'median':1185.86,
     'mean':1688.57,
     'std_dev':2155.02,
     'MAD_avg':1001.38,
     'count':3,
     'DOS':'2018-01-30',
     'outliers':0
    },
    {'claim_id': 562332121,
     'submitted_amt':1942.14,
     'min':16.88,
     'max':989.88,
     'median':421.48,
     'mean':418.69,
     'std_dev':410.78,
     'MAD_avg':356.35,
     'count':2,
     'DOS':'2018-01-30',
     'outliers':1
    }
]

def add_claim():
    del parsed[0]
    for row in parsed:
        row.create( claim_id = int(row[0]),
                    submitted_amt = Decimal(row[1]),
                    min = Decimal(row[2]),
                    max = Decimal(row[3]),
                    median = Decimal(row[4]),
                    mean = Decimal(row[5]),
                    std_dev = Decimal(row[6]),
                    MAD_avg = Decimal(row[7]),
                    count = int(row[8]),
                    DOS = datetime.strptime(row[9],'%Y-%m-%d'),
                    outliers = int(row[10]))


# 'factored_amt = DecimalField(max_digits=7, decimal_places=2)
# 'actual_amt' = DecimalField(max_digits=7, decimal_places=2)
# 'shortage_amt' = DecimalField(max_digits=7, decimal_places=2)
# 'shortage_recovered' = DecimalField(max_digits=7, decimal_places=2)
# 'shortage_status' = CharField(max_length=2)
# 'claim_status' = CharField(max_length=2)
# 'interest_chg' = DecimalField(max_digits=4, decimal_places=2)
# 'fees' = DecimalField(max_digits=4, decimal_places=2)'


if __name__ == '__main__':
    db.connect()
    db.create_tables([Claim], safe=True)

    claim_file = open("c:\Project1\claim.csv", 'r')
    claim_data = claim_file.read()
    claim_file.close

    fields = claim_data.splitlines()
    parsed=[]

    for field in fields:
        parsed.append(field.split(','))


    # with open('c:\Project1\claim.csv', 'r') as claim_file:
    #     reader = csv.reader(claim_file, delimiter='\t')
    #     claim_list = list(reader)
    #
    # parsed=[]
    #
    # for field in claim_list:
    #     parsed.append(field.split(','))

    add_claim()

    print(parsed)

