
import java.util.ArrayList;

public class HotelManager {

    private ArrayList<Room> rooms;
    private ArrayList<Booking> bookings;

    public HotelManager() {

        rooms = new ArrayList<>();
        bookings = new ArrayList<>();

        rooms.add(new Room(101, "Standard"));
        rooms.add(new Room(102, "Standard"));
        rooms.add(new Room(201, "Deluxe"));
        rooms.add(new Room(202, "Deluxe"));
        rooms.add(new Room(301, "Suite"));
    }

    public ArrayList<Room> getRooms() {
        return rooms;
    }

    public ArrayList<Booking> getBookings() {
        return bookings;
    }

    public Room findRoom(int roomNumber) {

        for (Room room : rooms) {

            if (room.getRoomNumber() == roomNumber) {
                return room;
            }

        }

        return null;
    }

    public boolean bookRoom(int roomNumber,
                            String customerName,
                            String phone,
                            String checkIn,
                            String checkOut) {

        Room room = findRoom(roomNumber);

        if (room != null && !room.isBooked()) {

            room.bookRoom();

            Customer customer = new Customer(customerName, phone);

            bookings.add(new Booking(room, customer, checkIn, checkOut));

            return true;
        }

        return false;
    }

    public boolean cancelBooking(int roomNumber) {

        for (Booking booking : bookings) {

            if (booking.getRoom().getRoomNumber() == roomNumber) {

                booking.getRoom().cancelBooking();

                bookings.remove(booking);

                return true;
            }

        }

        return false;
    }

}