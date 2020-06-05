using System;
using System.Net;
using System.Net.Sockets;
using System.Text;
using System.IO;

public class SynchronousSocketClient
{
    private Socket soc;

    public void StartClient()
    {
        // Data buffer for incoming data.  
        byte[] bytes = new byte[1024];
       

        // Connect to a remote device.  
        try
        {
            // Establish the remote endpoint for the socket.  
            // This example uses port 11000 on the local computer.  
            IPHostEntry ipHostInfo = Dns.GetHostEntry(Dns.GetHostName());

            //IPAddress ipAddress = ipHostInfo.AddressList[0];

            IPAddress ipAddress = IPAddress.Parse("127.0.0.1");

            IPEndPoint remoteEP = new IPEndPoint(ipAddress, 65432);

            // Create a TCP/IP  socket.  
            soc = new Socket(ipAddress.AddressFamily,
                SocketType.Stream, ProtocolType.Tcp);

            // Connect the socket to the remote endpoint. Catch any errors.  
            try
            {
                soc.Connect(remoteEP);

                Console.WriteLine("Socket connected to {0}",
                    soc.RemoteEndPoint.ToString());

                // Encode the data string into a byte array.  
                byte[] msg = Encoding.ASCII.GetBytes("Connect");

                // Send the data through the socket.  
                int bytesSent = soc.Send(msg);

                // Receive the response from the remote device.  
                int bytesRec = soc.Receive(bytes);
                Console.WriteLine("Received from server = {0}",
                    Encoding.ASCII.GetString(bytes, 0, bytesRec));

               

            }
            catch (ArgumentNullException ane)
            {
                Console.WriteLine("ArgumentNullException : {0}", ane.ToString());
            }
            catch (SocketException se)
            {
                Console.WriteLine("SocketException : {0}", se.ToString());
            }
            catch (Exception e)
            {
                Console.WriteLine("Unexpected exception : {0}", e.ToString());
            }

        }
        catch (Exception e)
        {
            Console.WriteLine(e.ToString());
        }
    }

    public void CloseConnection()
    {
        byte[] msg = Encoding.ASCII.GetBytes("Close Connection");
        int bytesSent = soc.Send(msg);
        // Release the socket.  
        soc.Shutdown(SocketShutdown.Both);
        soc.Close();

    }

    public void requestVideo(int videoID)
    {
        byte[] bytes = new byte[1024];
        Console.WriteLine("Requesting Video {0}", videoID.ToString());

        string path = @"/Users/itsyuezeng/Projects/SmartWorkerClient/received.mp4";
        // Encode the data string into a byte array.  
        byte[] msg = Encoding.ASCII.GetBytes("Video 111");

        // Send the data through the socket.  
        int bytesSent = soc.Send(msg);
        using (FileStream fs = File.Create(path))
        {
            int package = 0;
            Console.Write("000000000");

            while (true)
            {
                int length = soc.Receive(bytes);
                Console.Write("package size {0} <EOF>", length.ToString());
                if (length > 0)
                {
                    
                    Console.WriteLine("Get package {0}", package.ToString());
                    package += 1;

                    fs.Write(bytes, 0, bytes.Length);

                }
                else
                {
                    break;
                }
                
            }

            Console.WriteLine("Done downloading video ", videoID.ToString());

        }

    }



    public static int Main(String[] args)
    {
        var client = new SynchronousSocketClient { };
        client.StartClient();
        client.requestVideo(1000);
        return 0;
    }
}