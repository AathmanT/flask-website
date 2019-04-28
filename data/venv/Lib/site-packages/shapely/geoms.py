class GeometrySequence(object):
    """
    Iterative access to members of a homogeneous multipart geometry.
    """

    # Attributes
    # ----------
    # _factory : callable
    #     Returns instances of Shapely geometries
    # _geom : c_void_p
    #     Ctypes pointer to the parent's GEOS geometry
    # _ndim : int
    #     Number of dimensions (2 or 3, generally)
    # __p__ : object
    #     Parent (Shapely) geometry
    _factory = None
    _geom = None
    __p__ = None
    _ndim = None

    def __init__(self, parent, type):
        self._factory = type
        self.__p__ = parent

    def _update(self):
        self._geom = self.__p__._geom
        self._ndim = self.__p__._ndim
        
    def _get_geom_item(self, i):
        g = self._factory()
        g._owned = True
        g._geom = lgeos.GEOSGetGeometryN(self._geom, i)
        return g

    def __iter__(self):
        self._update()
        for i in range(self.__len__()):
            yield self._get_geom_item(i)

    def __len__(self):
        self._update()
        return lgeos.GEOSGetNumGeometries(self._geom)

    def __getitem__(self, i):
        self._update()
        M = self.__len__()
        if i + M < 0 or i >= M:
            raise IndexError("index out of range")
        if i < 0:
            ii = M + i
        else:
            ii = i
        return self._get_geom_item(i)

    @property
    def _longest(self):
        max = 0
        for g in iter(self):
            l = len(g.coords)
            if l > max:
                max = l


class HeterogeneousGeometrySequence(GeometrySequence):
    """
    Iterative access to a heterogeneous sequence of geometries.
    """

    def __init__(self, parent):
        super(HeterogeneousGeometrySequence, self).__init__(parent, None)

    def _get_geom_item(self, i):
        sub = lgeos.GEOSGetGeometryN(self._geom, i)
        g = geom_factory(sub)
        g._owned = True
        return g

