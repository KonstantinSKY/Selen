# SELEN 
this is a mini framework or an add-on for the selenium and unitest frameworks

## Basic goals

- making it easier to write code of tests
- improving code readability
- to reduce the amount of code written
- accelerating the development of tests based on selenium and unittest frameworks
- error reduction



## Quick start and what can Selen do:

### New find method and simplified adding locators as method arguments

In Selenium it was like this:
```python

driver.find_element(By.ID, "id")
driver.find_element(By.NAME, "name")
driver.find_element(By.XPATH, "xpath")
driver.find_element(By.LINK_TEXT, "link text")
driver.find_element(By.PARTIAL_LINK_TEXT, "partial link text")
driver.find_element(By.TAG_NAME, "tag name")
driver.find_element(By.CLASS_NAME, "class name")
driver.find_element(By.CSS_SELECTOR, "css selector")

```
in Selen now is:
```python
se.Find(ID, "id")
se.Find(NAME, "name")
se.Find(XPATH, "xpath")
se.Find(LINK, "link text")
se.Find(PART_LINK, "partial link text")
se.Find(TAG, "tag name")
se.Find(CLASS, "class name")
se.Find(CSS, "css selector")
```
- No exception handling is required, the logic is already inside the White method
***-`se` is short from `self`

### Simplified adding locators to methods by several variants
In usual Selenium Was like:
```python
driver.find_element(By.XPATH, "//body/div[@id='fb-root']/div[@id='root']/div[1]/div[1]/div[2]/div[1]")
driver.find_element(By.CLASS_NAME, ""Login_submit_wrapper__2-PYe"")

#or
driver.find_element("xpath", "//body/div[@id='fb-root']/div[@id='root']/div[1]/div[1]/div[2]/div[1]")
driver.find_element("class name", ""Login_submit_wrapper__2-PYe"")

#or with locator variables
xpath_locator = ("xpath", "//body/div[@id='fb-root']/div[@id='root']/div[1]/div[1]/div[2]/div[1]")
class_locator = ("class_name", "Login_submit_wrapper__2-PYe"")

driver.find_element(*xpath_locator)
driver.find_element(class_locator[0], class_locator[1])
```
With Selen is:
```python
se.Find(XPATH, "//body/div[@id='fb-root']/div[@id='root']/div[1]/div[1]/div[2]/div[1]")
se.Find(CLASS, ""Login_submit_wrapper__2-PYe"")

#or with locator variables
xpath_locator = (XPATH, "//body/div[@id='fb-root']/div[@id='root']/div[1]/div[1]/div[2]/div[1]")
class_locator = (CLASS, "Login_submit_wrapper__2-PYe"")

se.Find_element(xpath_locator)
se.Find_element(class_locator)
```
## Principles and rules of the Selen using

### `Find()` and `find()` are differents method
Methods `Find` with Capital first letter used if it calls first after the WebDriver (for All WEB page elements) and the lowercase method `find` is used when calling after another already found element.
There are several more methods that work in the same principle. But more on that later.

`se.Find(locator(s),[locators(s), ... locators(s])`

`se.find(locator(s),[locator(s), ...locators(s)])`

In Selenium Was:
```python
driver.find_element(By.XPATH, "//xpath string...").find_element(By.CLASS_NAME, Login_submit_wrapper__2-PYe)

#or with locator variables
xpath_locator = ("xpath", "//body/div[@id='fb-root']/div[@id='root']/div[1]/div[1]/div[2]/div[1]")
class_locator = ("class_name", "Login_submit_wrapper__2-PYe"")
tag_locator = ("tag name", "input")

driver.find_element(*xpath_locator).find_element(*class_locator).find_element(*tag_locator)
```
Now with Selen:
```python
se.Find(XPATH, "//xpath string...").find(CLASS, "Login_submit_wrapper__2-PYe)

#or with locator variables
xpath_locator = (XPATH, "//body/div[@id='fb-root']/div[@id='root']/div[1]/div[1]/div[2]/div[1]")
class_locator = (CLASS, "Login_submit_wrapper__2-PYe)
tag_locator = (TAG, "input")

se.Find(xpath_locator).find(class_locator).find(tag_locator)
```
### Even shorter code in method chains to find a set of elements
Several ways to search for elements by a chain of locators, all locators in one `Find` method  
```python
# all locator as tuples inside one method 
se.Find((XPATH, "//xpath string..."),(CLASS, "Login_submit_wrapper__2-PYe))

#or with locator variables
xpath_locator = (XPATH, "//body/div[@id='fb-root']/div[@id='root']/div[1]/div[1]/div[2]/div[1]")
class_locator = (CLASS, "Login_submit_wrapper__2-PYe)
tag_locator = (TAG, "input")

se.Find(xpath_locator, class_locator, tag_locator)

#or All locators in one variable : Tuple of tuples
locators = ((XPATH, "//body/div[@id='fb-root']/div[@id='root']/div[1]/div[1]/div[2]/div[1]"),
            (CLASS, "Login_submit_wrapper__2-PYe),
            (TAG, "input"))

se.Find(locators)

#or Combined addition of locators  
se.Find(locators, xpath_locator, (TAG, "a"))
se.Find((Tag, "a"), xpath_locators, locators)
# ! Any combinations as You wish
```
### Assigning an element or elements to a variables 
The ways of assigning elements to variables in Selen and Selenium are different

