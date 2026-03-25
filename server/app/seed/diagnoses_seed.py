"""
Seed script to populate the diagnosis table with 100 ICD-10 codes.
Run this after the database and table are created.
"""
import asyncio
from sqlalchemy import insert
from app.core.database import AsyncSessionLocal
from app.models.diagnosis_model import Diagnosis


async def seed_diagnoses():
    diagnoses_data = [
        # A00-B99: Certain Infectious and Parasitic Diseases
        {"code": "A09", "description": "Infectious gastroenteritis and colitis"},
        {"code": "A15.0", "description": "Tuberculosis of lung"},
        {"code": "A41.9", "description": "Sepsis, unspecified organism"},
        {"code": "B34.9", "description": "Viral infection, unspecified"},
        {"code": "B17.1", "description": "Acute hepatitis C"},

        # C00-D49: Neoplasms
        {"code": "C34.90", "description": "Malignant neoplasm of unspecified part of unspecified bronchus or lung"},
        {"code": "C50.911", "description": "Malignant neoplasm of unspecified site of right female breast"},
        {"code": "C61", "description": "Malignant neoplasm of prostate"},
        {"code": "C67.9", "description": "Malignant neoplasm of bladder, unspecified"},
        {"code": "C18.9", "description": "Malignant neoplasm of colon, unspecified"},
        {"code": "C44.91", "description": "Basal cell carcinoma of skin, unspecified"},
        {"code": "D25.9", "description": "Leiomyoma of uterus, unspecified"},
        {"code": "D23.9", "description": "Other benign neoplasm of skin, unspecified"},
        {"code": "D64.9", "description": "Anemia, unspecified"},

        # E00-E89: Endocrine, Nutritional and Metabolic Diseases
        {"code": "E11.9", "description": "Type 2 diabetes mellitus without complications"},
        {"code": "E10.9", "description": "Type 1 diabetes mellitus without complications"},
        {"code": "E78.5", "description": "Hyperlipidemia, unspecified"},
        {"code": "E03.9", "description": "Hypothyroidism, unspecified"},
        {"code": "E66.9", "description": "Obesity, unspecified"},
        {"code": "E86", "description": "Volume depletion (Dehydration)"},

        # F01-F99: Mental, Behavioral and Neurodevelopmental Disorders
        {"code": "F32.9", "description": "Major depressive disorder, single episode, unspecified"},
        {"code": "F41.9", "description": "Anxiety disorder, unspecified"},
        {"code": "F10.10", "description": "Alcohol abuse, uncomplicated"},
        {"code": "F20.9", "description": "Schizophrenia, unspecified"},
        {"code": "F03.90", "description": "Unspecified dementia"},
        {"code": "F90.9", "description": "Attention-deficit hyperactivity disorder, unspecified type"},
        {"code": "F43.10", "description": "Post-traumatic stress disorder, unspecified"},

        # G00-G99: Diseases of the Nervous System
        {"code": "G40.909", "description": "Epilepsy, unspecified, not intractable, without status epilepticus"},
        {"code": "G43.909", "description": "Migraine, unspecified, not intractable, without status migrainosus"},
        {"code": "G20", "description": "Parkinson's disease"},
        {"code": "G47.33", "description": "Obstructive sleep apnea (adult) (pediatric)"},
        {"code": "G89.29", "description": "Other chronic pain"},

        # I00-I99: Diseases of the Circulatory System
        {"code": "I10", "description": "Essential (primary) hypertension"},
        {"code": "I25.10", "description": "Atherosclerotic heart disease of native coronary artery"},
        {"code": "I48.91", "description": "Unspecified atrial fibrillation"},
        {"code": "I50.9", "description": "Heart failure, unspecified"},
        {"code": "I63.9", "description": "Cerebral infarction, unspecified"},
        {"code": "I70.0", "description": "Atherosclerosis of aorta"},
        {"code": "I83.90", "description": "Asymptomatic varicose veins of unspecified lower extremity"},

        # J00-J99: Diseases of the Respiratory System
        {"code": "J06.9", "description": "Acute upper respiratory infection, unspecified"},
        {"code": "J18.9", "description": "Pneumonia, unspecified organism"},
        {"code": "J44.9", "description": "Chronic obstructive pulmonary disease, unspecified"},
        {"code": "J45.909", "description": "Unspecified asthma, uncomplicated"},
        {"code": "J20.9", "description": "Acute bronchitis, unspecified"},

        # K00-K95: Diseases of the Digestive System
        {"code": "K21.9", "description": "Gastro-esophageal reflux disease without esophagitis"},
        {"code": "K29.70", "description": "Gastritis, unspecified, without bleeding"},
        {"code": "K30", "description": "Functional dyspepsia"},
        {"code": "K52.9", "description": "Noninfective gastroenteritis and colitis, unspecified"},
        {"code": "K57.90", "description": "Diverticulosis without perforation or abscess without bleeding"},
        {"code": "K80.20", "description": "Calculus of gallbladder without cholecystitis"},
        {"code": "K59.00", "description": "Constipation, unspecified"},

        # L00-L99: Diseases of the Skin and Subcutaneous Tissue
        {"code": "L20.9", "description": "Atopic dermatitis, unspecified"},
        {"code": "L30.9", "description": "Dermatitis, unspecified"},
        {"code": "L40.9", "description": "Psoriasis, unspecified"},
        {"code": "L03.116", "description": "Cellulitis of left lower limb"},
        {"code": "L60.0", "description": "Ingrowing nail"},

        # M00-M99: Diseases of the Musculoskeletal System and Connective Tissue
        {"code": "M17.9", "description": "Osteoarthritis of knee, unspecified"},
        {"code": "M16.9", "description": "Osteoarthritis of hip, unspecified"},
        {"code": "M19.90", "description": "Osteoarthritis, unspecified site"},
        {"code": "M54.5", "description": "Low back pain"},
        {"code": "M79.10", "description": "Myalgia, unspecified site"},
        {"code": "M81.0", "description": "Age-related osteoporosis without current pathological fracture"},
        {"code": "M25.561", "description": "Pain in right knee"},

        # N00-N99: Diseases of the Genitourinary System
        {"code": "N39.0", "description": "Urinary tract infection, site not specified"},
        {"code": "N40.1", "description": "Enlarged prostate (Benign prostatic hyperplasia) with lower urinary tract symptoms"},
        {"code": "N18.9", "description": "Chronic kidney disease, unspecified"},
        {"code": "N20.0", "description": "Calculus of kidney"},
        {"code": "N92.0", "description": "Excessive and frequent menstruation with regular cycle"},
        {"code": "N76.0", "description": "Acute vaginitis"},

        # R00-R99: Symptoms, Signs, and Abnormal Findings
        {"code": "R05", "description": "Cough"},
        {"code": "R06.02", "description": "Shortness of breath"},
        {"code": "R10.9", "description": "Unspecified abdominal pain"},
        {"code": "R11.2", "description": "Nausea with vomiting, unspecified"},
        {"code": "R42", "description": "Dizziness and giddiness"},
        {"code": "R51", "description": "Headache"},
        {"code": "R53.83", "description": "Fatigue"},
        {"code": "R00.0", "description": "Tachycardia, unspecified"},
        {"code": "R79.9", "description": "Abnormal finding of blood chemistry, unspecified"},

        # S00-T88: Injury, Poisoning, and External Causes
        {"code": "S06.9X0A", "description": "Traumatic brain injury with loss of consciousness status unknown, initial encounter"},
        {"code": "S52.001A", "description": "Unspecified fracture of upper end of right ulna, initial encounter for closed fracture"},
        {"code": "S80.861A", "description": "Insect bite (nonvenomous), right lower leg, initial encounter"},
        {"code": "T78.40XA", "description": "Allergy, unspecified, initial encounter"},
        {"code": "T40.2X1A", "description": "Poisoning by other opioids, accidental (unintentional), initial encounter"},

        # Z00-Z99: Factors Influencing Health Status
        {"code": "Z00.00", "description": "Encounter for general adult medical examination without abnormal findings"},
        {"code": "Z01.411", "description": "Encounter for gynecological examination (general) (routine) with abnormal findings"},
        {"code": "Z23", "description": "Encounter for immunization"},
        {"code": "Z34.90", "description": "Encounter for supervision of normal pregnancy, unspecified, unspecified trimester"},
        {"code": "Z71.3", "description": "Dietary counseling and surveillance"},
        {"code": "Z79.4", "description": "Long-term (current) use of insulin"},
        {"code": "Z79.01", "description": "Long-term (current) use of anticoagulants"},
        {"code": "Z88.9", "description": "Allergy status to unspecified drugs, medicaments and biological substances"},
        {"code": "Z98.890", "description": "Personal history of surgery (Past medical/treatment history not elsewhere classified)"},

        # Additional Codes from Various Chapters
        {"code": "H25.9", "description": "Age-related cataract, unspecified"},
        {"code": "H90.3", "description": "Sensorineural hearing loss, bilateral"},
        {"code": "O80", "description": "Encounter for full-term uncomplicated delivery"},
        {"code": "P05.10", "description": "Newborn small for gestational age, unspecified weight"},
        {"code": "Q21.1", "description": "Atrial septal defect"},
        {"code": "U09.9", "description": "Post COVID-19 condition, unspecified"},
        {"code": "W19.XXXA", "description": "Unspecified fall, initial encounter"},
        {"code": "Y92.9", "description": "Unspecified place of occurrence of the external cause"},
    ]

    async with AsyncSessionLocal() as session:
        try:
            await session.execute(insert(Diagnosis), diagnoses_data)
            await session.commit()
            print(f"Seeded {len(diagnoses_data)} diagnoses successfully.")
        except Exception as e:
            await session.rollback()
            print(f"Error seeding diagnoses: {e}")


if __name__ == "__main__":
    asyncio.run(seed_diagnoses())