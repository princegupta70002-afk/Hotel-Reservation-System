public class Booking {

    private Room room;
    private Customer customer;
    private String checkInDate;
    private String checkOutDate;

    public Booking(Room room, Customer customer, String checkInDate, String checkOutDate) {
        this.room = room;
        this.customer = customer;
        this.checkInDate = checkInDate;
        this.checkOutDate = checkOutDate;
    }

    public Room getRoom() {
        return room;
    }

    public Customer getCustomer() {
        return customer;
    }

    public String getCheckInDate() {
        return checkInDate;
    }

    public String getCheckOutDate() {
        return checkOutDate;
    }

    @Override
    public String toString() {
        return room.getRoomNumber() + "," +
               room.getRoomType() + "," +
               customer.getName() + "," +
               customer.getPhone() + "," +
               checkInDate + "," +
               checkOutDate;
    }
}