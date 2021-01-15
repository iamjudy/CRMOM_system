from pyecharts import options as opt
import base64
import math
import random
import datetime
from io import BytesIO

from django.http import HttpResponse

from pyecharts.charts import Bar, Line
from pyecharts.globals import ThemeType


from pyecharts.charts import Bar, Line
from pyecharts.globals import ThemeType
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from plotly.offline import plot
from plotly.graph_objs import Scatter



from .models import (
    Supplier,
    Material,
    Product,
    Order,
    Dealer,
    Consume,
    Use,
    Retention,
)
from .forms import (
    SupplierForm,
    MaterialForm,
    ProductForm,
    OrderForm,
    DealerForm,
    RawRateForm,
    RawCustomerForm,
    RawOrderForm,
    RawCategoryForm,
)


# Supplier views
@login_required(login_url='login')
def create_supplier(request):
    forms = SupplierForm()
    if request.method == 'POST':
        forms = SupplierForm(request.POST)
        if forms.is_valid():
            s_ID = forms.cleaned_data['s_ID']
            s_name = forms.cleaned_data['s_name']
            s_phone = forms.cleaned_data['s_phone']
    context = {
        'form': forms
    }
    return render(request, 'store/create_supplier.html', context)


class SupplierListView(ListView):
    model = Supplier
    template_name = 'store/supplier_list.html'
    context_object_name = 'supplier'


# Material views
@login_required(login_url='login')
def create_material(request):
    forms = MaterialForm()
    if request.method == 'POST':
        forms = MaterialForm(request.POST)
        if forms.is_valid():
            m_ID = forms.cleaned_data['m_ID']
            m_name = forms.cleaned_data['m_name']
            m_amount = forms.cleaned_data['m_amount']
            m_price = forms.cleaned_data['m_price']
        if forms.is_valid():
            forms.save()
            return redirect('material-list')
        context = {
            'form': forms
        }
        return render(request, 'store/create_material.html', context)


class MaterialListView(ListView):
    model = Material
    template_name = 'store/material_list.html'
    context_object_name = 'material'


# Product views
@login_required(login_url='login')
def create_product(request):
    forms = ProductForm()
    if request.method == 'POST':
        forms = ProductForm(request.POST)
        if forms.is_valid():
            p_ID = forms.cleaned_data['p_ID']
            p_name = forms.cleaned_data['p_name']
            p_price = forms.cleaned_data['p_price']
    context = {
        'form': forms
    }
    return render(request, 'store/create_product.html', context)


class ProductListView(ListView):
    model = Product
    template_name = 'store/product_list.html'
    context_object_name = 'product'


# Order views
@login_required(login_url='login')
def create_order(request):
    forms = OrderForm()
    if request.method == 'POST':
        forms = OrderForm(request.POST)
        if forms.is_valid():
            o_id = forms.cleaned_data['o_id']
            o_amount = forms.cleaned_data['o_amount']
            o_price = forms.cleaned_data['o_price']
            o_date = forms.cleaned_data['o_date']

    context = {
        'form': forms
    }
    return render(request, 'store/create_order.html', context)


class OrderListView(ListView):
    model = Order
    template_name = 'store/order_list.html'
    context_object_name = 'order'


# Dealer views
@login_required(login_url='login')
def create_dealer(request):
    forms = DealerForm()
    if request.method == 'POST':
        forms = DealerForm(request.POST)
        if forms.is_valid():
            d_ID = forms.cleaned_data['d_ID']
            d_name = forms.cleaned_data['d_name']
            d_phone = forms.cleaned_data['d_phone']
    context = {
        'form': forms
    }
    return render(request, 'store/create_dealer.html', context)


class DealerListView(ListView):
        model = Dealer
        template_name = 'store/dealer_list.html'
        context_object_name = 'dealer'

def testt(request):
    import numpy as np  # 快速操作結構数组的工具
    import matplotlib.pyplot as plt  # 可視化繪製
    from sklearn.linear_model import LinearRegression  # 線性迴歸

    # 樣本數據集，第一列为x，第二列为y，在x和y之間建立回歸模型
    data = [
        [1, 5.43], [2, 4.78], [3, 4.550095], [4, 2.1], [5, 1.87],
        [6, 3], [7, 3.526170], [8, 3.156393], [9, 3.110301], [10, 3.149813],
        [11, 3.4], [12, 3.6]
    ]

    # 生成X和y矩阵
    dataMat = np.array(data)
    X = dataMat[:, 0:1]  # 變量x
    y = dataMat[:, 1]  # 變量y

    # 線性迴歸
    model = LinearRegression(copy_X=True, fit_intercept=True, n_jobs=1, normalize=False)
    model.fit(X, y)  # 線性迴歸建模
    x = str(model.coef_)
    print('系数矩阵:\n', x)

    print('线性回归模型:\n', model)
    # 使用模型預測
    predicted = model.predict(X)

    # 繪製散點圖 參數：x橫軸 y縱軸
    plt.scatter(X, y, marker='x')
    plt.plot(X, predicted, c='r')

    # 繪製x軸和y軸座標
    plt.xlabel("month")
    plt.ylabel("demand(000)")

    # 顯示圖形
    # 转成图片的步骤
    sio = BytesIO()
    plt.savefig(sio, format='png')
    data = base64.encodebytes(sio.getvalue()).decode()

    imd = "data:image/png;base64," + data
    context = {
        'img': imd,
        'x': x,
    }
    return render(request, "store/testt.html", context)


