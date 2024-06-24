Import("env")
for e in (env, DefaultEnvironment()):
    #print("Linkerflags: " + str(e["LINKFLAGS"]))
    link_flags:list[str] = e["LINKFLAGS"]
    # here it appears only once. let's remove that.
    fixed_flags = [x for x in link_flags if x != "-Wl,--end-group" and x != "-Wl,--start-group"]
    e.Replace(LINKFLAGS=fixed_flags)