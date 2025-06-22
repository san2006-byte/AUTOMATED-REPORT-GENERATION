import csv
from fpdf import FPDF

# Step 1: Read data
data = []
with open('sales_data.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        data.append(row)

# Step 2: Analyze data
total_units = 0
total_revenue = 0
product_summary = {}

for row in data:
    product = row['Product']
    units = int(row['Units Sold'])
    
    # Clean revenue: remove ₹ or other characters if any
    revenue_str = row['Revenue'].replace("₹", "").replace(",", "").strip()
    revenue = int(revenue_str)

    total_units += units
    total_revenue += revenue

    if product not in product_summary:
        product_summary[product] = {'units': 0, 'revenue': 0}
    product_summary[product]['units'] += units
    product_summary[product]['revenue'] += revenue

# Step 3: Generate PDF report
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", "B", 16)
pdf.cell(200, 10, "Sales Report", ln=True, align="C")

pdf.set_font("Arial", "", 12)
pdf.ln(10)
pdf.cell(200, 10, f"Total Units Sold: {total_units}", ln=True)
pdf.cell(200, 10, f"Total Revenue: Rs. {total_revenue}", ln=True)

pdf.ln(10)
pdf.set_font("Arial", "B", 14)
pdf.cell(200, 10, "Product-wise Summary", ln=True)

pdf.set_font("Arial", "", 12)
for product, stats in product_summary.items():
    pdf.cell(200, 10, f"{product} - Units: {stats['units']} | Revenue: Rs. {stats['revenue']}", ln=True)

# Step 4: Save the PDF
pdf.output("sales_report.pdf")
print("✅ PDF report generated: sales_report.pdf")
