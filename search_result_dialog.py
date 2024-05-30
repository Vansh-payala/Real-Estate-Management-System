from PyQt5.QtWidgets import QDialog, QTableWidget, QVBoxLayout, QHeaderView, QTableWidgetItem

class SearchResultDialog(QDialog):
    def __init__(self, headers, data, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Search Results")
        
        # Create the table widget
        self.table = QTableWidget()
        self.table.setColumnCount(len(headers))
        self.table.setHorizontalHeaderLabels(headers)
        self.table.setRowCount(len(data))

        # Populate the table with data
        for row, row_data in enumerate(data):
            for col, value in enumerate(row_data):
                item = QTableWidgetItem(str(value))
                self.table.setItem(row, col, item)

        # Adjust column widths to contents
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)

        # Apply some styling
        self.table.setStyleSheet("QTableWidget { background-color: white; \
                                   selection-background-color: #cce6ff; \
                                   border: 1px solid #d4d4d4; } \
                                   QHeaderView::section { background-color: #f2f2f2; \
                                   border: 1px solid #d4d4d4; } \
                                   QTableWidget::item:selected { background-color: #cce6ff; }")

        # Set the layout
        layout = QVBoxLayout()
        layout.addWidget(self.table)
        self.setLayout(layout)

        # Resize the dialog to match the size of the table
        self.adjustSize()
