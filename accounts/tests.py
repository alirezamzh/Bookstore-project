from django.test import TestCase

from django.contrib.auth import get_user_model

class CustomUserTest(TestCase):

    def test_create_user(self):
        User=get_user_model()
        user=User.objects.create_user(
            username='ali',
            email='ali@gmail.com',
            password='testpass123',
        )
        self.assertEqual(user.username,'ali')
        self.assertEqual(user.email,'ali@gmail.com')
        # self.assertEqual(user.password,'testpass123')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User=get_user_model()
        admin_user=User.objects.create_superuser(
            username='ghost',
            email='ghost@gmail.com',
            password='testpass123',
        )
        self.assertEqual(admin_user.username,'ghost')
        self.assertEqual(admin_user.email,'ghost@gmail.com')
        # self.assertEqual(user.password,'testpass123')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
