# Product-alternates-Using-Kmeans

This is a Python script that uses the K-means clustering algorithm to group similar products together based on their tags and prices. The script retrieves product data from a Shopify 
store and applies the K-means algorithm to cluster the products into two groups. It then creates a dictionary where the keys are the cluster labels and the values are lists of product
links belonging to that cluster. Finally, it outputs the dictionary as a JSON file.

Here is an overview of the files in the repository:

app.py: This is the main script that implements the product clustering logic.
requirements.txt: This file lists the Python packages required by the script.
README.md: This file contains information about the repository and how to use the script.

To use the script, you need to have Python installed on your system along with the required packages listed in requirements.txt. You can install the packages using the following command:

# pip install -r requirements.txt

Once the packages are installed, you can run the script by providing the domain name of your Shopify store as an input. The script will retrieve the product data from the store and 
output a JSON file containing the clustered product links.

# python app.py

The output JSON file will be saved as alternates.json in the same directory as the script.
