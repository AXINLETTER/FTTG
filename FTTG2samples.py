import os
import glob
import sys
sys.path.append("..") 
import cfg
import random
import json
import numpy

#add class number here
CLASS_DICT = {0: 'SlicingKnife', 1: 'FruitKnife', 2: 'BreadKnife', 3: 'PizzaShakeKnife', 4: 'PizzaHobKnife',
              5: 'TeaCup', 6: 'Goblet', 7: 'CoffeeCup',8: 'SmallScissor',
              9: 'TailorScissor', 10: 'ClawHammer', 11: 'MeatHammer', 12: 'Wardrobe',13: 'Bookshelf',

              14: 'Cucumber', 15: 'Banana', 16: 'Bread', 17: 'Cake', 18: 'Pizza', 19: 'Teapot',20: 'WineBottle',
              21: 'CoffeeMaker', 22: 'Paper',23: 'Tape', 24: 'CottonMaterial', 25: 'Rope',26: 'IronNail',
              27: 'RawMeat', 28: 'Cloth', 29: 'Book',

              30: ['SlicingKnife', 'FruitKnife', 'BreadKnife', 'PizzaShakeKnife', 'PizzaHobKnife'],
              31: ['TeaCup', 'Goblet', 'CoffeeCup'],  32: ['SmallScissor', 'TailorScissor'],
              33: ['ClawHammer', 'MeatHammer'], 34: ['Wardrobe', 'Bookshelf'],
              35: ['Cucumber', 'Banana', 'Bread', 'Cake', 'Pizza'], 36: ['CoffeeMaker', 'Teapot', 'WineBottle'],
              37: ['Paper', 'Tape', 'CottonMaterial', 'Rope'], 38: ['IronNail', 'RawMeat'], 39: ['Cloth', 'Book']}

def creatPos(NUM): #create positive samples
    save_folder = cfg.BASE
    traindata_head_path = cfg.BASE + 'train/Head'
    traindata_tail_path = cfg.BASE + 'train/Tail'
    t_cls = ["Cucumber", "Banana", "Bread", "Cake", 'Pizza', 'Pizza', "Teapot", "WineBottle", "CoffeeMaker",
             'Paper', 'Tape', 'CottonMaterial', 'Rope', 'IronNail', 'RawMeat', 'Cloth', 'Book']  # 15+2
    t_s_cls = [["Cucumber", "Banana", "Bread", "Cake", 'Pizza'], ["CoffeeMaker", "Teapot", "WineBottle"],
               ['Paper', 'Tape', 'CottonMaterial', 'Rope'], ['IronNail', 'RawMeat'], ['Cloth', 'Book']]
    #####################################################################################################
    list_h = [['SlicingKnife'],  # Cucumber
              ['FruitKnife'],  # Banana
              ['BreadKnife'],  # Bread
              ['BreadKnife'],  # Cake
              ['PizzaShakeKnife'],# Pizza ##
              ['PizzaHobKnife'],# Pizza ##
              ['TeaCup'],  # Teapot
              ['Goblet'],  # WineBottle
              ['CoffeeCup'],  # CoffeeMaker
              ['SmallScissor'],  # Paper
              ['SmallScissor'],  # Tape
              ['TailorScissor'],  # CottonMaterial
              ['TailorScissor'],  # Rope
              ['ClawHammer'],  # IronNail
              ['MeatHammer'],  # RawMeat
              ['Wardrobe'],  # Cloth
              ['Bookshelf']]  # Book##15+2## The order here corresponds to t_cls
    for i in range(len(t_cls)):##
        for k, value in CLASS_DICT.items():
            if k < 30:
                if value == list_h[i][0]:
                    index_h_sub = k  #
                if value == t_cls[i]:
                    index_sub = k  #
            else:
                if list_h[i][0] in value:
                    index_h_sup = k  #
                if t_cls[i] in value:
                    index_sup = k#
                    for j in range(len(t_s_cls)):
                        if value == t_s_cls[j]:
                            index_task = j#
        imglist_h_r = [img + " " + str(index_h_sub) + " " + str(index_h_sup) for img in
                       glob.glob(os.path.join(traindata_head_path, list_h[i][0], '*.jpg'))]
        imglist_tail = [img + " " + str(index_sub) + " " + str(index_sup) + " " + str(index_task) for img in
                        glob.glob(os.path.join(traindata_tail_path, t_cls[i], '*.jpg'))]
        for d in range(NUM):
            with open(save_folder + 'train_v3.txt', 'a')as f:
                f.write(random.choice(imglist_h_r) + ' ' + random.choice(imglist_tail) + " " + str(1))  # ~ relation + n/p
                f.write('\n')

