from django.db import migrations

def populate_business_units(apps, schema_editor):
    Category = apps.get_model('core', 'Category')
    Service = apps.get_model('core', 'Service')
    
    # Business units data
    business_data = {
        'agric': {
            'name': 'Agriculture',
            'description': 'Sustainable food production, processing, and agro-innovation across Africa.',
            'services': [
                ('Crop Farming', 'Cultivation of grains (maize, sorghum, millet, rice) and cash crops (cotton, soy, cassava).'),
                ('Poultry Division', 'End-to-end chicken production pipeline - Layers, Broilers, and Hatchery operations.'),
                ('Dairy Production', 'Cattle farms producing raw milk, yogurt, butter, and other dairy products.'),
                ('Fishery & Aquaculture', 'Tilapia and catfish farms, feed mills, and processing for local/export markets.'),
                ('Goat & Livestock Farming', 'Meat and breeding programs for goats, sheep, and cattle.'),
                ('Fertilizer & Agro-Chemicals', 'Production and distribution of organic & inorganic fertilizers, pesticides, and soil conditioners.'),
                ('Animal Feed Production', 'Feed mill plants producing poultry, fish, and livestock feed blends.'),
                ('Agro-Machinery & Equipment', 'Supply and leasing of tractors, planters, harvesters, irrigation systems.'),
                ('Food Processing & Packaging', 'Value-addition: grain milling, vegetable oil extraction, fruit juice packaging.'),
            ]
        },
        'pharmacy': {
            'name': 'Pharmacy & Laboratories',
            'description': 'Delivering affordable, high-quality healthcare and diagnostics across Africa.',
            'services': [
                ('Pharmaceutical Manufacturing', 'Production of tablets, capsules, syrups, and injectable drugs.'),
                ('Retail & Wholesale Pharmacies', 'Chain of licensed pharmacy stores supplying human & veterinary medicine.'),
                ('Medical Equipment Supply', 'Import/distribution of diagnostic, surgical, and hospital equipment.'),
                ('Diagnostic Laboratories', 'Pathology, blood tests, radiology, and advanced molecular testing.'),
                ('Veterinary Pharmaceuticals', 'Animal drugs, vaccines, and livestock health products.'),
                ('Herbal & Alternative Medicine', 'Research and production of certified herbal and natural health products.'),
                ('Research & Development (R&D)', 'Product formulation, clinical trials, and partnerships with universities.'),
                ('Hospital Partnerships', 'Managed services and pharmaceutical support for hospitals/clinics.'),
                ('Training & Capacity Building', 'Programs for pharmacists, lab scientists, and medical technologists.'),
            ]
        },
        'supply-chain': {
            'name': 'Supply Chain',
            'description': 'Connecting producers, distributors, and consumers through efficient logistics and technology.',
            'services': [
                ('Procurement Services', 'Sourcing raw materials, packaging, and technical goods for industries.'),
                ('Warehousing & Storage', 'Multi-location warehouses (dry, cold, bonded).'),
                ('Cold Chain Management', 'Temperature-controlled logistics for food & pharmaceuticals.'),
                ('Distribution Hubs', 'Regional depots linking factories to retailers and exporters.'),
                ('Inventory Management Systems', 'Software-enabled stock monitoring and forecasting.'),
                ('Vendor & Supplier Networks', 'Partner ecosystem management for upstream and downstream suppliers.'),
                ('E-Commerce Fulfillment', 'Order processing, packaging, and returns management for online platforms.'),
                ('Freight Consolidation', 'Combining small consignments into bulk shipments to reduce costs.'),
                ('Supply Chain Consulting', 'Optimization, digital transformation, and compliance audits.'),
            ]
        },
        'logistics': {
            'name': 'Logistics',
            'description': 'Efficient and reliable transport of goods and materials across borders.',
            'services': [
                ('Road Freight', 'Long-haul trucking for bulk and general cargo.'),
                ('Air Freight', 'Air cargo coordination with airlines and freight forwarders.'),
                ('Sea Shipping', 'Containerized and bulk vessel cargo through major ports.'),
                ('Courier & Express Services', 'Last-mile delivery for SMEs and e-commerce.'),
                ('Fleet Management', 'Vehicle leasing, maintenance, GPS tracking, and driver management.'),
                ('Customs & Border Clearance', 'Clearing and forwarding services for imports/exports.'),
                ('Logistics Technology (Telematics)', 'Real-time tracking and route optimization systems.'),
                ('Infrastructure & Terminals', 'Truck parks, fuel depots, and logistics centers.'),
                ('Sustainability & Green Logistics', 'Eco-friendly transport initiatives (EV trucks, carbon offsets).'),
            ]
        },
        'contractor': {
            'name': 'Contracting',
            'description': 'Delivering end-to-end construction, engineering, and project management solutions.',
            'services': [
                ('Farm Infrastructure', 'Design and construction of poultry houses, greenhouses, irrigation systems.'),
                ('Residential Construction', 'Houses, apartments, and community estates.'),
                ('Commercial & Industrial Buildings', 'Warehouses, factories, and office complexes.'),
                ('Civil Engineering Projects', 'Roads, bridges, drainage, and public works.'),
                ('Electrical & Mechanical Works', 'Power installations, HVAC, and plumbing.'),
                ('Equipment Leasing', 'Heavy machinery rentals — excavators, cranes, graders.'),
                ('Renovation & Maintenance', 'Facility upgrades and repairs.'),
                ('EPC Projects', 'Turnkey "Engineering, Procurement, Construction" contracts.'),
                ('Project Management & Consulting', 'Cost control, quality assurance, and safety supervision.'),
            ]
        },
        'energy': {
            'name': 'Energy',
            'description': 'Powering Africa through clean, reliable, and affordable energy.',
            'services': [
                ('Renewable Energy', 'Solar, wind, and biogas power plants.'),
                ('Oil & Gas', 'Upstream and downstream operations, refining, and retail.'),
                ('Power Generation', 'Diesel, gas, and hybrid generators for industries.'),
                ('Electrical Installations', 'Industrial and domestic wiring, transformers, substations.'),
                ('Fuel Distribution & Retail', 'Filling stations and fuel supply logistics.'),
                ('Battery & Storage Systems', 'Large-scale energy storage for backup and grid stability.'),
                ('Energy Equipment Supply', 'Import and sale of generators, inverters, panels, transformers.'),
                ('Energy Consulting', 'Audits, design, and feasibility studies for energy projects.'),
                ('Training & Safety Programs', 'Capacity building for engineers and field staff.'),
            ]
        },
        'real-estate': {
            'name': 'Real Estate & Infrastructure',
            'description': 'Creating sustainable spaces and modern infrastructure for Africa\'s growth.',
            'services': [
                ('Industrial Parks', 'Large-scale zones for factories and manufacturing.'),
                ('Residential Estates', 'Housing developments with utilities and green spaces.'),
                ('Commercial Properties', 'Offices, malls, and mixed-use complexes.'),
                ('Roads & Bridges', 'Civil infrastructure connecting cities and communities.'),
                ('Facility Management', 'Maintenance and operations of buildings and complexes.'),
                ('Land Development & Sales', 'Acquisition, titling, and marketing of land parcels.'),
                ('Urban Planning & Smart Cities', 'GIS, zoning, and sustainable city projects.'),
                ('Property Leasing & Brokerage', 'Real estate investment and agency services.'),
                ('Public Infrastructure Projects', 'Airports, schools, hospitals, and civic works.'),
            ]
        }
    }
    
    # Create categories and services
    for slug, data in business_data.items():
        category, created = Category.objects.get_or_create(
            slug=slug,
            defaults={
                'name': data['name'],
                'description': data['description']
            }
        )
        
        # Create services for this category
        for service_title, service_desc in data['services']:
            Service.objects.get_or_create(
                category=category,
                title=service_title,
                defaults={'description': service_desc}
            )

def reverse_populate_business_units(apps, schema_editor):
    Category = apps.get_model('core', 'Category')
    Service = apps.get_model('core', 'Service')
    
    # Delete all services and categories
    Service.objects.all().delete()
    Category.objects.all().delete()

class Migration(migrations.Migration):
    dependencies = [
        ('core', '0007_teammember'),
    ]

    operations = [
        migrations.RunPython(populate_business_units, reverse_populate_business_units),
    ]