class Codec {
public:

    // Linked List Node
    struct ListNode {
        string val;
        ListNode* next;

        ListNode(string v) {
            val = v;
            next = nullptr;
        }
    };

    // Head of linked list
    ListNode* head = nullptr;


    // ================= SERIALIZE =================

    void serializeHelper(TreeNode* root, string& result) {

        // NULL node
        if (root == nullptr) {
            result += "N,";
            return;
        }

        // Store node value
        result += to_string(root->val) + ",";

        // Left
        serializeHelper(root->left, result);

        // Right
        serializeHelper(root->right, result);
    }


    string serialize(TreeNode* root) {

        string result;

        serializeHelper(root, result);

        return result;
    }


    // ================= DESERIALIZE HELPER =================

    TreeNode* deserializeHelper(ListNode*& head) {

        // Safety check
        if (head == nullptr) {
            return nullptr;
        }

        // NULL node
        if (head->val == "N") {
            head = head->next;
            return nullptr;
        }

        // Create tree node
        TreeNode* root = new TreeNode(stoi(head->val));

        // Move linked-list head
        head = head->next;

        // Build left subtree
        root->left = deserializeHelper(head);

        // Build right subtree
        root->right = deserializeHelper(head);

        return root;
    }


    // ================= DESERIALIZE =================

    TreeNode* deserialize(string data) {

        // Empty data
        if (data.empty()) {
            return nullptr;
        }

        // Convert string → linked list
        stringstream ss(data);
        string value;

        ListNode* dummy = new ListNode("");
        ListNode* tail = dummy;

        while (getline(ss, value, ',')) {

            if (value.empty()) {
                continue;
            }

            tail->next = new ListNode(value);
            tail = tail->next;
        }

        // Actual head
        head = dummy->next;

        // Reconstruct tree
        return deserializeHelper(head);
    }
};