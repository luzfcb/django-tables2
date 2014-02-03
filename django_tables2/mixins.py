# coding: utf-8


class UniqueTableIdMixin(object):

    """
    Mixin to autogenerate unique table id

    Usage:

    .. code-block:: python

        >>> from django_tables2 import tables
        >>> class AutoTableID(UniqueTableIdMixin, tables.Table):
        ...     pass
        ... 
        >>> class AutoTableID2(UniqueTableIdMixin, tables.Table):
        ...     class Meta:
        ...         attrs = {'any_other': 'any_value'}
        ...         
        >>> class AutoTableID3(UniqueTableIdMixin, tables.Table):
        ...     class Meta:
        ...         attrs = {'id': 'magic', 'any_other': 'any_value'}
        ... 
        >>> a = AutoTableID([])
        >>> a.attrs
        {'id': 'autotableid_0'}
        >>> b = AutoTableID2([])
        >>> b.attrs
        {'any_other': 'any_value', 'id': 'autotableid2_0'}
        >>> c = AutoTableID3([])
        >>> c.attrs
        {'any_other': 'any_value', 'id': 'magic_0'}

    """

    # Tracks each time a Table instance is created. Used to retain order.
    _creation_counter = 0

    def __init__(self, *args, **kwargs):
        super(UniqueTableIdMixin, self).__init__(*args, **kwargs)
        # Increase the creation counter, and save our local copy.
        self._creation_counter = self.__class__._creation_counter
        self.__class__._creation_counter += 1
        self._base_table_name = self.attrs.get('id')
        if self._base_table_name:
            del self.attrs['id']
            self.attrs.update({'id': '%s_%d' % (self._base_table_name,
                                                self._creation_counter)})
        else:
            self.attrs.update(
                {'id': '%s_%d' % (str(self.__class__.__name__).lower(),
                                  self._creation_counter)})

    @property
    def table_id(self):
        return self.attrs.get('id')
