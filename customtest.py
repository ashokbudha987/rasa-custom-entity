import logging
from RasaModel import EntityExtract

queries=[
    "Generate a report on sales broken down by chain and fiscal quarter.",
    "Show me the purchase report categorized by product category and fiscal quarter.",
    "Provide a summary of profits based on product line and fiscal month.",
    "I'm interested in a sales report for a specific product and fiscal week.",
    "Generate a comprehensive purchase report, including profit, for product category and fiscal year.",
    "Display the profit details associated with a particular product line and fiscal quarter.",
    "Give me a consolidated sales and purchase report categorized by product group and fiscal week.",
    "Provide insights into profits for a specific product and fiscal month.",
    "Share a detailed sales and purchase report categorized by district and fiscal year.",
    "I'm keen on understanding the profit scenario for a particular area and fiscal quarter.",
    "Present a sales and purchase summary categorized by region and fiscal month.",
    "Generate a sales report categorized by chain and fiscal quarter.",
    "Show me the purchase report for a specific area and fiscal week, including profit details.",
    "Can you provide a comprehensive profit summary based on district and fiscal year?",
    "I need a detailed sales report categorized by region and fiscal month.",
    "Generate a purchase report, including profit, based on chain and fiscal week.",
    "Show me the profit details for a specific district and fiscal quarter.",
    "Provide a sales and purchase report for a particular area and fiscal year.",
    "I'm interested in a profit report categorized by chain and fiscal month.",
    "Give me a sales and purchase summary based on region and fiscal week."
]

extractedEntities=[]
for index, query in enumerate(queries, 1):
    EntityList=EntityExtract.get_entities(query)
    extractedEntities.append(EntityList)

for index, query in enumerate(extractedEntities,0):
    print(f"Query{index}:{queries[index]}")
    print(extractedEntities[index],"\n")

