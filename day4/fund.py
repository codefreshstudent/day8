import quartz_extensions.FundAnalysis.analysis as fa

symbol = '000001.OFCN'
start = '2018-01-01'
end = '2018-08-01'

nav = fa.nav(symbol, start, end)
print(nav.head().to_html())

nav.plot(figsize=(20,10))