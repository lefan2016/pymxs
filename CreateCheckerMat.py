
rt = pymxs.runtime
rt.clearlistener()
a = rt.plane(width=1000, length=1000 )
m = rt.standardmaterial()
map = rt.Checker()
m.diffuseMap = map
a.material = m
map_coord = m.diffuseMap.coords
map_coord.V_Offset = move_offset
c_time = rt.currentTime
move_offset = c_time * 0.333
map_coord.V_Offset = move_offset
