from lxml import etree
text='''
<div>
    <ul>
        <li class="item-0"><a href="0.html"> first item</a></li>
        <li class="item-1"><a href="0.html"> first item</a></li>
        <li class="item-2"><a href="0.html"> first item</a></li>
        <li class="item-3"><a href="0.html"> first item</a></li>
        <li class="item-4"><a href="0.html"> first item</a>
    </ul>
</dev>
'''
html = etree.HTML(text)
s = etree.tostring(html)
print(s)