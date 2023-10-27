def linearSearchProduct(productList,targetProduct):
      indices=[]
  
      for index, product in enumerate(productList):
        if product ==targetProduct:
          indices.append(index)
          
        return indices

products=["Shoes","Boot","Loafer","Shoes","Sandal","Shoes"]
target="Shoes"
result=linearSearchProduct(products , target)
print(result)