def classify_document(text: str) -> str:
    """"
    Classify the document based on its content.
    This is a placeholder function and should be replaced with actual NLP logic.
    """

    # Todo: To use ML-Based classification later as Transformer-based models
    # For now, we will use simple keyword matching for classification

    text = text.lower()

    if "prescription" in text or "rx" in text:
        return "Prescription"
    
    elif "discharge" in text and "summary" in text:
        return "Discharge Summary"
    
    elif "diagnosis" in text or "report" in text:
        return "Diagnosis Report"
    
    elif "policy" in text or "insurance" in text:
        return "Insurance Policy"
    
    elif "claim" in text or "settlement" in text:
        return "Claim Settlement"
    
    elif "invoice" in text or "bill" in text or "amount due" in text:
        return "Invoice"
    
    elif "lab result" in text or "test result" in text:
        return "Lab Result"
    
    elif "medical history" in text or "patient history" in text:
        return "Medical History"
    
    elif "medical report" in text or "doctor's note" in text or "physician's report" in text:
        return "Medical Report"
    
    elif "authorization" in text or "approval" in text:
        return "Authorization Letter"
    else:
        return "Unknown Document Type"
    