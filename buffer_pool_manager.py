import disk_manager as dm
import lru_replacer as lru

# setup_logger.py
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class BufferPoolManager:
    """
    A class to represent the BufferPoolManager
    The BufferPoolManager is responsible for fetching database pages from the DiskManager and 
    storing them in memory. 
    
    The BufferPoolManager must write the contents of a dirty Page back to disk before that object can be reused. It 
    writes dirty pages out to disk when it is either explicitly instructed to do so or when it needs to evict a page to make space for a new page.
    
    The BufferPoolManager is not allowed to free a Page that is pinned. 
    
    This BufferPoolManager implementation will use the LRUReplacer class. 
    

    Attributes
    ----------
    buffer_pool : array
        list with page objects
    page_table: array
        list of page_ids current in the buffer pool 
    buffer_total_no_of_frames: int
        total of frames that the buffer pool can hold
    disk_manager: DiskManager
        diskManager object
    replacer: LRUReplacer
        replacer object
   
    Methods
    -------
    getBufferPoll():
        returns all page objects in the buffer pool
    getPageTable():
        return the index of all pages objects currently in the buffer pool
    getDiskManager():
        return disk manager object
    getReplacer():
        return replace object
    fetchPage(page_id):
        returns a page stored in memory. If the page is not in memory, then the page must be read from the disk.
    newPage(page_id):
        reads a page from the disk using the disk manager
    deletePage(page_id):
        deletes a page from the buffer pool and from the disk
    unpinPage(page_id, is_dirty):
        uping a page so the replacer knows it is a free frame that can be evited if needed.
    flushPage(page_id):
        flushs a page with id = page_id from the buffer pool to disk regardless of its pin status.
    flushAllPages():
        flush all pages from the buffer pool to disk regardless of its pin status.
    
    """
    
    def __init__(self, no_of_frames):
        self.buffer_pool = []
        self.page_table = []
        self.disk_manager = dm.DiskManager()
        self.replacer = lru.LRUReplacer()
        self.buffer_total_no_of_frames = no_of_frames
        
    def getBufferPool(self):
        ##ADD YOUR CODE HERE
        return
    
    def getPageTable(self):
        ##ADD YOUR CODE HERE
        return
    
    def getReplacer(self):
        ##ADD YOUR CODE HERE
        return
    
    def getDiskManager(self):
       ##ADD YOUR CODE HERE
        return
    
    def fetchPage(self, page_id):
        # Fetch page from the buffer pool, if not in memory than get from disk
        #  1. search the page table for the requested page_id.
        #  1.1   if page exists in the bufferpool, increments its pin counter, pin it and return it immediately.
        #  1.2   if page is not in the bufferpool, fetch the page from disk using the disk manager and pin it. If the bufferpool is full, find a replacement page using the replacer.  If no pages can be evited (i.e., all pages are pinned), print a error message  
        #  2. if you need to evict a page, check if it is dirty. If so, write it back to the disk.
        #  3. delete the evicted page from the page table and insert the page you fecthed from disk.
        #  4. update the page metadata, and then return a pointer to it.
        ##ADD YOUR CODE HERE
        return
                    

    def loadPage(self, page_id):
        logger.info(f"Fetching a new page to the bufferpool. Page {page_id} is not in bufferpool, it has to be read from disk")
        
        # Goal: Fetch page from the disk manager and put in the buffer pool. 
        # Checks if page_id is valid in disk, if valid increment its pin count, pin it and return the page. 
        # Otherwise return a error message and page = None.
        ##ADD YOUR CODE HERE
        return
    
    def deletePage(self, page_id):
        logger.info(f"Deleting page {page_id} from bufferpool")
        
        #only delete the pages that are not pinned. if pinned print a error message and return False
        ##ADD YOUR CODE HERE
        return
   
    def unpinPage(self, page_id, is_dirty):
        logger.info(f"Unpinning page {page_id} in the bufferpool")
        #decrements the page pin counter and update page "dirtyness" with the value of is_dirty parameter".
        #if pin_count == 0 then unpin the page.
        ##ADD YOUR CODE HERE
        return

    def flushPage(self, page_id):
        logger.info(f"Flushing page {page_id} out of the bufferpool")
        #write page to disk and update its metadata
        ##ADD YOUR CODE HERE
        return

    def flushAllPages(self):
        logger.info(f"Flushing all pages out of the bufferpool")
        #write all pages to disk and update metadata
        ##ADD YOUR CODE HERE
        return
