import pandas as pd


def suppliers_rating(file_path, a1, a2):
    suppliers = pd.read_excel(file_path, sheet_name="Постачальники")
    products = pd.read_excel(file_path, sheet_name="Продукція")
    prices = pd.read_excel(file_path, sheet_name="Ціна")
    
    prices["Prices"] = prices["Price"].astype(float)
    suppliers["Rating"] = suppliers["Rating"].astype(float)
    
    prices = prices.dropna(subset=["Price"])
    suppliers = suppliers.dropna(subset=["Rating"])
    
    merged_data = prices.merge(suppliers, left_on="S_id", right_on="Id", how="left")
    merged_data = merged_data.merge(products, left_on="P_id", right_on="Id", how="left")
    
    Pmax = merged_data["Price"].max()   # max price
    Rmax = merged_data["Rating"].max()  # max rating
    
    merged_data["R"] = (
        a1 * (1 - merged_data["Price"] / Pmax) + 
        a2 * (merged_data["Rating"] / Rmax)
    )
    
    ranked_suppliers = merged_data.sort_values(by="R", ascending=False)
    
    result = ranked_suppliers[[
        "S_id", "R", "Name_x", "Adress", "P_id", "Name_y", "Price", "Term"
    ]].rename(
        columns = {
            "Name_x": "Name_S",
            "Name_y": "Name_P"
        }
    )   

    return result


if  __name__ == "__main__":
    file_path = "data.xlsx"  
    a1 = 0.4  # Price coef
    a2 = 0.6  # Rating coef

    if a1 + a2 != 1.0:
        raise Exception(f"a1 ({a1}) with a2 ({a2}) in sum must be 1.0, not {a1 + a2}")

    rating = suppliers_rating(file_path, a1, a2)
    print("Suppliers rating:")
    print(rating)

