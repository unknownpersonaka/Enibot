const result1 = document.evaluate(
    "/html/body/app-root/app-mediabook/div[2]/div/div[2]/div/app-right-panel/app-tabs/div/tabset/div/tab[2]/app-summary/perfect-scrollbar/div/div[1]/div/accordion/accordion-group[1]/div/div[2]/div/div/div/div/a[1]/span[1]",
    document,
    null,
    XPathResult.FIRST_ORDERED_NODE_TYPE,
    null,
).singleNodeValue;
result1.click();