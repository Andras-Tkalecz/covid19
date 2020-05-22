from openpyxl import load_workbook
import pandas as pd
import matplotlib

def loadWorkbook(wbName):
    # load the workbook from file and get the first sheet
    wb = load_workbook(wbName)
    ws = wb.active
    
    df = pd.DataFrame(ws.values)
    df.fillna(0, inplace=True)
    df.columns = df.iloc[0,:]
    df = df.drop([0])
    df.set_index(df.columns[0], inplace=True)
    df.columns.name = ''
    
    return df

def rollingPlot(df, window):
    df_ra = df.rolling(window, center=True, min_periods=1).mean()
    
    df_rad = df_ra.copy()
    for i, col in enumerate(df_rad.columns[1:]):
        df_rad.iloc[:,i+1] = df_ra.iloc[:,i+1]-df_ra.iloc[:,i]
    
    #filter negative values
    df_rad[df_rad < 0] = 0
    
    #stajl = ['seaborn-pastel' for i in range(5)]
    matplotlib.style.use('seaborn-pastel')
    labelz = [dat.strftime("%b %d") for dat in df_rad.columns]
    axes1 = df_rad.plot.area(stacked=True, title='Deaths per day')
    
    h, l = axes1.get_legend_handles_labels()
    axes1.legend(h,labelz)


df = loadWorkbook('Death per day.xlsx')
rollingPlot(df,7)
df.drop(df.columns[[1,2,3]], axis=1, inplace=True)
rollingPlot(df,7)