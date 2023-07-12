int partition(int *nums1, int start, int end) {
  int pivot = nums1[end];
  int aux;

  int j = start;
  for(int i = start; i < end; i++) {
    if(nums1[i] <= pivot) {
      aux = nums1[i];
      nums1[i] = nums1[j];
      nums1[j] = aux;
      j++;
    }
  }
  aux = nums1[end];
  nums1[end] = nums1[j];
  nums1[j] = aux;
  return j;
}

void quicksort(int *nums1, int start, int end) {
  if(start < end) {
    int pivot = partition(nums1, start, end);
    quicksort(nums1, pivot + 1, end);
    quicksort(nums1, start, pivot - 1);
  }
}

void merge(int* nums1, int nums1Size, int m, int* nums2, int nums2Size, int n){
  int j = 0, i = m;
  for(; i < nums1Size; i++) { nums1[i] = nums2[j]; j++; }
  quicksort(nums1, 0, nums1Size - 1);
}