def month_id(request):
    try:
        x=request.POST['m_ID']
    except KeyError:
        x='1'
    return x

def year_id(request):
    try:
        x = request.POST['y_ID']
    except KeyError:
        x = '2020'
    return x


def post_id(request):
        try:
            x = request.POST['filt_id']
        except KeyError:
            x = '001'
        return x

def Raw_EOQ(request):
    low = Material.objects.all().order_by('m_inventory')
    YS = Material.objects.all().filter(m_ID = post_id(request)).values('m_estdemand')
    theid = post_id(request)
    YearS = list(YS)
    Stotal = 0
    for i in YearS:
        Stotal += i['m_estdemand']
    Sday = float(Stotal)
    Y_Sales = Sday * 300
# 300*為每年販售天數*日銷
    OC = Material.objects.all().filter(m_ID = post_id(request)).values('m_price')
    O = list(OC)
    Order_Cost = 0
    for i in O:
        Order_Cost += i['m_price']
    Ordercost = float(Order_Cost)
# 訂購成本
    HC = Material.objects.all().filter(m_ID = post_id(request)).values('m_hcost')
    H = list(HC)
    H_Cost = 0
    for i in H:
        H_Cost += i['m_hcost']
    Holding = float(H_Cost)
# 100為生產準備費用
    e = (2 * Y_Sales * Ordercost)
    p = Holding

    try:
        Q = e / p
    except ZeroDivisionError:
        Q = 0
    C_EOQ = math.sqrt(Q)
    C_EOQ = round(C_EOQ, 0)
    int(C_EOQ)
    # product list 選單
    allproduct = Material.objects.values('m_ID').distinct()

    # 更新EOQ置資料庫
    inventory = Material.objects.filter(m_ID=post_id(request)).values('m_inventory')
    inv = list(inventory)
    left = 0
    for i in inv:
        left += i['m_inventory']
    products_in = int(left)
    new = products_in + C_EOQ
    Material.objects.filter(m_ID=post_id(request)).update(m_inventory=new)
    Material.objects.filter(m_ID=post_id(request)).update(m_date=datetime.datetime.now())
    reorder = Material.objects.filter(m_ID=post_id(request)).values('m_estdemand')
    re = list(reorder)
    r = 0
    for i in re:
        r += i['m_estdemand']
    d_demand = int(r)
    days = random.randint(15, 20)
    re_point = d_demand * days + 750
    return render(request, 'store/material.html', locals())


def raw_plot(request):
    allproduct = Material.objects.values('m_name').distinct()
    YS = Material.objects.all().filter(m_ID=post_id(request)).values('m_estdemand')
    YearS = list(YS)
    try:
        daydemand = YearS[0]['m_estdemand']
    except IndexError:
        daydemand = 0
    n = int(daydemand)

    supply = Material.objects.all().filter(m_ID=post_id(request)).values('m_estsupply')
    sup = list(supply)
    try:
        daysupply = sup[0]['m_estsupply']
    except IndexError:
        daysupply = 0
    s = int(daysupply)

    inventory = Material.objects.all().filter(m_ID=post_id(request)).values('m_inventory')
    inventory = list(inventory)
    try:
        inventory = inventory[0]['m_inventory']
    except IndexError:
        inventory = 0

    m = int(inventory)
    # 假設每三個期間再訂購一次 estdemand*3=estsupply
    x_data = [n, 2 * n, 3 * n - s, 4 * n - s, 5 * n - s, 6 * n - 2 * s, 7 * n - 2 * s, 8 * n - 2 * s, 9 * n - 3 * s,
              10 * n - 3 * s, 11 * n - 3 * s, 12 * n - 4 * s, 13 * n - 4 * s, 14 * n - 4 * s, 15 * n - 5 * s,
              16 * n - 5 * s, ]
    y_data = [inventory - x for x in x_data]
    plot_div = plot([Scatter(x=[i for i in range(17)], y=y_data,
                             mode='lines', name='inventory',
                             opacity=0.8, marker_color='red')],
                            output_type='div')
    return render(request, 'store/raw_plot.html', locals())

