"""Test the mixin table functionality."""
from __future__ import absolute_import, unicode_literals
from attest import Tests
import django_tables2 as tables

mixin = Tests()


@mixin.test
def unique_id_auto_generated_test():
    class AutoTableID(tables.UniqueTableIdMixin, tables.Table):
        pass
    assert {'id': 'autotableid_0'} == AutoTableID([]).attrs
    assert {'id': 'autotableid_1'} == AutoTableID([]).attrs

    class AutoTableID2(tables.UniqueTableIdMixin, tables.Table):

        class Meta:
            attrs = {'any_other': 'any_value'}
    assert {'any_other': 'any_value',
            'id': 'autotableid2_0'} == AutoTableID2([]).attrs
    assert {'any_other': 'any_value',
            'id': 'autotableid2_1'} == AutoTableID2([]).attrs

    class AutoTableID3(tables.UniqueTableIdMixin, tables.Table):

        class Meta:
            attrs = {'id': 'magic', 'any_other': 'any_value'}

    assert {'any_other': 'any_value',
            'id': 'magic_0'} == AutoTableID3([]).attrs
    assert {'any_other': 'any_value',
            'id': 'magic_1'} == AutoTableID3([]).attrs

