import time

from solc.exceptions import SolcError
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from solc import compile_standard


PATH = "input your .sol files root directory here"
#/Users/msmacpro/DEVELOPMENT/BlockChain/eth-projects/solidity-compiler/

def compileInSolidity(event):
    source = event.src_path
    file = event.src_path.split("/")[-1]
    spec = {
        "language": "Solidity",
        "sources": {
            file: {
                "urls": [
                    source
                ]
            }
        },
        "settings": {
            "optimizer": {
                "enabled": True
            },
            "outputSelection": {
                "*": {
                    "*": [
                        "metadata", "evm.bytecode", "abi"
                    ]
                }
            }
        }
    };
    out = compile_standard(spec, allow_paths=event.src_path);
    print(out)

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if ".sol" in event.src_path:
            try:
                print(f'event type: {event.event_type} path : {event.src_path}')
                compileInSolidity(event)
            except SolcError as errorObject:
                errors = errorObject['message']
                for e in errors:
                    print(e["formattedMessage"])

if __name__ ==  "__main__":
   event_handler = MyHandler()
   observer = Observer()
   observer.schedule(event_handler,  path=PATH,  recursive=False)
   observer.start()
   try:
       while True:
           time.sleep(1)
   except  KeyboardInterrupt:
       observer.stop()
   observer.join()