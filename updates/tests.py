from django.test import TestCase
from .models import Business,NeighborHood,Userprofile,Post


# Create your tests here.
class NeighborHoodTestClass(TestCase):
    #Set up method
    def setUp(self):
        self.new_neighborhood =NeighborHood(neighborhood_image="image.jpeg",name="Moringa",location="Ngong road",occupants_count=20)

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.new_neighborhood,NeighborHood))

    #Testing Save Method
    def test_save_method(self):
        self.new_neighborhood.save_neighborhood()
        neighborhoods=NeighborHood.objects.all()
        self.assertTrue(len(neighborhoods)>0)

    def test_delete_method(self):
        self.new_neighborhood.save_neighborhood()
        self.new_neighborhood.delete_neighborhood()


    # def find_neighborhood_by_id(self):
    #     neighborhood=NeighborHood.find_neighborhood_by_id()
    #     self.assertTrue(len(neighborhood)>0)

    def test_update_occupants(self):
        self.new_neighborhood.save_neighborhood()
        self.new_neighborhood = NeighborHood.objects.filter(id=1)
        neighborhood = self.new_neighborhood
        neighborhood.update_occupants(40)
        self.updated_neighborhood = NeighborHood.objects.get(id=1)
        self.assertEqual(self.updated_neighborhood.occupants_count,40)


class UserprofileTestClass(TestCase):
    #Set up method
    def setUp(self):
        self.new_userprofile =Userprofile(profile_image="image.jpeg",email="profile@gmail.com")

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.new_userprofile,Userprofile))

    #Testing Save Method
    def test_save_method(self):
        self.new_userprofile.save_userprofile()
        userprofiles=Userprofile.objects.all()
        self.assertTrue(len(userprofiles)>0)

    def test_delete_method(self):
        self.new_userprofile.save_userprofile()
        self.new_userprofile.delete_userprofile()



class BuinessTestClass(TestCase):


    def setUp(self):
        self.new_business=Business(business_image="image.jpeg",business_name="Masoko",email="masoko@gmail.com")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_business,Business))


    def test_save_method(self):

        self.new_business.save_business()
        businesses = Business.objects.all()
        self.assertTrue(len(businesses) > 0)

    def test_delete_method(self):

        self.new_business.save_business()
        self.new_business.delete_business()

    def test_find_business_by_id(cls,business_id):
        business=Business.find_business_by_id()
        self.assertTrue(len(business)>0)


class PostTestClass(TestCase):


    def setUp(self):
        self.new_post=Post(post_image="image.jpeg",title="Security",post="Don't waste water")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_post,Post))


    def test_save_method(self):

        self.new_post.save_post()
        posts = Post.objects.all()
        self.assertTrue(len(posts) > 0)

    def test_delete_method(self):

        self.new_post.save_post()
        self.new_post.delete_post()
