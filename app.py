import requests
import json
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import MultiLabelBinarizer

'''This function, named FindAlternateGroups, retrieves products data from an online store using its API, preprocesses the data by extracting relevant
 features and performing clustering, and then returns a JSON string containing the product alternates organized by cluster. The function takes the store 
 domain as input and returns the JSON string.'''

def FindAlternateGroups(store_domain):
    products = []
    page = 1
    while True:
        url = f"{store_domain}/products.json?page={page}"
        response = requests.get(url)
        if response.status_code == 200:
            page_products = json.loads(response.text)['products']
            if not page_products:
                break
            products.extend(page_products)
            page += 1
        else:
            break
    
    print(f"Retrieved {len(products)} products so far...")

    titles = []
    handles = []
    vendors = []
    tags = []
    prices = []
    for product in products:
        title = product['title']
        handle = product['handle']
        vendor = product['vendor']
        tag_list = product['tags']
        price = product['variants'][0]['price']
        titles.append(title)
        handles.append(handle)
        vendors.append(vendor)
        tags.append(tag_list)
        prices.append(price)
        
    print("Data extracted successfully! to be continued...")
    
    mlb = MultiLabelBinarizer()
    tag_matrix = mlb.fit_transform(tags)
    
    X = np.hstack((tag_matrix, np.array(prices).reshape(-1, 1)))
    
    kmeans = KMeans(n_clusters=2, random_state=0).fit(X)
    print("Clustering completed! to be continued...")
    
    alternates_dict = {}
    for i in range(len(kmeans.labels_)):
        label = kmeans.labels_[i]
        if label not in alternates_dict:
            alternates_dict[label] = []
        product_link = f"{store_domain}/products/{handles[i]}"
        alternates_dict[label].append(product_link)
    
    alternates_json = []
    for key, value in alternates_dict.items():
        alternates_json.append({"product alternates": value})
        
    return json.dumps(alternates_json, indent=4)

def __main__():

    store_domain = input("Enter store domain (Example:https://sartale2022.myshopify.com/collections/all): ")
    alternates = FindAlternateGroups(store_domain)
    print(alternates)
    with open("alternates.json", "w") as f:
        json.dump(alternates, f)

if __name__ == "__main__":
    __main__()
