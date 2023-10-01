import buffer_pool_manager as bm
import buffer_test
import buffer_pool_manager as bm
import page


def main():


    ## IMPLEMENT THE FOLLOWING STEPS USING YOUR BUFFER POOL MANAGER

    #TEST CASES:
    buffer_test.test_init()
    buffer_test.test_add1()
    buffer_test.test_add2()
    buffer_test.test_add3()
    buffer_test.test_add4()
    buffer_test.test_add5()
    buffer_test.test_add6()
    buffer_test.test_pin()
    buffer_test.test_delete1()
    buffer_test.test_delete2()




    #1. Create a BufferPool that can hold 16 frames
    buffer_mng = bm.BufferPoolManager(16)

    #2. Add 16 pages (page 0 to 15) to the BufferPool
    for page_id in range(16):
        buffer_mng.fetchPage(page_id)

    #3. Print the Buffer's Pool PageTable
    page_table_1 = buffer_mng.getPageTable()
    print("3. Page table " + str(page_table_1))

    #4. Print the replacer free frames list
    free_frames = buffer_mng.getReplacer().getFreeFrames()
    print("4. Free Frames " + str(free_frames))

    #5. Fetch page #14 from your bufferPool and prints the page_id
    page_14: page.Page = buffer_mng.getBufferPool()[14]
    print("5. Page 14 id: " + str(page_14.page_id))

    #6. Print page #14 pin counter
    print("6. Pin count of page 14: " + str(page_14.getPinCount()))

    #7. Fetch page #16 from your bufferPool and prints the page_id. Did it work? Why?
    page_16: page.Page = buffer_mng.fetchPage(16)
    if page_16 is not False:
        print("7. Id of page 16 is : " + str(page_16.page_id))
    else:
        print("7. Cannot fetch page 16")

    #8. Print the Buffer's Pool PageTable
    page_table_2 = buffer_mng.getPageTable()
    print("8. Page table " + str(page_table_2))

    #9. Unpin page #14. Page #14 is not dirty
    buffer_mng.unpinPage(14, False)
    print("9. Free Frames: " + str(buffer_mng.getReplacer().getFreeFrames()))
    print("page 14 is still present in the buffer as it is not yet removed but it was added to free frames" + str(buffer_mng.getPageTable()))

    #10. Try again to fetch page #16. Did it work? Why?
    page_16: page.Page = buffer_mng.fetchPage(16)
    if page_16 is not False:
        print("10. Id of page 16 is : " + str(page_16.page_id))
    else:
        print("10. Cannot fetch page 16")

    #11. Print the replacer free frame
    print("11. Free frames: " + str(buffer_mng.getReplacer().getFreeFrames()))
    print("Now page 14 should be removed from buffer and free frames: "+ str(buffer_mng.getPageTable()))

    #12. Unpin page #14 again. Page 14 is not dirty
    buffer_mng.unpinPage(14, False)

    #13.Print the replacer free frame
    print("13. Free frames: " + str(buffer_mng.getReplacer().getFreeFrames()))

    #14. Try again to fetch page #16.Did it work? Why?
    page_16: page.Page = buffer_mng.fetchPage(16)
    if page_16 is not False:
        print("14. Id of page 16 is : " + str(page_16.page_id))
    else:
        print("14. Cannot fetch page 16")

    #15. Print the Buffer's Pool PageTable
    print("15. Page Table: " + str(buffer_mng.getPageTable()))

    #16. Unpin page #9 and #12. They are both dirty

    #17. Fetch page #14 from your bufferPool and prints the page_id. What happened with the page that was replaced to make room for page #14?

    #18. Delete page #5. Did it work? Why?

    #19. Unpin page #5. The page is not dirty

    #20. Try to delete page #5 again. Did it work?

    #21. Print page table

    #22. Fetch page #5x

    return
    

main()