Selenium Example:
```python
# one_element is instance of WebElement
one_element = driver.find_element(By.XPATH, '//button[text()="Some text"]')

# many_elements is list (array) of instances of WebElement
many_elements = driver.find_elements(By.XPATH, '//button')
```
Selen Example:
```python
# one_element is instance of WebElement
one_element = se.Find(XPATH, '//button[text()="Some text"]').elem

# many_elements is list (array) of instances of WebElement
many_elements = se.Find(XPATH, '//button').elems
```
`Find` and other methods of finding WebElements and other similar methods return `one` WebElement and `many` WebElements at the same time and stores them in internal variables: `se.elem` and `se.elems`

They will be available by these names and it will also be possible to perform some actions with them until another method(s) saves new data there

All  searching methods always find a array of WebElements and gets a single WebWlement as the first element of the array

`se.elem == se.elems[0]`


### Chains of Selen methods and actions with them
Almost all methods of finding WebElements and actions on them can be assembled logical chains of code

If the code chain in one line getting the end, but actions on the last found elements can be continued in a new line, because these elements are stored in the variables: `se.elen` and `se.elems` 
Exampe:
```python
email="email@gmail.com"
se.Find(NAME, "email").type(email).sleep(0.2, 1).attr('value', email).parent(2).tag("span").attr('class', 'validation_status_ok')

```
The same code results:
```python
email = "email@email.com"
se.Find(NAME, "email").type(email).sleep(0.2, 1).attr('value', email")
se.parent(2).tag("span").attr('class', 'validation_status_ok')
#or
se.Find(NAME, "email")
se.type(email).
se.sleep(0.2, 1)
se.attr('value', email)
se.parent(2)
se.tag("span")
se.attr('class', 'validation_status_ok')
```
This code does next steps:
- found WebElement by attribute `NAME="email"`
- type text from the `email` variable to the WebElement
- random delay from 0.2 to 1 seconds
- check for new WebElement attribute `'value'= email`
- find new parrent element to 2 levels up
- find element by Tag `span`
- check attribute `'class' = 'validation_status_ok'`

## Findind by locators with indexes of element in array of elements in `se.elems`
Sometimes we need to find a lot of elements then select one or more of them by index and continue searching inside it

In Selenium: 
```python
driver.find_elements(By.XPATH, "//xpath string...")[3].find_element(By.CLASS_NAME, Login_submit_wrapper__2-PYe)
```
In Selen
```python
se.Find(XPATH, "//xpath string...", 3).find(CLASS, Login_submit_wrapper__2-PYe)
or 
se.Find((XPATH, "//xpath string...", 3), (CLASS, Login_submit_wrapper__2-PYe))
```

as well we can select WebElement any set of indexes
```Python

se.Find((XPATH, "//xpath string...", 0, 3, 5, ...), (CLASS, Login_submit_wrapper__2-PYe))

```
So, the full rule of using `Find` and `find` is:

`Find(locator, [locators])`

`find(locator, [locators])`

And rule of one locator
`locator = ('BY', content, [indexes ..])`

- this way is suitable and can be used in any finding operator

## More ways to find and filter elements
### Method `Wait()` - finding and waiting for the appearance of an element on the page and not only
The method `Wait` can take the same parameters as the `Find` method, but it will only expect the first element in the chain and the rest of the elements in the chain will be found in the same way as the find method does.
- No exception handling is required, the logic is already inside the White method

