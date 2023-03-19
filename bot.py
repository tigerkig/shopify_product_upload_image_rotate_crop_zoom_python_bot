import csv
import os 
import requests

dir_path = os.path.dirname(os.path.realpath(__file__))
file_name = dir_path + '\example.csv'
header_line = [
	"Handle",
	"Title",
	"Body (HTML)",
	"Vendor",
	"Product Category",
	"Type",
	"Tags",
	"Published",
	"Option1 Name",
	"Option1 Value",
	"Option2 Name",
	"Option2 Value",
	"Option3 Name",
	"Option3 Value",
	"Variant SKU",
	"Variant Grams",
	"Variant Inventory Tracker",
	"Variant Inventory Qty",
	"Variant Inventory Policy",
	"Variant Fulfillment Service",
	"Variant Price",
	"Variant Compare At Price",
	"Variant Requires Shipping",
	"Variant Taxable",
	"Variant Barcode",
	"Image Src",
	"Image Position",
	"Image Alt Text",
	"Gift Card",
	"SEO Title",
	"SEO Description",
	"Google Shopping / Google Product Category",
	"Google Shopping / Gender",
	"Google Shopping / Age Group",
	"Google Shopping / MPN",
	"Google Shopping / AdWords Grouping",
	"Google Shopping / AdWords Labels",
	"Google Shopping / Condition",
	"Google Shopping / Custom Product",
	"Google Shopping / Custom Label 0",
	"Google Shopping / Custom Label 1",
	"Google Shopping / Custom Label 2",
	"Google Shopping / Custom Label 3",
	"Google Shopping / Custom Label 4",
	"Variant Image",
	"Variant Weight Unit",
	"Variant Tax Code",
	"Cost per item",
	"Included / Armenia",
	"Included / International",
	"Price / International",
	"Compare At Price / International",
	"Status"]
result = []

def url_ok(url):
     
	try:
		response = requests.head(url)
		if response.status_code == 200:
			return True
		else:
			return False
	except requests.ConnectionError as e:
		return e

