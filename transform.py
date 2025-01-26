import pandas as pd

def get_data():
    df = pd.read_csv('apple_sales_2024.csv')
    data_dict = {}
    for col in df.columns:
        data_dict[col] = df[col].to_list()
    
    return data_dict


def top_30_revenues():
    data_dict = get_data()
    states = data_dict['State']
    revenues = data_dict['Services Revenue (in billion $)']
    state_n_revenue = list(zip(states, revenues))

    sorted_revenues = sorted(state_n_revenue, key=lambda x: x[1], reverse=True)
    top_30_revenues = sorted_revenues[:30]
    
    return top_30_revenues

def state_by_highest_sales_of_unit(unit_name):
    data_dict = get_data()
    item = data_dict[unit_name]
    item_max = max(item)
    max_index = item.index(item_max)
    state = data_dict['State'][max_index]

    return state, item_max

iphone = state_by_highest_sales_of_unit('iPhone Sales (in million units)')
ipad = state_by_highest_sales_of_unit('iPad Sales (in million units)')
mac = state_by_highest_sales_of_unit('Mac Sales (in million units)')
iwatch = state_by_highest_sales_of_unit('Wearables (in million units)')

if __name__ == 'main':
    get_data()
