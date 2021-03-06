
# /home/jarvis/Documents/Work/ResearchUSA/Code/ScanDB/CVCode/parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.5'

_lr_method = 'LALR'

_lr_signature = '28CD447818D24975A0E9EC918F4C8853'
    
_lr_action_items = {'SIC':([0,],[1,]),'NUM':([1,],[3,]),'$end':([2,3,],[0,-1,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'sic_code':([0,],[2,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> sic_code","S'",1,None,None,None),
  ('sic_code -> SIC NUM','sic_code',2,'p_sic_code','Parser.py',18),
  ('naics_code -> NAICS NAICS_NUM','naics_code',2,'p_naics_code','Parser.py',22),
  ('email -> EMAIL_TOK EMAIL','email',2,'p_email_withtok','Parser.py',26),
  ('email -> EMAIL','email',1,'p_email','Parser.py',30),
  ('website -> WEB','website',1,'p_website','Parser.py',34),
]