def creatNeg(NUM):#Creat negative samples
    save_folder = cfg.BASE
    traindata_head_path = cfg.BASE + 'train/Head'
    traindata_tail_path = cfg.BASE + 'train/Tail'
    t_cls = ["Cucumber", "Banana", "Bread", "Cake", 'Pizza', 'Pizza', "Teapot", "WineBottle", "CoffeeMaker",
             'Paper', 'Tape', 'CottonMaterial', 'Rope', 'IronNail', 'RawMeat', 'Cloth', 'Book']  # 15+2
    t_s_cls = [["Cucumber", "Banana", "Bread", "Cake", 'Pizza'], ["CoffeeMaker", "Teapot", "WineBottle"],
               ['Paper', 'Tape', 'CottonMaterial', 'Rope'], ['IronNail', 'RawMeat'], ['Cloth', 'Book']]
    #####################################################################################
    list_h = [['TeaCup', 'Goblet', 'CoffeeCup',
               'SmallScissor', 'TailorScissor', 'ClawHammer', 'MeatHammer','Wardrobe', 'Bookshelf'],#Cucumber 9
              ['TeaCup', 'Goblet', 'CoffeeCup',
               'SmallScissor', 'TailorScissor', 'ClawHammer', 'MeatHammer', 'Wardrobe', 'Bookshelf'],  # Banana 9
              ['TeaCup', 'Goblet', 'CoffeeCup',
               'SmallScissor', 'TailorScissor', 'ClawHammer', 'MeatHammer', 'Wardrobe', 'Bookshelf'],  # Bread 9
              ['TeaCup', 'Goblet', 'CoffeeCup',
               'SmallScissor', 'TailorScissor', 'ClawHammer', 'MeatHammer', 'Wardrobe', 'Bookshelf'],  # Cake 9
              ['TeaCup', 'Goblet', 'CoffeeCup',
               'SmallScissor', 'TailorScissor', 'ClawHammer', 'MeatHammer', 'Wardrobe', 'Bookshelf'],  # Pizza 9
              ['TeaCup', 'Goblet', 'CoffeeCup',
               'SmallScissor', 'TailorScissor', 'ClawHammer', 'MeatHammer', 'Wardrobe', 'Bookshelf'],  # Pizza 9
              ['SlicingKnife', 'FruitKnife', 'BreadKnife', 'PizzaShakeKnife', 'PizzaHobKnife',
               'SmallScissor', 'TailorScissor', 'ClawHammer', 'MeatHammer', 'Wardrobe', 'Bookshelf'],  # Teapot 9+2
              ['SlicingKnife', 'FruitKnife', 'BreadKnife', 'PizzaShakeKnife', 'PizzaHobKnife',
               'SmallScissor', 'TailorScissor', 'ClawHammer', 'MeatHammer', 'Wardrobe', 'Bookshelf'],  # WineBottle 9+2
              ['SlicingKnife', 'FruitKnife', 'BreadKnife', 'PizzaShakeKnife', 'PizzaHobKnife',
               'SmallScissor', 'TailorScissor', 'ClawHammer', 'MeatHammer', 'Wardrobe', 'Bookshelf'] , # CoffeeMaker 9+2
              ['SlicingKnife', 'FruitKnife', 'BreadKnife', 'PizzaShakeKnife', 'PizzaHobKnife', 'TeaCup', 'Goblet',
               'CoffeeCup', 'ClawHammer', 'MeatHammer', 'Wardrobe', 'Bookshelf'] , # Paper 10+2
              ['SlicingKnife', 'FruitKnife', 'BreadKnife', 'PizzaShakeKnife', 'PizzaHobKnife', 'TeaCup', 'Goblet',
               'CoffeeCup', 'ClawHammer', 'MeatHammer', 'Wardrobe', 'Bookshelf'] , # Tape 10+2
              ['SlicingKnife', 'FruitKnife', 'BreadKnife', 'PizzaShakeKnife', 'PizzaHobKnife', 'TeaCup', 'Goblet',
               'CoffeeCup', 'ClawHammer', 'MeatHammer', 'Wardrobe', 'Bookshelf'],  # CottonMaterial 10+2
              ['SlicingKnife', 'FruitKnife', 'BreadKnife', 'PizzaShakeKnife', 'PizzaHobKnife', 'TeaCup', 'Goblet',
               'CoffeeCup', 'ClawHammer', 'MeatHammer', 'Wardrobe', 'Bookshelf'],  # Rope 10+2
              ['SlicingKnife', 'FruitKnife', 'BreadKnife', 'PizzaShakeKnife', 'PizzaHobKnife', 'TeaCup', 'Goblet', 'CoffeeCup',
               'SmallScissor', 'TailorScissor', 'Wardrobe', 'Bookshelf'] , # IronNail 10+2
              ['SlicingKnife', 'FruitKnife', 'BreadKnife', 'PizzaShakeKnife', 'PizzaHobKnife', 'TeaCup', 'Goblet', 'CoffeeCup',
               'SmallScissor', 'TailorScissor', 'Wardrobe', 'Bookshelf'],  # RawMeat 10+2
              ['SlicingKnife', 'FruitKnife', 'BreadKnife', 'PizzaShakeKnife', 'PizzaHobKnife', 'TeaCup', 'Goblet', 'CoffeeCup',
               'SmallScissor', 'TailorScissor', 'ClawHammer', 'MeatHammer'], # Cloth 10+2
              ['SlicingKnife', 'FruitKnife', 'BreadKnife', 'PizzaShakeKnife', 'PizzaHobKnife', 'TeaCup', 'Goblet', 'CoffeeCup',
               'SmallScissor', 'TailorScissor', 'ClawHammer', 'MeatHammer']]  # Book 10+2
    for i in range(len(t_cls)):
        imglist_h_all = []
        imglist_t_all = []
        for h in range(len(list_h[i])):
            for k, value in CLASS_DICT.items():
                if k < 30:
                    if value == list_h[i][h]:
                        index_h_sub = k  #
                    if value == t_cls[i]:
                        index_sub = k  #
                else:
                    if list_h[i][h] in value:
                        index_h_sup = k  #
                    if t_cls[i] in value:
                        index_sup = k  #
                        for j in range(len(t_s_cls)):
                            if value == t_s_cls[j]:
                                index_task = j  #
            imglist_h_r = [img + " " + str(index_h_sub) + " " + str(index_h_sup) for img in
                    glob.glob(os.path.join(traindata_head_path, list_h[i][h], '*.jpg'))]
            imglist_h_all.append(imglist_h_r)
            imglist_tail = [img + " " + str(index_sub) + " " + str(index_sup) + " " + str(index_task) for img in
                            glob.glob(os.path.join(traindata_tail_path, t_cls[i], '*.jpg'))]
            imglist_t_all.append(imglist_tail)
        for j in range(len(imglist_h_all)):
            for d in range(NUM):
                with open(save_folder + 'train_v3.txt', 'a')as f:
                    f.write(random.choice(imglist_h_all[j]) + ' ' + random.choice(imglist_t_all[j]) + " " + str(-1))  # ~ relation + n/p
                    f.write('\n')

