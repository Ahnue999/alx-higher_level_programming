#!/usr/bin/python3
""" base class """


import json
import csv


class Base:
    """ base class """

    __nb_objects = 0

    def __init__(self, id=None):
        """ init """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ to json string """

        if list_dictionaries is None or list_dictionaries == []:
            return "[]"

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ save to file """

        if list_objs is None:
            list_objs = []

        new = list()

        filename = str(cls.__name__) + ".json"
        with open(filename, "w", encoding='utf-8') as fp:
            for obj in list_objs:
                new.append(obj.to_dictionary())
            string = cls.to_json_string(new)
            fp.write(string)

    @staticmethod
    def from_json_string(json_string):
        """ from json string """

        if json_string is None or json_string == "":
            return []

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ create """

        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                obj = cls(1, 1)
            else:
                obj = cls(1)

            obj.update(**dictionary)
            return obj

    @classmethod
    def load_from_file(cls):
        """ load from file """

        filename = cls.__name__ + ".json"

        try:
            with open(filename, encoding='utf=8') as fp:
                
                objlist = list()
                instances = fp.readlines()
                for line in instances:
                    if line:
                        objs = cls.from_json_string(line)
                        for obj in objs:
                            objlist.append(cls.create(**obj))
            return objlist
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ save to csv file """

        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline='', encoding='utf-8') as fp:

            writer = csv.writer(fp, delimiter=',')
            for obj in list_objs:
                ls = obj.to_dictionary().values()
                writer.writerow(ls)

    @classmethod
    def load_from_file_csv(cls):
        """ load to csv file """

        filename = cls.__name__ + ".csv"

        try:
            with open(filename, newline='', encoding='utf-8') as fp:
                reader = csv.reader(fp, delimiter=',')

                if cls.__name__ == "Rectangle":
                    attrs = ['id', 'width', 'height', 'x', 'y']
                else:
                    attrs = ['id', 'size', 'x', 'y']

                objlist = list()
                for obj in reader:
                    newd = dict()
                    for attr, objattr in zip(attrs, obj):
                        newd[attr] = int(objattr)
                    objlist.append(cls.create(**newd))

                return objlist
        except IOError:
            return []
