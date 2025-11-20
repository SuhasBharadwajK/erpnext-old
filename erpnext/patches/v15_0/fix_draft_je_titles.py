import frappe

def execute():
    draft_journals = frappe.get_all('Journal Entry', filters={'docstatus': 0}, fields=['name'])
    updated = 0
    for je in draft_journals:
        doc = frappe.get_doc('Journal Entry', je.name)
        new_title = doc.get_title()
        old_title = frappe.db.get_value('Journal Entry', doc.name, 'title')
        if new_title != old_title:
            doc.title = new_title
            doc.save(ignore_permissions=True)
            updated += 1
            print(f"Updated {doc.name}: '{old_title}' -> '{new_title}'")
    frappe.db.commit()
    print(f"Total draft Journal Entries updated: {updated}")