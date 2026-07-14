import java.io.*;
import java.util.ArrayList;

public class FileManager {

    private static final String FILE_NAME = "data/bookings.txt";

    public static void saveBookings(ArrayList<Booking> bookings) {

        try (BufferedWriter writer = new BufferedWriter(new FileWriter(FILE_NAME))) {

            for (Booking booking : bookings) {
                writer.write(booking.toString());
                writer.newLine();
            }

        } catch (IOException e) {
            System.out.println("Error saving bookings.");
        }
    }

    public static void loadBookings(HotelManager manager) {

        File file = new File(FILE_NAME);

        if (!file.exists()) {
            return;
        }

        try (BufferedReader reader = new BufferedReader(new FileReader(file))) {

            String line;

            while ((line = reader.readLine()) != null) {

                String[] data = line.split(",");

                int roomNumber = Integer.parseInt(data[0]);
                String customerName = data[2];
                String phone = data[3];
                String checkIn = data[4];
                String checkOut = data[5];

                manager.bookRoom(roomNumber, customerName, phone, checkIn, checkOut);
            }

        } catch (Exception e) {
            System.out.println("Error loading bookings.");
        }
    }
}