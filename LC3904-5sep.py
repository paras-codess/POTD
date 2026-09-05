class Solution {
public:
    int firstStableIndex(vector<int>& nums, int k) {
        int nums_size = nums.size();

        vector<int> postMin(nums_size, 0);

        postMin[nums_size - 1] = nums[nums_size - 1];

        for (int i = nums_size - 2; i >= 0; i--) {
            postMin[i] = min(nums[i],postMin[i+1]);
        }

        int maxi = INT_MIN;

        for(int i=0;i<nums_size;i++){
            maxi = max(maxi,nums[i]);
            int mini = postMin[i];

            if(maxi - mini <= k){
                return i;
            }
        }

        // for(auto it:postMin){
        //     cout<<it<<" ";
        // }

        return -1;
    }
};