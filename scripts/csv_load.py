import csv  # https://docs.python.org/3/library/csv.html

# https://django-extensions.readthedocs.io/en/latest/runscript.html

# python3 manage.py runscript csv_load

from unesco.models import Site, Category, Region, States, Iso

def run():
    fhand = open('unesco/whc-sites-2018-clean.csv')
    reader = csv.reader(fhand)
    next(reader)  # Advance past the header

    Site.objects.all().delete()
    Category.objects.all().delete()
    Region.objects.all().delete()
    States.objects.all().delete()
    Iso.objects.all().delete()

    for row in reader:
        print('read')


        try:
            s, created =  Site.objects.get_or_create(name=row[0])
        except:
            s=None

        try:
            y = row[3]
        except:
            y=None


        try:
            c, created =  Category.objects.get_or_create(name=row[7])
        except:
            c=None

        try:
            r, created =  Region.objects.get_or_create(name=row[9])
        except:
            r=None

        try:
            i, created =  Iso.objects.get_or_create(name=row[10])
        except:
            i=None

        try:
            st, created = States.objects.get_or_create(name=row[8])
        except:
            st=None




        area_hectares=row[6]
        try:
            float(area_hectares)
        except:
            area_hectares=None

        latitude=row[5]
        try:
            float(latitude)
        except:
            latitude=None

        longitude=row[4]
        try:
            float(longitude)
        except:
            longitude=None

        justification=row[2]
        try:
            str(justification)
        except:
            justification=None

        description=row[1]
        try:
            str(description)
        except:
            description=None



        site = Site(category=c,state=st, region=r,iso=i,name=s,year=y,description=description,justification=justification,longitude=longitude,latitude=latitude,area_hectares=area_hectares)
        site.save()

