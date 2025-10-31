from django.core.management.base import BaseCommand
from store.models import Product, Variation

class Command(BaseCommand):
    help = 'Add color and size variations to all products'

    def handle(self, *args, **kwargs):
        # Define variations
        colors = ['Red', 'Blue', 'Black']
        sizes = ['Small', 'Medium', 'Large']

        products = Product.objects.all()

        for product in products:
            self.stdout.write(f'Adding variations for {product.product_name}...')

            # Add color variations
            for color in colors:
                variation, created = Variation.objects.get_or_create(
                    product=product,
                    variation_category='color',
                    variation_value=color,
                    defaults={'is_active': True}
                )
                if created:
                    self.stdout.write(self.style.SUCCESS(f'  ✓ Added color: {color}'))
                else:
                    self.stdout.write(self.style.WARNING(f'  - Color {color} already exists'))

            # Add size variations
            for size in sizes:
                variation, created = Variation.objects.get_or_create(
                    product=product,
                    variation_category='size',
                    variation_value=size,
                    defaults={'is_active': True}
                )
                if created:
                    self.stdout.write(self.style.SUCCESS(f'  ✓ Added size: {size}'))
                else:
                    self.stdout.write(self.style.WARNING(f'  - Size {size} already exists'))

        self.stdout.write(self.style.SUCCESS('\n✅ All variations added successfully!'))