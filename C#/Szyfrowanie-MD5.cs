// Szyfrowanie MD5

using System;
using System.Security.Cryptography;
using System.Text;

namespace First
{
    public class Program
    {
        public static void Main()
        {
            Console.Write("Text: ");
            String txt = Console.ReadLine();
            MD5 md5 = new MD5CryptoServiceProvider();
            md5.ComputeHash(Encoding.ASCII.GetBytes(txt));
            byte[] result = md5.Hash;
            StringBuilder strBuilder = new StringBuilder();
            for (int i = 0; i < result.Length; i++)
            {
                strBuilder.Append(result[i].ToString("x2"));
            }
            var szyfr = strBuilder.ToString();
            Console.WriteLine(szyfr);
        }
    }
}
