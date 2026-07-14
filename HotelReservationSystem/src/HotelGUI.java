import java.awt.*;
import javax.swing.*;
import javax.swing.table.DefaultTableModel;

public class HotelGUI extends JFrame {

    private JTextField roomField;
    private JTextField nameField;
    private JTextField phoneField;
    private JTextField checkInField;
    private JTextField checkOutField;

    private JTable table;
    private DefaultTableModel model;

    private HotelManager manager;

    public HotelGUI() {

        manager = new HotelManager();

        setTitle("Hotel Reservation System");
        setSize(950,600);
        setLocationRelativeTo(null);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        JPanel inputPanel = new JPanel(new GridLayout(6,2,10,10));

        inputPanel.add(new JLabel("Room Number"));
        roomField = new JTextField();
        inputPanel.add(roomField);

        inputPanel.add(new JLabel("Customer Name"));
        nameField = new JTextField();
        inputPanel.add(nameField);

        inputPanel.add(new JLabel("Phone Number"));
        phoneField = new JTextField();
        inputPanel.add(phoneField);

        inputPanel.add(new JLabel("Check In"));
        checkInField = new JTextField();
        inputPanel.add(checkInField);

        inputPanel.add(new JLabel("Check Out"));
        checkOutField = new JTextField();
        inputPanel.add(checkOutField);

        JButton bookButton = new JButton("Book Room");
        JButton cancelButton = new JButton("Cancel Booking");

        inputPanel.add(bookButton);
        inputPanel.add(cancelButton);

        model = new DefaultTableModel();

        model.addColumn("Room");
        model.addColumn("Type");
        model.addColumn("Customer");
        model.addColumn("Phone");
        model.addColumn("Check In");
        model.addColumn("Check Out");

        table = new JTable(model);

        add(inputPanel, BorderLayout.NORTH);
        add(new JScrollPane(table), BorderLayout.CENTER);

                bookButton.addActionListener(e -> {

            try {

                int roomNumber = Integer.parseInt(roomField.getText());
            
                String customerName = nameField.getText();
                String phone = phoneField.getText();
                String checkIn = checkInField.getText();
                String checkOut = checkOutField.getText();

                boolean booked = manager.bookRoom(
                        roomNumber,
                        customerName,
                        phone,
                        checkIn,
                        checkOut
                );

                if (booked) {

                    Room room = manager.findRoom(roomNumber);

                    model.addRow(new Object[]{
                            room.getRoomNumber(),
                            room.getRoomType(),
                            customerName,
                            phone,
                            checkIn,
                            checkOut
                    });

                    FileManager.saveBookings(manager.getBookings());

                    JOptionPane.showMessageDialog(this,
                            "Room Booked Successfully");

                    roomField.setText("");
                    nameField.setText("");
                    phoneField.setText("");
                    checkInField.setText("");
                    checkOutField.setText("");

                } else {

                    JOptionPane.showMessageDialog(this,
                            "Room already booked or not found.");

                }

            } catch (Exception ex) {

                JOptionPane.showMessageDialog(this,
                        "Please enter valid information.");

            }

        
        });

        FileManager.loadBookings(manager);

        for (Booking booking : manager.getBookings()) {

            model.addRow(new Object[]{
                    booking.getRoom().getRoomNumber(),
                    booking.getRoom().getRoomType(),
                    booking.getCustomer().getName(),
                    booking.getCustomer().getPhone(),
                    booking.getCheckInDate(),
                    booking.getCheckOutDate()
            });
}

        setVisible(true);

       
}
}