with open(file_name) as csvfile:
	csv_reader = csv.reader(csvfile, delimiter=',')
	line_count = 0

	for row in csv_reader:
		if row[10] != '' and row[9] != '':
			if line_count > 0:
				Handle = row[1].lower().replace(" ", "-") + '-1-1'
				Title = row[1]
				Gender = ''
				Multi_size = row[9].split('-')

				if row[3] == 'M':
					Gender = 'Uomo'
				elif row[3] == 'F':
					Gender = 'Donna'
				elif row[3] == 'Bimbo':
					Gender = 'Bimbo'

				if len(Multi_size) == 2:
					misure = f"""
							<tr data-mce-fragment="1">
								<td style="width: 48.5841%;" data-mce-fragment="1">Vita</td>
								<td style="width: 48.4159%;" data-mce-fragment="1">{Multi_size[0]} cm</td>
							</tr>
							<tr data-mce-fragment="1">
								<td style="width: 48.5841%;" data-mce-fragment="1">Lunghezza totale</td>
								<td style="width: 48.4159%;" data-mce-fragment="1">{Multi_size[1]} cm</td>
							</tr>
						"""
				elif len(Multi_size) == 3:
					misure = f"""
							<tr data-mce-fragment="1">
								<td style="width: 48.5841%;" data-mce-fragment="1">Vita</td>
								<td style="width: 48.4159%;" data-mce-fragment="1">{Multi_size[0]} cm</td>
							</tr>
							<tr data-mce-fragment="1">
								<td style="width: 48.5841%;" data-mce-fragment="1">Cavallo</td>
								<td style="width: 48.4159%;" data-mce-fragment="1">{Multi_size[1]} cm</td>
							</tr>
							<tr data-mce-fragment="1">
								<td style="width: 48.5841%;" data-mce-fragment="1">Lunghezza totale</td>
								<td style="width: 48.4159%;" data-mce-fragment="1">{Multi_size[2]} cm</td>
							</tr>
						"""
				elif len(Multi_size) == 4:
					misure = f"""
							<tr data-mce-fragment="1">
								<td style="width: 48.5841%;" data-mce-fragment="1">Spalle</td>
								<td style="width: 48.4159%;" data-mce-fragment="1">{Multi_size[0]} cm</td>
							</tr>
							<tr data-mce-fragment="1">
								<td style="width: 48.5841%;" data-mce-fragment="1">Braccio</td>
								<td style="width: 48.4159%;" data-mce-fragment="1">{Multi_size[1]} cm</td>
							</tr>
							<tr data-mce-fragment="1">
								<td style="width: 48.5841%;" data-mce-fragment="1">Petto</td>
								<td style="width: 48.4159%;" data-mce-fragment="1">{Multi_size[2]} cm</td>
							</tr>
							<tr data-mce-fragment="1">
								<td style="width: 48.5841%;" data-mce-fragment="1">Lunghezza totale</td>
								<td style="width: 48.4159%;" data-mce-fragment="1">{Multi_size[3]} cm</td>
							</tr>
						"""

				Body_Html = f"""
						<p><strong>{row[2]}.</strong><br></p>
							<table width="100%">
								<tbody>
									<tr>
										<td><strong>SCHEDA PRODOTTO</strong></td>
									</tr>
								</tbody>
							</table>
							<table width="100%" data-mce-fragment="1">
								<tbody data-mce-fragment="1">
									<tr data-mce-fragment="1">
										<td style="width: 47.3768%;" data-mce-fragment="1">Sesso</td>
										<td style="width: 47.6232%;" data-mce-fragment="1">{Gender}</td>
									</tr>
									<tr data-mce-fragment="1">
										<td style="width: 47.3768%;" data-mce-fragment="1">Taglia</td>
										<td style="width: 47.6232%;" data-mce-fragment="1">{row[4]} <br>
										</td>
									</tr>
									<tr data-mce-fragment="1">
										<td style="width: 47.3768%;" data-mce-fragment="1">Colore</td>
										<td style="width: 47.6232%;" data-mce-fragment="1">{row[6]} <br>
										</td>
									</tr>
									<tr data-mce-fragment="1">
										<td style="width: 47.3768%;" data-mce-fragment="1">Composizione</td>
										<td style="width: 47.6232%;" data-mce-fragment="1">{row[7]} <br>
										</td>
									</tr>
									<tr data-mce-fragment="1">
										<td style="width: 47.3768%;" data-mce-fragment="1">Condizioni Usato</td>
										<td style="width: 47.6232%;" data-mce-fragment="1">{row[8]} <br>
										</td>
									</tr>
								</tbody>
							</table>
							<p><br></p>
							<table width="100%" data-mce-fragment="1">
								<tbody data-mce-fragment="1">
									<tr data-mce-fragment="1">
										<td data-mce-fragment="1"><strong>MISURE</strong>
										</td>
									</tr>
								</tbody>
							</table>
							<table width="100%" data-mce-fragment="1">
								<tbody data-mce-fragment="1">
									{misure}
								</tbody>
							</table>
						<br>
							<span data-mce-fragment="1">Guida alle taglie e misure,</span>
							<strong data-mce-fragment="1">
								<a href="https://www.secondchancy.com/pages/guida-misure" title="Guida Misure" data-mce-fragment="1" data-mce-href="https://www.secondchancy.com/pages/guida-misure">clicca qui.</a>
							</strong>
						<br>
					"""
				
				Vendor = row[12]
				Product_Category = "Apparel & Accessories > Clothing"
				Type = row[11]
				tagsArray = [i.strip() for i in row[14].split('/')]
				Tags = ', '.join(tagsArray)
				Published = 'TRUE'
				Option_1_Name = 'Size'
				Option_1_Value = row[5]
				Option_2_Name = 'Color'
				Option_2_Value = row[6]
				Varient_SKU = f"{row[15]}-{row[0]}"

				a = []
				for word in row[10].split():
					try: a.append(float(word))
					except ValueError: pass
				Varient_Price = int(a[0])
					
				SEO_Description = row[2]
				imageName = row[0][1:5]
				
				for value in [1,2,3,4]:
					Image_Src = f'https://amgw.co.uk/shopify_images/a{imageName}_{value}.jpg'

					if url_ok(Image_Src) == True:
						if value == 1:
							new_line = [ Handle, Title, Body_Html, Vendor, Product_Category, Type, Tags, Published, Option_1_Name, Option_1_Value, Option_2_Name, Option_2_Value, "", "", Varient_SKU, "0", "shopify", "1", "deny", "manual", Varient_Price, Varient_Price, "TRUE", "TRUE", "", Image_Src, value, "", "FALSE", "", SEO_Description, "", "", "", "", "", "", "", "", "", "", "", "", "", Image_Src, "kg", "", "", "TRUE", "TRUE", "", "", "active" ]
						else:
							new_line = [Handle, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", Image_Src, value, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ]
						result.append(new_line)
					else:
						print(f"{Image_Src} ===> Invalid image URL ===> {row[0]}")
					print(row[0])
			else:
				result.append(header_line)
			line_count += 1

with open('output.csv', 'w', newline='', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerows(result)

