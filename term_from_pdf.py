import PyPDF2
import re


def extract_terms(pdf_path):
    """PDF fayldan terminlarni ro'yxat ko'rinishida ajratib olish funksiyasi."""

    terms = set()  # Takrorlanmaslik uchun setdan foydalanamiz

    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)

        for page in reader.pages:
            text = page.extract_text()
            # Qalin yozilgan so'zlarni topish uchun muntazam ifoda
            bold_words = re.findall(r'\b(\w+)\b', text)
            terms.update(bold_words)  # topilgan so'zlarni setga qo'shamiz

    return list(terms)  # Setni ro'yxatga o'tkazib qaytaramiz


# PDF fayl yo'lini kiriting
pdf_file = 'Dictionary_of_Computer_and_Internet_Terms_Words.pdf'
extracted_terms = extract_terms(pdf_file)

# Terminlar ro'yxatini chop etish
print(extracted_terms)
