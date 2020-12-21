/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(   x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        if (!l2 && l1->val == 0 && !l1->next) {
            return nullptr;
        }
        if (l2) {
            l1->val += l2->val;
        }

        if (!l1->next) {
            l1->next = new ListNode(l1->val / 10, nullptr);
        } else {
            l1->next->val += l1->val / 10;
        }

        l1->val %= 10;
        
        if (l2) {
            l1->next = addTwoNumbers(l1->next, l2->next);
        } else {
            l1->next = addTwoNumbers(l1->next, nullptr);
        }

        return l1;
    }
};