def EOQ_calculate(request):
        low = Product.objects.all().order_by('p_inventory')
        YS = Product.objects.all().filter(p_ID = post_id(request)).values('p_estdemand')
        theid = post_id(request)
        YearS = list(YS)
        Stotal = 0
        for i in YearS:
            Stotal += i['p_estdemand']
        Sday = float(Stotal)
        Y_Sales = Sday * 300
    #300*為每年販售天數*日銷
        OC = Product.objects.all().filter(p_ID = post_id(request)).values('p_cost')
        O = list(OC)
        Order_Cost = 0
        for i in O:
            Order_Cost += i['p_cost']
        Ordercost = float(Order_Cost)
    #訂購成本
        HC = Product.objects.all().filter(p_ID = post_id(request)).values('p_hcost')
        H = list(HC)
        H_Cost = 0
        for i in H:
            H_Cost += i['p_hcost']
        Holding = float(H_Cost)
        #100為生產準備費用
        e =  (2*Y_Sales*Ordercost)
        p = Holding
        #Q = e/p
        try:
            Q = e/p
        except ZeroDivisionError:
            Q = 0
        C_EOQ = math.sqrt(Q)
        C_EOQ = round(C_EOQ,0)
        int(C_EOQ)
    #product list 選單
        allproduct = Product.objects.values('p_ID').distinct()

    #更新EOQ置資料庫
        inventory = Product.objects.filter(p_ID = post_id(request)).values('p_inventory')
        inv = list(inventory)
        left = 0
        for i in inv:
            left += i['p_inventory']
        products_in = int(left)
        new = products_in + C_EOQ
        Product.objects.filter(p_ID = post_id(request)).update(p_inventory = new)

        reorder = Product.objects.filter(p_ID = post_id(request)).values('p_estdemand')
        re = list(reorder)
        r = 0
        for i in re:
            r += i['p_estdemand']
        d_demand = int(r)
        days = random.randint(15, 20)
        re_point = d_demand * days + 750
        return render(request, 'store/order.html', locals())

def rate(request):
    form = RawRateForm(request.POST or None)
    rate = 0
    rate1 = 0
    first = 0
    second = 0
    third = 0
    num = 0
    if form.is_valid():
        sn = form.cleaned_data['經銷商名稱']
        pn = form.cleaned_data['產品名稱']
        before = form.cleaned_data['前期顧客數量']
        today = form.cleaned_data['本期留存顧客數量']
        d = Dealer.objects.get(d_name=sn)
        d1 = d.d_ID
        p = Product.objects.get(p_name=pn)
        p1 = p.p_ID
        sale = Order.objects.filter(d_ID=d1, p_ID=p1)
        for q in sale:
            num += q.o_amount
        rate = round(((today/before)*100), 2)
        rate1 = 100 - rate
        first = round(today, 2)
        second = round((today * rate/100), 2)
        third = round((second * rate/100), 2)
    context = {
        'form': form,
        'rate': rate,
        'rate1': rate1,
        'first': first,
        'second': second,
        'third': third,
        'num': num
    }
    return render(request, "rate.html", context)

def cat(request):
    return render(request, "category.html")


def time(request):
    form = RawCustomerForm(request.POST or None)
    timesave = []
    timespan = 0
    if form.is_valid():
        sn = form.cleaned_data['經銷商名稱']
        pn = form.cleaned_data['產品名稱']
        d = Dealer.objects.get(d_name=sn)
        d1 = d.d_ID
        p = Product.objects.get(p_name=pn)
        p1 = p.p_ID
        order_list = Order.objects.filter(d_ID=d1, p_ID=p1)

        for o in order_list:
            timesave.append(o.o_date)
            annual_duration = timesave[-1] - timesave[0]
            number = len(timesave)
            timespan = annual_duration / number

            # tt = int(timespan)
    context = {
        'form': form,
        'time': timespan,
        # 'tt' : tt
    }  # 建立字典做對應 看time.html
    return render(request, 'time.html', context)

def new(request):
    form = RawOrderForm(request.POST or None)

    if form.is_valid():
         Order.objects.create(**form.cleaned_data)
         pn = form.cleaned_data['p_ID']
         q = form.cleaned_data['o_amount']
         pro = Product.objects.get(p_ID=pn)
         p_new = pro.p_inventory - q
         Product.objects.filter(p_ID=pn).update(p_inventory=p_new)

    context = {
         'form': form
    }

    return render(request, "new.html", context)