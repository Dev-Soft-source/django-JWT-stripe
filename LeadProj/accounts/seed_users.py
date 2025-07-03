# accounts/seed_users.py

from accounts.models import User
import logging

logger = logging.getLogger(__name__)

def create_seed_users():
    users = [
        {
            'email': 'admin@example.com',
            'password': 'adminpass',
            'first_name': 'Admin',
            'last_name': 'User',
            'role': 'admin',
            'is_staff': True,
            'is_superuser': True,
        },
        {
            'email': 'customer@example.com',
            'password': 'customerpass',
            'first_name': 'Customer',
            'last_name': 'User',
            'role': 'customer',
        },
        {
            'email': 'agent@example.com',
            'password': 'agentpass',
            'first_name': 'Agent',
            'last_name': 'User',
            'role': 'customer',
        },
    ]

    for u in users:
        if not User.objects.filter(email=u['email']).exists():
            user = User.objects.create_user(
                email=u['email'],
                password=u['password'],
                first_name=u['first_name'],
                last_name=u['last_name'],
                role=u['role'],
            )
            user.is_staff = u.get('is_staff', False)
            user.is_superuser = u.get('is_superuser', False)
            user.save()
            logger.info(f"[Seed] Created {u['role']} user: {u['email']}")
