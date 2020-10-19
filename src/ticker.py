# https://stackoverflow.com/questions/8420422/python-windows-equivalent-of-sigalrm
# https://stackoverflow.com/questions/323972/is-there-any-way-to-kill-a-thread
import time, threading
import multiprocessing

class Ticker(threading.Thread):
  """A very simple thread that merely blocks for :attr:`interval` and sets a
  :class:`threading.Event` when the :attr:`interval` has elapsed. It then waits
  for the caller to unset this event before looping again.

  Example use::

    t = Ticker(1.0) # make a ticker
    t.start() # start the ticker in a new thread
    try:
      while t.evt.wait(): # hang out til the time has elapsed
        t.evt.clear() # tell the ticker to loop again
        print time.time(), "FIRING!"
    except:
      t.stop() # tell the thread to stop
      t.join() # wait til the thread actually dies

  """
  # SIGALRM based timing proved to be unreliable on various python installs,
  # so we use a simple thread that blocks on sleep and sets a threading.Event
  # when the timer expires, it does this forever.
  def __init__(self, interval):
    super(Ticker, self).__init__()
    self.interval = interval
    self.evt = threading.Event()
    self.evt.clear()
    self.should_run = threading.Event()
    self.should_run.set()

  def stop(self):
    """Stop the this thread. You probably want to call :meth:`join` immediately
    afterwards
    """
    self.should_run.clear()

  def consume(self):
    was_set = self.evt.is_set()
    if was_set:
      self.evt.clear()
    return was_set

  def run(self):
    """The internal main method of this thread. Block for :attr:`interval`
    seconds before setting :attr:`Ticker.evt`

    .. warning::
      Do not call this directly!  Instead call :meth:`start`.
    """
    while self.should_run.is_set():
      time.sleep(self.interval)
      self.evt.set()


t = Ticker(1.0) # make a ticker
t.start() # start the ticker in a new thread
try:
    while t.evt.wait(): # hang out til the time has elapsed
        t.evt.clear() # tell the ticker to loop again
        print (time.time(), "FIRING!")
except:
    t.stop() # tell the thread to stop
    t.join() # wait til the thread actually dies