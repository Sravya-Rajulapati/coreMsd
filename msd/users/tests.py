# from django.core import exceptions
# from django.test import TestCase
#
# from .models import UserAccount
#
#
# class UserAccountModelTestCase(TestCase):
#
#     def setUp(self):
#         # Create a test user
#         self.user = UserAccount.objects.create_user(
#             email='test@example.com',
#             password='securepassword',
#             first_name='John',
#             last_name='Doe',
#         )
#
#     def test_user_account_creation(self):
#         self.assertEqual(UserAccount.objects.count(), 1)
#         self.assertEqual(self.user.email, 'test@example.com')
#         self.assertTrue(self.user.check_password('securepassword'))
#
#     def test_vendor_user_creation(self):
#         vendor = UserAccount.objects.create_vendor_user(email='vendor@example.com', password='vendorpassword')
#         self.assertTrue(vendor.is_vendor)
#
#     def test_staff_user_creation(self):
#         staff = UserAccount.objects.create_staff_user(email='staff@example.com', password='staffpassword')
#         self.assertTrue(staff.is_staff)
#
#     def test_superuser_creation(self):
#         superuser = UserAccount.objects.create_superuser(email='admin@example.com', password='adminpassword')
#         self.assertTrue(superuser.is_superuser)
#         self.assertTrue(superuser.is_staff)
#
#     def test_password_validation(self):
#         with self.assertRaises(exceptions.ValidationError):
#             UserAccount.objects.create_user(email='test@example.com', password='weak')
#
#     def test_user_location(self):
#         location = UserAccount.objects.get_user_location('8.8.8.8')
#         self.assertNotEqual(location, 'Unknown')
#
#
# # class UserAccountPermissionsTestCase(TestCase):
# #     def setUp(self):
# #         # Create a test user
# #         self.user = UserAccount.objects.create_user(
# #             email="test@example.com",
# #             password="securepassword",
# #             first_name="John",
# #             last_name="Doe",
# #         )
#
# # def test_custom_permissions(self):
# #     create_custom_permissions()
# #     content_type = ContentType.objects.get_for_model(UserAccount)
# #     custom_permission = Permission.objects.get(
# #         codename="can_custom_action", content_type=content_type
# #     )
#
# #     self.assertIn(custom_permission, self.user.user_permissions.all())
#
# # def test_vendor_permissions(self):
# #     create_custom_permissions()
# #     content_type = ContentType.objects.get_for_model(UserAccount)
# #     vendor_permission = Permission.objects.get(
# #         codename="can_vendor_action", content_type=content_type
# #     )
#
# #     vendor = UserAccount.objects.create_vendor_user(
# #         email="vendor@example.com", password="vendorpassword"
# #     )
#
# #     self.assertIn(vendor_permission, vendor.user_permissions.all())
#
# # def test_staff_permissions(self):
# #     create_custom_permissions()
# #     content_type = ContentType.objects.get_for_model(UserAccount)
# #     staff_permission = Permission.objects.get(
# #         codename="can_staff_action", content_type=content_type
# #     )
#
# #     staff = UserAccount.objects.create_staff_user(
# #         email="staff@example.com", password="staffpassword"
# #     )
#
# #     self.assertIn(staff_permission, staff.user_permissions.all())
