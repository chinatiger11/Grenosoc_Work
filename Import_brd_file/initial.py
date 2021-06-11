

import time

def init_HFSS(import_brd_file):
	ts_n = time.time()
	index_num = import_brd_file.find("oppo") + import_brd_file.find("adi")
	if ts_n > 1630425600:
		raise ValueError("time out")
	# elif index_num <= -1:
		# raise ValueError("path error")
	else:
		return "AnsoftHfss.HfssScriptInterface", "ImportExport"
