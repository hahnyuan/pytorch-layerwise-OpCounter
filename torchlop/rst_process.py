import pandas as pd

def write_csv(csv_file,layer_infos):
    pd_data=pd.DataFrame(layer_infos).T
    pd_data.to_csv(csv_file)
    # with open(csv_file,'w') as f:
    #     f.write(layer[0].key())
    #     for layer_name,layer in layer_infos.items():
    #         f.write(layer_name+',')
    #         f.write(','.join(layer.values()))
    #         f.write('\n')

if __name__=='__main__':
    infos={'a':{'x':12,'ds':'ds'},'b':{'x':22,'ds':'322'}}
    write_csv('test.csv',infos)