def creatMid(NUM):
    save_folder = cfg.BASE
    traindata_head_path = cfg.BASE + 'train/Head'
    traindata_tail_path = cfg.BASE + 'train/Tail'
    t_cls = ["Cucumber", "Cucumber", "Banana", "Banana", "Bread", "Bread", "Cake", "Cake", "Teapot", "Teapot",
             "WineBottle", "WineBottle", "CoffeeMaker", "CoffeeMaker",
             'Paper', 'Tape', 'CottonMaterial', 'Rope', 'IronNail', 'RawMeat', 'Cloth', 'Book']  # 22
    t_s_cls = [["Cucumber", "Banana", "Bread", "Cake"], ["CoffeeMaker", "Teapot", "WineBottle"],
               ['Paper', 'Tape', 'CottonMaterial', 'Rope'], ['IronNail', 'RawMeat'], ['Cloth', 'Book']]
    #####################################################################################################
    list_h = [['FruitKnife'],  # Cucumber #22
              ['BreadKnife'],  # Cucumber
              ['SlicingKnife'],  # Banana
              ['BreadKnife'],  # Banana
              ['SlicingKnife'],  # Bread
              ['FruitKnife'],  # Bread
              ['SlicingKnife'],  # Cake
              ['FruitKnife'],  # Cake
              ['Goblet'],  # Teapot
              ['CoffeeCup'],  # Teapot
              ['TeaCup'],  # WineBottle
              ['CoffeeCup'],  # WineBottle
              ['TeaCup'],  # CoffeeMaker
              ['Goblet'],  # CoffeeMaker
              ['TailorScissor'],  # Paper
              ['TailorScissor'],  # Tape
              ['SmallScissor'],  # CottonMaterial
              ['SmallScissor'],  # Rope
              ['MeatHammer'],  # IronNail
              ['ClawHammer'],  # RawMeat
              ['Bookshelf'],  # Cloth
              ['Wardrobe']]  # Book
    for i in range(len(t_cls)):
        for k, value in CLASS_DICT.items():
            if k < 27:
                if value == list_h[i][0]:
                    index_h_sub = k  #
                if value == t_cls[i]:
                    index_sub = k  #
            else:
                if list_h[i][0] in value:
                    index_h_sup = k  #
                if t_cls[i] in value:
                    index_sup = k#
                    for j in range(len(t_s_cls)):
                        if value == t_s_cls[j]:
                            index_task = j#
        imglist_h_r = [img + " " + str(index_h_sub) + " " + str(index_h_sup) for img in
                       glob.glob(os.path.join(traindata_head_path, list_h[i][0], '*.jpg'))]
        imglist_tail = [img + " " + str(index_sub) + " " + str(index_sup) + " " + str(index_task) for img in
                        glob.glob(os.path.join(traindata_tail_path, t_cls[i], '*.jpg'))]
        for d in range(NUM):
            with open(save_folder + 'train.txt', 'a')as f:
                f.write(random.choice(imglist_h_r) + ' ' + random.choice(imglist_tail) + " " + str(0))  # ~ relation + n/p
                f.write('\n')



# ########## Creat samples #############
# creatPos(20000)#NUM*17
# creatNeg(3500)#NUM*183
# creatMid(20000)#NUM*22





