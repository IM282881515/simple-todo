#!/usr/bin/env python
# coding: utf-8
import web
from config import settings

from model import tododb

render = settings.render

class Edit:

    def GET(self, id):
        db=tododb.tododb()
        rec = db.get(id)
        return render.todo.edit(rec)

    def POST(self, id):
        i = web.input()
        title = i.get('title', None)
        if not title:
            return render.error('标题是必须的', None)

        db=tododb.tododb()
        rec = db.update(id, title)
        return render.error('修改成功！', '/')


class Delete:
    def GET(self, id):
        db=tododb.tododb()
        rec = db.delete(id)
        return render.error("<em>删除成功</em>", '/')


class Index:
    def GET(self):
        db=tododb.tododb()
        rec = db.get_all()
        return render.index(rec)

class New:
    def POST(self):
        i = web.input()
        title = i.get('title', None)
        db=tododb.tododb()
        db.New(title)
        return render.error('添加成功！', '/')