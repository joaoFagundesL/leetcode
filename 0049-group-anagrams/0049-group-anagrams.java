import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

public class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {

        int len = strs.length;

        if (len == 0)
            return new ArrayList<>();

        HashMap<String, List<String>> hash = new HashMap<>();

        for (int i = 0; i < len; i++) {
            String frequency = getFrequency(strs[i]);

            if (!hash.containsKey(frequency)) {
                ArrayList<String> list = new ArrayList<>();
                list.add(strs[i]);

                hash.put(frequency, list);
            } else {
                // get will return the value associated with its key
                hash.get(frequency).add(strs[i]);
            }
        }

        return new ArrayList<>(hash.values());
    }

    public String getFrequency(String str) {
        final int CHARACTER_QUANTITY = 26;

        int[] arr_char = new int[CHARACTER_QUANTITY];

        for (int i = 0; i < str.length(); i++) {
            arr_char[str.charAt(i) - 'a'] += 1;
        }

        StringBuilder hash_key = new StringBuilder("");

        char c_aux = 'a';

        for (int i = 0; i < CHARACTER_QUANTITY; i++) {
            hash_key.append(c_aux);
            hash_key.append(arr_char[i]);

            ++c_aux;
        }

        return hash_key.toString();
    }
}
