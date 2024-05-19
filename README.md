# Tripay Python SDK (UnOfficial)

[Docs](https://tripay.co.id/developer)

Enum Mode 

    class ModeEnum(str, Enum):  
	    sandbox = "https://tripay.co.id/api-sandbox/"  
		  prod = "https://tripay.co.id/api/"

Authentication

    async def payment():
	    t = Tripay(api_key, private_key, mode)
   
  ## Closed Transaction
  **Create Transaction**
  

    async def payment():
		    t = Tripay(api_key, private_key, mode)		
			return await t.ClosedTransaction.create(merchant_code, payload, order_items)

  **Detail Transaction**
		  
	    async def payment():
		    t = Tripay(api_key, private_key, mode)		
				
				return await t.ClosedTransaction.detail(payload)

example payload:

    { "reference": "T0001000000000000006" }

## Open Transaction
Open Transaction isn't support Sanbox Mode

**Create Transaction**

    async def payment():
		    t = Tripay(api_key, private_key, mode)	
				return await t.OpenTransaction.create(payload, order_items)
Example order items:

    [  { 'sku': 'PRODUK1', 'name': 'Nama Produk 1', 'price': 500000, 'quantity': 1, 'product_url': 'https://tokokamu.com/product/nama-produk-1', 'image_url': 'https://tokokamu.com/product/nama-produk-1.jpg' }, { 'sku': 'PRODUK2', 'name': 'Nama Produk 2', 'price': 500000, 'quantity': 1, 'product_url': 'https://tokokamu.com/product/nama-produk-2', 'image_url': 'https://tokokamu.com/product/nama-produk-2.jpg' } ]

**Detail**

    async def payment():
		    t = Tripay(api_key, private_key, mode)	
				return await t.OpenTransaction.detail(uuid)

**Listing Payment**

	

    async def payment():
		    t = Tripay(api_key, private_key, mode)
		    return await t.OpenTransaction.listing_payment(uuid)


   

