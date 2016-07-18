def setLogging():
   import logging
   logging.basicConfig(filename='/local/smasilam/tmp/myapp.log', level=logging.INFO)
   logger = logging.getLogger('debug_log')
   logger.setLevel(logging.DEBUG)
   ch = logging.StreamHandler()
   ch.setLevel(logging.DEBUG)
   formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
   ch.setFormatter(formatter)
   logger.addHandler(ch)
   logger.debug('debug message')
   logger.info('info message')
   logger.warn('warn message')
   logger.error('error message')
   logger.critical('critical message')
   return logger

log = setLogging()

class myThread (threading.Thread):
    def __init__(self, threadID, name, counter, handle, logger):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.handle =  handle #Handle for IFC/Leaf
        self.logger = logger
    def run(self):
        print "Starting " + self.name
        collectFaults(self.name, self.counter, 1000 , self.handle,self.logger)
        createConfig(self.name, self.counter, 1000 , self.handle,self.logger)
        print "Exiting " + self.name

def print_time(threadName, delay, counter):
    while counter:
        if exitFlag:
            thread.exit()
        time.sleep(delay)
        print "%s: %s" % (threadName, time.ctime(time.time()))
        counter -= 1

def collectFaults(threadName, delay, counter, handle,log):
    while counter:
        if exitFlag:
            thread.exit()
        length = len(handle.lookupByClass('fault.Inst'))
        time.sleep(delay)
        printStr =  "%s: %s : %s " % (threadName, time.ctime(time.time()),str(length))
        log.error(printStr)
        counter -= 1

def createConfig(threadName, delay, counter, handle,log):
    while counter:
        if exitFlag:
            thread.exit()
        mo = handle.create('fv.Tenant', name = name)
        d.commit(mo)
        length = len(handle.lookupByClass('fv.Tenant',pfilter='fv.Tenant.name == "'+ name + '"'))
        if length != 1:
            print 'Tenant not created ' + name
        time.sleep(delay)
        mo.delete()
        d.commit(mo)
        printStr =  "%s: %s : %s " % (threadName, time.ctime(time.time()),str(length))
        counter -= 1

# Create new threads

count = 1 
for leaf in leafList:
    name = "Thread-"+ leaf.lookupByClass('top.System')[0].name
    thread = myThread(count, name, 1, leaf,log)
    thread.start()
    count += 1

# Start new Threads
thread1.start()
thread2.start()

print "Exiting Main Thread"



ifcCount = len(d.lookupByClass('fvCEp',pfilter='fv.CEp.mac == "00:12:01:00:00:16"'))
leaf=  givenNodeNameReturnHdl('scale2-leaf45')
leafCount = len(leaf.lookupByClass('epmMacEp',pfilter='epm.MacEp.addr == "00:12:01:00:00:16"'))
