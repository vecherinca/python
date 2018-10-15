{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Already exist\n"
     ]
    }
   ],
   "source": [
    "# Задача-1:\n",
    "# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,\n",
    "# из которой запущен данный скрипт.\n",
    "# И второй скрипт, удаляющий эти папки.\n",
    "\n",
    "#скрипт создающий 9 директорий на моем рабочем столе\n",
    "import sys\n",
    "import os\n",
    "try:\n",
    "    for i in range(1, 10):\n",
    "        os.mkdir(\"dir_\" + str(i))\n",
    "except:\n",
    "    print(\"Уже существуют\")\n",
    "\n",
    "   "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Уже удалены\n"
     ]
    }
   ],
   "source": [
    "#Скрипт удаляющий директории\n",
    "\n",
    "try:\n",
    "    for i in range(1, 10):\n",
    "        os.rmdir(\"dir_\" + str(i))\n",
    "except:\n",
    "    print(\"Уже удалены\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "/Users/maria/Desktop\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "['марина',\n",
       " ' Klimina_Certificate.jpeg',\n",
       " 'Новая папка',\n",
       " 'Снимок экрана 2018-09-25 в 22.47.33.png',\n",
       " 'Снимок экрана 2018-09-27 в 21.35.26.png',\n",
       " '.MASHA.mov.icloud',\n",
       " 'Снимок экрана 2018-10-11 в 21.20.53.png',\n",
       " 'Снимок экрана 2018-10-01 в 20.46.59.png',\n",
       " 'Снимок экрана 2018-09-25 в 17.57.34.png',\n",
       " 'Снимок экрана 2018-10-05 в 16.52.55.png',\n",
       " 'lesson3',\n",
       " 'Снимок экрана 2018-10-01 в 22.17.52.png',\n",
       " 'updated_dataset.tsv',\n",
       " '<?xml version=\"1.0\" encoding.textClipping',\n",
       " '.DS_Store',\n",
       " 'Снимок экрана 2018-09-25 в 17.57.24.png',\n",
       " 'Снимок экрана 2018-09-25 в 17.57.18.png',\n",
       " 'Снимок экрана 2018-09-26 в 1.29.20.png',\n",
       " 'Снимок экрана 2018-10-10 в 19.47.09.png',\n",
       " '.localized',\n",
       " 'Untitled.ipynb',\n",
       " 'Снимок экрана 2018-10-01 в 20.03.15.png',\n",
       " 'User Presets',\n",
       " 'Снимок экрана 2018-09-27 в 21.57.07.png',\n",
       " 'Снимок экрана 2018-09-25 в 17.57.40.png',\n",
       " 'Снимок экрана 2018-10-05 в 23.20.49.png',\n",
       " 'Снимок экрана 2018-10-11 в 21.50.58.png',\n",
       " 'MODULES.ipynb',\n",
       " 'KLEMAN.pages',\n",
       " 'Снимок экрана 2018-10-13 в 14.42.17.png',\n",
       " 'Снимок экрана 2018-10-04 в 17.01.21.png',\n",
       " 'Снимок экрана 2018-09-25 в 22.41.32.png',\n",
       " 'Снимок экрана 2018-09-28 в 18.31.47.png',\n",
       " 'Снимок экрана 2018-09-25 в 2.53.46.png',\n",
       " '897 1.jpeg',\n",
       " 'Снимок экрана 2018-09-26 в 0.04.38.png',\n",
       " '.учебка.pdf.icloud',\n",
       " 'Снимок экрана 2018-09-25 в 19.51.10.png',\n",
       " 'Снимок экрана 2018-10-11 в 20.19.13.png',\n",
       " '.MASHA.m4v.icloud',\n",
       " 'frida',\n",
       " '.1.psd.icloud',\n",
       " 'Снимок экрана 2018-10-04 в 21.27.03.png',\n",
       " '1',\n",
       " 'Снимок экрана 2018-10-04 в 21.38.43.png',\n",
       " 'Снимок экрана 2018-10-05 в 16.53.49.png',\n",
       " '.MASHA_.mov.icloud',\n",
       " '09.jpg',\n",
       " 'Adobe Photoshop Lightroom CC 1.4.0.0',\n",
       " 'Снимок экрана 2018-10-11 в 20.11.51.png',\n",
       " 'Снимок экрана 2018-10-01 в 20.03.08.png',\n",
       " 'Без названия.pages',\n",
       " 'Test3.docx',\n",
       " 'Снимок экрана 2018-09-25 в 22.43.03.png',\n",
       " 'BackPropSimple_withTask.ipynb',\n",
       " '.Porsche_Klimina.jpeg.icloud',\n",
       " 'Снимок экрана 2018-09-25 в 19.17.59.png',\n",
       " 'Снимок экрана 2018-09-25 в 22.44.32.png',\n",
       " 'Снимок экрана 2018-10-12 в 19.07.19.png',\n",
       " 'Sample',\n",
       " 'Klimina Mariia_Transcript.jpeg',\n",
       " '.ipynb_checkpoints',\n",
       " 'Снимок экрана 2018-10-10 в 16.54.07.png',\n",
       " 'Klimina Mariia. Passport.jpeg',\n",
       " 'Снимок экрана 2018-10-01 в 15.15.26.png',\n",
       " \" Luke's Answer_Klimina Mariia_GPA_ISSUE.png\",\n",
       " 'Portfolio_3_Климина.docx',\n",
       " 'Снимок экрана 2018-10-05 в 16.53.33.png',\n",
       " 'Снимок экрана 2018-09-25 в 20.44.00.png',\n",
       " 'Снимок экрана 2018-10-11 в 20.09.52.png',\n",
       " '-1.jpg',\n",
       " 'Снимок экрана 2018-10-05 в 23.54.07.png',\n",
       " '5.jpg',\n",
       " 'Снимок экрана 2018-09-25 в 17.56.54.png',\n",
       " 'Снимок экрана 2018-10-05 в 16.54.10.png',\n",
       " 'Снимок экрана 2018-10-13 в 20.54.52.png',\n",
       " '2.jpg',\n",
       " 'Klimina Mariia _ Transcript.jpeg',\n",
       " 'лето2018пленкапечать',\n",
       " 'Снимок экрана 2018-10-05 в 16.53.21.png',\n",
       " 'мо3 2.pages',\n",
       " 'masha',\n",
       " 'марин',\n",
       " 'Снимок экрана 2018-09-25 в 19.25.48.png',\n",
       " '1.jpg',\n",
       " 'Домашнее задание_Климина.ipynb',\n",
       " '.1_1.psd.icloud',\n",
       " 'Снимок экрана 2018-10-05 в 16.54.03.png']"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Задача-2:\n",
    "# Напишите скрипт, отображающий папки текущей директории, в моем случае это рабочий стол.\n",
    "print(os.getcwd())\n",
    "file = os.listdir()\n",
    "file"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Задача-3:\n",
    "# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.\n",
    "import shutil\n",
    "def copy_file(first_file,backup_file):\n",
    "    shutil.copy(first_file,backup_file)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "# Задача-1:\n",
    "# Напишите небольшую консольную утилиту,\n",
    "# позволяющую работать с папками текущей директории.\n",
    "# Утилита должна иметь меню выбора действия, в котором будут пункты:\n",
    "# 1. Перейти в папку\n",
    "# 2. Просмотреть содержимое текущей папки\n",
    "# 3. Удалить папку\n",
    "# 4. Создать папку\n",
    "# При выборе пунктов 1, 3, 4 программа запрашивает название папки\n",
    "# и выводит результат действия: \"Успешно создано/удалено/перешел\",\n",
    "# \"Невозможно создать/удалить/перейти\"\n",
    "\n",
    "# Для решения данной задачи используйте алгоритмы из задания easy,\n",
    "# оформленные в виде соответствующих функций,\n",
    "# и импортированные в данный файл из easy.py "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Я не разобралась как верно импортировать функции чтобы они работали,но я создала каркас утилиты \n",
    "\n",
    "\n",
    "\n",
    "def show_menu():\n",
    "    menu_items = [\n",
    "        '1 - перейти в папку',\n",
    "        '2 - просмотреть содержимое текущей папки',\n",
    "        '3 - удалить папку',\n",
    "        '4 - создать папку',\n",
    "        '0 - выход'\n",
    "    ]\n",
    "\n",
    "    for menu_item in menu_items:\n",
    "        print(menu_item)\n",
    "show_menu()\n",
    "\n",
    "action = input('Выберите действие: ')\n",
    "if action == '1':\n",
    "        dir_name = input('Введите название директории для перехода: ')\n",
    "class cd:\n",
    "    def __init__(self, newPath):\n",
    "        self.newPath = os.path.expanduser(newPath)\n",
    "        \n",
    "if action == '2':\n",
    "    dir_name.ls()\n",
    "if action == '3':\n",
    "    \"\"\"\"\"\"\n",
    "if action == '4':\n",
    "    \"\"\"\"\"\"\n",
    "if action == '':\n",
    "    exit()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
