# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def sortList(self, head):
        ''' In the common sorting algorithms, there are only two, which can guarantee
            Nlog(N) in the worst case. The two are merge sorting and heap sorting.
            Heap sorting is apparently not suitable for this challenge, because it
            requires array to store the elements.
            We are going to solve this challenge with bottom-up merge sorting.
        '''
        if head == None:    return None

        mergeSize = 1           # Bottom-up merge sorting.
        finishSort = False

        # Add a pseudo head node to make the process uniform.
        # In the original list, during the merging, the head node might change.
        # But after adding this pseudo head node, the head node never changes.
        pseudoHead = ListNode(-1)
        pseudoHead.next = head

        while not finishSort:
            # Start a new round of merging.
            endOfSorted = pseudoHead

            while endOfSorted.next != None:
                # The start position of the first merged list.
                firstToSort = endOfSorted.next

                # The start position of the second merged list.
                secondToSort = firstToSort
                for _ in xrange(mergeSize):
                    secondToSort = secondToSort.next
                    if secondToSort == None:    break

                if secondToSort == None:
                    # Reach the end of the whole list. No need to
                    # merge anymore.
                    if firstToSort == pseudoHead.next:
                        # Did not merge anything in this round, because
                        # mergeSize >= listSize. Whole list is sorted.
                        finishSort = True
                    break

                # Record how many nodes in first and second list are
                # merged. firstListCount will finally be mergeSize.
                # secondListCount might be either less than or equal
                # to mergeSize.
                firstListCount, secondListCount = 0, 0

                # Merge the firstToSort and secondToSort.
                #
                # Actually we do NOT need to get the end positions of
                # lists. We can determine their end during the merge
                # process with two counters.
                #
                # In my first answer, I found the end positions of
                # both to-merge lists. It leads to Time Limit Exceeded.
                while firstListCount < mergeSize and \
                      secondListCount < mergeSize and \
                      secondToSort != None:
                    if firstToSort.val <= secondToSort.val:
                        endOfSorted.next = firstToSort
                        endOfSorted = endOfSorted.next
                        firstToSort = firstToSort.next
                        firstListCount += 1
                    else:
                        endOfSorted.next = secondToSort
                        endOfSorted = endOfSorted.next
                        secondToSort = secondToSort.next
                        secondListCount += 1

                if firstListCount == mergeSize:
                    # THere may be some left nodes in second to-sort list.
                    while secondListCount < mergeSize and \
                          secondToSort != None:
                        endOfSorted.next = secondToSort
                        endOfSorted = endOfSorted.next
                        secondToSort = secondToSort.next
                        secondListCount += 1
                else:
                    # THere may be some left nodes in first to-sort list.
                    while firstListCount < mergeSize:
                        endOfSorted.next = firstToSort
                        endOfSorted = endOfSorted.next
                        firstToSort = firstToSort.next
                        firstListCount += 1
                    endOfSorted.next = secondToSort

            # Double the mergeSize for the next round.
            mergeSize = mergeSize << 1

        # Skip the pseudo head node.
        return pseudoHead.next
