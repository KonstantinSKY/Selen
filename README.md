# SELEN 
## Easier and shorter than clear Selenium
this is a Python mini framework or an add-on for the Selenium and unitest frameworks

## Introduction

Selenium WebDriver is a popular tool for automating web browser interactions, allowing testers and developers to simulate user behavior and test website functionality. However, working with Selenium WebDriver can be challenging, especially for those who are new to it. The process of finding web elements, waiting for page loads, and performing actions on those elements can be time-consuming and prone to errors.

This is where Selen comes in. Selen is a Python library that simplifies the use of Selenium WebDriver. Its basic goals include making it easier to write code for tests, improving code readability, reducing the amount of code written, accelerating the development of tests based on Selenium and unittest frameworks, and reducing errors.

Selen builds on top of Selenium WebDriver, providing a higher-level API that makes it easier to interact with web pages. With Selen, you can quickly automate browser interactions, navigate pages, fill out forms, click buttons, and much more. You can also easily locate web elements using a wide range of locator strategies, such as ID, name, class name, XPath, and CSS selector. Additionally, Selen provides a variety of convenience methods for working with web elements, such as clicking, typing, selecting options from dropdowns, and checking attributes.

Selen also simplifies the process of setting up Selenium WebDriver. It automatically updates the appropriate driver for the browser you want to use, so you don't have to worry about downloading and setting up drivers yourself.

In this guide, we'll explore the basics of using Selen, including how to install it, how to use its methods and attributes, and how to interact with web elements using Selen. By the end of this guide, you'll have a good understanding of how to use Selen to automate web browser interactions with ease.

## Table of contents

Introduction

