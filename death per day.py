from openpyxl import load_workbook
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

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
    #create rolling average
    df_ra = df.rolling(window, center=True, min_periods=1).mean().round()
    
    #calculate week-wise differences
    df_rad = df_ra.copy()
    for i, col in enumerate(df_rad.columns[1:]):
        df_rad.iloc[:,i+1] = df_ra.iloc[:,i+1]-df_ra.iloc[:,i]
    
    #filter negative values
    df_rad[df_rad < 0] = 0
    
    #stacked-area plot
    matplotlib.style.use('seaborn-pastel')
    labelz = ["%s,  \u2020 %d" % (dat.strftime("%b %d"),df_rad[dat].sum()) for dat in df_rad.columns]
    axes1 = df_rad.plot.area(stacked=True, title='Deaths per day')
    h1, l1 = axes1.get_legend_handles_labels()
    axes1.legend(h1,labelz)
    plt.tight_layout()
    
    #separate week plots
    axes2 = df_rad.plot.area(stacked=False, title='Deaths per day', subplots=True)
    for i,axe in enumerate(axes2):
        h,l = axe.get_legend_handles_labels()
        axe.legend(h,[labelz[i]])
    
    plt.tight_layout()
    
    
df = loadWorkbook('Death per day.xlsx')
rollingPlot(df,7)

#first and last week comparison
df.drop(df.columns[[1,2,3,4,5]], axis=1, inplace=True)
rollingPlot(df,7)
rollingPlot(df[:-24],7)
