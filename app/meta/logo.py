def logo(version):
  str = """
██████╗ ██╗   ██╗████████╗██╗  ██╗ ██████╗ ███╗   ██╗                       
██╔══██╗╚██╗ ██╔╝╚══██╔══╝██║  ██║██╔═══██╗████╗  ██║                       
██████╔╝ ╚████╔╝    ██║   ███████║██║   ██║██╔██╗ ██║                       
██╔═══╝   ╚██╔╝     ██║   ██╔══██║██║   ██║██║╚██╗██║                       
██║        ██║      ██║   ██║  ██║╚██████╔╝██║ ╚████║                       
╚═╝        ╚═╝      ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝                       
                                                                            
██████╗  ██████╗  ██████╗ ████████╗███████╗████████╗██████╗  █████╗ ██████╗ 
██╔══██╗██╔═══██╗██╔═══██╗╚══██╔══╝██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗
██████╔╝██║   ██║██║   ██║   ██║   ███████╗   ██║   ██████╔╝███████║██████╔╝
██╔══██╗██║   ██║██║   ██║   ██║   ╚════██║   ██║   ██╔══██╗██╔══██║██╔═══╝ 
██████╔╝╚██████╔╝╚██████╔╝   ██║   ███████║   ██║   ██║  ██║██║  ██║██║     
╚═════╝  ╚═════╝  ╚═════╝    ╚═╝   ╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝
version: {0}
  """.format(version)

  print(str)