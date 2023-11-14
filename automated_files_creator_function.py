{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPV3KBB4yR38dRT4iCDeK2p",
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
        "<a href=\"https://colab.research.google.com/github/ShahjahanMirza/helper_functions/blob/main/automated_files_creator_function.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "3wqgKlf-4eWK"
      },
      "outputs": [],
      "source": []
    },
    {
      "cell_type": "code",
      "source": [
        "# create the folder where you need all these folders\n",
        "# add the files you need data from\n",
        "def automted_file_creator(directory_name):\n",
        "  \"\"\"\n",
        "  goes in the directory provided, reads the files' names and\n",
        "  create new sub directories based on the names of the files,\n",
        "  reads data from each file, and make directories based on the data\n",
        "  inside the files in each respective directory\n",
        "  \"\"\"\n",
        "  # eg: Directory : Projects\n",
        "  # files in directory: '1' and '2'\n",
        "  # data in files: ('1': a,b) and ('2': c,d)\n",
        "  # create sub-directories in projects names : '1' and '2'\n",
        "  # read data from files '1' and '2'\n",
        "  # go to file '1'\n",
        "  # read a, make a sub-directory in '1' named a\n",
        "  # read b, make a sub-directory in '1' named a\n",
        "  # go to file '2'\n",
        "  # read c, make a sub-directory in '1' named c\n",
        "  # read d, make a sub-directory in '1' named d\n",
        "\n",
        "  import os\n",
        "  # os.mkdir(directory_name)\n",
        "\n",
        "  files = []\n",
        "  for dirpath, dirnames, filenames in os.walk(directory_name):\n",
        "    files = filenames\n",
        "\n",
        "  for i in files:\n",
        "    os.mkdir(directory_name + i.replace('.txt','/'))\n",
        "    with open(directory_name+i, 'r') as f:\n",
        "      for line in f:\n",
        "        os.mkdir(directory_name+i.replace('.txt','/')+line)"
      ],
      "metadata": {
        "id": "tmO0eIQJRhZc"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "automted_file_creator('/content/ML-Projects-2'+'/')"
      ],
      "metadata": {
        "id": "tDXl372LSNpc"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# step - 1\n",
        "import os\n",
        "os.mkdir('/content/ML-Projects/')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 211
        },
        "id": "l3k7xAu5Poc0",
        "outputId": "07b98d76-70b3-4b0c-be39-82f57bfc63bd"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "error",
          "ename": "FileExistsError",
          "evalue": "ignored",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mFileExistsError\u001b[0m                           Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-3-a665cede55b2>\u001b[0m in \u001b[0;36m<cell line: 4>\u001b[0;34m()\u001b[0m\n\u001b[1;32m      2\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mos\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      3\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 4\u001b[0;31m \u001b[0mos\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mmkdir\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m'/content/ML-Projects/'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
            "\u001b[0;31mFileExistsError\u001b[0m: [Errno 17] File exists: '/content/ML-Projects/'"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# step - 2\n",
        "files = []\n",
        "for dirpath,dirnames,filenames in os.walk('/content/ML-Projects'):\n",
        "  files = filenames\n",
        "\n",
        "files"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "F8rGjXDNPptc",
        "outputId": "bd6785cc-c869-4b5f-a9a6-b75a14f520cd"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "['cnn.txt', 'regression.txt', 'transfer learning.txt', 'classification.txt']"
            ]
          },
          "metadata": {},
          "execution_count": 4
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# step - 3\n",
        "path = '/content/ML-Projects/'\n",
        "files"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "qMlHxdcxQJ8W",
        "outputId": "ae6dcd70-7eb1-4953-dc66-e8a082f84a3c"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "['cnn.txt', 'regression.txt', 'transfer learning.txt', 'classification.txt']"
            ]
          },
          "metadata": {},
          "execution_count": 5
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# step - 4\n",
        "for i in files:\n",
        "  os.mkdir(path + i.replace('.txt','/'))\n",
        "  with open(path+i, 'r') as f:\n",
        "    for line in f:\n",
        "      os.mkdir(path+i.replace('.txt','/')+line)"
      ],
      "metadata": {
        "id": "Uee_evlrQOUF"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "!git clone https://github.com/ShahjahanMirza/helper_functions/blob/main/automated_files_creator_function.ipynb"
      ],
      "metadata": {
        "id": "ALg82d9UOEuV",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "0e688ca9-cbfa-41d3-fc7c-857eb9d76b28"
      },
      "execution_count": 1,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Cloning into 'automated_files_creator_function.ipynb'...\n",
            "fatal: repository 'https://github.com/ShahjahanMirza/helper_functions/blob/main/automated_files_creator_function.ipynb/' not found\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "o_uZPU_tIr1-"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}