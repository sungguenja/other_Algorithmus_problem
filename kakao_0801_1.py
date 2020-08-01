def priceCheck(products, productPrices, productSold, soldPrice):
    # Write your code here
    error = 0
    for j in range(len(productSold)):
        i = products.index(productSold[j])
        if productPrices[i] != soldPrice[j]:
            error += 1
    return error