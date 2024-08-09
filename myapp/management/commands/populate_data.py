from django.core.management.base import BaseCommand
from myapp.models import Author, Books, Publisher, User
from datetime import date

class Command(BaseCommand):
  def handle(self, *args, **kwargs):
      users = [
          User(username='user1', email='user1@example.com'),
          User(username='user2', email='user2@example.com'),
          User(username='user3', email='user3@example.com'),
          User(username='user4', email='user4@example.com'),
          User(username='user5', email='user5@example.com'),
          User(username='user6', email='user6@example.com'),
          User(username='user7', email='user7@example.com'),
          User(username='user8', email='user8@example.com'),
          User(username='user9', email='user9@example.com'),
          User(username='user10', email='user10@example.com'),
          User(username='user11', email='user11@example.com'),
          User(username='user12', email='user12@example.com'),
          User(username='user13', email='user13@example.com'),
          User(username='user14', email='user14@example.com'),
          User(username='user15', email='user15@example.com'),
      ]
      User.objects.bulk_create(users)

      publishers = [
          Publisher(firstname='John', lastname='Doe', joindate=date(2020, 1, 1), popularity_score=85),
          Publisher(firstname='Jane', lastname='Smith', joindate=date(2021, 6, 15), popularity_score=90),
          Publisher(firstname='Mike', lastname='Johnson', joindate=date(2019, 11, 3), popularity_score=78),
          Publisher(firstname='Emily', lastname='Clark', joindate=date(2022, 2, 10), popularity_score=88),
          Publisher(firstname='William', lastname='Brown', joindate=date(2021, 11, 20), popularity_score=92),
          Publisher(firstname='Michael', lastname='Scott', joindate=date(2020, 4, 14), popularity_score=81),
          Publisher(firstname='Anna', lastname='Taylor', joindate=date(2019, 8, 7), popularity_score=85),
          Publisher(firstname='David', lastname='Jones', joindate=date(2021, 3, 22), popularity_score=87),
          Publisher(firstname='Sarah', lastname='Wilson', joindate=date(2020, 5, 18), popularity_score=89),
          Publisher(firstname='Robert', lastname='Miller', joindate=date(2022, 1, 30), popularity_score=90),
          Publisher(firstname='Jessica', lastname='Moore', joindate=date(2021, 9, 12), popularity_score=83),
          Publisher(firstname='Christopher', lastname='Taylor', joindate=date(2019, 11, 24), popularity_score=84),
          Publisher(firstname='Daniel', lastname='Anderson', joindate=date(2022, 7, 1), popularity_score=91),
      ]
      Publisher.objects.bulk_create(publishers)

      authors = [
          Author(firstname='Emily', lastname='Bronte', address='123 Main St', zipcode=12345, telephone='123-456-7890', joindate=date(2020, 3, 10), popularity_score=95),
          Author(firstname='Charlotte', lastname='Bronte', address='456 Elm St', zipcode=54321, telephone='987-654-3210', joindate=date(2021, 7, 25), popularity_score=85),
          Author(firstname='Jane', lastname='Austen', address='789 Oak St', zipcode=67890, telephone='456-789-1234', joindate=date(2019, 2, 20), popularity_score=92),
          Author(firstname='Leo', lastname='Tolstoy', address='202 Birch St', zipcode=33445, telephone='654-321-0987', joindate=date(2022, 1, 15), popularity_score=94, recommendedby=None),
          Author(firstname='Mark', lastname='Twain', address='303 Cedar St', zipcode=55667, telephone='789-012-3456', joindate=date(2020, 9, 5), popularity_score=87, recommendedby=None),
          Author(firstname='Herman', lastname='Melville', address='404 Pine St', zipcode=77889, telephone='012-345-6789', joindate=date(2021, 8, 15), popularity_score=91, recommendedby=None),
          Author(firstname='George', lastname='Orwell', address='505 Willow St', zipcode=99000, telephone='234-567-8901', joindate=date(2022, 3, 5), popularity_score=96, recommendedby=None),
          Author(firstname='F. Scott', lastname='Fitzgerald', address='606 Chestnut St', zipcode=11122, telephone='345-678-9012', joindate=date(2021, 12, 20), popularity_score=93, recommendedby=None),
          Author(firstname='Ernest', lastname='Hemingway', address='707 Walnut St', zipcode=22334, telephone='456-789-0123', joindate=date(2020, 6, 25), popularity_score=88, recommendedby=None),
          Author(firstname='Virginia', lastname='Woolf', address='808 Spruce St', zipcode=33445, telephone='567-890-1234', joindate=date(2022, 5, 30), popularity_score=89, recommendedby=None),
          Author(firstname='James', lastname='Joyce', address='909 Cypress St', zipcode=44556, telephone='678-901-2345', joindate=date(2021, 11, 15), popularity_score=90, recommendedby=None),
          Author(firstname='Franz', lastname='Kafka', address='1010 Poplar St', zipcode=55667, telephone='789-012-3456', joindate=date(2020, 7, 10), popularity_score=86, recommendedby=None),
          Author(firstname='Gabriel', lastname='Garcia Marquez', address='1111 Fir St', zipcode=66778, telephone='890-123-4567', joindate=date(2022, 2, 25), popularity_score=95, recommendedby=None),
      ]
      Author.objects.bulk_create(authors)

      books = [
          Books(title='Atomic Habits', genre='Fiction', price=20, published_date=date(2021, 5, 10), author=authors[0], publisher=publishers[0]),
          Books(title='The wings of Fire', genre='Non-Fiction', price=25, published_date=date(2020, 4, 15), author=authors[1], publisher=publishers[1]),
          Books(title='The Black Hole', genre='Science Fiction', price=30, published_date=date(2019, 3, 20), author=authors[2], publisher=publishers[2]),
          Books(title='Great Expectations', genre='Bildungsroman', price=22, published_date=date(2021, 6, 5), author=authors[0], publisher=publishers[0]),
          Books(title='War and Peace', genre='Historical Fiction', price=35, published_date=date(2022, 2, 15), author=authors[1], publisher=publishers[1]),
          Books(title='The Adventures of Tom Sawyer', genre='Adventure', price=18, published_date=date(2020, 9, 20), author=authors[2], publisher=publishers[2]),
          Books(title='Moby-Dick', genre='Adventure', price=28, published_date=date(2021, 8, 30), author=authors[3], publisher=publishers[3]),
          Books(title='1984', genre='Dystopian', price=32, published_date=date(2022, 3, 10), author=authors[4], publisher=publishers[4]),
          Books(title='The Great Gatsby', genre='Tragedy', price=24, published_date=date(2021, 12, 25), author=authors[5], publisher=publishers[5]),
          Books(title='The Old Man and the Sea', genre='Literary Fiction', price=20, published_date=date(2020, 6, 30), author=authors[6], publisher=publishers[6]),
          Books(title='Mrs Dalloway', genre='Modernist', price=27, published_date=date(2022, 5, 10), author=authors[7], publisher=publishers[7]),
          Books(title='Ulysses', genre='Modernist', price=30, published_date=date(2021, 11, 20), author=authors[8], publisher=publishers[8]),
          Books(title='The Metamorphosis', genre='Existentialist', price=15, published_date=date(2020, 7, 15), author=authors[9], publisher=publishers[9]),
      ]
      Books.objects.bulk_create(books)

      authors[0].followers.add(User.objects.get(username='user6'), User.objects.get(username='user7'))
      authors[1].followers.add(User.objects.get(username='user8'), User.objects.get(username='user9'))
      authors[2].followers.add(User.objects.get(username='user10'), User.objects.get(username='user11'))
      authors[3].followers.add(User.objects.get(username='user12'), User.objects.get(username='user13'))
      authors[4].followers.add(User.objects.get(username='user14'), User.objects.get(username='user15'))
      authors[5].followers.add(User.objects.get(username='user1'), User.objects.get(username='user3'))
      authors[6].followers.add(User.objects.get(username='user2'), User.objects.get(username='user4'))
      authors[7].followers.add(User.objects.get(username='user5'), User.objects.get(username='user6'))
      authors[8].followers.add(User.objects.get(username='user7'), User.objects.get(username='user3'))
      authors[9].followers.add(User.objects.get(username='user1'), User.objects.get(username='user10'))
      authors[10].followers.add(User.objects.get(username='user8'), User.objects.get(username='user11'))
      authors[11].followers.add(User.objects.get(username='user12'), User.objects.get(username='user13'))
      authors[12].followers.add(User.objects.get(username='user14'), User.objects.get(username='user15'))


      authors[0].recommendedby = authors[1]
      authors[1].recommendedby = authors[2]
      authors[2].recommendedby = authors[3]
      authors[3].recommendedby = authors[4]
      authors[4].recommendedby = authors[5]
      authors[5].recommendedby = authors[6]
      authors[6].recommendedby = authors[7]
      authors[7].recommendedby = authors[8]
      authors[8].recommendedby = authors[9]
      authors[9].recommendedby = authors[10]
      authors[10].recommendedby = authors[11]
      authors[11].recommendedby = authors[12]
      authors[12].recommendedby = authors[0]


      authors[0].save()
      authors[1].save()
      authors[2].save()
      authors[3].save()
      authors[4].save()
      authors[5].save()
      authors[6].save()
      authors[7].save()
      authors[8].save()
      authors[9].save()
      authors[10].save()
      authors[11].save()
      authors[12].save()
      

      publishers[0].recommendedby = publishers[1]
      publishers[1].recommendedby = publishers[2]
      publishers[2].recommendedby = publishers[3]
      publishers[3].recommendedby = publishers[4]
      publishers[4].recommendedby = publishers[5]
      publishers[5].recommendedby = publishers[6]
      publishers[6].recommendedby = publishers[7]
      publishers[7].recommendedby = publishers[8]
      publishers[8].recommendedby = publishers[9]
      publishers[9].recommendedby = publishers[10]
      publishers[10].recommendedby = publishers[11]
      publishers[11].recommendedby = publishers[12]
      publishers[12].recommendedby = publishers[0]

      publishers[0].save()
      publishers[1].save()
      publishers[2].save()
      publishers[3].save()
      publishers[4].save()
      publishers[5].save()
      publishers[6].save()
      publishers[7].save()
      publishers[8].save()
      publishers[9].save()
      publishers[10].save()
      publishers[11].save()
      publishers[12].save()

      self.stdout.write(self.style.SUCCESS('Successfully populated data'))
