"""
Data Analyst Portfolio: Revenue Leakage Detection
Vibe: Forensic | Logic: Financial Integrity

Detecting the 'Invisible Drain'. This script reconciles invoice logs 
with payment gateway settlements.
"""

def detect_leakage(invoices, settlements):
    """
    Compares what was billed vs what was actually received.
    """
    print("Initiating Revenue Integrity Audit...")
    leakage_detected = []
    
    for invoice_id, amount in invoices.items():
        settled_amount = settlements.get(invoice_id, 0)
        if settled_amount < amount:
            leakage = amount - settled_amount
            leakage_detected.append({
                "invoice_id": invoice_id,
                "amount_due": amount,
                "amount_received": settled_amount,
                "leakage": leakage
            })
            
    return leakage_detected

if __name__ == "__main__":
    billing = {"INV-001": 1500, "INV-002": 3000, "INV-003": 4500}
    banking = {"INV-001": 1500, "INV-002": 2850} # INV-003 missing, INV-002 short
    
    report = detect_leakage(billing, banking)
    for entry in report:
        print(f"Leakage in {entry['invoice_id']}: {entry['leakage']} missing.")
