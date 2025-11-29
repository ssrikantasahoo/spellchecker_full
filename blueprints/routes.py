from flask import Blueprint, render_template, request, jsonify
from services.spell_checker import SpellCheckerService
import logging
bp=Blueprint('bp',__name__)
log=logging.getLogger(__name__)

@bp.route('/')
def home(): return render_template('index.html')

@bp.route('/api/check',methods=['POST'])
def api_check():
    txt=request.json.get('text','')
    svc=SpellCheckerService()
    res=svc.check(txt)
    log.info(f"IN:{txt} OUT:{res['corrected']}")
    return jsonify(res)
