#!/usr/bin/env python
# coding: utf-8
from sqldb import sqldb
from datetime import datetime

class tododb:
    def __init__(self):
        self.db = sqldb('todo.db')

    def New(self, title):
        self.db.insert("todo", {"title":title, "post_date":datetime.now()})
        self.db.commit()

    def get_all(self):
        rec = self.db.select('todo')
        return rec

    def get(self, id):
        list = self.db.getcolumname('todo')

        rec = self.db.select("todo", {"id":id})
        var={}
        if len(rec) !=0:
            vars = rec[0]
            for i in range(0, len(list)):
                var[list[i]]=vars[i]

        return var


    def delete(self, id):
        self.db.delete('todo', {'id':id })
        self.db.commit();

    def update(self, id, title):
        self.db.update('todo', {'title':title}, {'id':id})
        self.db.commit();


    def create_todo_table(self):
        var = {'id':'id INTEGER PRIMARY KEY', 'title':'TEXT', 'finished':'BOOL', 'post_date':'TEXT'}
        self.db.create_table_if_not_exists('todo', var)

if __name__ == "__main__":
    db = tododb();
    #db.create_todo_table();
    print db.db.getcolumname('todo');

#    db = sqldb()
#    db.create_table("to", {'id':'INTEGER PRIMARY KEY AUTOINCREMENT', 'title':'TEXT'});
#    db.insert('to', {'title':'ppp'})

    '''
    a=[1,2,3,4]
    for i  in range(0, len(a)):
        print i,a[i]

    '''

