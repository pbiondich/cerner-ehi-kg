# CV_PROC_HX

> Stores Cardiology Historical Orders details coming inbound to Cerner system.

**Description:** CV Procedure Historical orders table  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 24

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVITY_SUBTYPE_CD` | DOUBLE | NOT NULL |  | Internal coded value for the activity subtype of the associated order (e.g. echo, non-invasive vascular) |
| 2 | `COMPLETED_DT_TM` | DATETIME |  |  | The Date and Time when the exam was performed. |
| 3 | `COMPLETED_LOCATION_CD` | DOUBLE | NOT NULL |  | The unique identifier for the exam room in which the exam was performed. |
| 4 | `COMPLETED_TZ` | DOUBLE |  |  | The Time zone associated with the corresponding dt_tm column. |
| 5 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 6 | `CV_PROC_HX_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 7 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | The unique Millennium identifier of the patient from encounter encounter table. Foreign key to an ENCOUNTER table. |
| 8 | `ENTRY_MODE_CD` | DOUBLE |  |  | Code that is used to identify the method in which a result was entered |
| 9 | `EVENT_CD` | DOUBLE |  |  | Code value that represents the type of result/report. i.e. rbc, Cardiac cath, ECG 12-lead, etc.. |
| 10 | `EVENT_ID` | DOUBLE |  |  | Event Identifier for a parent row from clinical event which this record is associated to |
| 11 | `FRGN_SYS_ACCESSION_REFERENCE` | VARCHAR(200) |  |  | Accession number from the foreign system for the procedure. This is an alphanumeric field. |
| 12 | `FRGN_SYS_ORDER_REFERENCE` | VARCHAR(200) |  |  | The unique identifier defined in the foreign system for order. This is an alphanumeric field. |
| 13 | `FRGN_SYS_STUDY_REFERENCE` | VARCHAR(255) |  |  | Study Identifier from the foreign system for the procedure. This is an alphanumeric field. |
| 14 | `ORDER_CATALOG_CD` | DOUBLE | NOT NULL |  | Internal coded value for the order catalog item. Foreign key to ORDER_CATALOG table. |
| 15 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | The unique Identifier for the Millennium Order. Foreign key to the ORDERS table. |
| 16 | `PDF_DOC_IDENTIFIER` | VARCHAR(250) |  |  | field to hold the document identifier for the pdf store which is a MMF key. Added to support Migration Project |
| 17 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | The unique Millennium Identifier of the person from PERSON table whom the order is placed for. Foreign key to the PERSON table. |
| 18 | `REFERENCE_TXT` | VARCHAR(100) |  |  | The combination of the reference nbr and the contributor system code provides a unique identifier to the origin of the clinical event data for the record. |
| 19 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 20 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 21 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 22 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 23 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 24 | `VENDOR_CD` | DOUBLE |  |  | The code value of the contributing source of the STUDY . The vendor code from code set 73. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

