{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMwYc4YuKCAuIkeFci82+Sv",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/ankitg-02/data_analysis/blob/main/sales_2.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "id": "bahI-QEL351m"
      },
      "outputs": [],
      "source": [
        "import pandas as pd"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "sp=pd.read_csv(\"/content/Sample-sales-data-excel.csv\")"
      ],
      "metadata": {
        "id": "NnAywh3w4A7-"
      },
      "execution_count": 3,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "sample=pd.DataFrame(sp)"
      ],
      "metadata": {
        "id": "atynYSXX4Rc-"
      },
      "execution_count": 4,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "sales=dict(sample)"
      ],
      "metadata": {
        "id": "VU4bDFvl4XIF"
      },
      "execution_count": 5,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(sales)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "b8GFykAJ4f6d",
        "outputId": "b97620c0-ff3f-4661-f798-ccb76cfc5440"
      },
      "execution_count": 6,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "{'Row ID': 0          1\n",
            "1          2\n",
            "2          3\n",
            "3          4\n",
            "4          5\n",
            "        ... \n",
            "9989    9990\n",
            "9990    9991\n",
            "9991    9992\n",
            "9992    9993\n",
            "9993    9994\n",
            "Name: Row ID, Length: 9994, dtype: int64, 'Order ID': 0       CA-2016-152156\n",
            "1       CA-2016-152156\n",
            "2       CA-2016-138688\n",
            "3       US-2015-108966\n",
            "4       US-2015-108966\n",
            "             ...      \n",
            "9989    CA-2014-110422\n",
            "9990    CA-2017-121258\n",
            "9991    CA-2017-121258\n",
            "9992    CA-2017-121258\n",
            "9993    CA-2017-119914\n",
            "Name: Order ID, Length: 9994, dtype: object, 'Order Date': 0        11/8/2016\n",
            "1        11/8/2016\n",
            "2        6/12/2016\n",
            "3       10/11/2015\n",
            "4       10/11/2015\n",
            "           ...    \n",
            "9989     1/21/2014\n",
            "9990     2/26/2017\n",
            "9991     2/26/2017\n",
            "9992     2/26/2017\n",
            "9993      5/4/2017\n",
            "Name: Order Date, Length: 9994, dtype: object, 'Ship Date': 0       11/11/2016\n",
            "1       11/11/2016\n",
            "2        6/16/2016\n",
            "3       10/18/2015\n",
            "4       10/18/2015\n",
            "           ...    \n",
            "9989     1/23/2014\n",
            "9990      3/3/2017\n",
            "9991      3/3/2017\n",
            "9992      3/3/2017\n",
            "9993      5/9/2017\n",
            "Name: Ship Date, Length: 9994, dtype: object, 'Ship Mode': 0         Second Class\n",
            "1         Second Class\n",
            "2         Second Class\n",
            "3       Standard Class\n",
            "4       Standard Class\n",
            "             ...      \n",
            "9989      Second Class\n",
            "9990    Standard Class\n",
            "9991    Standard Class\n",
            "9992    Standard Class\n",
            "9993      Second Class\n",
            "Name: Ship Mode, Length: 9994, dtype: object, 'Customer ID': 0       CG-12520\n",
            "1       CG-12520\n",
            "2       DV-13045\n",
            "3       SO-20335\n",
            "4       SO-20335\n",
            "          ...   \n",
            "9989    TB-21400\n",
            "9990    DB-13060\n",
            "9991    DB-13060\n",
            "9992    DB-13060\n",
            "9993    CC-12220\n",
            "Name: Customer ID, Length: 9994, dtype: object, 'Customer Name': 0            Claire Gute\n",
            "1            Claire Gute\n",
            "2        Darrin Van Huff\n",
            "3         Sean O'Donnell\n",
            "4         Sean O'Donnell\n",
            "              ...       \n",
            "9989    Tom Boeckenhauer\n",
            "9990         Dave Brooks\n",
            "9991         Dave Brooks\n",
            "9992         Dave Brooks\n",
            "9993        Chris Cortes\n",
            "Name: Customer Name, Length: 9994, dtype: object, 'Segment': 0        Consumer\n",
            "1        Consumer\n",
            "2       Corporate\n",
            "3        Consumer\n",
            "4        Consumer\n",
            "          ...    \n",
            "9989     Consumer\n",
            "9990     Consumer\n",
            "9991     Consumer\n",
            "9992     Consumer\n",
            "9993     Consumer\n",
            "Name: Segment, Length: 9994, dtype: object, 'Country': 0       United States\n",
            "1       United States\n",
            "2       United States\n",
            "3       United States\n",
            "4       United States\n",
            "            ...      \n",
            "9989    United States\n",
            "9990    United States\n",
            "9991    United States\n",
            "9992    United States\n",
            "9993    United States\n",
            "Name: Country, Length: 9994, dtype: object, 'City': 0             Henderson\n",
            "1             Henderson\n",
            "2           Los Angeles\n",
            "3       Fort Lauderdale\n",
            "4       Fort Lauderdale\n",
            "             ...       \n",
            "9989              Miami\n",
            "9990         Costa Mesa\n",
            "9991         Costa Mesa\n",
            "9992         Costa Mesa\n",
            "9993        Westminster\n",
            "Name: City, Length: 9994, dtype: object, 'State': 0         Kentucky\n",
            "1         Kentucky\n",
            "2       California\n",
            "3          Florida\n",
            "4          Florida\n",
            "           ...    \n",
            "9989       Florida\n",
            "9990    California\n",
            "9991    California\n",
            "9992    California\n",
            "9993    California\n",
            "Name: State, Length: 9994, dtype: object, 'Postal Code': 0       42420\n",
            "1       42420\n",
            "2       90036\n",
            "3       33311\n",
            "4       33311\n",
            "        ...  \n",
            "9989    33180\n",
            "9990    92627\n",
            "9991    92627\n",
            "9992    92627\n",
            "9993    92683\n",
            "Name: Postal Code, Length: 9994, dtype: int64, 'Region': 0       South\n",
            "1       South\n",
            "2        West\n",
            "3       South\n",
            "4       South\n",
            "        ...  \n",
            "9989    South\n",
            "9990     West\n",
            "9991     West\n",
            "9992     West\n",
            "9993     West\n",
            "Name: Region, Length: 9994, dtype: object, 'Product ID': 0       FUR-BO-10001798\n",
            "1       FUR-CH-10000454\n",
            "2       OFF-LA-10000240\n",
            "3       FUR-TA-10000577\n",
            "4       OFF-ST-10000760\n",
            "             ...       \n",
            "9989    FUR-FU-10001889\n",
            "9990    FUR-FU-10000747\n",
            "9991    TEC-PH-10003645\n",
            "9992    OFF-PA-10004041\n",
            "9993    OFF-AP-10002684\n",
            "Name: Product ID, Length: 9994, dtype: object, 'Category': 0             Furniture\n",
            "1             Furniture\n",
            "2       Office Supplies\n",
            "3             Furniture\n",
            "4       Office Supplies\n",
            "             ...       \n",
            "9989          Furniture\n",
            "9990          Furniture\n",
            "9991         Technology\n",
            "9992    Office Supplies\n",
            "9993    Office Supplies\n",
            "Name: Category, Length: 9994, dtype: object, 'Sub-Category': 0         Bookcases\n",
            "1            Chairs\n",
            "2            Labels\n",
            "3            Tables\n",
            "4           Storage\n",
            "           ...     \n",
            "9989    Furnishings\n",
            "9990    Furnishings\n",
            "9991         Phones\n",
            "9992          Paper\n",
            "9993     Appliances\n",
            "Name: Sub-Category, Length: 9994, dtype: object, 'Product Name': 0                       Bush Somerset Collection Bookcase\n",
            "1       Hon Deluxe Fabric Upholstered Stacking Chairs,...\n",
            "2       Self-Adhesive Address Labels for Typewriters b...\n",
            "3           Bretford CR4500 Series Slim Rectangular Table\n",
            "4                          Eldon Fold 'N Roll Cart System\n",
            "                              ...                        \n",
            "9989                               Ultra Door Pull Handle\n",
            "9990    Tenex B1-RE Series Chair Mats for Low Pile Car...\n",
            "9991                                Aastra 57i VoIP phone\n",
            "9992    It's Hot Message Books with Stickers, 2 3/4\" x 5\"\n",
            "9993    Acco 7-Outlet Masterpiece Power Center, Wihtou...\n",
            "Name: Product Name, Length: 9994, dtype: object, 'Sales': 0       261.9600\n",
            "1       731.9400\n",
            "2        14.6200\n",
            "3       957.5775\n",
            "4        22.3680\n",
            "          ...   \n",
            "9989     25.2480\n",
            "9990     91.9600\n",
            "9991    258.5760\n",
            "9992     29.6000\n",
            "9993    243.1600\n",
            "Name: Sales, Length: 9994, dtype: float64, 'Quantity': 0       2\n",
            "1       3\n",
            "2       2\n",
            "3       5\n",
            "4       2\n",
            "       ..\n",
            "9989    3\n",
            "9990    2\n",
            "9991    2\n",
            "9992    4\n",
            "9993    2\n",
            "Name: Quantity, Length: 9994, dtype: int64, 'Discount': 0       0.00\n",
            "1       0.00\n",
            "2       0.00\n",
            "3       0.45\n",
            "4       0.20\n",
            "        ... \n",
            "9989    0.20\n",
            "9990    0.00\n",
            "9991    0.20\n",
            "9992    0.00\n",
            "9993    0.00\n",
            "Name: Discount, Length: 9994, dtype: float64, 'Profit': 0        41.9136\n",
            "1       219.5820\n",
            "2         6.8714\n",
            "3      -383.0310\n",
            "4         2.5164\n",
            "          ...   \n",
            "9989      4.1028\n",
            "9990     15.6332\n",
            "9991     19.3932\n",
            "9992     13.3200\n",
            "9993     72.9480\n",
            "Name: Profit, Length: 9994, dtype: float64}\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "\n",
        "count_conumer=0\n",
        "for i in sales['Segment']:\n",
        "  if i=='Consumer':\n",
        "    count_conumer+=1\n",
        "print(\"count of conumers=\",count_conumer)\n",
        "count_corporate=0\n",
        "for j in sales['Segment']:\n",
        "  if j=='Corporate':\n",
        "    count_corporate+=1\n",
        "print(\"count of corporates=\",count_corporate)\n",
        "count_home_office=0\n",
        "for k in sales['Segment']:\n",
        "  if k=='Consumer':\n",
        "   count_home_office+=1\n",
        "print(\"count of home offices=\",count_home_office)\n",
        "max_segment=max(count_conumer,count_corporate,count_home_office)\n",
        "print(\"max of segment=\",max_segment)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "GbV_nB804k74",
        "outputId": "b41c25a6-d633-4a3a-a1d0-1bb3e141b867"
      },
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "count of conumers= 5191\n",
            "count of corporates= 3020\n",
            "count of home offices= 5191\n",
            "max of segment= 5191\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "pip install itertools"
      ],
      "metadata": {
        "id": "Gwsm0f-sYY4R",
        "outputId": "f94cb1b1-5a4b-4569-82d1-0e3a288a35bd",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": 1,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\u001b[31mERROR: Could not find a version that satisfies the requirement itertools (from versions: none)\u001b[0m\u001b[31m\n",
            "\u001b[0m\u001b[31mERROR: No matching distribution found for itertools\u001b[0m\u001b[31m\n",
            "\u001b[0m"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from itertools import groupby"
      ],
      "metadata": {
        "id": "gpFY1Vrw5htm"
      },
      "execution_count": 2,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "sales_via_segment=groupby(\"Segment\")"
      ],
      "metadata": {
        "id": "j9iBaVJw5tLz"
      },
      "execution_count": 3,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(\"sales_via_segment=\",sales_via_segment)"
      ],
      "metadata": {
        "id": "GUXk-EHb5-SV",
        "outputId": "542d4699-d148-4098-f05e-5bab673d1b5f",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "sales_via_segment= <itertools.groupby object at 0x7efc4a631260>\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "kN-qE_UI6FQL"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}