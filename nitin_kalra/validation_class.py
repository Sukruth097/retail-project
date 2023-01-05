
import os
import pandas as pd
import glob
import json
import shutil




class validation:

    def __init__(self):
        self.schema_col_count= 0
        self.schema_dtype= []
        self.schema_col_name =[]
        self.init_df = []


    def read_json(self,file):
        with open(file,'r') as f:
            file =f.read()
            schema =json.loads(file)
            self.schema_dtype=list(schema['columns'].values())
            self.schema_col_name = list(schema['columns'].keys())
            self.schema_col_count = len(schema['columns'])
            return self.schema_col_count, self.schema_dtype, self.schema_col_count, self.schema_col_name

    def read_df(self, file):
        self.init_df=[]
        for i in range(0, len(file)):
            df= pd.read_csv(file[i])
            self.init_df.append(df)
        return self.init_df

    def validate(self,match_path, unmatch_path):
        for i in range(0, len(self.init_df)):
            df_column_name= list(self.init_df[i])
            b = self.init_df[i].dtypes.values
            df_data_type= list(map(lambda x:str(x).replace('dtype',"").replace(')',""),b))
            if df_data_type == self.schema_dtype and self.init_df[i].shape[1]==self.schema_col_count and df_column_name == self.schema_col_name:
                shutil.move(csv[i],match_path)
            else:
                shutil.move(csv[i],unmatch_path)


    def merging(self,path):
        if len(self.init_df)==1:
            df= pd.read_csv(self.init_df)
            df.to_csv(path, index=False, header=True)
        elif len(self.init_df)== 0:
            print('no files in directory')
        else:
            df = pd.concat(self.init_df)
            df.to_csv(path,header=True, index=False) 

       

obj =validation()
path = r'D:\data-science\Dbanyan\schema.json'
obj.read_json(path)

path = r'D:\data-science\Dbanyan\Raw_Data'
csv = glob.glob(os.path.join(path, "*.csv"))
obj.read_df(csv)

unmatch_path =r'D:\data-science\Dbanyan\validated_unmatched'
match_path = r'D:\data-science\Dbanyan\validated_matched'
obj.validate(match_path,unmatch_path)


path = r'D:\data-science\Dbanyan\validated_matched'
csv = glob.glob(os.path.join(path, "*.csv"))
obj.read_df(csv)

des =r'D:\data-science\Dbanyan\validated_data'
obj.merging(des)
