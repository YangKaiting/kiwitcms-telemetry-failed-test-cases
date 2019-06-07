# kiwitcms-telemetry-failed-test-cases


[Prerequisites](#prerequisites-exclamation) | [Installation of Plugin](#installation-of-plugin) | [Feature Walkthrough](#feature-walkthrough) | [Un-installation of Plugin](#un-installation-of-plugin)

## Getting Started

This is a telemetry plugin for the open source testcase management tool - [Kiwi](http://kiwitcms.org/). 
It is a feature for summarising all the failed test cases on per product basis.


These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites :exclamation:
- The Kiwi TCMS source code. Get it [here](https://github.com/kiwitcms/Kiwi)


### Installation Of Plugin


- in the directory root of **your** Kiwi project, run `pip install ~/dist/telemetry_plugin-0.1.tar.gz`. Take note that **'~'** is the directory where you clone this telemetry plugin to.

### Feature Walkthrough
After this plugin is installed in your project. Login to your Kiwi TCMS and you will find a new sub-tab called **Failed Testcases Report** under 'Telemetry' tab.
![alt text](https://github.com/YangKaiting/kiwitcms-telemetry-failed-test-cases/blob/master/assets/tp-header.jpeg)

Clicking on **Failed Testcases Report** will bring you to this page as shown below.
This is a summary of all the products available, with all the testcases that were run for the product. Details shown will be the number of times each testcase was run for this product, the failure count, and the failure rate.
![alt text](https://github.com/YangKaiting/kiwitcms-telemetry-failed-test-cases/blob/master/assets/tp-report.jpeg)



### Un-Installation Of Plugin

- To uninstall, run `pip uninstall telemetry-plugin`


