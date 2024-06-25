# In your Django app, create a management command file (e.g., initialize_permissions.py)

# app_name/management/commands/initialize_permissions.py
from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.apps import apps


class Command(BaseCommand):
    help = "Initialize groups and permissions for CustomUser"

    def handle(self, *args, **kwargs):
        # Your permission initialization logic here
        custom_user_model = apps.get_model("Homepage", "CustomUser")
        custom_user_content_type = ContentType.objects.get_for_model(custom_user_model)

        ADMIN_CUSTOM_PERMISSIONS = [
            ("admin_add_product", "Can add product"),
            ("admin_delete_product", "Can delete product"),
            ("admin_update_product", "Can update product"),
            ("admin_edit_customer_profile", "Can edit customer profile"),
            ("admin_delete_customer_profile", "Can delete customer profile"),
            ("admin_edit_seller_profile", "Can edit seller profile"),
            ("admin_delete_seller_profile", "Can delete seller profile"),
            ("admin_edit_csr_profile", "Can edit CSR profile"),
            ("admin_delete_csr_profile", "Can delete CSR profile"),
            ("admin_edit_manager_profile", "Can edit manager profile"),
            ("admin_delete_manager_profile", "Can delete manager profile"),
            ("admin_view_blog", "Can view blog"),
            ("admin_create_blog", "Can create blog"),
            ("admin_update_blog", "Can update blog"),
            ("admin_delete_blog", "Can delete blog"),
            ("admin_view_order_status", "Can check order status"),
            ("admin_update_order_status", "Can update order status"),
            ("admin_create_order_status", "Can check order status"),
            ("admin_delete_order_status", "Can update order status"),
            ("admin_access_user_data", "Can access user data"),
            ("admin_handle_customer_enquires", "Can respond to customer enquires"),
            ("admin_view_order_detail", "Can view order detail"),
            ("admin_approve_orders", "Can approve orders"),  # comming soon
            ("admin_delete_orders", "Can approve orders"),  # comming soon
            ("admin_update_orders", "Can approve orders"),  # comming soon
            ("admin_view_orders", "Can approve orders"),  # comming soon
            (
                "admin_create_discounts_and_promotions",
                "Can approve discounts and promotions",
            ),
            (
                "admin_update_discounts_and_promotions",
                "Can approve discounts and promotions",
            ),
            (
                "admin_delete_discounts_and_promotions",
                "Can approve discounts and promotions",
            ),
            (
                "admin_view_discounts_and_promotions",
                "Can approve discounts and promotions",
            ),
        ]

        admin_permissions = {}
        for codename, description in ADMIN_CUSTOM_PERMISSIONS:
            admin_permission, created = Permission.objects.get_or_create(
                codename=codename,
                content_type=custom_user_content_type,
                defaults={"name": description},
            )
            admin_permissions[codename] = admin_permission
            if created:
                print(f"Permission created for {description}")
            else:
                print(f"Permission '{description}' already exists")

        admin_group, created = Group.objects.get_or_create(name="ADMINISTRATOR")
        for codename, permission in admin_permissions.items():
            try:
                admin_group.permissions.add(permission)
            except Permission.MultipleObjectsReturned:
                print(f"Multiple objects returned for codename: {codename}")
        print(
            f"group permission count--- : {admin_group.permissions.all().count()}------: permission list count----: {len(ADMIN_CUSTOM_PERMISSIONS)}"
        )
        admin_group.save()
