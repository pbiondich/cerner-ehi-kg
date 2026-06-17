# UKRWH_MAT_BIRTH

> Contains birth details associated to a maternity encounter.

**Description:** UKRWH_MAT_BIRTH  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 60

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `APGAR_1_MIN_SCORE` | DOUBLE |  |  | The Apgar score of the neonate 1 minute after the delivery. |
| 3 | `APGAR_5_MIN_SCORE` | DOUBLE |  |  | The Apgar score of the neonate 5 minutes after the delivery. |
| 4 | `BABY_ALIVE_LABOUR_ONSET_NM_SK` | VARCHAR(100) |  |  | Fetal Heart Rate Heard at Onset of Labour Millennium Nomenclature Identifier. |
| 5 | `BABY_BIRTH_DT_TM` | DATETIME |  |  | Date and time of birth of baby. |
| 6 | `BABY_NAME` | VARCHAR(255) |  |  | A number to provide a unique identifier for each Hospital Provider Spell for a Health Care Provider. |
| 7 | `BABY_PERSON_SK` | VARCHAR(40) |  |  | The Millennium system generated unique person identifier of the baby. |
| 8 | `BBA_NM_SK` | VARCHAR(100) |  |  | Unattended delivery Millennium Nomenclature Identifier. |
| 9 | `BIRTH_LOC_DETAIL_NM_SK` | VARCHAR(100) |  |  | Actual Delivery Location Detail Millennium Nomenclature Identifier. Indicates if delivered in ambulance - theatre or toilet. |
| 10 | `BIRTH_LOC_NM_SK` | VARCHAR(100) |  |  | Actual Delivery Location Millennium Nomenclature Identifier. Type of unit in which baby was delivered. |
| 11 | `BIRTH_ORDER_NBR` | DOUBLE |  |  | Sequence in which the baby was born. |
| 12 | `BIRTH_WEIGHT` | VARCHAR(9) |  |  | Weight of baby in grammes at birth. Output as a string in the following format nnnn.nn g . |
| 13 | `CORD_PH_RESULT` | DOUBLE |  |  | Cord pH Result Mixed. |
| 14 | `C_SECTION_GRADE_NM_SK` | VARCHAR(100) |  |  | Caesarean Section Grading Millennium Nomenclature Identifier. |
| 15 | `C_SECTION_INDICATION_NM_SK` | VARCHAR(100) |  |  | Primary Indication for C Section Millennium Nomenclature Identifier |
| 16 | `DELIVERED_BY_NAME` | VARCHAR(255) |  |  | Baby Delivered by Person Name. |
| 17 | `DEL_METHOD_REF` | VARCHAR(40) |  |  | Delivery Method (Current Baby) Millennium Code Value. The method for delivering baby. |
| 18 | `DEL_OUTCOME_NM_SK` | VARCHAR(100) |  |  | Method of Delivery Millennium Nomenclature Identifier. The delivery method for each baby. |
| 19 | `DEL_PRSNL_STATUS_NM_SK` | VARCHAR(100) |  |  | Status of Clinician Conducting Delivery Millennium Nomenclature Identifier. |
| 20 | `EXTRACT_DT_TM` | DATETIME | NOT NULL |  | Date and Time of when extract was created. |
| 21 | `FEEDING_METHOD_NM_SK` | VARCHAR(100) |  |  | Baby Feed Type (At Discharge from Hospital) Millennium Nomenclature Identifier. Method of feed - as captured at the point of baby s discharge from hospital. In the case of a home birth - this will be captured at the postnatal visit closest to 48 hours of birth. |
| 22 | `FIRST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | First date/time row was inserted into table. |
| 23 | `GEST_AGE_DEL` | VARCHAR(15) |  |  | Gestation at DATE TIME OF BIRTH (BABY) in weeks and days in the format # weeks - # days . |
| 24 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Unique number assigned by Health Facts. Typically the universal Cerner assigned client id of the health system. |
| 25 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL |  | Unique number assigned by Health Facts. Typically the universal Cerner assigned client id of the sending health system but may be adjusted if there is >1 HF feed from the client. |
| 26 | `HR_10_MIN_NM_SK` | VARCHAR(100) |  |  | Heart Rate at 10 minutes Millennium Nomenclature Identifier |
| 27 | `HR_20_MIN_NM_SK` | VARCHAR(100) |  |  | Heart Rate at 20 minutes Millennium Nomenclature Identifier |
| 28 | `HR_5_MIN_NM_SK` | VARCHAR(100) |  |  | Heart Rate at 5 minutes Millennium Nomenclature Identifier |
| 29 | `LABOUR_START_DT_TM` | DATETIME |  |  | Onset of Established Labour Date Time. Date/time when established labour is confirmed - regular painful contractions and progressive cervical dilatation from 4 cm. |
| 30 | `LAST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | Last date/time row was updated. |
| 31 | `LOCAL_PATIENT_IDENT` | VARCHAR(40) |  |  | An identifier - other than a name - which identifies a PERSON. |
| 32 | `LOC_BABY_BIRTH_DT_TM` | DATETIME |  |  | Date and time of birth of baby converted to local date/time. |
| 33 | `LOC_LABOUR_START_DT_TM` | DATETIME |  |  | Onset of Established Labour Date Time converted to local date/time. |
| 34 | `LOC_MEM_RUPTURE_DT_TM` | DATETIME |  |  | Date and time on which membranes ruptured converted to local date/time. |
| 35 | `LOC_NEO_DEATH_DT_TM` | DATETIME |  |  | Date and time of death of baby converted to local date/time. |
| 36 | `MEM_RUPTURE_DT_TM` | DATETIME |  |  | Date and time on which membranes ruptured. |
| 37 | `NB_GEST_ASSESS_NM_SK` | VARCHAR(100) |  |  | Gestation Appearance Millennium Nomenclature Identifier. |
| 38 | `NB_SEX_REF` | VARCHAR(40) |  |  | Child s Gender. |
| 39 | `NEO_CARE_LEVEL_NM_SK` | VARCHAR(100) |  |  | Critical Care level for the day. |
| 40 | `NEO_DEATH_DT_TM` | DATETIME |  |  | Date and time of death of baby. |
| 41 | `NEO_OUTCOME_REF` | VARCHAR(40) |  |  | Neonate Outcome Millennium Code Value . Neonatal outcome indicating live birth - fetal death or neonatal death. |
| 42 | `NHS_NBR_IDENT` | VARCHAR(40) |  |  | A number used to identify a person uniquely within the NHS in England and Wales. This field contains the NHS Number of the patient - which is the primary identifier of a person registered for health care; it is unique. Records for babies under six weeks of age and for patients admitted through accident and emergency tend to have null entries for this field. |
| 43 | `NOTIFYING_MIDWIFE_NAME` | VARCHAR(255) |  |  | Name of notifying midwife. |
| 44 | `PREGNANCY_CHILD_SEQ_SK` | VARCHAR(40) |  |  | Millennium system generated unique identifier for a fetus / birth with appended for sequence |
| 45 | `PREGNANCY_CHILD_SK` | VARCHAR(40) |  |  | Millennium system generated unique identifier for a fetus / birth. |
| 46 | `PREGNANCY_SK` | VARCHAR(40) |  |  | Millennium system generated unique identifier for a pregnancy. |
| 47 | `PREG_OUTCOME_REF` | VARCHAR(40) |  |  | Pregnancy Outcome (Current Fetus) Millennium Code Value. Outcome of each fetus identified at the dating scan. |
| 48 | `PRES_DEL_NM_SK` | VARCHAR(100) |  |  | Presentation at Onset of Labour Millennium Nomenclature Identifier. The presentation of the (first) fetus at onset of labour. |
| 49 | `RESP_10_MIN_NM_SK` | VARCHAR(100) |  |  | Respiratory Effort at 10 minutes Millennium Nomenclature Identifier. |
| 50 | `RESP_20_MIN_NM_SK` | VARCHAR(100) |  |  | Respiratory Effort at 20 minutes Millennium Nomenclature Identifier. |
| 51 | `RESP_5_MIN_NM_SK` | VARCHAR(100) |  |  | Respiratory Effort at 5 minutes Millennium Nomenclature Identifier. |
| 52 | `TOTAL_LABOUR_LENGTH` | VARCHAR(5) |  |  | Total length of labour in hours and minutes formatted as a string in HH:MM . |
| 53 | `TOTAL_NBR_BABIES` | DOUBLE |  |  | Total newborns delivered in the pregnancy. |
| 54 | `TOTAL_UPDATES` | DOUBLE | NOT NULL |  | The numbers of updates that have occurred on this table. |
| 55 | `UKRWH_MAT_BIRTH_KEY` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the UKRWH_MAT_BIRTH table. |
| 56 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 57 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 58 | `UPDT_TASK` | VARCHAR(40) | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 59 | `UPDT_USER` | VARCHAR(40) | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 60 | `WATER_BIRTH_NM_SK` | VARCHAR(100) |  |  | Delivered In Water Indicator Millennium Nomenclature Identifier. Whether or not the baby was delivered in a birthing pool. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

