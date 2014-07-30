# Documentation for *Raise the Bar!*

## Pages
### Main Page
The main page is a dashboard. It has two main windows:

1. A list of the most-recent notes added, organized by modified time.
2. A list of the firms in the system, with a little search tool to help select a specific firm.

### Add Firm
A simple form to add a firm that doesn't exist in the system

### Firm Dossier
This is the firm page. It has a list of all existing notes, organized by reverse chronological order. It also has an "Add a Note" button, so that you can add a note.

### Add a Note
This is a page where you can add a note. It necessarily must have a firm linked to its creation. On this page, you add the following information:

1. NoteForm (user that added the note, content of the note, contact (if applicable))
2. If new contact, a modal ContactForm (first, last, email, phone)
3. If desired, a modal ReminderForm (reminder date, content)

### Reminders
This has a list of all reminders for a given day. Has a calendar feature to select a particular day for to see if there are any scheduled/past reminders.