[Installation](#Installation)

* [Install all needed Python modules with `requirements.txt`](#requirements)
* [Automatic getting common WebDrivers](#automatic)

[Getting Started](#Started)

* [Simple Usage](#Simple_Usage)
* [Example Explained](#Example_Explained)

[Connection between Selen and Selenium WebDriver and Selenium WebElements](#connection)

* [Using Selenium WebDriver from Selen](#WebDriver)
* [Internal variables and attributes of a Selen instance](#Internal_variables)
    - [`.url` - the main Project URL storage ](#storage)
    - [`.elem` and `se.elems` - the current WebElement storages ](#elems)
    - [`.stat` - the current statisticts or statuses storage](#stat)
    - [Configure variables](#config)
    - [The attributes available to locate elements on a page](#locatore) 
    - [Keys attributes](#keys) 

* [Getting the page data by URL with options](#Get_method)
* [WEB elements](#WebElements)
* [`.page_src()`Page Source ! ](#PageSource)
* [`title()`Page Title ](#PageSource)
* [`curr_url()`Page URL ](#PageSource)
* [`se.sleep()` Additional sleep for any delays](#sleep)

[Chains of Selen methods and actions with them](#chains)
[The difference between methods with names starts with a capital and the same but with a small one](#difference)

[Locating element and finding WebElements](#Locating)
* [Locators in Selen](#locators)
* [`Wait` Waiting for WebElement present on the page](#wait)
* [`Find()`     and `find()` finding by any locators](#find)
* [`Tag()`     and `tag()` finding by Tag name](#tag)
* [`Cls()`      and `cls()`finding by class name attribute] (#class)
* [`Xpath()`    and `xpath()` by XPath query](#xpath)
* [`Contains()` and `Contains()`by contains of WebElement](#contains)
* [`Img()`      and `Img()`finding and checking Images](#Img)
* [`Id()`  by ID attribute](#id)
* [`Parent()` finding parent WebElement](#parent)

[Actions with Page and WebElements](#actions)

* [`click()` Different Clicks WebElemens with many options](#clicks)
    - [regular click](#1)
    - [action click](#1)
    - [double click](#1)
    - [context click](#1)
    - [random click](#1)
* [`type()` Insert any text to WebElements](#type) 
* [`text()` Getting text from WebElements](#text)
* [`dropdown_select()` insert any text to WebElements](#dropdown)
    - [select by Value](#dd_value)
    - [select by Index](#dd_index)
    - [select by Text !](#dd_text)
    - [Random select from dropdown](#dd_random)
* [`dropdown_multiselect()`](#multi)
    - [select by Value](#dms_value)
    - [select by Index](#dms_insex)
    - [random select](#dms_radom)
[Testing and checking](#testing)
* [`assertion`]
* [Basic page test `se.check_page()`](#check_page)
* [Image tests](#images)
* [Links (href) tests](#links)
* [`attr()` checking attributes of WebElements](#attr)


[Outputs and prints](#outs)
* [`out()`]
* [`se.print`]

[How to create testcases](#testcases)
<!-- +++++++++++++++++++++++++++++++++S+++++++++++++++++CONTENTS+++++++++++++++++++++++++++++++++++++++++++++++ -->

<a name="Installation"></a> 
## Installation

<a name="requirements"></a> 

### Install all needed Python modules with `requirements.txt`

<a name="automatic"></a> 

### Automatic getting common WebDrivers

<a name="Started"></a> <!-- ==================================== Getting started ============================== -->
## Getting started

<a name="Simple_Usage"></a>  <!-- ==================================== Simple Usage ============================== -->

### Simple Usage
If you have installed Selen Python module with bindings and Selenium Python bindings, you can start using it like this.
```python
from Selen import *

se = Selen("Firefox")
se.get("http://www.python.org")
se.title("Pyhton")
se.Find(NAME, "q").type("pycon").key(RETURN)
se.page_src("No result found")
```
### Example Explained

<a name="connection"></a>  <!-- ==================================== Simple Usage ============================== -->

## Connection between Selen and Selenium WebDriver and Selenium WebElements
The Selen is a class that creates its own instances with Methods and Attributes (instance variables).

`Selen([Browser: str], [url=Project_URL: str])`

Arguments:

`Browser`  -  The available browsers (by default is "Chrome" if the argument is empty):

- "Chrome"
- "Firefox"
- "Edge"
- "Opera"

`url` is optional argument to set attribute `url` as the main Project url

Creating instances examples:  

`se = Selen("Chrome")`

`se = Selen("Firefox", url="http://www.python.org")`


<a name="WebDriver"></a> <!-- === Calling and Using regular Selenium WebDriver from Selen ======================== -->

### Calling and Using regular Selenium WebDriver from Selen
During initialization of instance, Selen creates a Selenium driver inside it. 
You can call the WebDriver it directly

`se.WD.`

and continue to use it and work with it as with regular Selenium, like 

`se.WD.find_element(By.NAME, "q")`. 

`se.WD` is just link to Selenium WebDriver instance like `webdriver.Firefox()` 

<a name="Internal_variables"></a> 
### Internal variables or attributes of a Selen instance
An instance of the Selenium class contains internal variables that can be changed by the instance itself during operation or by users

<a name="url"></a>
#### `se.url`

This variable should contain the project's main url, or it can simply remain an empty string

It can be set at instantiation time or any time later:
```python
se = Selen("Firefox", url="http://www.python.org")`

# or at any time as follows:
se = Selen("Chrome")
se.url = "http://www.python.org"

# to use the variable:
my_main_url = se.url 
```

<a name="elems"></a>
#### `se.elem` and `se.elems` - the Web Elements storages

```py

```



<a name="stat"></a>

#### `se.stat` - the current statisticts or statuses storage

<a name="locators"></a>
#### The attributes available to locate elements on a page. 

These are the attributes available and their Selenium equivalents
```python
 Selen                       Selenium
ID                          By.ID = "id" 
NAME                        By.NAME = "name" 
XPATH                       By.XPATH = "xpath" 
TAG                         By.TAG_NAME = "tag name"
CLASS                       By.CLASS_NAME = "class name"
CSS                         By.CSS_SELECTOR = "css selector"
LINK                        By.LINK_TEXT = "link text"
PART_LINK                   By.PARTIAL_LINK_TEXT = "partial link text" 
```


<a name="keys"></a>
#### Configure instance attributes
`se.ok_assert`

`se.ok_print`

<a name="keys"></a>

#### Keys attributes for call key pressing


<a name="Get_method"></a>
### Getting the page data by URL with options
There are two ways to navigate to a page given by the URL:

Selenium regular way:
`se.WD.get( url: str )`

Selen advanced way `se.get([url: str], [check_data: dict])`
```python
se = Selen("Firefox")
se.get("https//www.python.org")

# or if the main URL is set when the Selen class is instantiated
se = Selen("Firefox", url="http://www.pyhon.org")
se.get()
```

If `se.url` is already set, you can navigate to nested page by sublinks only
```python
se.get(downloads/)
se.get(downloads/release/python-31011/
```
While executing `se.get()`, after opening page, Selen automatically check if the requested url matches the current url of the loaded page with result:
```
%  Page "https://www.python.org/" navigated   =======================================================================================
✓  Current_URL https://www.python.org/  ..... OK
```
`se.get()` can also do some basic testing of the current opened page: checks title, Wait checks - expectations for some element, checks all images and links.

For using the options, set additional data as dictionary object:
```python
se = Selen("Firefox", url="http://www.pyhon.org")
se.get("downloads",{
    "wait": (TAG, "h1"), 
    "title": "Download Python | Python.org"
    })

```
Try it yourself!

<a name="WebElements"></a>
### WEB Elements, Assigning an element or elements to a variables 
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

Even if the code chain in one line getting the end You can call next methods and actions on the last found elements can be continued in a new line, because these elements are stored in the variables: `se.elen` and `se.elems` 
Example:
```python
email="email@gmail.com"
se.Find(NAME, "email").type(email).sleep(0.2, 1).attr('value', email).parent(2).tag("span").attr('class', 'validation_status_ok')

```
The same code results:
```python
email = "email@email.com"
se.Find(NAME, "email").type(email).sleep(0.2, 1).attr('value', "email")
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

<a name="Locating"></a>
## Locating and finding of WebElements

<a name="Locating"></a>
### Locators and Simplified adding locators to methods by several variants
In usual Selenium Was like:
```python
driver.find_element(By.XPATH, "//body/div[@id='fb-root']/div[@id='root']/div[1]/div[1]/div[2]/div[1]")
driver.find_element(By.CLASS_NAME, "Login_submit_wrapper__2-PYe")

#or
driver.find_element("xpath", "//body/div[@id='fb-root']/div[@id='root']/div[1]/div[1]/div[2]/div[1]")
driver.find_element("class name", "Login_submit_wrapper__2-PYe")

#or with locator variables
xpath_locator = ("xpath", "//body/div[@id='fb-root']/div[@id='root']/div[1]/div[1]/div[2]/div[1]")
class_locator = ("class_name", "Login_submit_wrapper__2-PYe")

driver.find_element(*xpath_locator)
driver.find_element(class_locator[0], class_locator[1])
```
With Selen is:
```python
se.Find(XPATH, "//body/div[@id='fb-root']/div[@id='root']/div[1]/div[1]/div[2]/div[1]")
se.Find(CLASS, "Login_submit_wrapper__2-PYe")

#or with locator variables
xpath_locator = (XPATH, "//body/div[@id='fb-root']/div[@id='root']/div[1]/div[1]/div[2]/div[1]")
class_locator = (CLASS, "Login_submit_wrapper__2-PYe")

se.Find(xpath_locator)
se.Find(class_locator)
```
## Findind by locators with indexes of element in array of elements in `se.elems`
Sometimes we need to find a lot of elements then select one or more of them by index and continue searching inside it

In Selenium: 
```python
driver.find_elements(By.XPATH, "//xpath string...")[3].find_element(By.CLASS_NAME, "Login_submit_wrapper__2-PYe")
```
In Selen
```python
se.Find(XPATH, "//xpath string...", 3).find(CLASS, "Login_submit_wrapper__2-PYe")
or 
se.Find((XPATH, "//xpath string...", 3), (CLASS, "Login_submit_wrapper__2-PYe"))
```

as well we can select WebElement any set of indexes
```Python

se.Find((XPATH, "//xpath string...", 0, 3, 5, ...), (CLASS, "Login_submit_wrapper__2-PYe"))

```
So, the full rule of using `Find` and `find` is:

`Find(locator, [locators])`

`find(locator, [locators])`

And rule of one locator
`locator = ('BY', content, [indexes ..])`

- this way is suitable and can be used in any finding operator


### New find method and simplified adding locators as method arguments<name="Find">
<a name="Locatiing"></a>

In Selenium, it was like this:
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

- -`se` is short from `self`

```
## Principles and rules of the Selen using

### `Find()` and `find()` are different methods
Method `Find` (with Capital first letter) used if it calls first after the WebDriver (for All WEB page elements). 

The lowercase method `find` is used when calling after another already found element.

There are several more methods that work in the same principle. 

`se.Find(locator(s),[locators(s), ... locators(s])`

`se.find(locator(s),[locator(s), ...locators(s)])`

In Selenium Was:
```python
driver.find_element(By.XPATH, "//xpath string...").find_element(By.CLASS_NAME, "Login_submit_wrapper__2-PYe")

#or with locator variables
xpath_locator = ("xpath", "//body/div[@id='fb-root']/div[@id='root']/div[1]/div[1]/div[2]/div[1]")
class_locator = ("class_name", "Login_submit_wrapper__2-PYe")
tag_locator = ("tag name", "input")

driver.find_element(*xpath_locator).find_element(*class_locator).find_element(*tag_locator)
```
Now with Selen:
```python
se.Find(XPATH, "//xpath string...").find(CLASS, "Login_submit_wrapper__2-PYe")

#or with locator variables
xpath_locator = (XPATH, "//body/div[@id='fb-root']/div[@id='root']/div[1]/div[1]/div[2]/div[1]")
class_locator = (CLASS, "Login_submit_wrapper__2-PYe")
tag_locator = (TAG, "input")

se.Find(xpath_locator).find(class_locator).find(tag_locator)
```
### Even shorter code in method chains to find a set of elements
Several ways to search for elements by a chain of locators, all locators in one `Find` method  
```python
# all locator as tuples inside one method 
se.Find((XPATH, "//xpath string..."),(CLASS, "Login_submit_wrapper__2-PYe"))

#or with locator variables
xpath_locator = (XPATH, "//body/div[@id='fb-root']/div[@id='root']/div[1]/div[1]/div[2]/div[1]")
class_locator = (CLASS, "Login_submit_wrapper__2-PYe")
tag_locator = (TAG, "input")

se.Find(xpath_locator, class_locator, tag_locator)

#or All locators in one variable : Tuple of tuples
locators = ((XPATH, "//body/div[@id='fb-root']/div[@id='root']/div[1]/div[1]/div[2]/div[1]"),
            (CLASS, "Login_submit_wrapper__2-PYe"),
            (TAG, "input"))

se.Find(locators)

#or Combined addition of locators  
se.Find(locators, xpath_locator, (TAG, "a"))
se.Find((TAG, "a"), xpath_locators, locators)
# ! Any combinations as You wish
```


## Findind by locators with indexes of element in array of elements in `se.elems`
Sometimes we need to find a lot of elements then select one or more of them by index and continue searching inside it

In Selenium: 
```python
driver.find_elements(By.XPATH, "//xpath string...")[3].find_element(By.CLASS_NAME, "Login_submit_wrapper__2-PYe")
```
In Selen
```python
se.Find(XPATH, "//xpath string...", 3).find(CLASS, "Login_submit_wrapper__2-PYe")
or 
se.Find((XPATH, "//xpath string...", 3), (CLASS, "Login_submit_wrapper__2-PYe"))
```

as well we can select WebElement any set of indexes
```Python

se.Find((XPATH, "//xpath string...", 0, 3, 5, ...), (CLASS, "Login_submit_wrapper__2-PYe"))

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
se.Wait(ID, "myDynamicElement").find(CLASS, "Login_submit_wrapper__2-PYe")

#or with locator variables
id_locator = (ID, "MyDynamicElement")
class_locator = (CLASS, "Login_submit_wrapper__2-PYe")
tag_locator = (TAG, "input")

se.Wait(xpath_locator).find(class_locator).find(tag_locator)

# all locator as tuples inside one method 
se.Wait((ID, "myDynamicElement"),(CLASS, "Login_submit_wrapper__2-PYe"))

#or with locator variables
xpath_locator = (ID, "myDynamicElement")
class_locator = (CLASS, "Login_submit_wrapper__2-PYe")
tag_locator = (TAG, "input")

se.Wait(xpath_locator, class_locator, tag_locator)

#or All locators in one variable : Tuple of tuples
locators = ((ID, "myDynamicElement"),
            (CLASS, "Login_submit_wrapper__2-PYe"),
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
- Find images inside All Page (WebDriver). 

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

By default, it jumps up for 1 level

<a name="actions"></a>
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
Example: Checking if the Tag "h2" contains text "Log in" 
```python
se.Wait(TAG, "h2").text("Log in")

# Result:
"""
Wait Element found ('tag name', 'h2')  ... OK
Checked: Text "Log in" at element: "/html/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/h2[1]" ... OK
"""
# Or we can Check and Click
se.Wait(TAG, "h2").text("Log in").click()
# Result:
"""
Wait Element found ('tag name', 'h2')  ... OK
Checked: Text "Log in" at element: "/html/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/h2[1]" ... OK
Clicked element: /html/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/h2[1]
"""
# But if wrong result:
se.Wait(TAG, "h2").text("Login")
# Result if se.assert=True:
"""
Wait Element found ('tag name', 'h2')  ... OK
Traceback (most recent call last):
  File "/Users/sky/Projects/ibench/Front-end/ibench.py", line 93, in <module>
     ....
  File "/Users/sky/Projects/ibench/Front-end/selen.py", line 158, in assertion
    assert False, message
AssertionError: !!! Wrong Text "Log in" at element: "/html/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/h2[1]"
!!! !!! Wrong Text "Log in" at element: "/html/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/h2[1]"

Process finished with exit code 1
"""
# Result if se.assert=False
"""
Wait Element found ('tag name', 'h2')  ... OK
!!! !!! Wrong Text "Log in" at element: "/html/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/h2[1]"
Got: Log in
Expected: Login
"""
#Process continued
```

when using this method, you do not need to click on the element and clear it, this logic is already inside

<a name="actions"></a>
### Select from dropdown WebElement `dropdown_select()` 

You can select any option from dropdown list by text or by integer index (position in list)

This method works with `<select>` tag element only.

`.dropdown_select(data)`

`data` is string or integer type

```python
se.Tag("select").dropdown_select("Canada")

se.Tag("select").dropdown_select(23)
```


## Getting and checking  WebDriver or WebElement(s) data

<a name="testing"></a>
## Testing and Cheking

<a name="check_page"></a>
### Basic page test `se.check_page()`

One method for several checking actions:    
- wait and found element on the page  
- check page title
- check current url
- check all images
- check all links

`se.check_page([data: dict])`

- `data` - parameters of page tests in Python dictionary format `{key: value}`

Possible keys for `data` parameters:
- `wait` - the key of the tuple locator value for wait and find WebElement
- `title` - the key of the string title for checking
- `url` - the key of the string url for checking wit current page url

if `data` is absent by default the method will check Images and Links only
```python
se.check_page({
    "wait": (TAG, "h1"), 
    "title": "Download Python | Python.org"
    "url": "https://www.python.org/downloads/"
    })

# or by default check Images and Links only
se.check_page()
```

### `text()`  - Text of WebElement(s)

    `text(["text": str])`

`text: str` - is optional parameter

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


### `xpath_query()` - Absolute XPATH of WebElement

This method return absolute xpath of WebElement. The found xpath automatically performs a reverse check for the search for the element using exactly this xpath.
This method is always final and after it the chain of methods cannot continue
```python
se.Find(NAME, "email").xpath_query().out("XPath:")
# Result
"""
XPath: /html/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[1]/div[1]/input[1]
"""

```
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

Returns all Element Attributes in dictionary format

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
## Setting of the project, setting variable


### `se.print()` print to STDOUT any text if se.ok_print = "YES"
- do not confuse with usually print

### `assertion()` - break work if se.ok_assertion = "NO"

### `IS` - return boolean, as result of checking element

### sleep - Advansed method for delays

`sleep(second, [finish_random_delay])`

if only the first argument is specified, the delay occurs for the number of seconds equal to this argument

if the second argument is specified, then the delay occurs as a random time in seconds between the first and second arguments


### 'display' - show the element if it is hidden

and visibility

## Check methods

## Checking Links (href)



## Cookies
