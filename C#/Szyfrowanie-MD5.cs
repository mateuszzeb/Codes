// Szyfrowanie MD5

// Using 
using System.Security.Cryptography;
using System.Text;

// Class
class MD5_
{
    public string get_md5_string(string txt)
    {
        MD5 md5 = new MD5CryptoServiceProvider();
        md5.ComputeHash(Encoding.ASCII.GetBytes(txt));
        byte[] result = md5.Hash;
        StringBuilder strBuilder = new StringBuilder();
        for (int i = 0; i < result.Length; i++)
        {
            strBuilder.Append(result[i].ToString("x2"));
        }
        string szyfr = strBuilder.ToString();
        return szyfr;
    }
}

// Example
// MD5_ md5 = new MD5();
// Console.WriteLine(md5.get_md5_string("admin"));
//
// Output: 
// 21232f297a57a5a743894a0e4a801fc3
