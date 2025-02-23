# setup_logger.py
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Replacer:
    """
    A class to represent the page replacer
    The Replacer keeps track of when Page objects are accessed so that it can decide which one to 
    evict when it must free a frame to make room for copying a new physical page from disk.


    Methods
    -------
    victim():
        return which frame should be evicted from the BufferPool. 
    pin(page_id):
        pin a page in the BufferPool
    unpin():
        unpin a page in the buffer pool
    replacerSize():
        returns the number of frames that are currently in the Replacer.

    """
    def __init__(self):
        pass

    def victim(self):
        pass

    def pin(self, page_id):
        pass
    
    def unpin(self, page_id):
        pass

    def replacerSize(self):
        pass

class LRUReplacer(Replacer):
    """
    A subclass of Replacer that implement a specific replacement strategy.
    The LRU replacer discards the least recently used page first. 
    This algorithm requires keeping track of what page objects was used when, so that it can decide 
    which one to evict when it must free a frame to make room for copying a new physical page from disk.

    Attributes
    ----------
    free_frames : array
        frames that can be evited, if needed. When initialized, there is no free frame in it. Only unpinned 
        frames can be added to the free_frames list.
   
    Methods
    -------
    victim():
        identifies the frame from the free_frames list that was accessed the least recently. if there is such a frame, then store its 
        contents in the output parameter and return true. if there is no frame to be evicted (free_frames list is
        empty, then return False.
    pin(page_id):
        when a page is pinned, its corresponding frame in the Buffer Pool cannot be evicted until its pin counter 
        is 0 again. This function removes the frame containing the pinned page from the free_frames list in the Replacer
    unpin():
        when the pin_count of a page becomes 0, the frame can be unpined. This method should add the frame 
        containing the unpinned page into the Replacer free_frames list.
    getFreeFrames():
        return free_frames list
    """
    
    def __init__(self):
        super().__init__()
        self.free_frames = []
        
    def getFreeFrames(self):
        ##ADD YOUR CODE HERE
        return self.free_frames
    
    def pin(self, page_id):
        logging.info(f"Page {page_id} is pinned. It is Removed from the free_frames list")
        ##ADD YOUR CODE HERE
        if page_id in self.free_frames:
            self.free_frames.remove(page_id)
        return

    def unpin(self, page_id):
        logging.info(f"Page {page_id} is unpinned. It is added it to the free_frames list")
        ##ADD YOUR CODE HERE
        self.free_frames.append(page_id)
        return
    
    ## delete from memory and flush to disk
    def victim(self):
        logging.info("Evicting the page that was accessed the least recently. Remove it from the free frames list")
        ##ADD YOUR CODE HERE
        """
        identifies the frame from the free_frames list that was accessed the least recently. if there is such a frame, 
        then store its contents in the output parameter and return true. if there is no frame to be evicted (free_frames
        list is empty, then return False.
        """
        if len(self.free_frames) == 0:
            logger.info("No frame to be evicted. The free_frames list is empty.")
            return False
        else:
            least_recently_used_frame = self.free_frames.pop(0)
            logger.info(f"Evicted frame: {least_recently_used_frame}")
            return least_recently_used_frame
        
    def replacerSize(self):
        ##ADD YOUR CODE HERE
        return