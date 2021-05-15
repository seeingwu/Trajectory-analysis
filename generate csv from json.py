import json
import pandas as pd

def Json2csv(json_path, csv_path):
    f = open(json_path, encoding='utf-8') # read json
    data = json.load(f) # convert it to the dictionary
    
    df = pd.DataFrame(data['features']) 
    # read the data according to the key
    df['geometry/type'] = df['geometry'].apply(lambda x: x['type'])
    df['longitude'] = df['geometry'].apply(lambda x: x['coordinates'][0])
    df['latitude'] = df['geometry'].apply(lambda x: x['coordinates'][1])
    df['properties/name'] = df['properties'].apply(lambda x: x['name'] if 'name' in x.keys() else '')
    df['properties/styleUrl'] = df['properties'].apply(lambda x: x['styleUrl'])
    df['properties/styleHash'] = df['properties'].apply(lambda x: x['styleHash'])
    df['properties/description'] = df['properties'].apply(lambda x: x['description'])
    def desc(x, col):
        # select the data from properties/description
        x_list = x['description'].split('\n') 
        value = [v for v in x_list if v.find(col) != -1]
        if value == []:
            return ''
        else:
            return value[0].split(': ')[1]
        
    df['Network ID'] = df['properties'].apply(lambda x: desc(x, 'Network ID'))
    df['Encryption'] = df['properties'].apply(lambda x: desc(x, 'Encryption'))
    df['properties/description/Time'] = df['properties'].apply(lambda x: desc(x, 'Time'))
    df['properties/description/Signal'] = df['properties'].apply(lambda x: desc(x, 'Signal'))
    df['properties/description/Accuracy'] = df['properties'].apply(lambda x: desc(x, 'Accuracy'))
    df['properties/description/Type'] = df['properties'].apply(lambda x: desc(x, 'Type'))
    # delete the repetitive columns.
    df.drop(columns = ['geometry', 'properties'], inplace = True)
    # split the time and date
    df1=df['properties/description/Time'].str.split('T',expand=True)
    df['date']=df1[0]
    df['time']=df1[1].str.split('.',expand=True)[0]
    
    # sort the data
    df=df.sort_values(by='time',ascending=True)
    
    
    # 导出数据
    df.to_csv(csv_path, index = False)
    

