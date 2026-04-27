from datetime import datetime, timedelta

def calculate_fine(days_overdue):
    # No fine if returned on time or early
    if days_overdue <= 0:
        return 0
    
    # We need to figure out which week the student is in
    weeks = (days_overdue // 7) + 1
    rate = 10
    total = 0
    
    # The fine jumps: 10/day, then 20/day, then 60/day...
    multiplier = 1
    for w in range(1, weeks + 1):
        multiplier *= w
        week_rate = rate * multiplier
        
        # Check how many days are in the current week vs total days left
        days_in_week = min(7, days_overdue - (w-1)*7)
        total += days_in_week * week_rate
        
        if (w * 7) >= days_overdue:
            break
            
    return total

def issue_book(books_dict, records, student, book_name, days):
    # Check if this student already has a book (Optional safety check)
    if student in records:
        return f"❌ {student} already has a book issued. Return it first!"

    if book_name in books_dict and books_dict[book_name] > 0:
        books_dict[book_name] -= 1
        
        today = datetime.now()
        due = today + timedelta(days=days)
        
        # This ADDS a new key to the existing records dictionary
        records[student] = {
            "book": book_name,
            "issue_date": today.strftime("%Y-%m-%d"),
            "due_date": due.strftime("%Y-%m-%d"),
            "days_allowed": days
        }
        return f"✅ '{book_name}' issued to {student}."
    
    return "❌ Book out of stock."

def return_book(books_dict, records, student):
    if student in records:
        # Get the record and put the book back in inventory
        info = records.pop(student)
        books_dict[info['book']] += 1
        
        # Calculate the difference between today and the due date
        due_date = datetime.strptime(info['due_date'], "%Y-%m-%d")
        today = datetime.now()
        
        # We only care about the date difference, not the exact seconds
        diff = (today.date() - due_date.date()).days
        
        fine_amount = calculate_fine(diff)
        
        result = f"✅ Success: '{info['book']}' is back in the library."
        if fine_amount > 0:
            result += f"\n📢 Note: Book was {diff} day(s) late. Fine: ₹{fine_amount}"
        else:
            result += "\n✨ Returned on time. Thank you!"
            
        return result
    
    return "❌ Error: We don't have an issued record for that student name."