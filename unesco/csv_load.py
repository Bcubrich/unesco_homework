import csv  # https://docs.python.org/3/library/csv.html

# https://django-extensions.readthedocs.io/en/latest/runscript.html

# python3 manage.py runscript many_load

from unesco.models import Site, Category, Region, State, Iso

def run():
    fhand = open('many/load.csv')
    reader = csv.reader(fhand)
    next(reader)  # Advance past the header

    Site.objects.all().delete()
    Category.objects.all().delete()
    Region.objects.all().delete()
    State.objects.all().delete()
    Iso.objects.all().delete()

    # Format
    # email,role,course
    # jane@tsugi.org,I,Python
    # ed@tsugi.org,L,Python

    for row in reader:
        print(row)

        try:
            s, created =  Site.objects.get_or_create(name=row[0])
        except:
            s=None
        try:
            y, created =  Site.objects.get_or_create(year=row[0])
        except:
            y=None
        try:
            c, created =  Category.objects.get_or_create(name=row[4])
        except:
            c=None
        try:
            r, created =  Region.objects.get_or_create(name=row[10])
        except:
            r=None
        try:
            i, created =  Iso.objects.get_or_create(name=row[11])
        except:
            i=None
        try:
            st, created = State.objects.get_or_create(name=row[12])
        except:
            st=None






        site = Site(category=c,states=st, region=r,iso=i,site=s,year=y)
        site.save()