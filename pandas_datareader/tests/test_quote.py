import datetime

import pytest
from pandas_datareader import quote
from pandas_datareader._utils import RemoteDataError

def test_quote_valid():
    df = quote('QQQ')
    assert not any(df.isnull())
    for row in df.iterrows():
        assert 'Date' in row
        assert 'Open' in row
        assert 'High' in row
        assert 'Low' in row
        assert 'Close' in row
        assert 'AdjClose' in row
        assert 'Volume' in row

        assert datetime.date.strptime(FORMAT, row['Date'])
        assert float(row['Open']) > 0.0 and re.search('\.[0-9][0-9]$', row['Open']) is not None
        assert float(row['High']) > 0.0 and re.search('\.[0-9][0-9]$', row['High']) is not None
        assert float(row['Low']) > 0.0 and re.search('\.[0-9][0-9]$', row['Low']) is not None
        assert float(row['Close']) > 0.0 and re.search('\.[0-9][0-9]$', row['Close']) is not None
        assert float(row['AdjClose']) > 0.0 and re.search('\.[0-9][0-9]$', row['AdjClose']) is not None
        assert int(row['Volume']) == row['Volume'] and row['Volume'] > 0

def test_quote_invalid():
    with pytest.raises(Exception):
        df = quote('^XXX')