`Wait(locator, [locators])`

In Selenium it was like:
```python
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

try:
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "myDynamicElement"))
    )
except:
    driver.quit()
```
Now with Selen:
```python
from selen import *

se.Wait(ID, "myDynamicElement")
```
And more examples:
```python
se.Wait(ID, "myDynamicElement").find(CLASS, "Login_submit_wrapper__2-PYe)

#or with locator variables
id_locator = (ID, "MyDynamicElement")
class_locator = (CLASS, "Login_submit_wrapper__2-PYe)
tag_locator = (TAG, "input")

se.Wait(xpath_locator).find(class_locator).find(tag_locator)

# all locator as tuples inside one method 
se.Wait((ID, "myDynamicElement),(CLASS, "Login_submit_wrapper__2-PYe))

#or with locator variables
xpath_locator = (ID, "myDynamicElement")
class_locator = (CLASS, "Login_submit_wrapper__2-PYe)
tag_locator = (TAG, "input")

se.Wait(xpath_locator, class_locator, tag_locator)

#or All locators in one variable : Tuple of tuples
locators = ((ID, "myDynamicElement"),
            (CLASS, "Login_submit_wrapper__2-PYe),
            (TAG, "input"))

se.Wait(locators)

#or Combined addition of locators  
se.Wait(locators, xpath_locator, (TAG, "a"))
se.Wait((TAG, "a"), xpath_locators, locators)
# ! Any combinations as You wish
```

### Methods `Tag()` and `tag()` finding element(s) only by Tag Name

    `Tag("tag name", [ index, index2, .., index n ])`

    `tag("tag name", [ index, index2, .., index n ])`

### Methods `Cls()` and `cls()` finding element(s) only by Class Name

    `Cls("class name",  [ index, index2, .., index n ])`

    `cls("class name", [ index, index2, .., index n ])`

### Methods `Xpath()` and `xpath()` finding element(s) only by xpath

    `Xpath("xpath query", [ index, index2, .., index n ])`

    `xpath("xpath query", [ index, index2, .., index n ])`

### Methods `Id()`  finding element only by ID

    `Id("ID", [ index, index2, .., index n ])`

### Metods `Contains()` and `contains()` - finding elements containing a specific date
    
    `Contains(data, [ index, index2, .., index n ])` 

    `contains(data, [ index, index2, .., index n ])`

`data` - can be text of WebElement (str) or attribute of WebElement (dict = '{"attribute name": "attribute value"}') 

### Metods `Img()` and `img()` - finding elements containing a images and pictures
    
    `Img([ index, index2, .., index n ][check=bool])` 
- Find images inside All Page (WebDeiver). 

    `img([ index, index2, .., index n ][check=bool])` 
- find images inside the last found WebElement

The method is used to save image information to an inner variable `se.stat` as dictionary

- By default `check=False`

If set `check=True` the method checks the elements with the image for the presence of the source of the image, `alt` attribute, as well as its being loaded.
Example:
```python
se.Img(check=True)

# Result:
"""
Found images: 4
Image: xpath: /html/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/header[1]/a[1]/img[1]
 source: data:image/png;base64,iVBORw0KGgoAAAhQpUuTh8g+dO7jQI9xT/QAAAABJRU5ErkJggg==
 alt = iBench - real-time developers Hiring
 visible: True
Checked  ... OK
Image: xpath: /html/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/img[1]
 source: https://ibench.net/static/media/for-client.7fc250cc.webp
 alt = Marketplace``
 visible: True
Checked  ... OK
Image: xpath: /html/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[4]/div[2]/img[1]
 source: https://ibench.net/static/media/for-company.4dd08eef.webp
 alt = Marketplace
 visible: True
Checked  ... OK
Image: xpath: /html/body[1]/div[2]/span[1]/img[1]
 source: data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==
 alt = 
 visible: False
!!! Invisible Image, xpath: /html/body[1]/div[2]/span[1]/img[1]
!!! Image without ALT attribute, xpath: /html/body[1]/div[2]/span[1]/img[1]
"""
```


### `parents()` jump to the parent element by a different number of levels
    
    `parents([level number])`

By defauts it jumps up for 1 level


## Actions with elements 

### `click()` click and action click in one
    
    `click([action=bool, pause=second(int) ])`
    
By defaulf `action=False` `pause=0`

In this case `action=False` - a simple click

In this case `action=True` - a click through the Selenium action.chain

