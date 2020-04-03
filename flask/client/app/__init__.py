from flask import Flask, session
from web3 import Web3, HTTPProvider
import json
from flask_session import Session
from werkzeug.utils import secure_filename

# Flask App initialization
app = Flask(__name__)
app.secret_key = 'secret_key'

BASE_PATH = '/Users/isaackane/Desktop/实训/'

UPLOAD_FOLDER = BASE_PATH + 'Fedblock-master/flask/client/uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif','pkl'])

SESSION_TYPE = 'redis'
app.config.from_object(__name__)
Session(app)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

server = Web3(HTTPProvider('http://localhost:7545'))

#CONTRACT_ADDRESS = server.toChecksumAddress("0xBbf5BC6267700d4347F460C1F41d535422E3c8C3")
#CONTRACT_ADDRESS = server.toChecksumAddress("0x3Eba6FF915ec245a832042fFfa63D7a615384836")
#DEFAULT_ACCOUNT = server.toChecksumAddress("0x4E61fC726f46E6d7f9488d466058cc2E07868De6")
#DEFAULT_ACCOUNT = server.toChecksumAddress("0xf847465aaC31C383540B56eb2B5a57f2C8192172")
DEFAULT_ACCOUNT = server.toChecksumAddress(server.eth.accounts[1])

with open('../../contract.txt') as f:
    CONTRACT_ADDRESS = f.read()

print(CONTRACT_ADDRESS)
with open('../../build/contracts/LearningContract.json') as f:
    voter_contract_data = json.load(f)

CONTRACT_ABI = voter_contract_data['abi']


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


from app import views
