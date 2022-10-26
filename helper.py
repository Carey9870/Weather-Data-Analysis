def UniqueWindSpeeds(w_data):
    uws = w_data['Wind Speed_km/h'].unique()
    return uws

def WeatherClear(w_data):
    wc = w_data[w_data.Weather == 'Clear'].count()
    return wc

def WindSpeed4Kmperhr(w_data):
    ws = w_data.groupby(['Wind Speed_km/h']).get_group(4).count()
    return ws

def rename(w_data):
    r = w_data.rename(columns={'Weather':'Weather Condition'}, inplace=True)
    return r

def Visibility(w_data):
    vi = w_data.Visibility_km.mean()
    return vi

def StandardDeviation(w_data):
    std = w_data.Press_kPa.std()
    return std

def Variance(w_data):
    var = w_data['Rel Hum_%'].var()
    return var

def Snow(w_data):
    sn = w_data[w_data['Weather Condition'] == 'Snow']
    return sn

def Instances(w_data):
    ii = w_data[(w_data['Wind Speed_km/h'] > 24) & (w_data['Visibility_km'] == 25)]
    return ii

def MeanValue(w_data):
    wco = w_data.groupby(['Weather Condition']).mean()
    return wco

def Min(w_data):
    w_min = w_data.groupby(['Weather Condition']).min()
    return w_min

def Max(w_data):
    w_max = w_data.groupby(['Weather Condition']).max()
    return w_max

def Fog(w_data):
    fog = w_data.groupby(['Weather Condition']).get_group('Fog')
    return fog

def Cv(w_data):
    cv40 = w_data[(w_data['Weather Condition'] == 'Clear') | (w_data['Visibility_km'] > 40)]
    return cv40

def Wcc(w_data):
    wcc50 = w_data[((w_data['Weather Condition'] == 'Clear') & (w_data['Rel Hum_%'] > 50)) | (w_data['Visibility_km'] > 40)]
    return wcc50