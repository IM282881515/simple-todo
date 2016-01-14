#!/usr/bin/env python
# coding: utf-8
import sqlite3 as db
import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

'''
仅对sqlite数据库操作进行简单的封装

'''
class sqldb:
    #先验证数据库是否存在
    def __init__(self, path):
        #如果数据库存在，就直接连接
        self.conn = db.connect(path)
        self.cu = self.conn.cursor()

    def __del__(self):
        self.cu.close()
        self.conn.close()
        pass

    def _where(self, vars=None):
        str_where=''
        if vars == None: vars={}
        else:  str_where=' where '
        nSize =len(vars);i=0

        for k in vars.keys():
            str_where += '%s=%s'%(str(k), vars[k]);i+=1;
            if i!=nSize: str_where += " and ";

        return str_where

    #vars_where为字典变量，例如{'id':1}
    def select(self, tables, vars_where=None, what='*', where=None, order=None, group=None):
        str_sql  ="select %s from %s %s"%(what,tables,self._where(vars_where))
        if order!=None:str_sql += str(order);
        rec = self.excute(str_sql)
        dbre = self.cu.fetchall()
        return dbre
        pass

    #vars_where为字典变量，例如{'id':1}
    def delete(self, tables, vars_where=None):
        str_sql  ="delete from %s %s"%(tables,self._where(vars_where))
        rec = self.excute(str_sql)
        pass

    #vars_values是要增加内容 key是字段名，例如{'title':'美好的一天'}
    def insert(self, tables, vars_values):
        #str_sql  = 'INSERT INTO \''; str_sql+=tables; str_sql+='\' (';
        str_sql  ='INSERT INTO \'%s\' ('%tables
        nSize =len(vars_values);
        i=0
        for k in vars_values.keys():
            str_sql += str(k); i+=1;
            if i!=nSize: str_sql += ',';

        str_sql+=") VALUES(";
        i=0
        for k in vars_values.keys():
            str_sql+='\'';str_sql += str(vars_values[k]); i+=1;
            if i!=nSize: str_sql += '\',';

        str_sql+="\')";

        print str_sql
        rec = self.excute(str_sql)
        pass

    def update(self, tables, vars_values, vars_where=None):
        #str_sql  = 'UPDATE '; str_sql+=tables; str_sql+=' set ';
        str_sql  ='UPDATE %s set '%tables

        nSize =len(vars_values);i=0
        for k in vars_values.keys():
            str_sql += '%s=\'%s\''%(str(k), str(vars_values[k]))
            i+=1;
            if i!=nSize: str_sql += ',';

        str_sql += self._where(vars_where)
        print str_sql

        rec = self.excute(str_sql)
        pass

    def create_table(self,tables, var_value):
        str_sql  = 'create table \''; str_sql+=tables; str_sql+='\' ( ';

        nSize = len(var_value)
        i=0
        for k in var_value.keys():
            str_sql+=str(k); str_sql+=' '; str_sql+=str(var_value[k]); i+=1;
            if i!=nSize: str_sql+=',';
        str_sql +=')'

        rec = self.excute(str_sql)

    def create_table_if_not_exists(self,tables, var_value):
        str_sql  = 'create table IF NOT EXISTS \''; str_sql+=tables; str_sql+='\' ( ';

        nSize = len(var_value)
        i=0
        for k in var_value.keys():
            str_sql+=str(k); str_sql+=' '; str_sql+=str(var_value[k]); i+=1;
            if i!=nSize: str_sql+=',';
        str_sql +=')'

        rec = self.excute(str_sql)

    def excute(self,str_sql):
        rec = self.cu.execute(str_sql)
        return rec

    def commit(self):
        self.conn.commit();

    def getcolumname(self, tables):
        str_sql='PRAGMA table_info('
        str_sql+=tables; str_sql+=')'

        str_sql='PRAGMA table_info(%s)'%tables
        print str_sql

        rec = self.excute(str_sql)
        vars = self.cu.fetchall()

        list=[]
        for var in vars:
            list.append(var[1])
        return list

      #  var={}
      #  for data in rec:
      #      pass


