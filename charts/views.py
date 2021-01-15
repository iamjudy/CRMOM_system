from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from pyecharts import options as opts
from pyecharts.charts import Bar, Line
from pyecharts.globals import ThemeType
from pyecharts.faker import Faker
import random
import math
from store.models import Material
import datetime

from store.models import (
    Supplier,
    Material,
    Product,
    Order,
    Dealer,
    Consume,
    Use,
    Retention,
)

# Create your views here.
def demo(request):
    import store
    bar = Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))

    #x = store.models.Product.objects.get(sortno=1)
    #y = store.models.Product.objects.get(sortno=2)

    bar.add_xaxis(["純色腮紅", "三色修容餅", "柔焦無瑕粉餅", "經典緞光唇膏", "精萃水亮唇膏"])
    bar.add_yaxis("康是美", [100, 50, 45, 20, 50])
    bar.add_yaxis("寶雅", [80, 40, 10, 100, 70])
    bar.add_yaxis("屈臣氏", [20, 30, 45, 130, 80])

    bar.set_global_opts(title_opts=opts.TitleOpts(title="品類需求量", subtitle="個"))

    return HttpResponse(bar.render_embed())

def demoo(request):
    import store
    line = Line(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))

    #x = store.models.Product.objects.get(sortno=1)
    #y = store.models.Product.objects.get(sortno=2)

    line.add_xaxis(["1月", "2月", "3月", "4月", "5月", "6月"])
    line.add_yaxis("純色腮紅", [2000, 1800, 2800, 1900, 2000, 1400])
    line.add_yaxis("三色修容餅", [2100, 1900, 2400, 1600, 1850, 1600])
    line.add_yaxis("柔焦無瑕粉餅", [1900, 2000, 2050, 1900, 2000, 1950])
    line.add_yaxis("經典緞光唇膏", [2000, 1800, 1900, 2000, 1900, 2000])
    line.add_yaxis("精萃水亮唇膏", [1700, 1500, 2200, 1800, 1670, 1700])
    line.set_global_opts(title_opts=opts.TitleOpts(title='2020存貨走勢圖'))

    return HttpResponse(line.render_embed())

def test(request):
    from plotly.offline import plot
    import plotly.graph_objs as go

    fig = go.Figure()
    scatter = go.Scatter(x=["1月", "2月", "3月", "4月"], y=[120,100,224,140],
                         mode='lines', name='test',
                         opacity=0.8, marker_color='green')
    fig.add_trace(scatter)


    plt_div = plot(fig, output_type='div')

    return HttpResponse(plt_div)





def catchart(request):
    line = Line(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
    # form = RawCategoryForm(request.POST or None)
    p = request.POST.get('pp_name')
    pp = Product.objects.get(p_ID=p)
    pp_n = pp.p_name
    print(type(p))
    an = int(request.POST.get('a_amount'))
    bn = int(request.POST.get('b_amount'))
    cn = int(request.POST.get('c_amount'))
    ac = 0
    bc = 0
    cc = 0
    aq = 0
    bq = 0
    cq = 0
    ad = Order.objects.filter(d_ID='1', p_ID=p)
    bd = Order.objects.filter(d_ID='2', p_ID=p)
    cd = Order.objects.filter(d_ID='3', p_ID=p)
    for q in ad:
        aq += q.o_amount
    for w in bd:
        bq += w.o_amount
    for e in cd:
        cq += e.o_amount
    ac = round(((aq / an) * 100), 2)
    bc = round(((bq / bn) * 100), 2)
    cc = round(((cq / cn) * 100), 2)

    d1 = Dealer.objects.get(d_ID='1')
    d1_n = d1.d_name
    d2 = Dealer.objects.get(d_ID='2')
    d2_n = d2.d_name
    d3 = Dealer.objects.get(d_ID='3')
    d3_n = d3.d_name

    x = [d1_n, d2_n, d3_n]
    y1 = [ac, bc, cc]

    line.set_global_opts(title_opts=opts.TitleOpts(title='品類需求佔有率', subtitle='%'))
    line.add_xaxis(x)
    line.add_yaxis(pp_n, y1)

    return HttpResponse(line.render_embed())