`pause` only works in the second case through the Selenium action.chain by setting a pause in seconds between moving the cursor to the element and directly clicking


### `double_click()` - double click

    `double_click([pause=second(int)])`

### `context_click()` -context click or usually slick by right mouse button

    `context_click([pause=second(int)])`  

### `type()` - inserts text into the selected WebWlement
    
    `type("Text")`
Examples:
```python

```

when using this method, you do not need to click on the element and clear it, this logic is already inside

## Getting and checking  WebDriver or WebElement(s) data

### `text()`  - Text of WebElement(s)
   
    `text(["text": str])`

`text: str` - is optional parametr

- if no text argument is used here, that the Method returns text of the WebElement
    
- if a text argument is added in brackets, then this method compares the text arguments in brackets with the text inside the WebElement and checks

### `title()` - The Title of opened page
    
    `title(["text": str])`

- if no text argument is used here, that the Method returns the Title  of Web PageWeb.
    
- if a text argument is added in brackets, then this method compares the text arguments in brackets with the Title of current WebPage and checks

### `curr_url()` - The Current URL of opened page

    `curr_url(["text": str])`
- if no text argument is used here, that the Method returns URL of curent opened page
    
- if a text argument is added in brackets, then this method compares the text arguments in brackets with the URL of The opened  the WebPage and checks


### `xpath_query()` - Absolute XPATH of WebElements

This method returns absolute xpath of WebElement. The found xpath automatically performs a reverse check for the search for the element using exactly this xpath.
This method is always final and after it the chain of methods cannot continue

### `count()` - Numbers of found Elements

    `count([number: int])`
- if no text argument is used here, that the Method returns count of the WebElements in `se.elems`. In this case, this method is final and the chain of methods cannot continue
    
- if an integer argument is added in brackets, then this method compares the number with the real counts of the selected WebElement and checks

### `attr()`  - Get or check of WebElements attributes

    `attr("attr_name", ["value"])`

This method checks if the element contains the specified attribute 

- if the attribute is exists and `value` is present, it checks if the attribute is equal to this value. 

- if the value is not specified, then the method returns the attribute value. In this case, this method is final and the chain of methods cannot continue
 

### `all_attrs()` - Get all attributes of WebElement

## Advanced Methods

### `out()` - content output to STDOUT

    `out([message: str])`

`message` - this is the default parameter which accepts the text to be displayed before the content

The content that this method displays on the screen depends on the method after which it is applied

If `out()` follows a method that found and/or returns WebElement then out put will be content of WebElement:
```python
se.Cls('FrontPage_btnWrapper__2Q75S').out("Wrapper element:")
# Result:
"""
Wrapper element: WebElement
<div class="FrontPage_btnWrapper__2Q75S"><a class="FrontPage_btn__2yqXx" href="/registration-startup">I want to try iBench</a><div class="FrontPage_btnTip__3yVoD">Our service is free for you</div></div>
{
    "tag name": "div",
    "abs xpath": "/html/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]",
    "visible": true,
    "attributes": {
        "class": "FrontPage_btnWrapper__2Q75S"
    }
}
"""
```

If `out()` follows a method that returns text then the output will be text:
```python
se.Tag('h1').text().out("Text of element:")
# Result
"""
Text of element: Looking for a developers, UX/UI designer, QA or DevOps...or development agency?
"""

se.title().out("Page Title")
# Result:
"""
Page title: iBench - real-time developers Hiring
"""

se.curr_url().out("URL:")
# Result:
"""
URL: https://ibench.net/
"""
se.Tag('h1').xpath_query().out()
# Result:
"""
/html/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/h1[1]
"""
```

If `out()` follows a method that returns dictionary then the output will be dictionary:
```python
se.Img(1).images.out("Images statistic:")
# Result:
'''
Images statistic:
{
    "/html/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/img[1]": {
        "source": "https://ibench.net/static/media/for-client.7fc250cc.webp",
        "alt": "Marketplace",
        "visible": true,
        "loaded": true
    }
}
'''
```




### `IS` - return boolean, as result of checking element

### sleep - Advansed method for delays

`sleep(second, [finish_random_delay])`

if only the first argument is specified, the delay occurs for the number of seconds equal to this argument

if the second argument is specified, then the delay occurs as a random time in seconds between the first and second arguments


### 'display' - show the element if it is hidden

and visibility

## Check methods

## Links

## Images

## Cookies
