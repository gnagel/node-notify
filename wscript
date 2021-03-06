def set_options(opt):
  opt.tool_options("compiler_cxx")

def configure(conf):
  conf.check_tool("compiler_cxx")
  conf.check_tool("node_addon")
  # @oli
  conf.check_cfg(package='gtkmm-2.4', args='--cflags --libs', uselib_store='LIBGTKMM')
  conf.check_cfg(package='libnotifymm-1.0', args='--cflags --libs', uselib_store='LIBNOTIFYMM')

def build(bld):
  obj = bld.new_task_gen("cxx", "shlib", "node_addon") 
  obj.cxxflags = ["-g", "-D_FILE_OFFSET_BITS=64", "-D_LARGEFILE_SOURCE", "-Wall"]
  obj.target = "gtknotify"
  obj.source = "src/node_gtknotify.cpp"
  # @oli
  obj.uselib = ['LIBGTKMM', 'LIBNOTIFYMM']
