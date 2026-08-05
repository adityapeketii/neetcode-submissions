class Solution {
public:
    bool isValid(string s) {
        stack <char> st;
        int n = s.length();

        for(int i = 0 ; i < n ; i++)
        {
            char ch = s[i];
            if (ch == '(' || ch == '[' || ch == '{')
            {
                st.push(ch);
            }
            else {
                if(ch == ')')
                {
                    if(st.empty() == false && st.top() == '(')
                    {
                        st.pop();
                    }
                    else return false;
                }
                else if(ch == ']')
                {
                    if(st.empty() == false && st.top() == '[')
                    {
                        st.pop();
                    }
                    else return false;
                }
                else if(ch == '}')
                {
                    if(st.empty() == false && st.top() == '{')
                    {
                        st.pop();
                    }
                    else return false;
                }

            }
        }
        if(st.empty())
        {
            return true;
        }
        else return false;
    }
};
